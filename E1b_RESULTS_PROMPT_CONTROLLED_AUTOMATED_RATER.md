# ClinVeritas E1b Results: Prompt-Controlled Automated-Rater Run

> **Correction notice (this is the revised version of this document).**
> The original version headlined a 4-way strict-accuracy jump (0.475 → 0.776) as the main
> E1b result. That framing was misleading: the jump came almost entirely from fixing a
> *label-taxonomy* convention (S vs S\*), not from improved grounding judgement. Under the
> honest primary metric (3-way, with insufficient-F1 as the headline — matching RepoVeritas),
> **E1b is not an improvement over E1; on the capability the benchmark exists to measure,
> it is a regression.** This document reports the corrected result. All numbers are
> reproducible via `recompute_e1_metrics.py`.

## Status

Prompt-controlled automated-rater run over the full 219-row ClinVeritas E1 evaluation set.
This is a model-based prompt-sensitivity experiment, **not** human inter-rater reliability
and **not** a benchmark leaderboard result. Run provenance: see `RUN_PROVENANCE.md`
(the rater was accessed through a chat interface, not a controlled API — this is not a
controlled benchmark).

E1b was created after the E1 pilot showed heavy overuse of `S*`. The E1b prompt (see
`E1b_PROMPT_TEMPLATE.md`) added one instruction: use `S`, not `S*`, when a claim is directly
supported by ordinary wording, normal paraphrase, or normal clinical shorthand; reserve `S*`
for genuine inference.

**In-sample caveat:** the E1b prompt was written from error analysis performed on this same
219-row set. Any gain is in-sample prompt-fitting, not demonstrated generalisation.

## Why the primary metric is 3-way, not 4-way

`S*` ("supported via a tagged inference") is a **bookkeeping distinction in the labelling
protocol**, not a natural capability a rater should be scored on as a separate class. It has
only **7 gold instances in 219 rows**. Scoring it as a 4th class lets a labelling-convention
artefact dominate macro-F1 (in E1, S\*-F1 = 0.059). The honest primary task is three-way —
**Grounded (S ∪ S\*) / Insufficient / Contradicted** — with **Insufficient-F1 as the headline
metric**, because abstention detection is the safety-relevant capability and the reason this
benchmark exists. The 4-way numbers are retained below as an appendix.

## Primary result — 3-way (Grounded / Insufficient / Contradicted)

| Metric | E1 | E1b | Change |
|---|---:|---:|---|
| Accuracy | **0.840** | 0.804 | ▼ −0.036 |
| Macro-F1 | **0.696** | 0.645 | ▼ −0.051 |
| **Insufficient-F1 (headline)** | **0.708** | **0.386** | ▼▼ **−0.322** |
| Contradicted-F1 | 0.476 | **0.667** | ▲ +0.191 |
| Grounded-F1 | 0.903 | 0.881 | ▼ −0.022 |

The headline: **the E1b prompt roughly halved insufficient-detection F1.** It improved
contradiction detection and left grounding roughly flat, but the net effect on the class that
matters most is a large regression. E1b is better *only* on contradiction and *only* if you
ignore insufficiency.

## The mechanism — one instruction, one side effect

The E1b instruction ("prefer `S` for ordinary support") did what it was told, and then kept
going: the rater collapsed toward `S` on rows where the gold label was `I`. The confusion
matrices make it concrete.

E1 (Gold I row): `I` predicted correctly 34/44; only 1 gold-`I` row leaked to `S`.
E1b (Gold I row): `I` predicted correctly **11/44**; **33 gold-`I` rows leaked to `S`.**

Those 33 rows are overwhelmingly **broad consent attestations** — "patient understands and
agrees" claims that the transcript does not actually support. The E1b prompt made the rater
more willing to accept ordinary conversational cooperation as full plan agreement. That is the
exact failure ClinVeritas was built to catch, re-introduced by a prompt tweak aimed at a
different problem.

## Confusion matrices

E1b, rows = gold, cols = predicted:

| Gold \ Pred | `S` | `S*` | `I` | `C` |
|---|---:|---:|---:|---:|
| `S` | 149 | 0 | 1 | 3 |
| `S*` | 6 | 1 | 0 | 0 |
| `I` | 33 | 0 | 11 | 0 |
| `C` | 5 | 0 | 1 | 9 |

## Baseline context (3-way)

| System | Accuracy | Macro-F1 | Insufficient-F1 |
|---|---:|---:|---:|
| Majority-`S` baseline | 0.731 | 0.281 | 0.000 |
| E1 | 0.840 | 0.696 | 0.708 |
| E1b | 0.804 | 0.645 | 0.386 |

Note that E1b's insufficient-F1 (0.386) is well above the baseline's floor of 0, so it still
detects *some* insufficiency — but it gave back nearly half of E1's ability to do so.

## Appendix — 4-way strict metrics (secondary)

Retained for completeness; the S/S\* split makes this a weaker measure of the actual task.

| Metric | E1 | E1b |
|---|---:|---:|
| 4-way accuracy | 0.475 | 0.776 |
| 4-way macro-F1 | 0.452 | 0.541 |

The 4-way accuracy rise (0.475 → 0.776) is almost entirely the S* → S correction: E1 predicted
`S*` 94 times, E1b predicted it once. This is taxonomy compliance, not grounding skill.

## Interpretation

E1b's real lesson is a strong result *for* ClinVeritas, once told honestly: **a prompt change
that fixed surface-level label compliance actively degraded the safety-relevant capability**,
and the degradation was invisible under 4-way accuracy but obvious under insufficient-F1.
Fine-grained, safety-aware evaluation is not optional for this task — a single vanity metric
would have reported E1b as a clean win while the model quietly got worse at the thing that
matters. The E1c pilot (next) tests whether a consent-specific rule can undo this specific
side effect.

## Limitations

- Single automated rater via chat interface; not a controlled API benchmark, not κ.
- Prompt developed in-sample on these 219 rows; gains are not demonstrated generalisation.
- Gold labels are single-rater author-adjudicated, pending the κ study.
