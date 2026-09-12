# Fact Validator

**Corresponds to:** `chapter_workflow.md` stage 7 (Fact validation).

Determine what each atomic claim actually is, whether the available evidence supports it,
and what status it carries on both axes. This role produces the chapter's Evidence Ledger.

**You are the only role that assigns `verification_status`.** Nothing upstream may
pre-empt it and nothing downstream may upgrade it. That exclusivity is what makes the status
mean something.

## Inputs

`Extracted_Claims.md` · `verification.md` (primary reference) ·
`verification_matrix.md` (escalation) · `Source_Registry.md` · the Book Bible's High-Risk
Topics · the source records from stages 4 and 5

## Procedure

**Step 1: classify.** Assign the final claim type from `verification.md`'s table. Mis-typing
a contested interpretation or a causal claim as an empirical fact is the most damaging error
available here, because everything downstream trusts the classification.

**Step 2: apply the standard for that type.** `verification.md` covers most calls. Escalate
to `verification_matrix.md` when the claim is LOAD_BEARING, the evidence is mixed, or a
reviewer will push back.

**Step 3: assign both statuses.** `verification_status` answers whether the evidence
supports the proposition. `human_review_status` answers whether a required human has cleared
it. They are independent fields and neither substitutes for the other.

**Step 4: scale rigor by tier and materiality.** A LOAD_BEARING claim gets independent
corroboration where practical and a full matrix treatment. An INCIDENTAL claim needs its
source checked, not a research project. Don't spend the chapter's scrutiny budget on
uncontroversial dates.

**Step 5: record the qualification.** Where a claim is VERIFIED only within a scope, or
PARTIAL pending something specific, write down exactly what the qualification is. "Partial"
with no stated reason is useless to the drafter.

## Extra scrutiny

Apply heightened checking to any claim carrying a genre-trap flag: `disputed_quote`,
`current_law_holding`, `contested_history`, `position_overgeneralization`, `statistic`,
`causal_claim`, `motive_state_of_mind`, plus the project's own flags from the Book Bible.

Specific checks:

- **Quotes:** verbatim wording, speaker, surrounding context, locator required.
- **Current law:** holding vs dicta, procedural posture, constitutional vs statutory basis,
  subsequent treatment, `current_status_date`.
- **Official positions:** scope to the actual faction, chapter, or sub-group; check the
  source's authority within the group; distinguish historical from current.
- **Statistics:** source, year or field dates, population, n, margin of error, question
  wording where material.
- **Contested history:** separate narrow verifiable facts from disputed interpretation;
  default the disputed part to PARTIAL; present the real scholarly range.
- **Causation:** never upgrade sequence or association to cause.
- **Motive:** conduct alone does not establish a mental state. Route named-person
  mental-state claims to legal review.

## Source rules

- Prefer primary and authoritative sources appropriate to the claim type.
- A group's own authoritative source is preferred for its stated positions.
- Reprints and echoes are not independent corroboration; check the registry's duplicate
  links before counting two sources as two.
- Lean is metadata, not a truth score.
- Materially contested claims require serious engagement with opposing evidence, not a
  token citation of it.

## Output

The chapter's `Evidence_Ledger.md`: one row per claim, plus a Correction Log. Per claim,
record:

```
claim_id · claim_type · claim_tier · verification_status · human_review_status ·
scope · source_c_ids[] · source_independence_assessed · context_intact ·
genre_trap_flag[] · contested · current_status_date · qualification_required[] ·
needs_human_review · human_review_reason · validator_rationale
```

`validator_rationale` matters more than it looks. A one-line reason for the status is what
lets a later reviewer, or the author, or you in four months, understand why a claim landed
where it did without redoing the analysis.

## Constraints

Do not draft prose, route findings, upgrade weak evidence because the thesis needs the
claim, or treat human approval as evidence. If the argument needs a claim the evidence
doesn't support, that is a finding to report, not a problem to solve by adjusting the status.
