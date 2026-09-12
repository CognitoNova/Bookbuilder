# Changelog

## v4.6: a prompt-and-placeholder fallback for images the Illustrator can't produce itself

The `:::image ... :::` block now accepts a `prompt:` field as an alternative to `path:`.
When the Illustrator role (v4.5) has no image-generation capability available, it still
does the full job — deciding an image belongs, writing the brief, writing a specific
generation prompt — and reserves the image's exact manuscript position with `prompt:` set
and `path:` omitted, rather than leaving a gap or inventing a picture. Both build scripts
render this as a dashed "AWAITING IMAGE GENERATION" placeholder box holding the brief and
the full prompt, visibly distinct from the red `\[MISSING IMAGE]` warning a block gets when
neither field resolves to anything (that's a defect; this is a tracked to-do). Field values
can now span multiple lines via continuation (any line not starting with a recognized field
name extends the previous field), since a generation prompt is often longer than one line.
`build\_interior\_docx.py`'s final output lists every still-pending image by ID so the list
of outstanding prompts is always visible at build time. New `Image\_Manifest.md` status,
`PROMPTED`, plus a "Pending Generation" section in that file listing each outstanding
prompt in one place. Explicitly scoped to generated illustrations, diagrams, and charts —
`illustrator.md` and `print\_layout\_spec.md` both say plainly this is not a way to
manufacture a stand-in for a real photograph; a planned photograph without a source stays
`PLANNED` with a sourcing brief instead.

## v4.5: an Illustrator role and interior image support

Added a 16th agent role, **Illustrator** (`references/agent\_roles/illustrator.md`),
cross-cutting like the Editorial Director and Librarian: consulted at chapter workflow
stage 9 to flag where a chart, map, diagram, or photograph would materially help a
chapter's argument (most chapters need none), and again at stage 19 to finalize captions,
rights/generation records, and placement. Also the role for cover/spine/back-cover art
(`cover\_design\_spec.md`), which it implements rather than duplicates. Images get a
persistent `IMG-<BOOKCODE>-<CHAPTER>-<NUMBER>` ID, parallel to Claim IDs and C-IDs, tracked
in a new control file, `00\_Book\_Control/Image\_Manifest.md` (template added to
`assets/templates/book\_control\_templates.md`).

`build\_interior\_docx.py` and `build\_chapter\_docx.py` now parse a `:::image ... :::` fenced
block (same pattern as `:::callout`) with `path`, `caption`, `credit`, and `width` fields,
and actually place the image: centered, sized to the field or a sensible default, with the
caption in smaller italic text directly below and a credit line if supplied, per
`print\_layout\_spec.md`'s Images section (rewritten to document the block format and the ID
scheme). New `--images-dir` flag on both scripts resolves a relative `path:` against a
shared assets folder instead of assuming images sit beside the manuscript. When Pillow is
installed, a missing-300-DPI figure gets a build-time warning naming the offending image
rather than shipping soft; either way a missing image file becomes a visible red
placeholder in the document itself, not a silent gap. `chapter\_workflow.md` stage 9 and
stage 19, `agent\_roles.md`'s table and separation-of-authority section, the
`Approved\_Outline.md` template (new "Illustration Notes" section), `project\_setup.md`'s
scaffolding step, and `SKILL.md`'s routing list and reference index all updated to match.

## v4.4: recognized "Appendix A: Title" as a chapter-level heading

`CHAPTER\_HEADING\_RE` now also matches `# Appendix A: Title` (any letter/number after
"Appendix"), so back-matter appendices can sit in `Current\_Manuscript.md` and
`build\_interior\_docx.py` alongside numbered chapters, rendered the same way (their own
section, running header, optional endnotes). Needed for a real manuscript (, migrated from
a single flat file, with nine reference appendices between the last chapter and the bibliography;
without this they had no path into the compiled manuscript at all.

## v4.3: Part-divider support in the print interior

`build\_interior\_docx.py` now recognizes an optional `# Part I: Title` heading in
`Current\_Manuscript.md` (added via a new `PART\_HEADING\_RE`, checked only in the
whole-manuscript/strict parse) and renders it as its own divider page — eyebrow "PART I" plus
title, dropped down the page, no body text, same section/header/footer treatment as a chapter
opener. Chapter titles moved from Word's Heading 1 style to Heading 2 (Part dividers now own
Heading 1) so the table of contents field (`\\o "1-2"`) nests chapters under their Part; a
manuscript with no Part headings builds exactly as before, just with chapter titles on
Heading 2 instead of Heading 1 (same visual size, 24pt). `find\_unrecognized\_h1\_lines` no
longer flags Part headings as unrecognized H1s. Prompted by migrating a real 6-Part, 20-chapter
manuscript (Into this project structure) into this project structure — the tooling had no way
to represent a Part grouping before this.

