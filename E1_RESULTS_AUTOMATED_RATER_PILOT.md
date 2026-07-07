# ClinVeritas E1 Results: Automated-Rater Pilot

> **Revised version.** Reordered to make the 3-way metric (with insufficient-F1 as the
> headline) primary and the 4-way strict metric an appendix, for consistency with the
> corrected E1b/E1c docs. No prediction data changed; all numbers are reproducible via
> `recompute_e1_metrics.py`.

## Status

Preliminary automated-rater pilot over the 219-row ClinVeritas E1 evaluation set. This is a
model-based pilot, **not** human inter-rater reliability and **not** a benchmark leaderboard.
Run provenance: see `RUN_PROVENANCE.md` (rater accessed via chat interface, not a controlled
API). Prompt: `E1_PROMPT_TEMPLATE.md`.

## Evaluation setup

- Evaluation set: 219 ClinVeritas rows (SN40 39, Consent121 121, ACISN75 59).
- Inputs shown to rater: transcript + note claim only (blind file, no labels).
- Gold: internal single-rater author-adjudicated labels.
- Validation: 219/219 parsed, 0 JSON errors, 0 missing/dup/extra IDs, 0 invalid labels.

## Why the primary metric is 3-way

`S*` (supported-via-tagged-inference) is a protocol bookkeeping distinction with only 7 gold
instances, not a capability to score as its own class. The honest primary task is three-way —
**Grounded (S ∪ S\*) / Insufficient / Contradicted** — with **Insufficient-F1 as the headline**.
4-way strict metrics are retained as an appendix.

## Primary result — 3-way

| Metric | Score |
|---|---:|
| Accuracy | 0.840 |
| Macro-F1 | 0.696 |
| **Insufficient-F1 (headline)** | **0.708** |
| Contradicted-F1 | 0.476 |
| Grounded-F1 | 0.903 |

Read plainly: the E1 pilot detects grounding well, detects insufficiency reasonably (0.708),
and is weakest on contradiction (0.476) — it under-calls the outright-wrong claims.

## Per-label metrics (3-way, P / R / F1)

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Grounded (S∪S\*) | 0.901 | 0.906 | 0.903 | 160 |
| Insufficient | 0.654 | 0.773 | 0.708 | 44 |
| Contradicted | 0.833 | 0.333 | 0.476 | 15 |

## Confusion matrix (4-way, for detail)

Rows = gold, cols = predicted:

| Gold \ Pred | `S` | `S*` | `I` | `C` |
|---|---:|---:|---:|---:|
| `S` | 62 | 78 | 12 | 1 |
| `S*` | 2 | 3 | 2 | 0 |
| `I` | 1 | 9 | 34 | 0 |
| `C` | 2 | 4 | 4 | 5 |

The dominant pattern is `S` → `S*` (78 rows): the rater recognised grounding but over-attributed
it to inference. That is a *labelling-convention* confusion, invisible once S and S\* are
collapsed — which is exactly why the 3-way metric is the honest one.

## Baseline context (3-way)

| System | Accuracy | Macro-F1 | Insufficient-F1 |
|---|---:|---:|---:|
| Majority-`S` baseline | 0.731 | 0.281 | 0.000 |
| E1 pilot | 0.840 | 0.696 | 0.708 |

The majority baseline gets 0 on insufficiency and contradiction by construction; it exists only
to show the dataset is `S`-heavy and that raw accuracy alone is a poor measure here.

## Batch-level (3-way accuracy)

| Batch | N | 3-way accuracy |
|---|---:|---:|
| sn40 | 39 | see recompute script |
| consent121 | 121 | see recompute script |
| acisn75 | 59 | see recompute script |

(Per-batch 3-way numbers are printed by `recompute_e1_metrics.py --by-batch`; left to the script
so this doc never drifts from the data.)

## Appendix — 4-way strict metrics (secondary)

| Metric | Score |
|---|---:|
| 4-way accuracy | 0.475 |
| 4-way macro-F1 | 0.452 |

4-way is dragged down by S\*-F1 = 0.059 (support 7), a bookkeeping-class artefact.

## Interpretation

The E1 pilot's two honest findings: (1) the S/S\* boundary is where an unguided rater stumbles
most, motivating the E1b prompt experiment; (2) contradiction detection is the weakest of the
three real classes. Both are inputs to later experiments, not benchmark claims.

## Limitations

- Single automated rater via chat interface; not controlled API, not κ.
- Gold labels single-rater author-adjudicated, pending κ study.
