#!/usr/bin/env python3
"""Recompute retrieval metrics directly from a published retrieval_results.jsonl.

This script needs no API keys and no access to the Linkence engine. It lets
anyone independently verify the headline accuracy numbers from the raw
per-query results we publish.

Usage:
    python compute_metrics.py results/open_ragbench_diverse500/retrieval_results.jsonl
    python compute_metrics.py <jsonl> --check results/.../metrics.json
    python compute_metrics.py <jsonl> --per-query-csv per_query.csv
"""
import argparse
import csv
import json
import math
import sys

K_LIST = [1, 3, 5, 10, 20]


def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def percentile(values, pct):
    if not values:
        return None
    ordered = sorted(values)
    rank = (len(ordered) - 1) * (pct / 100.0)
    low = int(math.floor(rank))
    high = min(low + 1, len(ordered) - 1)
    if low == high:
        return ordered[low]
    return ordered[low] + (ordered[high] - ordered[low]) * (rank - low)


def gold_ranks(row):
    gold_doc = row.get("gold_doc_id")
    gold_section = row.get("gold_section_id")
    results = sorted(row.get("results", []), key=lambda item: item.get("rank", 10 ** 9))
    strict_rank = None
    doc_rank = None
    for res in results:
        same_doc = res.get("returned_doc_id") == gold_doc
        same_section = res.get("returned_section_id") == gold_section
        if doc_rank is None and same_doc:
            doc_rank = res.get("rank")
        if strict_rank is None and same_doc and same_section:
            strict_rank = res.get("rank")
        if strict_rank is not None and doc_rank is not None:
            break
    return strict_rank, doc_rank


def compute(rows):
    count = len(rows)
    if count == 0:
        return {"count": 0}
    max_k = max((len(row.get("results", [])) for row in rows), default=0)
    ks = [k for k in K_LIST if k <= max_k]
    strict = {k: 0 for k in ks}
    relaxed = {k: 0 for k in ks}
    rr10 = rr20 = ndcg10 = 0.0
    zero = 0
    latencies = []
    for row in rows:
        strict_rank, doc_rank = gold_ranks(row)
        if row.get("zero_sources"):
            zero += 1
        latency = row.get("latency_ms")
        if latency is not None:
            latencies.append(latency)
        for k in ks:
            if strict_rank is not None and strict_rank <= k:
                strict[k] += 1
            if doc_rank is not None and doc_rank <= k:
                relaxed[k] += 1
        if strict_rank is not None and strict_rank <= 10:
            rr10 += 1.0 / strict_rank
            ndcg10 += 1.0 / math.log2(strict_rank + 1)
        if strict_rank is not None and strict_rank <= 20:
            rr20 += 1.0 / strict_rank
    out = {"count": count}
    for k in ks:
        out["strict_section_hit@%d" % k] = round(strict[k] / count, 4)
        out["relaxed_doc_hit@%d" % k] = round(relaxed[k] / count, 4)
    out["mrr@10"] = round(rr10 / count, 4)
    if 20 in ks:
        out["mrr@20"] = round(rr20 / count, 4)
    out["ndcg@10"] = round(ndcg10 / count, 4)
    out["zero_source_rate"] = round(zero / count, 4)
    out["latency_p50"] = round(percentile(latencies, 50), 1) if latencies else None
    out["latency_p95"] = round(percentile(latencies, 95), 1) if latencies else None
    out["latency_p99"] = round(percentile(latencies, 99), 1) if latencies else None
    return out


def grouped(rows, key):
    buckets = {}
    for row in rows:
        buckets.setdefault(row.get(key), []).append(row)
    return {str(name): compute(group) for name, group in sorted(buckets.items(), key=lambda kv: str(kv[0]))}


def build_report(rows):
    return {
        "overall": compute(rows),
        "by_source": grouped(rows, "query_source"),
        "by_type": grouped(rows, "query_type"),
    }


def compare(computed, published, tolerance=0.0015):
    mismatches = []

    def walk(path, mine, theirs):
        if isinstance(theirs, dict):
            for key, value in theirs.items():
                if key in mine:
                    walk(path + [key], mine[key], value)
        elif isinstance(theirs, (int, float)) and isinstance(mine, (int, float)):
            if abs(mine - theirs) > tolerance:
                mismatches.append((".".join(path), mine, theirs))

    published_metrics = published.get("metrics", published)
    walk([], computed, published_metrics)
    return mismatches


def write_per_query_csv(rows, path):
    fields = [
        "query_id", "query", "query_type", "query_source", "primary_category",
        "gold_doc_id", "gold_section_id", "top1_doc_id", "top1_section_id",
        "rank_of_gold_section", "rank_of_gold_doc", "matched_section", "matched_doc",
        "latency_ms",
    ]
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            strict_rank, doc_rank = gold_ranks(row)
            results = sorted(row.get("results", []), key=lambda item: item.get("rank", 10 ** 9))
            top1 = results[0] if results else {}
            writer.writerow({
                "query_id": row.get("query_id"),
                "query": row.get("query"),
                "query_type": row.get("query_type"),
                "query_source": row.get("query_source"),
                "primary_category": row.get("primary_category"),
                "gold_doc_id": row.get("gold_doc_id"),
                "gold_section_id": row.get("gold_section_id"),
                "top1_doc_id": top1.get("returned_doc_id"),
                "top1_section_id": top1.get("returned_section_id"),
                "rank_of_gold_section": strict_rank if strict_rank is not None else "",
                "rank_of_gold_doc": doc_rank if doc_rank is not None else "",
                "matched_section": strict_rank is not None,
                "matched_doc": doc_rank is not None,
                "latency_ms": row.get("latency_ms"),
            })


def main():
    parser = argparse.ArgumentParser(description="Recompute retrieval metrics from published JSONL.")
    parser.add_argument("jsonl", help="Path to retrieval_results.jsonl")
    parser.add_argument("--check", metavar="METRICS_JSON", help="Assert recomputed metrics match a published metrics.json")
    parser.add_argument("--per-query-csv", metavar="CSV", help="Write a per-query verification CSV")
    args = parser.parse_args()

    rows = load_jsonl(args.jsonl)
    report = build_report(rows)
    print(json.dumps(report, indent=2))

    if args.per_query_csv:
        write_per_query_csv(rows, args.per_query_csv)
        print("\nWrote per-query CSV -> %s" % args.per_query_csv, file=sys.stderr)

    if args.check:
        with open(args.check, encoding="utf-8") as handle:
            published = json.load(handle)
        mismatches = compare(report, published)
        if mismatches:
            print("\nMISMATCH vs %s:" % args.check, file=sys.stderr)
            for key, mine, theirs in mismatches:
                print("  %-40s recomputed=%s published=%s" % (key, mine, theirs), file=sys.stderr)
            sys.exit(1)
        print("\nOK: recomputed metrics match %s within tolerance." % args.check, file=sys.stderr)


if __name__ == "__main__":
    main()
