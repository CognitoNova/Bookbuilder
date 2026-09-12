---
name: bookbuilder-v4
description: "Write, research, fact-check, review, and produce a rigorously sourced nonfiction book that argues a thesis, from an empty folder to a print-ready interior. Use when starting a new book or book series; opening, researching, outlining, or drafting a chapter; building an evidence ledger or claim ledger; running a red-team, fairness, legal-risk, defamation, citation, continuity, or whole-manuscript consistency review; doing a voice/style 'humanizer' pass on drafted prose; assigning claim IDs or auditing citations; or producing a print interior (table of contents, trim size, running headers, page numbers, endnotes). Also trigger on 'book bible', 'chapter ticket', 'evidence ledger', 'claim ledger', 'source registry', 'citation manifest', 'red team', 'humanizer pass', 'publish-ready', or a 6x9 / 5.5x8.5 interior request."
---

# Book Builder

A complete system for producing serious argumentative nonfiction: a book that takes a
position and survives scrutiny of it. It covers the whole arc, from the first interview
about what the book is, through per-chapter research and drafting, through the review
gates that catch the ways this kind of book actually fails, to a print-ready interior file.

Two things make it different from generic writing help. First, **every factual
proposition is traceable**: claims get persistent IDs, sources get persistent IDs, and
the link between them survives drafting, editing, and polishing, so at the end you can
prove where every fact came from. Second, **the gates are real**: red-team review,
fairness verification, legal-risk review, and citation audits each run at the point
where the failure they catch is cheapest to fix.

The skill is publisher-agnostic and topic-agnostic. Imprint, brand, style exceptions,
and subject matter are all captured per project at setup, not baked in here.

## Before anything else: figure out where the user is

This skill covers a lot of ground. Don't run the whole pipeline reflexively. Work out
which of these the author actually wants right now:

- **Starting a brand-new book (or series)** → read `references/project_setup.md` and run
  the Book Brief Interview. Don't scaffold files before that conversation happens. If the
  author pastes or attaches a completed Master Book Brief instead of answering live, use
  that file's Step 1 fast path (intake from a brief) rather than interviewing from scratch.
- **Working on a specific chapter** (opening, researching, outlining, drafting, reviewing)
  → read `references/chapter_workflow.md` in full. It's the actual protocol, not a summary.
- **A voice/style pass on already-drafted prose** → `references/humanizer_checklist.md`.
- **A whole-manuscript consistency review** → `references/consistency_reviewer_role.md`.
- **Anything about claims, sources, citations, or verification status** →
  `references/traceability.md` for the ID model and `references/verification.md` for how
  status gets assigned.
- **Running one workflow stage as its own specialist pass** (a subagent for research,
  red-team, citation, legal, illustration) → `references/agent_roles.md` for the 16-role
  structure.
- **Charts, diagrams, maps, photographs, or other interior images** →
  `references/agent_roles/illustrator.md` for the role and
  `references/print_layout_spec.md`'s Images section for placement and format.
- **Producing a print interior** → "Building the print interior" below.
- **Cover, spine, or back-cover design** → `references/cover_design_spec.md`.

If a project already exists in the working folder, check its `Project_Status.md` before
assuming anything. A request to "work on the book" rarely means starting from scratch.

## The two-layer model

Everything in this skill sits in one of two layers. Keep them straight; conflating them
is the most common way this workflow goes wrong.

**The chapter loop** runs once per chapter: research → extract → validate → red-team →
outline → draft → audit → humanize → review → approve → integrate. Twenty stages,
detailed in `references/chapter_workflow.md`.

**Book-level work** runs once per book, not per chapter: project setup, whole-manuscript
consistency review, series continuity (if the book is part of a series), the final
citation manifest, and the print build.

Do not research an entire book before drafting a word. Research one chapter, write it,
review it, integrate it, then open the next. That ordering is what keeps the work
tractable and what the whole file structure assumes.

## Starting a new book

Full procedure in `references/project_setup.md`. In brief:

