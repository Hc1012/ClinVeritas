# E1c Consent-Stress Rows 041–060 Score Report

## Format validation

- Parsed rows: 20
- JSON parse errors: 0
- Duplicate eval IDs: 0
- Missing expected IDs: 0
- Extra IDs: 0
- Invalid labels: 0

## Score

- Scored rows: 20 / 20
- Accuracy: 0.950
- Macro-F1: 0.469
- Gold counts: {'S': 15, 'I': 5}
- Prediction counts: {'S': 14, 'I': 6}
- Disagreements: 1

## Per-label metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| S | 1.000 | 0.933 | 0.966 | 15 |
| S* | 0.000 | 0.000 | 0.000 | 0 |
| I | 0.833 | 1.000 | 0.909 | 5 |
| C | 0.000 | 0.000 | 0.000 | 0 |
| Macro | — | — | 0.469 | — |

## Confusion matrix

Rows = gold label, columns = predicted label.

| Gold \ Pred | S | S* | I | C |
|---|---:|---:|---:|---:|
| S | 14 | 0 | 1 | 0 |
| S* | 0 | 0 | 0 | 0 |
| I | 0 | 0 | 5 | 0 |
| C | 0 | 0 | 0 | 0 |

## Disagreements

- `CONSENT_C015`: model `I` vs gold `S` — Patient Agreements: The patient understands and agrees with the recommended medical treatment plan.

## Comparison with earlier runs on same rows

| Run | Accuracy | Notes |
|---|---:|---|
| E1 original prompt | 0.350 | Heavy `S*` overuse |
| E1b prompt-controlled | 0.800 | Improved `S*`, still permissive on broad consent |
| E1c consent-stress | 0.950 | Stricter broad-consent insufficiency prompt |
