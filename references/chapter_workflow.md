# The Chapter Workflow

This is the gated, chapter-by-chapter production protocol. It exists because nonfiction
that makes factual and contested claims needs a paper trail: every claim traceable to a
source, every contested framing pressure-tested before the author sees it, every stage
visible so the author is never asked to approve something they haven't actually seen.

Follow it in order. Each stage produces a specific file in that chapter's folder; blank
skeletons are in `assets/templates/chapter_folder_templates.md`. Each stage names the
specialist role responsible; full role definitions are in `agent_roles.md` and
`agent_roles/`. Consult the Librarian before any research-, drafting-, or review-heavy
stage to avoid redoing work the project already did.

## Why a workflow instead of "just write the chapter"

A single-pass draft is faster but produces a chapter nobody has pressure-tested.
Argumentative nonfiction fails in predictable ways: a claim that sounds right but isn't
sourced, a comparison that looks even-handed but isn't (one side gets the sympathetic case
study, the other gets the weakest example of its position), a sentence that implies
someone's private motive when only their public actions are documented, a statistic
remembered rather than sourced. The gates below catch each failure mode at the cheapest
possible point, before the author has to catch it in a finished draft.

## On skipping gates

Gates are soft during drafting. If the author wants momentum and says "let's just see how
it flows," draft it. But **a skipped gate is deferred, not waived.** Record it as an open
debt in `Project_Status.md`, say plainly that you're doing so, and come back to it before
stage 18. This happens in practice and it's fine; what isn't fine is letting a shortcut
become permanent silently.

Two lines are hard, not soft: a chapter cannot reach **author final approval** (stage 18)
with outstanding debts, and the book cannot reach **publish-ready** with any unresolved
item in the final citation manifest.

## On author approval

Treat short affirmatives as real approval. An author moving through many chapters will say
"proceed" or "approved" far more often than they'll write a paragraph of feedback. That's
normal, not inattention. Move to the next stage on a clear affirmative, and treat it as
approving the stage just presented.

---

## The stages

### 0. Author Input (`Author_Input.md`)

Create this the moment a chapter folder exists, even empty. It's a standing place for the
author to drop ideas, leads, or direction at any point in the chapter's life, not just at
kickoff. Check it before starting the Chapter Ticket and again before outlining, drafting,
and review. The author shouldn't have to remember to resurface their own note.

### 1. Chapter Ticket (`Chapter_Ticket.md`)

State the chapter's title, placement in the book, purpose, central question, proposed
thesis, and explicit scope boundaries: what this chapter will and won't cover, especially
where it could overlap an adjacent chapter. Read `Author_Input.md` first and fold in
anything usable.

If a chapter's scope changes substantially mid-project, don't silently overwrite the old
ticket. Add a "This Ticket Supersedes an Earlier Version" section stating what changed and
why, so the project keeps an honest history of its own decisions.

### 2. Research Plan (`Research_Plan.md`)

List the specific research questions this chapter needs answered and the method for each
(primary sources, scholarly sources, or internal cross-reference to a chapter already
written). Identify what must be proven, what cannot safely be claimed, and which opposing
arguments must be addressed.

Don't start pulling sources until this exists. It's what keeps research from sprawling
into everything tangentially related to the topic.

**Role:** Research Planning (`agent_roles/research_planning.md`).

### 3. Author approval of scope

Present the Chapter Ticket and Research Plan together. Wait for a real go-ahead before
spending effort on research.

### 4. Primary-source research (`Primary_Sources.md`)

Government documents, court opinions, official statistics, datasets, archival material,
direct statements from the people or institutions involved, contemporaneous reporting.

For every source record: issuing authority or author, title, date, source type, pinpoint
locator, URL, access date, archive URL for anything web-hosted, and whether it's an
original or a reprint. Assign or reuse a **C-ID** per `traceability.md`, checking the
Source Registry first so an existing source keeps its existing identity.

State for each source what it establishes and what it does not.

**Role:** Primary Source (`agent_roles/primary_source.md`).

### 5. Scholarly research (`Scholarly_Sources.md`)

Peer-reviewed research, academic books, expert analysis that contextualizes or tests the
primary-source material. Separate consensus, majority interpretation, minority
interpretation, disputed findings, correlation, and causation. Prefer systematic reviews
and major studies over a single outlier finding.

For any materially contested claim, deliberately seek the strongest sources that
*disagree* with the book's position. The red team at stage 8 needs real ammunition, and
the point of cross-spectrum research is exposing weak assumptions and omitted context, not
mechanical balance.