1. **Run the Book Brief Interview.** A structured conversation covering title, thesis,
   target of critique, audience, register, length, chapter spine, flashpoints, citation
   style, standalone-or-series, imprint, and required human reviewers. Propose answers
   where you can infer them and have the author correct you, rather than making them
   fill in blanks you could have filled yourself. If the author instead pastes a completed
   Master Book Brief (`assets/templates/master_book_brief_template.md`), the same 15
   answers come from that document instead of a live back-and-forth — see
   `project_setup.md`'s Step 1 fast path.
2. **Capture the author's voice.** Ask for one or two samples of their own prose and
   write `Voice_Profile.md`. The humanizer is far better with a target than without one.
3. **Scaffold the control files** from `assets/templates/book_control_templates.md` into
   `00_Book_Control/`: `Book_Bible.md`, `Master_Outline.md`, `Project_Status.md`,
   `Claim_Ledger.md`, `Source_Registry.md`, `Citation_Audit.md`, `Image_Manifest.md`.
4. **Fill the imprint profile** from `assets/templates/imprint_profile.md` if the book
   belongs to a publisher or series with its own brand standard.
5. **Open the Introduction and each chapter in turn** per the chapter workflow. Create
   chapter folders as chapters are opened, not all at once.

## Gates: soft during drafting, hard at publication

The workflow has gates. During drafting they are **soft**: if the author wants momentum
and says "just draft it," draft it. But every skipped gate is recorded as an open debt in
`Project_Status.md`, and debts must clear before two hard lines:

1. **Author final approval of a chapter** (stage 18). A chapter cannot be marked APPROVED
   with outstanding gate debts.
2. **Publish-ready** (the final citation manifest and the print build). This is an
   absolute block. A manuscript is not publish-ready while any factual proposition drafted
   as fact is not VERIFIED, any claim lacks a resolvable source, any quote is unconfirmed,
   any HIGH legal risk is uncleared, or any required human review is outstanding.

A skipped gate is deferred, never waived. Say so plainly when the author skips one, log
it, and come back to it.

## The claim and source model, in one paragraph

Every factual proposition gets a **Claim ID** (`CL-<BOOKCODE>-<CHAPTER>-<NUMBER>`) that
identifies the proposition, not the sentence, and follows it if the prose moves. Every
source gets a **C-ID** (`C0042`) that is permanent across the whole project. A claim may
cite several sources; a source may support several claims. Claims are graded on two
independent axes: `verification_status` (does the evidence support it) and
`human_review_status` (has a required human cleared it). Those are different questions and
an approval never upgrades evidence. Claims also carry a **tier** so that a load-bearing
causal accusation gets more scrutiny than an incidental date. Full detail in
`references/traceability.md`.

## Style rules

Apply `references/style_rules.md` while drafting, not as a cleanup pass afterward. The
rules that matter most across every project: no claims about anyone's private motive or
state of mind, acronyms spelled out on first use per chapter, active fairness checking
when the argument could read as one-sided, and whatever punctuation or house rules the
project's own Book Bible adds on top.

## Building the print interior

Once the manuscript is complete (or far enough along for a preview), read
`references/print_layout_spec.md`, then run the build script:

```bash
pip install python-docx --break-system-packages   # if not already installed
pip install Pillow --break-system-packages        # optional, enables the image DPI check
python scripts/build_interior_docx.py \
  --manuscript "Current_Manuscript.md" \
  --title "Book Title" \
  --subtitle "Subtitle" \
  --author "Author Name" \
  --publisher "Publisher Name" \
  --motto "Publisher motto, if any" \
  --trim 6x9 \
  --notes "Citation_Audit.md" \
  --images-dir "assets/images" \
  --output "Book Title - Interior.docx"
```

This produces a genuinely print-formatted `.docx`: correct trim-size page setup with
mirrored gutter margins, a real Word table-of-contents field tied to chapter headings (so
it never drifts out of sync), chapters starting on their own page with alternating running
headers and page numbers, block quotes, `:::callout ... :::` boxes, and `:::image ... :::`
figures (charts, maps, diagrams, photographs — see `references/print_layout_spec.md`'s
Images section and `references/agent_roles/illustrator.md`) all rendered distinctly,
markdown bold/italic converted to real formatting, and a back-matter Notes section built
from the citation audit file. `--images-dir` is only needed if images live somewhere other
than beside the manuscript file; omit it otherwise.

