#!/usr/bin/env python3
"""Render an honest accuracy chart from the reproduced metrics.

Plots strict section retrieval accuracy@K for each run under results/. Every
bar is backed by a metrics.json that compute_metrics.py can independently
reproduce from the raw retrieval_results.jsonl.

Usage:
    pip install matplotlib
    python make_chart.py            # writes assets/accuracy_chart.png
"""
import glob
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

KS = [1, 3, 5, 10]
ACCENT = "#22c55e"


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_runs():
    runs = []
    for metrics_path in sorted(glob.glob(os.path.join(repo_root(), "results", "*", "metrics.json"))):
        run_dir = os.path.dirname(metrics_path)
        with open(metrics_path, encoding="utf-8") as handle:
            overall = json.load(handle).get("metrics", {}).get("overall", {})
        manifest_path = os.path.join(run_dir, "manifest.json")
        count = overall.get("count", "")
        label = os.path.basename(run_dir).replace("open_ragbench_", "")
        if os.path.exists(manifest_path):
            with open(manifest_path, encoding="utf-8") as handle:
                count = json.load(handle).get("selected_query_count", count)
        values = [overall.get("strict_section_hit@%d" % k) for k in KS]
        runs.append((label, count, values))
    return runs


def main():
    runs = load_runs()
    if not runs:
        print("No results/*/metrics.json found.", file=sys.stderr)
        sys.exit(1)

    plt.rcParams.update({"font.size": 11, "axes.edgecolor": "#334155"})
    fig, ax = plt.subplots(figsize=(9, 5))
    bar_w = 0.8 / len(runs)
    x = range(len(KS))
    for idx, (label, count, values) in enumerate(runs):
        offset = idx * bar_w
        positions = [i + offset for i in x]
        bars = ax.bar(positions, [v * 100 for v in values], width=bar_w,
                      label="%s (n=%s)" % (label, count))
        if len(runs) == 1:
            for rect in bars:
                rect.set_color(ACCENT)
        for rect, value in zip(bars, values):
            ax.text(rect.get_x() + rect.get_width() / 2, value * 100 + 0.8,
                    "%.1f%%" % (value * 100), ha="center", va="bottom", fontsize=9)

    center = (len(runs) - 1) * bar_w / 2
    ax.set_xticks([i + center for i in x])
    ax.set_xticklabels(["@%d" % k for k in KS])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Strict section retrieval accuracy (%)")
    ax.set_xlabel("Top-K")
    ax.set_title("Linkence on Open RAG Bench - strict section accuracy@K")
    ax.legend(frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()

    out_path = os.path.join(repo_root(), "assets", "accuracy_chart.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, dpi=150)
    print("Wrote %s" % out_path)


if __name__ == "__main__":
    main()