Fewer items than primary sources is fine. Each should do real interpretive work.

**Role:** Scholarly Evidence (`agent_roles/scholarly_evidence.md`).

### 6. Fact extraction (`Extracted_Claims.md`)

Convert the research into **atomic propositions**, each independently checkable, each
carrying a persistent Claim ID. This is the stage that makes everything downstream
possible, and it's the one most often skipped by instinct because it feels like overhead.
It isn't: a single sentence routinely contains three propositions with three different
evidentiary situations.

Split compound claims. Separate fact from inference, event from motive, association from
causation, quote from paraphrase, number from interpretation, observable conduct from
state of mind. Preserve every qualifier (dates, jurisdiction, scope, population, sample
characteristics, legal posture, uncertainty language). Assign each claim a **tier**
(LOAD_BEARING / SUPPORTING / INCIDENTAL) so scrutiny can scale.

The extractor proposes claim types but does not decide what's true.

**Role:** Fact Extractor (`agent_roles/fact_extractor.md`). Full ID and tier rules in
`traceability.md`.

### 7. Fact validation (`Evidence_Ledger.md`)

Classify each atomic claim by type, then assign its status on both axes:
`verification_status` and `human_review_status`. Apply `verification.md`, escalating to
`verification_matrix.md` for hard calls.

The Evidence Ledger is this stage's output and the chapter's working source of truth: one
row per claim the chapter will actually make, with its Claim ID, the claim as it will
appear in prose, its C-IDs, both status fields, and any required qualification.

Keep a **Correction Log** subsection for anything that turned out wrong during research
and was fixed or dropped, and for candidate claims or case studies that were considered
and set aside, with the reason. A project that records its own quality control is more
trustworthy than one with a silently corrected history.

Only this stage assigns `verification_status`. Nothing downstream may upgrade it.

**Role:** Fact Validator (`agent_roles/fact_validator.md`).

### 8. Red-team review and named-person triage (`Opposition_Brief.md`)

Two things happen here, both before any prose exists, because both are far cheaper to fix
in an outline than in a draft.

**Red team (argument level).** Write 5 to 8 objections a smart, motivated critic who
doesn't share the book's conclusion would actually raise: unfair comparisons, cherry-picked
examples, unstated assumptions, claims broader than the evidence supports, anything that
would make a fair-minded reader on the other side feel strawmanned. More objections for a
high-risk or high-sensitivity chapter, fewer for a bridging chapter introducing no new
claims. For each objection, propose the actual structural fix, not a rhetorical rebuttal.

At this stage the red team works from the Evidence Ledger and the chapter's plan, since
there's no draft yet. Its prose-level checks run later, at stage 15.

**Named-person triage.** Every claim the extractor flagged as involving an identifiable
person, especially state-of-mind or reputation-affecting claims, gets a quick risk read
now: LOW, MED, or HIGH. Anything landing HIGH gets reformulated (attribute it, disclose the
factual basis, narrow it to documented conduct) or dropped *before* it's drafted and
polished. The full manuscript-level legal review still happens at stage 16; this is the
cheap pass that stops the expensive mistake.

**Roles:** Red Team (`agent_roles/red_team.md`), Legal Risk (`agent_roles/legal_risk.md`).

### 9. Detailed Outline (`Approved_Outline.md`)

Section by section, what the chapter covers and in what order, incorporating the red team's
fixes. Move from documented facts to analysis, counterargument, limitations, and the
book's own affirmative case. Note which claims will carry citations.

This is the last stop before prose. A wrong turn here is expensive to unwind once 800 words
sit on top of it.

Do not add facts that aren't in the Evidence Ledger. If the outline needs one, send it back
to stage 2.

Once the outline is settled, have the Illustrator scan it for anywhere a chart, map,
diagram, or photograph would help the argument more than prose would — most chapters need
none, and that's a fine outcome. Log any candidate in `00_Book_Control/Image_Manifest.md`
as `PLANNED` with a one-line brief and, for a chart, which claims it would visualize; don't
block outline approval on it, since the image itself isn't produced until stage 19.

**Roles:** Chapter Architect (`agent_roles/chapter_architect.md`); Illustrator
(`agent_roles/illustrator.md`) for image candidates.

### 10. Author approval of outline

Present the outline for approval before drafting.

### 11. Draft 1 (`Draft_1.md`)

Write the chapter from the approved outline. Every factual proposition keeps its Claim ID in
the claim map and carries its inline `[C-ID]`.

