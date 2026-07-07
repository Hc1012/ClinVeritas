#!/usr/bin/env python3
"""Recompute ClinVeritas E1/E1b/E1c metrics from committed prediction files.

Reports BOTH the 4-way strict metric and the honest 3-way metric (S and S* collapsed
to "grounded"), because S* is a labelling-protocol bookkeeping distinction (7 gold
instances) rather than a capability to score as its own class. The 3-way metric, with
insufficient-F1 as the headline, is the primary result of the project.

Layout-aware: works from the repo root with the foldered layout (e1/, e1/runs/...,
e1/baselines/) and also with a flat layout; falls back to a recursive search by
filename. Every number in the E1 results documents is reproducible with this script.

Usage (from repo root):
  python tools/recompute_e1_metrics.py
  python tools/recompute_e1_metrics.py --by-batch
"""
import argparse, json, os, sys
from collections import Counter
from pathlib import Path

GOLD_NAMES = [
    "clinveritas_E1_gold_labels_WITH_TEXT.jsonl",
    "clinveritas_E1_gold_internal_WITH_TEXT.jsonl",  # legacy name
]
RUN_NAMES = {
    "E1":  "E1_AUTOMATED_RATER_FULL219_PREDICTIONS_MERGED.jsonl",
    "E1b": "E1b_AUTOMATED_RATER_FULL219_PREDICTIONS_MERGED.jsonl",
    "majority_S": "majority_S_predictions.jsonl",
}
E1C_NAME = "E1c_CONSENT_STRESS_ROWS_041_060_PREDICTIONS.jsonl"
SEARCH_DIRS = [".", "e1", "e1/runs/e1", "e1/runs/e1b", "e1/runs/e1c", "e1/baselines"]


def resolve(name):
    for d in SEARCH_DIRS:
        p = Path(d) / name
        if p.exists():
            return str(p)
    hits = list(Path(".").rglob(name))
    return str(hits[0]) if hits else None


def load_gold(path):
    g, meta = {}, {}
    for line in open(path):
        d = json.loads(line)
        g[d["eval_id"]] = d["gold_label"]
        meta[d["eval_id"]] = {"batch": d.get("batch"), "candidate_type": d.get("candidate_type")}
    return g, meta


def load_pred(path):
    return {json.loads(l)["eval_id"]: json.loads(l)["label"] for l in open(path)}


def score(gold, pred, ids, collapse):
    def c(l):
        return "S" if (collapse and l in ("S", "S*")) else l
    ids = [i for i in ids if i in pred]
    n = len(ids)
    acc = sum(c(gold[i]) == c(pred[i]) for i in ids) / n if n else 0.0
    label_space = sorted({c(gold[i]) for i in ids} | {c(pred[i]) for i in ids})
    per = {}
    for L in label_space:
        tp = sum(c(pred[i]) == L and c(gold[i]) == L for i in ids)
        fp = sum(c(pred[i]) == L and c(gold[i]) != L for i in ids)
        fn = sum(c(pred[i]) != L and c(gold[i]) == L for i in ids)
        p = tp / (tp + fp) if tp + fp else 0.0
        r = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * p * r / (p + r) if p + r else 0.0
        per[L] = (round(p, 3), round(r, 3), round(f1, 3))
    gold_only = sorted({c(gold[i]) for i in ids})
    macro = round(sum(per[L][2] for L in gold_only) / len(gold_only), 3) if gold_only else 0.0
    return round(acc, 3), macro, per, n


def report(title, gold, pred, ids):
    a4, m4, p4, n = score(gold, pred, ids, collapse=False)
    a3, m3, p3, _ = score(gold, pred, ids, collapse=True)
    print(f"\n=== {title} (n={n}) ===")
    print(f"  PRIMARY 3-way (S*=S):  acc={a3}  macro-F1={m3}")
    if "I" in p3:
        print(f"    -> Insufficient-F1 (HEADLINE) = {p3['I'][2]}  (P={p3['I'][0]} R={p3['I'][1]})")
    if "C" in p3:
        print(f"    -> Contradicted-F1 = {p3['C'][2]}  Grounded-F1 = {p3.get('S',(0,0,0))[2]}")
    print(f"  appendix 4-way strict: acc={a4}  macro-F1={m4}")
    print(f"    per-class 4-way (P,R,F1): {p4}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gold", default=None)
    ap.add_argument("--by-batch", action="store_true")
    args = ap.parse_args()

    gold_path = args.gold or next((p for p in (resolve(n) for n in GOLD_NAMES) if p), None)
    if not gold_path or not os.path.exists(gold_path):
        sys.exit(f"ERROR: gold file not found (searched {SEARCH_DIRS} and recursively). Pass --gold.")

    gold, meta = load_gold(gold_path)
    all_ids = list(gold)
    print(f"Gold: {gold_path}  ({len(gold)} rows)  distribution={dict(Counter(gold.values()))}")

    run_paths = {}
    for name, fname in RUN_NAMES.items():
        p = resolve(fname)
        if p:
            run_paths[name] = p
            report(name, gold, load_pred(p), all_ids)
        else:
            print(f"\n(skip {name}: {fname} not found)")

    e1c_path = resolve(E1C_NAME)
    if e1c_path:
        e1c = load_pred(e1c_path)
        slice_ids = list(e1c)
        print(f"\n\n########## E1c consent-stress slice (n={len(slice_ids)}, rows 041-060) ##########")
        print(f"gold on slice = {dict(Counter(gold[i] for i in slice_ids if i in gold))}")
        for name in ("E1", "E1b"):
            if name in run_paths:
                report(f"{name} on E1c slice", gold, load_pred(run_paths[name]), slice_ids)
        report("E1c on E1c slice", gold, e1c, slice_ids)

    if args.by_batch:
        print("\n\n########## Per-batch, 3-way ##########")
        for name in ("E1", "E1b"):
            if name not in run_paths:
                continue
            pred = load_pred(run_paths[name])
            print(f"\n--- {name} ---")
            for b in sorted({m["batch"] for m in meta.values()}):
                bids = [i for i in all_ids if meta[i]["batch"] == b]
                a3, m3, p3, n = score(gold, pred, bids, collapse=True)
                iF1 = p3.get("I", (0, 0, 0))[2]
                print(f"  {b:12s} n={n:3d}  3-way acc={a3}  macro-F1={m3}  I-F1={iF1}")

    print("\nNote: 3-way (Grounded/Insufficient/Contradicted) is the PRIMARY metric; "
          "insufficient-F1 is the headline. 4-way is retained only for completeness.")


if __name__ == "__main__":
    main()
