# Book Control File Templates

Copy each section into its own file when scaffolding a new book, all in a
`00_Book_Control/` folder. Replace every `[bracketed]` placeholder. These files are the
book's single source of truth. Keep them current after every chapter, not just at
milestones.

---

## Book_Bible.md

```markdown
# Book Bible

## Project Identity

**Title:** *[Book Title]*
**Subtitle:** *[Subtitle]*
**Book code:** [2 to 4 characters, used in every Claim ID for this book]
**Format:** [e.g. serious argumentative nonfiction]
**Working length:** [target word range]
**Target chapter count:** [Introduction + N chapters + Conclusion]
**Citation style:** [Chicago / Bluebook / house]
**Research cutoff:** [date]
**Standalone or series:** [Standalone / Book N of "[Series Name]"]
**Publisher:** [Publisher, or "self-published"]
**Author byline:** [As it appears on the title page]

---

## One-Sentence Premise

[The book's argument, in one sentence.]

## Audience

[Who this is written for.]

## Register

[Scholarly / journalistic / polemical-but-rigorous / other. How this book should sound, in
general terms. If the voice pass should target a specific named register from
`humanizer_checklist.md` (e.g. "macro-synthesis nonfiction") rather than the author's own
captured prose, that specific choice is set in `Voice_Profile.md`'s "Target register" field,
not here — this section is the general description, that one is the humanizer's actual
input.]

## Core Definitions

[Every key term the book relies on, defined precisely. Every later chapter depends on these
staying stable; terminology drift is the most common whole-manuscript defect.]

## Core Distinctions

[Pairs of concepts the book keeps carefully separate. These are usually the book's actual
intellectual contribution. State them precisely enough that a reviewer could hold a chapter
to them.]

## Target of Critique

[The ideas, doctrines, institutions, policies, movements, or public actions this book argues
for or against.]

## Treatment of This Book's Core Commitment

[A plain statement that the book's own starting premise doesn't by itself guarantee good
character, judgment, or governance, plus where in the book it appears. See
references/style_rules.md.]

## High-Risk Topics

[Subjects in this book requiring full legal-risk review: named living controversial figures,
active litigation, discrimination-adjacent material, allegations of illegality, anything
else specific to this title.]

## Genre Traps for This Book

[The generic categories that apply (disputed quotes, current law and status, contested
history, position overgeneralization, statistics, causal claims, motive and state-of-mind
claims), plus this book's specifics: named cases, statutes, organizations, disputed events,
contested studies.]

## Named Individuals Discussed

[Inventory from setup, so the legal-risk role knows where to expect named-person exposure.]

## Required Human Reviewers

[Which subject-matter disciplines must sign off before publication, and who if known.]

## House Style Rules

[This project's own rules: punctuation prohibitions, number and date formatting, serial
comma, quotation format. See references/style_rules.md's House rules section.]

## Narrative Structure and Emphasis

[The book's overall shape: roughly how much is positive vision vs historical context vs case
studies vs forward-looking agenda. A stated target keeps the book from drifting into being
ninety percent criticism with a short positive coda.]

## Approved Phrases

[Recurring lines the author wants used sparingly, with placement notes where a line is
reserved for a specific chapter.]

## Open Editorial Decisions

- [ ] [Anything not yet decided]

## Resolved Editorial Decisions

[Move items here once resolved, with date and rationale. Don't delete the history.]

## Version Control

**Current version:** 1.0
**Last updated:** [date]
**Author approval:** [YES / pending]

### Change Log

| Version | Date | Change | Rationale | Approved by |
|---|---|---|---|---|
| 1.0 | [date] | Initial version | (n/a) | [name] |
```

---

## Master_Outline.md

```markdown
# Master Outline
**[Book Title]**

Status: [Structure approved / in progress]
Last updated: [date]

---

## Introduction
**Status:** [Not Started / Drafting / Approved]

[Beats the Introduction needs to cover, and the question it should close on.]

---

## Part [I]: [Part Title]
*[One line: what this Part answers for the reader.]*

1. [Chapter Title]: *[Status]*
   *([Once approved, a dense parenthetical: what the chapter opens on, its main case
   studies, how it resolved. Dense enough that someone could reconstruct the chapter's
   shape from this line alone.])*

[Repeat per chapter, grouped under Parts if the book uses them.]

---

## Conclusion: [Title]
**Status:** [Not Started / Approved]

[What the Conclusion needs to answer, and any approved closing lines.]

---

## Chapter Count Summary

[Introduction + N chapters + Conclusion = total units.]

## Editorial Director's Recommendation

[A living paragraph: what's done, what's next, what's still open. Rewrite whenever a chapter
is finalized rather than letting it go stale.]
```

---

## Project_Status.md

