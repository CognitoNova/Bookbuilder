# Chapter Folder Templates

Every chapter (Introduction, each numbered chapter, and the Conclusion) gets its own folder containing these files, created and filled in as the chapter moves through `references/chapter_workflow.md`. `Author_Input.md` is created as soon as the folder exists, before any other file, even if it starts out empty; each other file is added when its workflow stage is reached.

Stage map, so it's clear which file belongs where:

| Stage | File |
|---|---|
| 0 | `Author_Input.md` |
| 1 | `Chapter_Ticket.md` |
| 2 | `Research_Plan.md` |
| 4 | `Primary_Sources.md` |
| 5 | `Scholarly_Sources.md` |
| 6 | `Extracted_Claims.md` |
| 7 | `Evidence_Ledger.md` |
| 8 | `Opposition_Brief.md` |
| 9 | `Approved_Outline.md` |
| 11 | `Draft_1.md` |
| 12, 13, 14 | `Fact_Check.md`, `Draft_2.md` |
| 15, 17 | `Continuity_Review.md` |
| 16 | `Legal_Review.md` |
| 19 | `Approved_Chapter.md` |

---

## Author_Input.md

```markdown
# Author Input: [Chapter Title]

Raw ideas, leads, direction, and reminders from the author, logged here before they're incorporated into the Research Plan or Evidence Ledger. Review this file before starting formal research on this chapter, and mark entries as incorporated once addressed. Create this file the moment the chapter folder is created, even if it's empty at first: it's the one place the author can drop a note at any point in the chapter's life without waiting for the workflow to reach a specific stage.

## Notes

- (none yet)
```

---

## Chapter_Ticket.md

```markdown
# Chapter Ticket: [Chapter Title]
**Placement:** [Where this sits in the book]
**Status:** Proposed, awaiting scope/thesis approval
**Logged:** [date]

## Chapter Purpose

[What this chapter needs to accomplish and why it belongs here.]

## Central Question

[The one question this chapter answers.]

## Proposed Thesis

[The chapter's actual argument, in enough detail that the author can approve or redirect it before research begins.]

## Scope Boundaries

**In scope:** [...]
**Out of scope:** [...], especially anything that belongs to an adjacent chapter instead.

## Chapter Type & Workflow

[Risk profile, expected number of red-team objections, whether full or light legal-risk review applies.]

**Approval gate:** awaiting author sign-off before research begins.
```

---

## Research_Plan.md

```markdown
# Research Plan: [Chapter Title]
**Status:** Proposed, pending scope approval
**Logged:** [date]

## Research Questions

1. [Specific, answerable questions this chapter's research needs to resolve.]

## Method

[Primary sources, scholarly sources, or internal cross-reference to an already-approved chapter.]

## Deliverables

- Primary_Sources.md
- Scholarly_Sources.md
- Evidence_Ledger.md
- Opposition_Brief.md
- Approved_Outline.md
```

---

## Primary_Sources.md

```markdown
# Primary Sources: [Chapter Title]

| # | Source | What It Supports |
|---|---|---|
| 1 | [Author/body, title, date] | [The specific claim this source verifies] |
```

---

## Scholarly_Sources.md

```markdown
# Scholarly Sources: [Chapter Title]

| # | Source | What It Supports |
|---|---|---|
| 1 | [Author, title, publication, date] | [The specific claim or context this source provides] |
```

---

## Extracted_Claims.md

```markdown
# Extracted Claims: [Chapter Title]

Stage 6 output. Atomic propositions with persistent Claim IDs, before any verification.
Format and tier rules: `references/traceability.md`.

| Claim ID | Atomic proposition | Tier | Type candidate | C-IDs | Support | Flags |
|---|---|---|---|---|---|---|
| CL-[CODE]-##-001 | [One proposition, independently checkable] | LOAD_BEARING / SUPPORTING / INCIDENTAL | [proposed type] | | DIRECT_SUPPORT / PARTIAL_SUPPORT / CONTEXT_ONLY / CONTRADICTS / NO_SUPPORT_FOUND | [genre traps; named_person; causal; state_of_mind] |

## Full records

[For LOAD_BEARING and SUPPORTING claims, the full JSON record per
`references/agent_roles/fact_extractor.md`, including statistic and quote metadata where
applicable. INCIDENTAL claims need only the table row above.]

## Contradictions detected

[Pairs of findings supporting incompatible propositions. Do not resolve these here; both
claims are emitted and flagged for the Fact Validator.]
```

