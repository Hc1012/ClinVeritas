# E1 → E1b Prompt Sensitivity Summary

> **Revised version.** The original summary reported E1b as a substantial improvement based on
> 4-way accuracy. Under the honest primary metric (3-way, insufficient-F1 headline), E1b is a
> regression on the safety-relevant class. This version reports that. Numbers reproducible via
> `recompute_e1_metrics.py`.

## Purpose

Compare the E1 automated-rater pilot with the E1b prompt-controlled run. The E1b prompt added
one instruction: prefer `S` over `S*` for ordinary support, reserving `S*` for genuine inference.

Both runs used the same 219-row set and transcript-only blind inputs. Run provenance:
`RUN_PROVENANCE.md` (chat interface, not controlled API). **Both prompts were developed using
error analysis on this same evaluation set — gains are in-sample, not demonstrated generalisation.**

## Headline — 3-way (Grounded / Insufficient / Contradicted)

| Metric | E1 | E1b |
|---|---:|---:|
| Accuracy | **0.840** | 0.804 |
| Macro-F1 | **0.696** | 0.645 |
| **Insufficient-F1** | **0.708** | **0.386** |
| Contradicted-F1 | 0.476 | **0.667** |

The E1b prompt fixed the `S`/`S*` overuse it targeted, but as a side effect roughly **halved
insufficient-detection F1** by collapsing broad consent claims into `S`. It is better on
contradiction, worse on the class that matters most.

## Why 4-way accuracy is misleading here

| Metric | E1 | E1b |
|---|---:|---:|
| 4-way accuracy | 0.475 | 0.776 |
| 4-way macro-F1 | 0.452 | 0.541 |

The 4-way accuracy jump is almost entirely the S\* → S correction (E1 predicted `S*` 94×; E1b
once). `S*` is a 7-instance protocol bookkeeping label, not a capability. Scoring it as a class
lets a naming convention masquerade as a capability change. The 3-way table above is the honest
comparison.

## Prediction distribution shift

| Label | Gold | E1 pred | E1b pred |
|---|---:|---:|---:|
| `S` | 153 | 67 | 193 |
| `S*` | 7 | 94 | 1 |
| `I` | 44 | 52 | 13 |
| `C` | 15 | 6 | 12 |

E1b's `I` predictions dropped from 52 to 13 — the visible trace of the insufficiency regression.

## The real takeaway

Different prompts expose different failure modes, and **the one metric that would have called
E1b a clean win (4-way accuracy) is the one that hides the regression that matters.**

- E1 failure mode: overuse of `S*` (a labelling-convention error).
- E1b failure mode: overuse of `S` on broad consent attestations (a *safety-relevant* error —
  accepting ungrounded "understands and agrees" claims).

This is direct evidence for ClinVeritas's core claim: clinical grounding needs fine-grained,
safety-aware evaluation, because coarse metrics reward the wrong behaviour.

## Next experiment

E1c tests whether a consent-specific rule can undo E1b's consent over-support, while keeping the
S/S\* fix — see `E1c_RESULTS_CONSENT_STRESS_PILOT.md`.
