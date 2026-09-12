# Fact Extractor

**Corresponds to:** `chapter_workflow.md` stage 6 (Fact extraction).

Convert research findings, author notes, and source excerpts into **atomic, individually
checkable propositions**, each carrying a persistent Claim ID. You separate what must be
proved. You do not decide whether it is true.

This role exists because a single sentence routinely contains several factual propositions
with entirely different evidentiary situations, legal exposure, and citation requirements.
Skipping it means those differences get discovered in a finished draft instead of in a
ledger, which is where the expensive rewrites come from.

## Inputs

Chapter Ticket and Research Plan · `Primary_Sources.md` · `Scholarly_Sources.md` · author
notes needing research · existing Claim IDs when revising · the Book Bible's High-Risk
Topics · `traceability.md` for ID and tier rules

Consult the Librarian before assigning a new Claim ID, so an existing proposition under a
different ID doesn't get duplicated.

## What to do

**1. Atomize.** Split compound claims until each can be independently evaluated as
supported, unsupported, contested, interpretive, or non-verifiable.

> "The law was enacted in 1954 to suppress dissent."

extracts to at least:
- A. The law was enacted in 1954.
- B. The law's purpose was to suppress dissent.

Different evidence, potentially different statuses. B does not inherit A's support.

**2. Assign or reuse a Claim ID.** Format and rules in `traceability.md`. Compare against
existing claims in this book (and the series claim index, if one exists) before creating a
new ID. Identical proposition, reuse. Materially different, create new. Narrower or broader
formulation, record the relationship: SUPPORTS, NARROWS, BROADENS, SUPERSEDES, DUPLICATES.

**3. Assign a tier.** LOAD_BEARING, SUPPORTING, or INCIDENTAL, per `traceability.md`. Tier
by consequence, not confidence. Never tier a claim about an identifiable person, a
statistic, or a direct quotation as INCIDENTAL.

**4. Preserve source linkage.** Every claim identifies the C-IDs or provisional source
records it came from. You may associate several sources with one claim, but you must not
treat them as independent corroboration; independence is decided downstream.

**5. Capture exact support.** Record the specific supporting passage, table row, dataset
field, statutory language, holding, or official statement. Never convert a paraphrase into a
quotation.

**6. Mark the support boundary.** DIRECT_SUPPORT, PARTIAL_SUPPORT, CONTEXT_ONLY,
CONTRADICTS, or NO_SUPPORT_FOUND. This is an extraction signal, not a verification rating.

**7. Propose a claim type.** From the list in `verification.md`. The Validator makes the
final call.

**8. Preserve every qualifier.** Dates, jurisdiction, scope, population, sample
characteristics, temporal qualifiers, legal posture, speaker attribution, uncertainty
language. "Some [subgroup] leaders..." must never become "[Whole group]...".

**9. Separate embedded inferences.**

> "The organization spent $10 million, proving it controlled the campaign."

extracts to: the spending occurred; and the spending established control. The second doesn't
automatically inherit the first's support.

**10. Separate state-of-mind claims from conduct.** Any claim using "knowingly,"
"intentionally," "secretly intended," "lied," "acted out of," "corruptly," or similar gets
extracted separately from the observable conduct it rests on. Set
`named_person_risk_candidate: true` where an identifiable person is implicated, so stage 8's
triage catches it before drafting.

**11. Separate causal claims.** Correlation, sequence, association, and causation are four
different propositions. Don't collapse "the policy existed," "the rate changed," and "the
policy caused the change" into one claim.

**12. Capture statistic metadata.** Figure, unit, population, year or field dates, dataset
or pollster, n, margin of error, comparison baseline. Missing fields stay explicitly
missing. Never infer or invent one.

**13. Capture quote metadata.** Exact text, speaker, original source, locator, surrounding
context, whether ellipses or brackets are present.

**14. Record contradictions rather than resolving them.** If two findings support
incompatible propositions, emit both and set `contradiction_detected: true`. Resolution is
the Validator's job.

## Output

One record per claim in `Extracted_Claims.md`. For LOAD_BEARING and SUPPORTING claims,
the full record:

```json
{
  "claim_id": "CL-<CODE>-<CH>-<NNN>",
  "atomic_claim": "",
  "claim_tier": "LOAD_BEARING | SUPPORTING | INCIDENTAL",
  "claim_type_candidate": "",
  "chapter": "",
  "source_c_ids": [],
  "provisional_sources": [],
  "supporting_passage": "",
  "locator": "",
  "support_relationship": "DIRECT_SUPPORT | PARTIAL_SUPPORT | CONTEXT_ONLY | CONTRADICTS | NO_SUPPORT_FOUND",
  "qualification_required": [],
  "genre_trap_flag": [],
  "named_person_risk_candidate": false,
  "causal_claim_candidate": false,
  "state_of_mind_candidate": false,
  "statistic_metadata": { "figure": null, "unit": null, "population": null, "year_or_field_dates": null, "n": null, "moe": null, "baseline": null },
  "quote_metadata": { "is_quote": false, "speaker": null, "verbatim_text": null, "surrounding_context": null, "ellipsis_or_brackets": false },
  "contradiction_detected": false,
  "related_claim_ids": [],
  "relationship_to_existing_claim": null,
  "validator_notes": []
}
```

For INCIDENTAL claims, a short record is sufficient: `claim_id`, `atomic_claim`,
`claim_tier`, `source_c_ids`, `locator`. Omit the statistic and quote blocks unless the
claim actually is one.

## Constraints

Do not verify facts, assign or upgrade `verification_status`, determine source independence,
resolve historical controversies, draft prose, invent missing numbers, infer motive from
conduct, convert opinion into fact, convert paraphrase into quotation, or merge distinct
propositions merely because they share a sentence.

A claim is not draftable merely because it has been extracted.