```markdown
# Project Status
**[Book Title]**

Last updated: [date]

---

## Phase

[One paragraph: where the project stands right now, in plain language.]

## Completed

- **[Chapter Title]: APPROVED and integrated, [date].** [Dense summary matching the Master
  Outline entry's detail level.]

## In Progress

- **[Chapter Title]:** currently at stage [N] ([stage name]).

## Not Started

[What hasn't been touched.]

## Open Gate Debts

[Every stage skipped for momentum, and which chapter owes it. A chapter cannot reach stage
18 (author final approval) with an entry here. This list is the reason skipping a gate is
safe: it makes the shortcut visible instead of permanent.]

| Chapter | Stage skipped | Date skipped | Reason | Cleared |
|---|---|---|---|---|

## Open Editorial Decisions

[Mirror of the Book Bible's list, or a pointer to it.]

## Resolved Editorial Decisions

[Mirror, or pointer.]

## Recommended Next Steps

1. [The next concrete action.]

## Standing Pre-Publication Rechecks

[Any claim or figure time-sensitive enough to need a final check against the public record
immediately before print. Extend this every time a chapter introduces one; don't defer it to
a single pass at the end.]
```

---

## Claim_Ledger.md

```markdown
# Claim Ledger
**[Book Title]**

Every factual proposition in the book, with its persistent ID and current status. Chapter
Evidence Ledgers are the working view; this is the book-level roll-up that the final
citation manifest is built from.

Book code: **[CODE]** · Claim ID format: `CL-[CODE]-<chapter>-<number>`

Last updated: [date]

---

| Claim ID | Chapter | Proposition | Tier | Type | C-IDs | Verification | Human Review | Qualification | Manuscript location |
|---|---|---|---|---|---|---|---|---|---|
| CL-[CODE]-00-000 | | | LOAD_BEARING / SUPPORTING / INCIDENTAL | | | VERIFIED / PARTIAL / UNVERIFIED / OPINION_NOT_VERIFIABLE | NOT_REQUIRED / PENDING / APPROVED / HOLD / REVISE | | |

---

## Superseded and Related Claims

| Claim ID | Relationship | Related Claim ID | Note |
|---|---|---|---|
| | SUPPORTS / NARROWS / BROADENS / SUPERSEDES / DUPLICATES | | |

## Claims Blocked from Publication

[Any claim currently drafted or planned whose status blocks publish-ready: non-VERIFIED
material used as fact, uncleared HIGH legal risk, or outstanding required human review.]
```

---

## Source_Registry.md

```markdown
# Source Registry
**[Book Title, or Series Name if shared across a series]**

One source, one permanent C-ID, one canonical description. This registry is authoritative
for source identity, verification metadata, archive information, and citation rendering.

**If this book is part of a series, this file is shared across the whole series.** Never
create a second registry, never renumber, and never reconstruct a prior entry from memory.

Last assigned C-ID: [C0000]

---

### C#### — [Canonical Source Title]

- **Author / issuing authority:**
- **Canonical title:**
- **Publication / decision date:**
- **Source type:**
- **Tier:** [primary / secondary]
- **Perspective / lean:** [metadata only, not a truth score]
- **URL:**
- **Archive URL:**
- **Access date:**
- **Pinpoint locator:**
- **Canonical description:** [How this source is described everywhere it appears. One
  wording, used consistently.]
- **Claims supported:** CL-[CODE]-##-###
- **Duplicate / reprint relationships:** [C####-dupN, if any]
- **Context intact:** [yes / no]
- **Quote verified:** [yes / no / n/a]
- **Current-status date:** [for legal or time-sensitive sources]
- **Book relevance:** [which books in a series this source serves]
- **[Style] rendering:** [the full citation as it will appear in the endnotes]
- **Notes:**

---
```

---

## Citation_Audit.md

```markdown
# Citation Audit and Reference Compilation
**[Book Title]**

Compiled: [date]
Compiled from each chapter's source files, verified during that chapter's own citation
audit.

This is the book's working master reference list in [citation style] form. It compiles
sources already verified chapter by chapter; it introduces no new claim. Items marked
**[PIN AT FINAL AUDIT]** are substantively correct but need one more detail confirmed before
print. Endnote numbering restarts at 1 per chapter.

---

## [Chapter Title]

1. [Full citation in the project's style.]

[Repeat per chapter as each clears its citation audit.]

---

## Open Items Across All Chapters

[Every **[PIN AT FINAL AUDIT]** flag, consolidated so a final pre-print pass can work
through them in one place.]

## Manifest Status

**manifest_complete:** [true / false]

[Which chapters are compiled here, what's outstanding, and any unresolved blocking codes
from references/traceability.md. This must read `true` with no outstanding blocks before the
book is publish-ready.]
```

---

## Master_Book_Brief.md

Only created when a book's setup came from a pasted brief (`project_setup.md`'s Step 1
fast path). A live-interview setup has no brief to preserve, so skip this file entirely.