---

## Evidence_Ledger.md

```markdown
# Evidence Ledger: [Chapter Title]

Stage 7 output, and the chapter's working source of truth. One row per claim the chapter
will actually make. Status definitions: `references/verification.md`.

| Claim ID | Claim as it will appear in prose | Tier | Type | C-IDs | Verification | Human Review | Qualification | Rationale |
|---|---|---|---|---|---|---|---|---|
| CL-[CODE]-##-001 | | | | | VERIFIED / PARTIAL / UNVERIFIED / OPINION_NOT_VERIFIABLE | NOT_REQUIRED / PENDING / APPROVED / HOLD / REVISE | [what specifically is unresolved, if PARTIAL] | [one line: why this status] |

## Not draftable as fact

[Every claim in the table above whose verification_status is not VERIFIED, listed here so
the drafter can see at a glance what must not be stated flatly. PARTIAL claims may be
drafted only with their qualification in the prose; UNVERIFIED claims may not be drafted as
fact in any form.]

## Correction Log

[Anything that turned out wrong during research and was fixed or dropped, and why. Also log
any candidate claim or case study that was considered and set aside, so the reasoning stays
visible rather than the project having a silently corrected history.]
```

---

## Opposition_Brief.md

```markdown
# Opposition Brief: [Chapter Title]

Stage 8 output. Red-team review at the argument level, plus named-person triage. Both run
before drafting, because both are far cheaper to fix in an outline than in a draft.

## Objections

5 to 8 objections a smart, motivated critic who doesn't share the book's conclusion would
actually raise. More for a high-risk or high-sensitivity chapter; fewer is acceptable for a
bridging chapter introducing no new claims.

### Objection 1: [The objection]

[Why this is a real concern, stated in terms its serious advocates would recognize.]

**Response:** [The structural fix to the outline, not a rhetorical rebuttal bolted on.]

[Repeat for each objection.]

## Evidence sufficiency

[Is the evidence actually adequate for what the chapter wants to argue? What would a critic
immediately ask for that isn't in the ledger?]

## Named-person triage

| Person | Claim IDs | Statement | Risk | Action taken |
|---|---|---|---|---|
| | | | LOW / MED / HIGH | [attributed / basis disclosed / narrowed to conduct / dropped] |

[Anything rated HIGH is reformulated or dropped now, before drafting. The full
manuscript-level legal review still runs at stage 16; this is the cheap pass that prevents
the expensive mistake.]

## Assessment

[Overall determination and recommendation to proceed to outline.]
```

---

## Approved_Outline.md

```markdown
# Detailed Outline: [Chapter Title]
**Status:** Proposed, awaiting author approval
**Logged:** [date]

## 1. [Section Name]

[What this section covers.]

[Repeat per section.]

## Illustration Notes

[Any chart, map, diagram, or photograph the Illustrator flagged as helping this chapter's
argument, with a one-line brief and which section it belongs near. Leave as "None" if the
chapter doesn't need one — most don't. Logged in full in
`00_Book_Control/Image_Manifest.md`; this is just a pointer so the outline shows the whole
plan for the chapter in one place.]

**Awaiting author approval before Draft 1.**
```

---

## Draft_1.md

```markdown
# [Chapter Title]

[Full chapter prose, written from the approved outline, style rules applied as it's written.
Every factual proposition carries its inline [C-ID]. Gaps marked SOURCE REQUIRED rather
than filled.]

---

## Claim map

| Claim ID | Draft location | C-IDs | Verification | Human Review |
|---|---|---|---|---|
| CL-[CODE]-##-001 | ch##:¶##:s# | | | |

## Claims awaiting human review

[Every claim whose human_review_status is not APPROVED or NOT_REQUIRED. The chapter can be
drafted and reviewed with these outstanding; it cannot reach publish-ready.]

## Unresolved red-team items

[Anything from the Opposition Brief the draft did not manage to answer.]
```

---

## Draft_2.md

