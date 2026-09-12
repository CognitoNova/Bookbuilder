# Drafting

**Corresponds to:** `chapter_workflow.md` stage 11 (Draft 1).

Write the chapter from the approved outline, using only the approved Evidence Ledger and
source packet. Distinguish documented fact, interpretation, inference, and normative
argument clearly enough that a reader always knows which they're reading.

## Inputs

Book Bible · Chapter Ticket · approved outline · Evidence Ledger · source packet ·
`Voice_Profile.md` · Core Definitions and Distinctions · continuity notes from prior
chapters · word-count target

Consult the Librarian before drafting, for the reading order it recommends (Book Bible,
Master Outline, this chapter's ticket and outline, its Evidence Ledger, its research notes,
any existing draft) and to surface any related prose already written elsewhere in the book.

## Draftability

A proposition may be written as fact only when `verification_status` is VERIFIED. PARTIAL
may be drafted only with its qualification stated in the prose. UNVERIFIED may not be
drafted as fact at all, in any hedged form. `OPINION_NOT_VERIFIABLE` may be written as
opinion when its factual premises are disclosed and cited.

`human_review_status` may still be PENDING while drafting. The chapter simply stays blocked
from publish-ready until that gate clears.

## Hard rules

1. Every factual proposition keeps its Claim ID in the claim map.
2. Every empirical fact, attributed statement, official position, statistic, quote, date,
   historical fact, legal characterization, and named-person factual assertion carries its
   inline `[C-ID]`.
3. Preserve fact-versus-belief markers: "[Organization]'s policy states..." reads
   differently from "The statute requires...", and the difference has to survive drafting.
4. Preserve scope. Never widen "some leaders of X" into "X".
5. Preserve current-status qualifiers on anything time-sensitive.
6. Answer the red team's strongest objection where the outline says to.
7. Never invent a number, quotation, motive, or causal relationship.
8. Critique ideas, policies, institutions, movements, and public conduct. Do not assert
   unsupported reputation-affecting facts about named people.
9. Do not silently merge multiple Claim IDs into one broader proposition.
10. Mark any gap as `SOURCE REQUIRED` rather than filling it.
11. If the prose materially changes a claim's scope, route it back to Fact Extraction.

## Output

Chapter draft with inline `[C-IDs]` · claim-to-C-ID map · list of claims whose
`human_review_status` is not APPROVED or NOT_REQUIRED · any unresolved red-team items

## Constraints

- Do not browse freely and silently introduce new claims mid-draft. Anything not in the
  approved ledger goes back to Research Planning first.
- Apply the style rules while writing, not as a cleanup pass afterward.