```markdown
# Master Book Brief
**[Book Title]**

Pasted by the author: [date]
Filled from `assets/templates/master_book_brief_template.md` (or close enough in shape to
recognize as one).

This file is a fixed record of what the author actually provided at setup — it does not
get edited as the project evolves. `Book_Bible.md` is the living document; this is what it
was built from. Compare the two anytime to see how the project's self-understanding has
developed since day one.

---

## As Pasted

[The author's brief, verbatim, exactly as given — no cleanup, no correction, no
paraphrasing.]

---

## Intake Log

[What Claude did with the brief at setup:]

**Taken as stated:** [Which of the 15 interview items the brief answered directly, used
without modification.]

**Proposed and confirmed:** [Which items the brief left blank or unclear, what was
proposed to fill them, and that the author confirmed or corrected each — with the final
confirmed version, not just the proposal, if it changed.]

**Still open:** [Anything genuinely unresolved after intake, carried into
`Project_Status.md`'s Open Editorial Decisions rather than guessed at here.]
```

---

## Image_Manifest.md

```markdown
# Image Manifest
**[Book Title]**

Every chart, map, diagram, photograph, and piece of cover art in the book, with its
persistent Image ID and current status. See `references/agent_roles/illustrator.md` for
the role and `references/print_layout_spec.md`'s Images section for placement and the
`:::image ... :::` embedding syntax.

Book code: **[CODE]** · Image ID format: `IMG-[CODE]-<chapter>-<number>` (chapter `00`
for cover or other book-level art)

Last updated: [date]

---

| Image ID | Chapter | Kind | Brief | Claim IDs visualized | Status | Rights / generation record | File path | DPI check |
|---|---|---|---|---|---|---|---|---|
| IMG-[CODE]-00-000 | | chart / map / diagram / photograph / illustration / cover | | | PLANNED / PROMPTED / SOURCED / GENERATED / DRAFT / APPROVED / PLACED / DROPPED | | | pass / fail / n/a |

`PROMPTED` means the role decided the image belongs and wrote a generation prompt, but had
no image-generation capability to actually produce it — the manuscript holds a reserved
placeholder box with that prompt (see `references/print_layout_spec.md`'s Images section).
Not a stalled state to chase down; it's a normal, expected handoff point until someone runs
the prompt through an image tool or otherwise supplies the file.

---

## Pending Generation

[One entry per `PROMPTED` image, so every outstanding prompt in the book can be reviewed or
handed to an image tool from one place, without hunting through the manuscript chapter by
chapter. Move an entry to "Captions and Credits" below once it's produced and placed.]

### IMG-[CODE]-00-000

**Caption:** [As it will read once placed.]
**Prompt:** [The exact generation prompt logged in the manuscript's `:::image` block.]

---

## Captions and Credits

[One entry per placed image — the exact caption and, if required by the source, the exact
credit line, kept here so a change in this table doesn't require hunting through the
manuscript to update the rendered text.]

### IMG-[CODE]-00-000

**Caption:** [As it will appear beneath the image in print.]
**Credit:** [If the source requires one; omit the line entirely if not.]

---

## Dropped or Superseded

[Anything logged here that was later dropped or replaced, with the reason and date. Don't
delete a row from the table above and lose the history — move it here instead, same
principle as the Claim Ledger's superseded relationships.]

## Cover and Back-Cover Art

[Status of the book-level art defined in `references/cover_design_spec.md`'s checklist:
front cover, spine, back cover. This is tracked here for one place to check status, but
reviewed against that file's standard, not against per-chapter citation rules.]
```

---

## Voice_Profile.md

```markdown
# Voice Profile
**[Author Name]**

Built from: [what samples this was derived from]
Last updated: [date]
Target register: [default — the author's own voice, below. Only fill in with a named register
from `humanizer_checklist.md` (e.g. "macro-synthesis nonfiction") if the Book Bible or the
author has explicitly chosen to write some or all chapters in that mode instead.]

The Voice/Style role reads this before every voice pass. Without it, that pass edits toward
generic competence rather than toward this author. If a target register is set above, the pass
uses that register's agent prompt instead of (or layered on top of) the profile below — see
`humanizer_checklist.md`.

## Sentence and paragraph shape

[Typical sentence length and how much it varies. Whether paragraphs open with a claim or
with scene. Typical paragraph length.]

## Register and distance

[How formal. How direct. Whether first person appears, and where.]

## Characteristic moves

[Rhetorical questions, short punch sentences, extended analogies, concrete examples before
abstractions, whatever recurs.]

## Vocabulary

[Level, and any recurring word choices or preferred phrasings.]

## What this author conspicuously does not do

[Often the most useful section. Constructions, hedges, or flourishes absent from their real
writing.]

## Sample passage

> [A short representative excerpt, kept here so the voice is legible without hunting for the
> original.]
```
