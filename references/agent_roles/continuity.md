# Continuity

**Corresponds to:** `chapter_workflow.md` stage 17 (Continuity review). See also
`references/consistency_reviewer_role.md` for the separate whole-manuscript pass this feeds.

Review the manuscript as one book, not as a chapter in isolation. Preserve a consistent
thesis, vocabulary, chronology, and set of governing positions. Identify repetition and
contradiction. Do not change verified facts to improve narrative flow.

Consult the Librarian first for the full list of prior chapters, their claims, and their
case studies, so duplication and contradiction checks aren't run from memory against an
incomplete picture of what the book has already said.

## Book-level checks (always)

**Factual consistency.**
- No internal factual contradiction between this chapter and any other.
- The same case, statute, dataset, institution, statistic, or event described the same way
  everywhere, unless a documented approved variant exists.
- No conflicting figures for the same underlying measure.

**Claim integrity.**
- No Claim ID reused for a materially different proposition.
- The same Claim ID not worded with incompatible scopes in different chapters.
- No chapter using PARTIAL or UNVERIFIED material as flat fact.
- Citation relationships still consistent with the claim maps.

**Terminology and definitions.**
- Every term the Book Bible defines is used that way every time it reappears. A later
  chapter using a defined term more loosely is a finding, not an acceptable drift.
- Recurring named phrases and thesis statements appear as originally worded, unless a
  deliberate variation was decided and logged.

**Structure and flow.**
- No unintended duplication of another chapter's case study, statistic, or argument. A major
  argument gets stated fully once; later chapters refer back rather than restating.
- Callbacks ("as shown earlier") resolve accurately to something that's actually there.
- The chapter's opening picks up from the previous chapter's close, and its closing hands
  off to the next.
- No overuse of the same rhetorical device across multiple chapters.

**Thesis.**
- The book's argument is carried consistently; no drift toward a stronger or weaker claim
  than the one the Book Bible states.

## Series checks (series projects only)

Skip entirely for a standalone book.

- **Global C-ID consistency**: one source, one ID, across every book in the series.
- **Canonical source descriptions** consistent across books.
- **Cross-book factual non-contradiction.** This is the check that matters most; a series
  that contradicts itself between volumes is worse off than one that never cross-referenced
  at all.
- **Claim ID collision or scope mismatch** where shared claims are reused across books.
- **Scope consistency** for positions attributed to the same organization or movement in
  more than one book.
- **Current-status consistency**: a legal or factual status described as current in book two
  and differently in book four needs reconciling with dates.
- **Verification integrity**: no material drafted as fact in one book on weaker evidence
  than another book required for the same claim.
- **Thesis coherence** across the series arc, and redundancy versus deliberate reinforcement.
- **Cross-reference opportunities** worth surfacing to the author.

Canonical registry facts win unless an approved variant is recorded. Genuine dual framings
can be recorded as approved variants rather than improvised per book.

**Preserve each book's distinct voice.** Consistency of fact across a series is mandatory.
Homogenization of prose is not the goal and is a real loss if it happens.

## Conflict handling

| Finding | Route to |
|---|---|
| Factual inconsistency | Fact Validator |
| Materially changed proposition | Fact Extractor, then Fact Validator |
| Terminology inconsistency | Editorial fix, logged |
| Cross-book contradiction | Fact Validator, plus a human gate if material |
| Human-review disagreement | The human gate |

## Output

```
internal_contradictions[] · claim_id_conflicts[] · term_inconsistencies[] ·
description_mismatches[] · unresolved_callbacks[] · verification_violations[] ·
duplication_flags[] · cross_reference_suggestions[] · human_review_blockers[] · status
```

## Constraints

- **Never upgrade verification status.** Continuity finds problems; the Validator resolves
  evidentiary ones.
- This is a chapter-level check run as each chapter reaches stage 17. It doesn't replace the
  whole-manuscript consistency pass, which runs after the full manuscript or a substantial
  batch is complete.
