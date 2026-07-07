# ClinVeritas E1c Results: Consent-Stress Prompt-Controlled Pilot

> **Revised version.** Adds the honest 3-way view of the E1 → E1b → E1c arc on this slice, an
> explicit in-sample-tuning caveat, and a caveat on the headline pull-quote. Numbers reproducible
> via `recompute_e1_metrics.py`.

## Status

Small consent-stress prompt-controlled pilot over **20 rows** (041–060, a consent-heavy slice).
Automated-rater prompt-sensitivity experiment — **not** human inter-rater reliability, **not** a
219-row benchmark result. Run provenance: `RUN_PROVENANCE.md` (chat interface, not controlled API).
Prompt: `E1c_PROMPT_TEMPLATE.md`.

**In-sample tuning caveat — read before quoting any number here.** The E1c prompt was written
specifically to fix E1b's consent failure, and it was evaluated on a slice *chosen because it
contains that failure*. This is prompt-fitting to a known weakness on a known slice. It
demonstrates that a targeted rule *can* address the failure; it does **not** estimate
generalisation. Treat E1c as a proof-of-mechanism, not a score.

## Prompt-control change

E1c kept E1b's `S`/`S*` fix and added consent-specific rules: broad "understands and agrees"
claims may not be labelled `S` from generic cooperation, politeness, minimal acknowledgement, or
passive continuation alone; they require explicit acceptance, option selection, teach-back, or
clear plan agreement.

## The honest arc on this slice — 3-way (Grounded / Insufficient)

This slice contains only `S` (15) and `I` (5) in the gold — no `C`, no `S*` — so 3-way here is
effectively Grounded vs Insufficient.

| Run | 3-way accuracy | 3-way macro-F1 | Insufficient-F1 | Insufficient-recall |
|---|---:|---:|---:|---:|
| E1 | 0.900 | 0.867 | 0.800 | 0.800 |
| E1b | 0.800 | 0.608 | 0.333 | **0.200** |
| E1c | 0.950 | 0.938 | 0.909 | 1.000 |

The arc is not "steady improvement." It is: **E1 already handled this slice well (0.90); E1b
broke it (insufficient-recall collapsed to 0.20 — it accepted 4 of 5 ungrounded consent claims);
E1c repaired E1b's self-inflicted damage (0.95).** E1c's value is undoing a regression that E1b
introduced, not surpassing a baseline that struggled.

## E1c confusion matrix (this slice)

Rows = gold, cols = predicted:

| Gold \ Pred | `S` | `I` |
|---|---:|---:|
| `S` | 14 | 1 |
| `I` | 0 | 5 |

E1c caught all 5 ungrounded consent claims (0 gold-`I` leaked to `S`), at the cost of one
over-cautious `S` → `I`.

## Main finding

Broad consent attestations need an *explicit* evidentiary rule. A general "don't overuse `S*`"
instruction (E1b) is not only insufficient for consent — it actively worsens consent insufficiency
detection. A consent-specific rule (E1c) restores it on this slice.

## On the pull-quote

If you quote a single line from this pilot, quote it **with its limits attached**, e.g.:

> On a 20-row, in-sample-tuned consent-stress slice, a consent-specific evidence rule restored
> insufficient-detection recall from 0.20 (E1b) to 1.00 (E1c), recovering ground that the E1b
> prompt had lost relative to E1.

Do **not** circulate a bare "80% → 95% accuracy" figure: it is 20 rows, in-sample-tuned, two
active classes, and the accuracy framing hides that E1b's real problem was insufficient-recall.

## Limitations

- 20 rows; in-sample-tuned on a slice selected for the target failure.
- Not scaled to 219; not a benchmark result until run on held-out rows.
- Single automated rater via chat interface; not controlled API, not κ.

## Recommended next step

Freeze the E1c prompt and evaluate it, unchanged, on rows the prompt was **not** tuned against —
ideally future Stage-2 generated rows or the κ-study additions — to get the first out-of-sample
estimate. Only that number is quotable as generalisation.
