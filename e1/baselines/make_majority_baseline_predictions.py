#!/usr/bin/env python3
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="blind JSONL")
    ap.add_argument("--label", default="S", choices=["S","S*","I","C"])
    ap.add_argument("--out", default="majority_baseline_predictions.jsonl")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as fin, open(args.out, "w", encoding="utf-8") as fout:
        for line in fin:
            if not line.strip():
                continue
            r = json.loads(line)
            fout.write(json.dumps({
                "eval_id": r["eval_id"],
                "label": args.label,
                "severity": None,
                "tags": [],
                "rationale": "Majority baseline."
            }) + "\n")

if __name__ == "__main__":
    main()