## v4.2: dropped the provenance line from the chapter export

`build\_chapter\_docx.py` no longer prints the "Status: APPROVED... · Citation status: ..."
line under the chapter title. Removed the feature entirely (not just defaulted off) per
author feedback on the first sample export — the metadata is still stripped from the parsed
body either way, so nothing about the chapter text changes.

## v4.1: per-chapter post-editing export, and a silent chapter-loss fix

Added `scripts/build\_chapter\_docx.py`: exports one chapter (`Approved\_Chapter.md`, or
`Draft\_2.md` if post-editing should start before the remaining review gates finish) as a
standard-manuscript-format `.docx` — double-spaced 12pt Times New Roman, 1" margins, a plain
running header, this chapter's own endnotes numbered at the end of the file. This is a
distinct deliverable from `build\_interior\_docx.py`'s trim-sized, typeset print interior,
meant for copyeditor/line-editor handoff per chapter rather than the whole finished book.
Endnotes are placed at the end of the exported chapter file rather than inline: KDP's own
text guidelines recommend footnote/endnote text sit "at the end of the chapter or book," and
this matches how the book's eventual back matter already groups notes by chapter. Reuses
`build\_interior\_docx.py`'s manuscript parser and inline-emphasis renderer rather than
duplicating markdown handling.

Building this surfaced a real bug in the shared parser: `parse\_manuscript()`'s chapter-
heading pattern only recognizes `# Chapter N: ...` / `# Introduction: ...` / etc., but
`Approved\_Chapter.md`'s own template heading is just `# <Title>`, with no prefix, and
nothing previously said the prefix needs adding when a chapter's text is appended to
`Current\_Manuscript.md`. Confirmed the actual failure mode: a chapter heading missing that
prefix doesn't error, it silently merges into the *previous* chapter, with the affected
chapter's text just vanishing into its neighbor in the compiled manuscript and the built
`.docx` reporting a normal-looking chapter count. Fixed three ways: `chapter\_workflow.md`
stage 19 and `editorial\_director.md` now say explicitly to add the `Chapter N:` prefix when
appending to `Current\_Manuscript.md`; `parse\_manuscript()` gained a `strict\_chapter\_headings`
flag (`build\_chapter\_docx.py` uses `False`, since a single-chapter file has no such
prefix to check against); and `build\_interior\_docx.py` now scans for any unrecognized H1
appearing after the first real chapter and refuses to build without `--allow-unrecognized- headings`, so this failure can't happen silently again regardless of whether the appending
convention was followed correctly that day.

## v4.0: renamed to bookbuilder-v4

Renamed the skill from `book-builder` to `bookbuilder-v4` (frontmatter `name:` and the
package folder). Kebab-case is required for a skill name (lowercase letters, digits, and
hyphens only), so `bookbuilder\_v4` became `bookbuilder-v4`. Nothing else changed: the
description, triggers, workflow, and file layout are identical to v3.2. Existing projects
built with `book-builder` don't need any changes; nothing inside a project folder refers to
the skill by its own name.

## v3.2: closed the Librarian-consultation gap

`agent\_roles.md` and `agent\_roles/librarian.md` both stated that the Librarian is consulted
before stages 2, 4, 5, 6, 11, 12, and 17, but only the stage-2 role file
(`research\_planning.md`) actually said so. A role file is what a specialist subagent for
that stage is likely to be given as its own instructions, so the other six stages could run
without ever being told to check the Librarian first, the exact condition that produces the
failure the Librarian exists to prevent: a source re-logged under a second C-ID, a
proposition re-extracted under a second Claim ID, a chapter drafted without checking what a
neighboring chapter already covers. Added a one- or two-line consultation cue, in each
file's own voice, to `primary\_source.md` (4), `scholarly\_evidence.md` (5),
`fact\_extractor.md` (6), `drafting.md` (11), `citation\_integrity.md` (12, the full-audit
section specifically, not the intentionally-cheap stage-14 drift check), and `continuity.md`
(17). `chapter\_workflow.md`'s stage 15 heading was also given its output filename
(`Continuity\_Review.md`, fairness-verification section) to match how every other stage cites
its file, since the template folder document already shows stages 15 and 17 sharing that one
file and the workflow document didn't say so.

