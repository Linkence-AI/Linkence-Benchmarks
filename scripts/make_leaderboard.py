#!/usr/bin/env python3
"""Build a single leaderboard.csv summarizing every run under results/.

Reads each results/<run>/metrics.json (+ manifest.json for context) and emits
one row per run with the headline accuracy/latency figures.

Usage:
    python make_leaderboard.py            # writes leaderboard.csv at repo root
    python make_leaderboard.py out.csv
"""
import csv
import glob
import json
import os
import sys

FIELDS = [
    "system", "dataset", "subset", "n_queries", "top_k",
    "strict_section_acc@1", "strict_section_acc@3", "strict_section_acc@5",
    "strict_section_acc@10", "strict_section_acc@20",
    "relaxed_doc_acc@10", "mrr@10", "ndcg@10",
    "embedding_model", "reranker", "latency_p50_ms", "latency_p95_ms",
    "code_commit_sha", "run_datetime_utc",
]


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def row_for(metrics_path):
    run_dir = os.path.dirname(metrics_path)
    overall = load_json(metrics_path).get("metrics", {}).get("overall", {})
    manifest_path = os.path.join(run_dir, "manifest.json")
    manifest = load_json(manifest_path) if os.path.exists(manifest_path) else {}
    return {
        "system": "Linkence",
        "dataset": manifest.get("dataset_name", ""),
        "subset": manifest.get("subset_name", os.path.basename(run_dir)),
        "n_queries": overall.get("count", ""),
        "top_k": manifest.get("top_k", ""),
        "strict_section_acc@1": overall.get("strict_section_hit@1", ""),
        "strict_section_acc@3": overall.get("strict_section_hit@3", ""),
        "strict_section_acc@5": overall.get("strict_section_hit@5", ""),
        "strict_section_acc@10": overall.get("strict_section_hit@10", ""),
        "strict_section_acc@20": overall.get("strict_section_hit@20", ""),
        "relaxed_doc_acc@10": overall.get("relaxed_doc_hit@10", ""),
        "mrr@10": overall.get("mrr@10", ""),
        "ndcg@10": overall.get("ndcg@10", ""),
        "embedding_model": manifest.get("embedding_model_used", ""),
        "reranker": manifest.get("reranker_used", ""),
        "latency_p50_ms": overall.get("latency_p50", ""),
        "latency_p95_ms": overall.get("latency_p95", ""),
        "code_commit_sha": manifest.get("code_commit_sha", ""),
        "run_datetime_utc": manifest.get("run_datetime_utc", ""),
    }


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo_root(), "leaderboard.csv")
    metrics_files = sorted(glob.glob(os.path.join(repo_root(), "results", "*", "metrics.json")))
    if not metrics_files:
        print("No results/*/metrics.json found.", file=sys.stderr)
        sys.exit(1)
    rows = [row_for(path) for path in metrics_files]
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print("Wrote %s (%d runs)" % (out_path, len(rows)))


if __name__ == "__main__":
    main()
