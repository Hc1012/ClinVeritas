# ClinVeritas E1 Prompt Template

Use this template for each model call.

## System / instruction

You are labelling a clinical-note claim against a consultation transcript.

Assign exactly one label:

- S = Supported: the transcript entails the claim.
- S* = Supported with tagged inference: the claim is supported only through a clearly valid inference under the ClinVeritas rules.
- C = Contradicted: the transcript asserts a competing or opposite fact.
- I = Insufficient: the transcript neither supports nor contradicts the claim.

Use semantic reading, not keyword matching. Generic acknowledgements such as "okay" or "no questions" do not automatically prove broad consent/agreement. For safety-netting, distinguish patient-directed advice from clinician contingency planning.

Return JSON only:
{
  "eval_id": "...",
  "label": "S|S*|I|C",
  "severity": "benign|relevant|treatment-changing|null",
  "tags": ["..."],
  "rationale": "short evidence-grounded explanation"
}

## Input

eval_id: {eval_id}

transcript:
{transcript}

note claim:
{claim}