**Always verify the output before handing it over:**

```bash
python /path/to/docx-skill/scripts/office/soffice.py --headless --convert-to pdf "Book Title - Interior.docx"
pdftoppm -jpeg -r 100 output.pdf page
```

Then actually look at the rendered title page, imprint page, TOC, a chapter opener, and a
regular body page. A field that renders correctly in XML doesn't guarantee it looks right.

Tell the author when handing off: the table of contents is a live field. If it doesn't
show page numbers on first open in Word, select all (Ctrl+A) and press F9, or right-click
the TOC and choose "Update Field."

## Exporting a chapter for post-editing

This is a different deliverable from the print interior above, and happens much earlier:
once a chapter reaches stage 19 (`Approved_Chapter.md` written), export it on its own as a
standard-manuscript-format `.docx` so it can move to a copyeditor or line editor without
waiting for the rest of the book.

```bash
pip install python-docx --break-system-packages   # if not already installed
python scripts/build_chapter_docx.py \
  --chapter "Approved_Chapter.md" \
  --book-title "Book Title" \
  --author "Author Name" \
  --notes "00_Book_Control/Citation_Audit.md" \
  --output "Chapter 7 - Editing Draft.docx"
```

This is deliberately plain, not typeset: double-spaced 12pt Times New Roman, 1" margins, a
running header reading "Author / Book Title / page #", and this chapter's own endnotes
numbered at the end of the file — the format an editor actually marks up, not a preview of
the finished book page. (If `Draft_2.md` is what you have and the author wants post-editing
to start before the remaining review gates finish, pass that instead of
`Approved_Chapter.md`; the script doesn't care which stage produced the file, only that it's
one chapter with one heading.)

## Reference index

- `references/project_setup.md`: the Book Brief Interview, voice capture, scaffolding, and how to set up a series.
- `references/chapter_workflow.md`: the full 20-stage chapter protocol and its special cases.
- `references/traceability.md`: Claim IDs, C-IDs, claim tiers, the source registry, citation blocking codes, and the final manifest.
- `references/verification.md`: the compact decision table for assigning verification status.
- `references/verification_matrix.md`: full per-claim-type evidentiary standards (load when a hard call needs it).
- `references/style_rules.md`: motive and causation rules, fairness patterns, acronyms, personal-narrative boundaries, legal caution.
- `references/humanizer_checklist.md`: the AI-prose tics to hunt in a voice pass and how to fix them, plus a reusable framework for optional named nonfiction registers (e.g. macro-synthesis nonfiction) an author can opt into for a chapter or a whole book instead of their own captured voice.
- `references/consistency_reviewer_role.md`: the whole-manuscript consistency and mechanics review.
- `references/agent_roles.md` and `references/agent_roles/`: the 16-role structure, each mapped to its workflow stage (includes `illustrator.md`).
- `references/print_layout_spec.md`: the print design specification, including image placement and the `:::image ... :::` embedding syntax.
- `references/cover_design_spec.md`: front cover, spine, and back cover specification.
- `assets/templates/imprint_profile.md`: publisher/series brand profile, filled per project.
- `assets/templates/master_book_brief_template.md`: fill-in form for the author to prepare a book's setup offline and paste in, instead of a live interview.
- `assets/templates/book_control_templates.md`: Book Bible, Master Outline, Project Status, Claim Ledger, Source Registry, Citation Audit, Image Manifest, Master Book Brief.
- `assets/templates/chapter_folder_templates.md`: per-chapter file skeletons.
- `assets/templates/front_matter_template.md`: title page and imprint page.
- `scripts/build_interior_docx.py`: the print-interior build script.
- `scripts/build_chapter_docx.py`: the per-chapter, standard-manuscript-format export for
  post-editing handoff.
