# ClinVeritas Guidelines Amendment v1.2 — ACI-Bench Consent Attestations

Applies to the ACI-Bench consent-attestation batch (`consent121`). This amendment does not replace Labelling Guidelines v1 or SN40 v1.1; it adds consent-specific operational rules forced by the 121-row ACI-Bench pass.

## Consent-A1 — Separate narrow question-answer claims from broad consent claims

`All questions were answered` is a narrower claim than `patient understands and agrees with the recommended treatment plan`.

- If the transcript shows the patient asked a question, the clinician answered it, and no unresolved question remains, label the narrow question-answer claim **S**.
- Do **not** require global plan agreement to support the narrow question-answer claim.
- If a row contains both `all questions answered` and `understands/agrees`, split them under R2. A supported question-answer component does not automatically support the broader consent/agreement component.

Anchor: C005 changed from **I → S** because the patient asked whether tramadol was okay with digoxin, the clinician answered, then the patient denied further questions. The note claim was only `All questions were answered`.

## Consent-A2 — Generic acknowledgement is not plan agreement

For broad consent/agreement attestations (`patient understands and agrees`, `agrees to the treatment plan`, `verbalizes understanding`), generic responses such as `okay`, `mm-hmm`, `yeah`, `alright`, `thanks`, or `no questions` are not enough by themselves.

A broad consent/agreement claim is **S** only when the transcript contains clear plan uptake, such as:

- direct agreement to the plan (`I agree`, `that sounds good`, `that sounds fine`, `sounds like a plan`, `that works`, `let's do it`);
- direct answer to a plan-soundness check (`does that sound okay?` → `that sounds good/fine/great`);
- patient election of a proposed option;
- teach-back or implementation language showing uptake of the plan.

Otherwise, label the broad attestation **I [template attestation]**, severity usually `relevant` unless a treatment-changing consent component is involved.

## Consent-A3 — Risks/benefits/signed-consent claims require transcript grounding

Claims such as `risks and benefits discussed`, `possible complications discussed`, `signed consent obtained`, or `patient elected to proceed after discussion` are factual attestation claims.

- Label **S** only when the transcript contains the relevant risk/benefit/complication discussion or signed/election process.
- If the transcript supports the procedure choice but not the full risk/benefit/signed-consent attestation, split if possible; otherwise row-level label follows the unsupported attestation component and the supported components are documented in `component_decomposition`.
- A clinician's post-encounter dictation of the attestation is not enough by itself to ground the patient's understanding, agreement, or consent process.

## Consent-A4 — Mixed consent rows use component decomposition, then row-level worst relevant component

When a candidate row contains multiple claims, decompose them. Preserve all sub-claim labels in `component_decomposition`.

For the row-level label used in summary counts, use the strongest unsupported/contradicted clinically relevant attestation component:

`C > I > S* > S`.

This keeps mixed rows like `all questions answered` + `understands and agrees` as **I** when the question-answer part is supported but the broader consent part is not.

## Consent-A5 — No contradictions observed in consent121

No ACI-Bench consent-attestation row in this pass contained a transcript-supported direct contradiction of the consent claim. Failures were **Insufficient**, not **Contradicted**: the transcript usually lacked clear agreement, risk/benefit discussion, signed consent, or whole-plan uptake.