**Draftability**, per `traceability.md`: only a VERIFIED proposition may be stated as flat
fact. A PARTIAL claim may appear only with its qualification stated in the prose. An
UNVERIFIED claim may not be drafted as fact in any form, hedged or otherwise. An
OPINION_NOT_VERIFIABLE claim may be written as opinion when its factual premises are
disclosed and cited.

Human review may still be PENDING at this point; that's fine for drafting, and the chapter
simply stays blocked from publish-ready until the gate clears.

Preserve fact-versus-belief markers, scope qualifiers, attributions, and current-status
qualifiers. Mark any gap as SOURCE REQUIRED rather than filling it. Never invent a number,
quotation, motive, or causal relationship. Apply the style rules while writing.

**Role:** Drafting (`agent_roles/drafting.md`).

### 12. Citation audit (`Fact_Check.md`)

Go claim by claim through the finished draft and verify each against its logged source: not
"does this sound right" but "does the source actually say this."

Check for every blocking code in `traceability.md`: orphan claims, orphan citations, missing
Claim IDs, status mismatches, claim-source mismatches, quote fidelity failures, and sources
needing a durable archive copy. Flag anything needing `[PIN AT FINAL AUDIT]`: substantively
correct but needing one more specific confirmation before print.

**Role:** Citation Integrity (`agent_roles/citation_integrity.md`).

### 13. Voice/style pass (`Draft_2.md`)

Hunt the prose patterns that make writing recognizable as AI-assisted, and fix them without
touching any claim, source, or piece of evidence. This is a wording pass, not a content
pass. Read `humanizer_checklist.md` for the specific tics and fixes, and read the project's
`Voice_Profile.md` so you're editing toward the author's actual voice rather than toward
generic "good prose."

This runs *after* the citation audit, so the audit isn't wasted on prose that's about to
change, and *before* the drift check that verifies the polish broke nothing.

**Role:** Voice/Style (`agent_roles/voice_style.md`).

### 14. Citation drift check

A diff, not a re-audit. Compare pre-humanize and post-humanize on exactly five things:
C-IDs, Claim IDs, the meaning of each factual proposition, scope qualifiers, and
attributions. Anything dropped, moved, altered, or detached from its proposition is drift
and gets fixed here.

Keep this cheap. It is not a second full pass over the sources.

**Role:** Citation Integrity (`agent_roles/citation_integrity.md`).

### 15. Fairness review (`Continuity_Review.md`, fairness-verification section)

Confirm every red-team objection from stage 8 was actually addressed in the finished prose,
word for word where the fix was a specific sentence, not merely addressed in spirit. Read
the objection, then find the sentence that answers it.

This is also where the red team's **prose-level** checks run, which couldn't run at stage 8
because no draft existed: fact-versus-interpretation leakage, overgeneralization
("[group] believes..." with no scope), contested history stated as settled, causal
overreach, and whether the chapter stayed on the right side of the ideas-not-people line.

**Role:** Red Team (`agent_roles/red_team.md`).

### 16. Legal-risk review

The full manuscript-level pass, complementing stage 8's triage. Required in full for any
chapter touching a High-Risk Topic as defined in that book's Book Bible. A lighter pass is
fine for a low-risk chapter, but log the determination either way so it's clear a decision
was made rather than skipped.

List every named or identifiable person, classify them public or private, classify each
statement about them (verifiable fact, disclosed-basis opinion, bare opinion, implied
fact), map each to its Claim IDs, and rate the risk LOW / MED / HIGH. Anything HIGH
requires human legal sign-off and cannot be self-cleared.

**Role:** Legal Risk (`agent_roles/legal_risk.md`).

### 17. Continuity review (`Continuity_Review.md`)

Check the finished chapter against the rest of the book: no unintended duplication of a
claim or case study another chapter already made, terminology consistent with how earlier
chapters defined it, no internal factual contradiction, no Claim ID reused for a materially
different proposition, and opening and closing lines that actually connect to the chapters
on either side.

For a series, also run the cross-book checks: global C-ID consistency, canonical source
descriptions, and cross-book factual non-contradiction. See
`agent_roles/continuity.md`.

**Role:** Continuity (`agent_roles/continuity.md`).

### 18. Author final approval

Present the finished chapter. This is the real gate: once granted, the chapter's status
changes to APPROVED everywhere it's referenced.

**Hard requirement:** no outstanding gate debts. If stages were skipped for momentum, they
get completed before this point, not after.

### 19. Manuscript integration

Write `Approved_Chapter.md` with a status header (approval date, citation-audit summary,
and any items on the pre-publication recheck list for time-sensitive claims). Then update,
in this order:

