# ClinVeritas E1 Evaluation Dataset v2 — RUNNABLE

This replaces an earlier v1 scaffold (not committed). v2 is the runnable E1 dataset because it
includes the **full transcript text** needed for model evaluation.

## Dataset size

Included rows: **219**

| Batch | Rows |
|---|---:|
| SN40 | 39 |
| Consent121 | 121 |
| ACISN75 | 59 |

Gold label distribution: {'C': 15, 'S': 153, 'I': 44, 'S*': 7}

## Files (paths relative to the repo root)

- `e1/clinveritas_E1_model_input_BLIND_WITH_TEXT.jsonl` — send this to models. Transcripts and claims, no labels.
- `e1/clinveritas_E1_gold_labels_WITH_TEXT.jsonl` — the answer key. It is public in this repository (see the contamination note in the main README), but it must **never** be included in model inputs when running an evaluation.
- `e1/clinveritas_E1_index.csv` — quick inspection table.
- `e1/prompts/` — the three verbatim prompts (E1, E1b, E1c).
- `tools/score_E1_predictions.py` — scoring script.
- `tools/make_majority_baseline_predictions.py` — sanity baseline.
- `tools/recompute_e1_metrics.py` — regenerates every number in the E1 results docs (3-way primary + 4-way appendix).

## Run the sanity baseline (from the repo root)

```bash
python tools/make_majority_baseline_predictions.py \
    --input e1/clinveritas_E1_model_input_BLIND_WITH_TEXT.jsonl \
    --label S --out e1/baselines/majority_S.jsonl

python tools/score_E1_predictions.py \
    --gold e1/clinveritas_E1_gold_labels_WITH_TEXT.jsonl \
    --pred e1/baselines/majority_S.jsonl --out e1/baselines/majority_S_scores.json
```

## Reproduce all reported E1/E1b/E1c numbers

```bash
python tools/recompute_e1_metrics.py --by-batch
```

## Expected prediction format

One JSON object per line:

```json
{"eval_id":"SN40_001","label":"C","severity":"relevant","tags":["range violation"],"rationale":"..."}
```

Valid labels: `S`, `S*`, `I`, `C`. Note that scoring is reported primarily **3-way** (S and S\*
collapsed to "grounded"), with insufficient-F1 as the headline; 4-way strict is an appendix metric.

## Provenance and caveats

- Gold labels are **adjudicated single-rater labels** (author-adjudicated under the frozen
  protocol + amendments). Suitable for internal pilot experiments, not a final benchmark release
  until an independent second-rater κ study is completed.
- How the committed E1/E1b/E1c automated-rater runs were produced (model, interface, blinding,
  limitations): see [`RUN_PROVENANCE.md`](../RUN_PROVENANCE.md).