Also clarified the two same-named "register" fields introduced across v3.1 and setup: the
Book Bible's general `## Register` (how the book should sound, in prose) now cross-references
`Voice\_Profile.md`'s specific `Target register` field (the humanizer's actual selector) so
the two aren't mistaken for the same setting.

## v3.1: named nonfiction registers for the voice pass

Added a reusable "named register" framework to `references/humanizer\_checklist.md` for the
stage-13 voice pass, for books whose Book Bible calls for a recognizable nonfiction mode rather
than the author's own captured prose. It sits beside the default `Voice\_Profile.md` target
rather than replacing it, still operates inside the existing pass's constraints (no claim,
C-ID, or attribution changes), and its choice is recorded in `Voice\_Profile.md`'s new "Target
register" field (or `Project\_Status.md` if no profile exists yet) so later chapters and the
whole-manuscript consistency review treat it as intended rather than as drift.

One register ships built in: **macro-synthesis nonfiction**, the cross-disciplinary,
wide-lens popular-science/macro-history mode. It's defined by craft technique (blend
disciplines, anchor abstractions in analogy, vary sentence rhythm, limit em-dashes) rather than
by instructing the agent to write in a specific living author's voice — a note names the
writer the mode is commonly associated with, for recognizability, but the operative agent
prompt never does. The section documents how to add further registers (scene-first narrative,
plain-spoken service nonfiction, etc.) the same way, so the mechanism doesn't need redesigning
per register.

`SKILL.md`'s reference index and `project\_setup.md`'s voice-capture step were both updated to
surface the option.

## v3.0: the merge

`book-builder` supersedes three earlier skills: `bookbuilder`, `viewpoint\_book\_builder`
(v1.2, and its genericized `Book\_Builder\_Skill\_v2`), and the two title-specific builders.
One system replaces all of them.

### Why

The two mature systems had each solved a different half of the problem.

`bookbuilder` had the **operational layer**, built from a real book: a 17-stage gated chapter
workflow, four control files, per-chapter folder templates, style rules, a humanizer
checklist targeting AI-prose tics, a whole-manuscript consistency pass, and a working
729-line print-interior build script. What it lacked was claim-level rigor: its evidence
ledger was a four-column table on a single five-level status scale, with no persistent
identifiers, no source registry, and no way to prove at the end that every fact resolved to
a source.

`viewpoint\_book\_builder` had the **rigor layer**: persistent Claim IDs, a global source
registry with permanent C-IDs, claim-type-specific verification standards, a two-axis status
model, citation-integrity auditing with named blocking codes, defamation review, and a final
citation manifest. What it lacked was any operational shell: no chapter loop (it read as one
linear pass over an entire book), no state tracking, no voice capture, no templates, and no
production stage at all. It stopped at "publish-ready" without producing a manuscript.

Maintaining both meant every improvement got made twice, and four overlapping book skills
competed for triggering.

### What came from where

**From `bookbuilder`, kept:** the gated chapter workflow and its author-approval norms; the
control-file architecture; per-chapter folder templates; the style rules; the humanizer
checklist; the consistency reviewer; the print layout spec and build script; the cover spec;
the Librarian and Editorial Director roles; and the hard-won practical wisdom in the prose
(treat short affirmatives as approval, a skipped gate is deferred not waived, sync cached
control files, verify a rendered docx visually before handing it over).

**From `viewpoint\_book\_builder`, kept:** Claim IDs and C-IDs; the source registry and its
duplicate-linking rules; the two-axis status model; the claim-type verification matrix; the
Fact Extractor and Fact Validator roles; citation-integrity auditing and its blocking codes;
the defamation reviewer; series continuity and research routing; the Book Brief Interview;
and the separation-of-authority principle that only one role may assign verification status.

### What changed in the merge

**Structural fixes to problems in both systems:**