- `Current_Manuscript.md`: bump the chapter count, append the full approved text. **Give the
  appended copy's heading the form `# Chapter <N>: <Title>`** (or `# Introduction: <Title>`,
  `# Conclusion: <Title>`, `# Prologue: <Title>`, `# Epilogue: <Title>`), even though
  `Approved_Chapter.md` itself just uses `# <Title>`. `scripts/build_interior_docx.py` uses
  that prefix to tell one chapter's heading apart from the next when it parses the compiled
  manuscript, and to render the chapter-opener "eyebrow" line; a heading it doesn't recognize
  doesn't raise an error, it silently merges into the previous chapter (the script does
  refuse to build without warning if this happens, but the fix is getting the heading right,
  not relying on the check to catch it every time). If the Master Outline groups chapters into
  Parts, insert a `# Part <N>: <Title>` line right before the first chapter of each new Part
  (once per Part, not once per chapter) — `build_interior_docx.py` renders it as its own
  divider page. A book with no Parts never needs this line.
- `Master_Outline.md`: mark status, write a dense parenthetical of what the chapter
  actually covers and how it resolved, update "Last updated."
- `Project_Status.md`: add a Completed bullet, update Phase and Recommended Next Steps,
  clear any gate debts this chapter closed, extend the pre-publication recheck list.
- `Claim_Ledger.md`: promote this chapter's claims to their final state with manuscript
  locations.
- `Source_Registry.md`: confirm every C-ID used is registered with a canonical description.
- `Citation_Audit.md`: add this chapter's numbered endnote list in the project's citation
  style, under a `## Chapter <N>: <Title>` heading matching the manuscript's own.
- `Image_Manifest.md`: for any image logged against this chapter, confirm it's produced or
  sourced, captioned, rights-cleared or generation-logged, and DPI-checked, then mark it
  `PLACED` and embed it in `Current_Manuscript.md` at the nearest paragraph break after its
  first mention, using the `:::image ... :::` block documented in
  `references/print_layout_spec.md`. If no image-generation capability is available to
  actually produce a planned illustration, diagram, or chart, write its generation prompt,
  embed the block with `prompt:` set and `path:` omitted (this still reserves its exact
  position and renders as a visible placeholder, not a gap), and mark it `PROMPTED` rather
  than treating the chapter as blocked on it. A `PLANNED` image the author decides to drop
  stays in the manifest marked `DROPPED` with a reason, rather than being deleted — same
  principle as the Evidence Ledger's Correction Log.

If control files are cached outside the main folder for faster access, sync them after
every edit and verify with a diff. A cache that has silently drifted is worse than no cache.

**Export the chapter for post-editing.** Once `Approved_Chapter.md` is written, hand it off
with `scripts/build_chapter_docx.py`, which produces a standard-manuscript-format `.docx`
(double-spaced, plain, with this chapter's endnotes) for a copyeditor or line editor to work
from, separate from the print-ready interior the whole book eventually gets from
`build_interior_docx.py`. See "Exporting a chapter for post-editing" in `SKILL.md`.

**Roles:** Editorial Director (`agent_roles/editorial_director.md`); Illustrator
(`agent_roles/illustrator.md`) for the Image Manifest and embedding.

---

## Special cases

**Author-written personal narrative** (an Introduction or Conclusion written by the author
rather than drafted for them): the workflow above doesn't fully apply. Never rewrite the
author's own prose unprompted. Instead, retroactively document it with a Chapter Ticket,
run fact extraction and the citation audit on any factual claims it makes (statistics,
quotes, dates), and if the outline shifted and the chapter should evolve, propose the exact
new sentences with enough surrounding original text quoted that placement is unambiguous,
then wait for explicit approval.

**Reopening an approved chapter's scope**: don't overwrite the old Chapter Ticket. Add a
superseding section stating what changed and why.

**Importing research the author already has** (a folder of PDFs, prior notes, an existing
bibliography): don't discard it and start fresh, and don't trust it blindly either. Run it
through stages 4 to 7: register each source with a C-ID, extract atomic claims, and
validate them like anything else. Material that arrives with no locator or no retrievable
source is UNVERIFIED until someone finds the source, however confident the note sounds.

**Full-manuscript milestones**: when a chapter's approval resolves a standing open
editorial decision or completes the final chapter, don't just update that chapter's files.
Check whether the book's Open Editorial Decisions, Recommended Next Steps, or Phase
description need updating too, and move resolved items to a Resolved section with date and
rationale rather than deleting them.