```markdown
# [Chapter Title]

[Stage 13 output: the citation-audited draft after the voice pass. Wording changed; claims,
sources, scope, and attributions untouched.]
```

---

## Fact_Check.md

```markdown
# Fact Check: [Chapter Title]
**Status:** [Complete, clean / Findings outstanding]

## Citation audit (stage 12)

| Claim ID | Claim | Cited source | Does the source say this? | Code |
|---|---|---|---|---|
| | | | yes / no / partly | [blank if clean, else a code from traceability.md] |

**Result: N of N propositions resolve end to end.**

### Blocking codes found

[ORPHAN_CLAIM, ORPHAN_CITATION, CLAIM_SOURCE_MISMATCH, STATUS_MISMATCH,
QUOTE_FIDELITY_FAILURE, MISSING_CLAIM_ID, NEEDS_ARCHIVE. During drafting these are findings
to fix; at publish-ready they block.]

### [PIN AT FINAL AUDIT]

[Substantively correct but needing one more specific confirmation before print. These also
go to Citation_Audit.md's consolidated open-items list.]

## Voice pass log (stage 13)

[Confirmation that the voice pass ran and that no substantive claims changed, so the drift
check can treat it as a wording-only revision.]

## Drift check (stage 14)

Diff of pre- and post-voice-pass on C-IDs, Claim IDs, proposition meaning, scope qualifiers,
and attributions.

**Result: [no drift / drift found and corrected].**
```

---

## Legal_Review.md

```markdown
# Legal-Risk Review: [Chapter Title]
**Scope:** [Full review / light pass]
**Determination logged:** [date]

[Log the scope determination either way, so it's clear a decision was made rather than a
stage skipped.]

| Person | Public/Private | Claim IDs | Statement | Statement type | Harm category | Risk | Fix | Route to lawyer |
|---|---|---|---|---|---|---|---|---|
| | PUBLIC / PRIVATE | | | FACT_VERIFIABLE / OPINION_DISCLOSED / OPINION_BARE / IMPLIED_FACT | | LOW / MED / HIGH | | yes / no |

## Outstanding HIGH-risk items

[Anything rated HIGH requires human legal sign-off and cannot be self-cleared. A chapter
carrying an uncleared HIGH cannot reach publish-ready.]
```

---

## Continuity_Review.md

```markdown
# Continuity Review: [Chapter Title]
**Status:** [Complete, clean / Findings outstanding]

## Handoff verification

[Does this chapter's opening pick up from the previous chapter's closing line, and does its
own closing line hand off to the next?]

## Fairness verification (stage 15)

[Confirm every Opposition Brief objection was actually addressed in the finished prose, word
for word where the fix was a specific sentence. Read the objection, then find the sentence
that answers it.]

## Prose-level red-team checks

[Fact-versus-interpretation leakage, overgeneralization without scope, contested history
stated as settled, causal overreach, unsupported motive claims, ideas-not-people line.]

## Terminology and definitional consistency

[Terms used as the Book Bible defines them. Core Distinctions still held apart.]

## Duplication check

[No unintended overlap with another chapter's claims or case studies.]

## Claim integrity

[No Claim ID reused for a materially different proposition. No non-VERIFIED material used as
fact. Citation relationships consistent with the claim map.]

## Series checks

[Series projects only. Global C-ID consistency, canonical source descriptions, cross-book
factual non-contradiction. Skip for a standalone book.]

**Result: [Clean, recommend proceeding to final author approval / Findings listed above].**
```

---

## Approved_Chapter.md

```markdown
**Status:** APPROVED by author, [date]
**Citation status:** [Citation audit clean (N propositions resolve end to end); drift check clean; legal-risk review [clean / HIGH items cleared by [reviewer] on [date]]; on the pre-publication recheck list for: [anything time-sensitive].]
**Gate debts:** [None. A chapter cannot reach this file with outstanding debts.]

# [Chapter Title]

[Final approved chapter text. This derives from Draft_2.md, the post-voice-pass version,
not from Draft_1.md, unless further changes were made during stages 15 to 18.]
```

Once this file is written, export it with `scripts/build_chapter_docx.py` for post-editing
handoff — see "Exporting a chapter for post-editing" in `SKILL.md`. That export is a working
copy for a copyeditor, separate from this file and from the eventual print interior.