* **A chapter loop is now explicit.** The rigor system read as a single linear pass over a
whole book, which would have meant researching every chapter before drafting a word. The
two-layer model (chapter loop versus book-level work) is now stated in `SKILL.md` and
built into the workflow.
* **Red team was split.** It previously ran pre-draft while being asked to check prose that
didn't exist yet. Argument-level review now runs at stage 8 (pre-draft); prose-level checks
and fairness verification run at stage 15.
* **Named-person risk moved earlier.** Formal legal review ran only after drafting and
polishing, so a HIGH-risk passage was fully written before anyone flagged it. A cheap
triage now runs at stage 8, with the full review still at stage 16.
* **Citation audit and voice pass were reordered.** Audit now precedes the voice pass, so the
audit isn't spent on prose about to change, and the post-voice check is an explicit
cheap diff rather than a second full audit.
* **Claim tiers added.** The old matrix said rigor should scale with materiality but nothing
implemented it, so a date in a transition sentence got the same 30-field record as a
central accusation. LOAD\_BEARING / SUPPORTING / INCIDENTAL now scales the required
treatment, with guards preventing anything about a person, statistic, or quote from being
tiered down.
* **Claim IDs no longer assume a series.** A configurable book code replaces hardcoded book
numbers.
* **Claims got a home.** Sources had a registry; claims were emitted as JSON into nowhere.
`Claim\_Ledger.md` is now a control file.
* **Gate debts are tracked.** `Project\_Status.md` has an Open Gate Debts table, which is what
makes soft gates safe: a skipped stage is visible instead of forgotten.
* **Voice capture added.** The humanizer was told to improve "voice" with no reference for
the author's actual voice. `Voice\_Profile.md` is now built at setup from real samples.
* **Author-supplied research has a path.** The pipeline assumed agent-driven search; most
authors arrive with a folder of PDFs. Setup asks, and the workflow routes existing material
through extraction and validation rather than trusting or discarding it.
* **The interview stopped asking the author to do the agent's job.** It previously asked the
author to classify claim-risk categories and name reviewer disciplines, both inferable from
the thesis. The agent now proposes and the author corrects.

**Reconciliations:**

* **Verification scale.** The two-axis model won. A mapping table in `traceability.md` lets
existing single-scale ledgers be read without migration.
* **Blocking strictness.** Soft gates during drafting, hard blocks at author final approval
and at publish-ready. This preserves the momentum the operational system allowed while
keeping the citation-manifest guarantee that justified the rigor system.
* **Evidence Ledger.** Now the output of fact validation, carrying Claim IDs, tiers, and both
status axes, while remaining the per-chapter working view. The book-level roll-up is
`Claim\_Ledger.md`.
* **Roles.** 12 plus 12 became 15, with the overlaps merged: one Citation Integrity role, one
Legal Risk role covering both triage and full review, one Continuity role with a
series-only section.

**Genericization:**

* All publisher-specific content removed: imprint, motto, byline, brand palette, typography,
logo, category colour coding, and the ten-title roster. These now live in a per-project
`Imprint\_Profile.md` template.
* The print script's hardcoded publisher and motto defaults are now empty, and the imprint
page is skipped entirely when neither is supplied.
* The em-dash prohibition became a configurable house rule with its mechanical enforcement
pattern preserved, rather than a universal.
* Topic-specific examples throughout the verification standards (named cases, named
doctrines, single-domain illustrations) were replaced with bracketed placeholders or
broadened so no one subject area leads. The `DOCTRINE\_OR\_BELIEF` claim type became
`DOCTRINE\_OR\_POSITION` and now explicitly covers any organization's stated position:
party platforms, corporate policy, professional codes, and religious doctrine alike.
* The subject-matter reviewer panel is project-defined rather than a fixed default.

**Progressive disclosure:**

* The 543-line verification matrix was split into a compact always-load decision table
(`verification.md`) and a per-claim-type escalation reference (`verification\_matrix.md`).
* `SKILL.md` became a routing hub rather than a 605-line document restating every agent
contract. The status model, previously stated in three files that could drift apart, now
has one home.

**Frontmatter:**

* The rigor system used non-standard `skill\_name:` / `version:` / `tags:` frontmatter, which
would not have triggered as an installed skill at all. Now standard `name:` +
`description:`, with trigger language covering the full surface.

### Migration

Existing projects don't need rewriting. Old evidence ledgers on the five-level scale are
readable through the mapping table in `traceability.md`. Existing source lists can be
imported into `Source\_Registry.md` as they are, assigning C-IDs to entries that lack them and
never renumbering ones that have them. New chapters use the new workflow; finished chapters
stay finished.

