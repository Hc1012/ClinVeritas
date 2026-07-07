# Run Provenance — E1 / E1b / E1c automated-rater experiments

> **This file is the single source of truth for how the automated-rater runs were produced.**
> It is deliberately explicit about limitations. These runs are prompt-sensitivity experiments,
> not human inter-rater reliability and not a controlled API leaderboard.

## Rater configuration

| Field | Value |
|---|---|
| Rater model + version | OpenAI ChatGPT chat UI; exact backend model/version not API-pinned and should be treated as unknown. |
| Provider / interface | OpenAI ChatGPT chat interface with file upload/download workflow, not API. |
| Decoding settings | Unknown; chat-interface defaults, no fixed temperature/top-p/seed exposed or recorded. |
| Run dates | July 2026, during the ClinVeritas repair/evaluation workflow. |
| Account / workspace | Hadi Chamas's ChatGPT account. |

## Execution protocol

| Field | Value |
|---|---|
| Chunking | E1 and E1b full runs used 219 rows split into 11 JSONL chunks of ~20 rows each, then merged. E1c was a 20-row consent-stress slice, rows 041–060. |
| One row = one call, or batched? | Batched by chunk: one prompt/file request per chunk, producing one JSONL output file per chunk. |
| Prompt used | E1: `E1_PROMPT_TEMPLATE.md`. E1b: `E1b_PROMPT_TEMPLATE.md`. E1c: `E1c_PROMPT_TEMPLATE.md`. |
| Re-runs / retries on any chunk? | The reported E1/E1b/E1c files are the committed JSONL outputs for their prompt condition. Earlier small pilot runs were used to test the pipeline/prompt style and are not reported as the full E1 result. No post-hoc editing of prediction labels was performed after scoring. |

## Isolation from gold labels

| Field | Value |
|---|---|
| Were rater sessions separate from sessions where labels/adjudications were discussed? | Yes at the chat-session level: E1/E1b/E1c rater prompts were run in separate chat sessions from the scoring/gold-analysis chat. |
| Did rater sessions receive gold labels, private comparison CSVs, score reports, or answer keys? | No. The rater sessions received the prompt template plus blind transcript + note_claim JSONL chunks only. |
| Did the blind input file include gold labels, severities, or tags? | No. `clinveritas_E1_model_input_BLIND_WITH_TEXT.jsonl` contains transcript + claim inputs only. |
| Account-level memory / cross-chat contamination risk | Unknown/not independently verified. Because the chat UI was used rather than an API-isolated run, account-level memory or hidden system behaviour cannot be ruled out. Treat the runs as prompt-sensitivity evidence, not clean model-capability benchmarks. |

## Validity caveat

The E1/E1b/E1c runs are useful for showing how automated-rater behaviour changes under prompt
variants. They should not be reported as:

- human inter-rater reliability;
- independent second-rater κ;
- a controlled API benchmark;
- a leaderboard-quality model-capability evaluation.

They may be reported as:

- a blind-input automated-rater prompt-sensitivity study;
- an in-sample prompt analysis over the committed E1-219 set;
- evidence that insufficiency detection is fragile under prompt changes.

## Gold-label provenance

The gold labels are author-adjudicated internal benchmark labels produced under the ClinVeritas
labelling protocol and amendments. LLM tools were used for workflow scaffolding, document drafting,
candidate-location support, and audit assistance; committed model-prediction JSONL files are model
outputs under evaluation, not ground truth. A separate independent human-rater κ study remains future
work.

## Note on earlier pilots

An early small pilot was used only to check whether JSONL outputs could be produced and scored. The
reported E1/E1b/E1c result files are the committed merged prediction files named in the results docs.
