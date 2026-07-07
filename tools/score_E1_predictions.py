#!/usr/bin/env python3
import argparse, json
from collections import Counter, defaultdict

VALID = {"S", "S*", "I", "C"}

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows

def norm_label(x):
    if x is None:
        return ""
    x = str(x).strip().upper()
    aliases = {
        "SUPPORTED": "S",
        "SUPPORT": "S",
        "SUPPORTED WITH INFERENCE": "S*",
        "SUPPORTED_WITH_INFERENCE": "S*",
        "S_STAR": "S*",
        "INSUFFICIENT": "I",
        "NEI": "I",
        "NOT ENOUGH INFO": "I",
        "CONTRADICTED": "C",
        "CONTRADICTION": "C",
    }
    return aliases.get(x, x)

def per_label_metrics(labels, y_true, y_pred):
    out = {}
    for lab in labels:
        tp = sum(1 for a,b in zip(y_true,y_pred) if a == lab and b == lab)
        fp = sum(1 for a,b in zip(y_true,y_pred) if a != lab and b == lab)
        fn = sum(1 for a,b in zip(y_true,y_pred) if a == lab and b != lab)
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2*prec*rec/(prec+rec) if prec+rec else 0.0
        out[lab] = {"precision": prec, "recall": rec, "f1": f1, "support": sum(1 for a in y_true if a == lab)}
    out["macro_f1"] = sum(out[lab]["f1"] for lab in labels) / len(labels)
    return out

def score_subset(rows):
    y_true = [r["gold_label"] for r in rows]
    y_pred = [r["pred_label"] for r in rows]
    labels = ["S", "S*", "I", "C"]
    return {
        "n": len(rows),
        "accuracy": sum(a == b for a,b in zip(y_true,y_pred)) / len(rows) if rows else 0.0,
        "gold_counts": dict(Counter(y_true)),
        "pred_counts": dict(Counter(y_pred)),
        "metrics": per_label_metrics(labels, y_true, y_pred),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", required=True)
    ap.add_argument("--pred", required=True, help="JSONL with eval_id and label")
    ap.add_argument("--out", default="E1_scores.json")
    args = ap.parse_args()

    gold = {r["eval_id"]: r for r in load_jsonl(args.gold)}
    preds = {r.get("eval_id"): r for r in load_jsonl(args.pred)}

    joined = []
    missing, invalid = [], []
    for eid, g in gold.items():
        p = preds.get(eid)
        if not p:
            missing.append(eid)
            continue
        lab = norm_label(p.get("label") or p.get("pred_label") or p.get("prediction"))
        if lab not in VALID:
            invalid.append({"eval_id": eid, "label": lab})
            continue
        joined.append({**g, "pred_label": lab})

    scores = score_subset(joined)
    scores["n_gold"] = len(gold)
    scores["n_scored"] = len(joined)
    scores["missing"] = missing
    scores["invalid"] = invalid

    by_batch = defaultdict(list)
    by_type = defaultdict(list)
    for r in joined:
        by_batch[r["batch"]].append(r)
        by_type[r["candidate_type"]].append(r)

    scores["by_batch"] = {k: score_subset(v) for k,v in by_batch.items()}
    scores["by_candidate_type"] = {k: score_subset(v) for k,v in by_type.items()}

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)

    print(json.dumps(scores, indent=2))

if __name__ == "__main__":
    main()
