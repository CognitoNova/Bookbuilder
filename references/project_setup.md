# Project Setup: The Book Brief Interview

Run this once at the start of every new book, whether it's a standalone title, the first
book of a series, or the next book in a series that already exists. Nothing else in the
workflow runs until it produces a Book Bible.

## Step 0: work out what already exists

Before asking anything, determine which situation you're in:

- **A brand-new project.** No control files anywhere. Everything gets created.
- **A new book in an existing project or series.** Control files exist from a prior book.
  Citation style, imprint, style-rule exceptions, reviewer panel, and the source registry
  all carry over.
- **An existing book already underway.** Read `Project_Status.md` first. The author almost
  certainly wants to continue, not restart.

If a project folder is connected, look before you ask. An author who has to re-answer
questions the files already answer will reasonably conclude the system isn't paying
attention.

**Also check whether the author has pasted or attached a Master Book Brief** (filled from
`assets/templates/master_book_brief_template.md`, or close enough to it in shape and
content to recognize as one — the author doesn't have to use the exact template). If so,
skip the live interview below and use "Step 1 (fast path): intake from a pasted brief"
instead.

## Step 1: interview

Ask these in one structured pass. **Propose answers wherever you can infer them** and have
the author correct you, rather than handing them fourteen blanks. You can usually draft a
plausible chapter spine, a genre-trap list, and a reviewer panel from the thesis and target
of critique alone. Getting corrected is faster for the author than composing from scratch.

Where a prior book in the project already answered something, state the existing value and
ask for confirmation instead of asking blind.

**1. Working title** and subtitle, if there is one.

**2. Thesis.** The central argument in one sentence. What is this book trying to prove?

**3. Target of critique.** What ideas, doctrines, institutions, policies, movements, or
public actions is the book arguing for or against?

**4. Named people.** Any identifiable individuals whose public conduct or statements the
book will discuss. This is an inventory, not a legal assessment; it tells the workflow where
to expect named-person risk. Confirm the standing line at the same time: the book critiques
ideas, institutions, and public conduct, not the private character of private individuals.

**5. Register and voice.** Scholarly, journalistic, polemical-but-rigorous, something else?

**6. Audience.** Who is this written for?

**7. Target length.** Approximate word count, chapter count, or both.

**8. Chapter spine.** A working list of chapters or topics. Propose one from the thesis and
let the author cut and reorder. This is a working spine, not a locked outline.

**9. Known flashpoints.** Which contested, controversial, or high-scrutiny claims does the
author already know the book will touch?

**10. Genre traps.** From answers 2, 3, and 9, *you* propose which high-risk claim categories
apply, and the author confirms or corrects. The generic set is in `traceability.md`:
disputed quotes, current law and its status, contested history, position overgeneralization,
statistics, causal claims, motive and state-of-mind claims about named people. Add the
book's own specifics: named cases, statutes, organizations, disputed events, contested
studies.

**11. Citation style.** Chicago, Bluebook, or a house style. Affects the registry's stored
renderings and the endnote build.

**12. Standalone or series.**
- *Series:* series name; whether this is the first book; and for an existing series, where
  the current `Source_Registry.md` and series outline live. Facts stay canonical across a
  series; voice stays book-specific. **Reuse the existing registry. Never start a second one.**
- *Standalone:* confirm that series-only machinery (cross-book routing, series continuity)
  won't be used.

**13. Imprint and reviewers.** Publisher name, motto, and brand standard if the book belongs
to one; fill `assets/templates/imprint_profile.md` if so. Also: which subject-matter
disciplines must review before publication? Propose these from the subject rather than
asking cold. A book making legal arguments needs a legal reader; one making clinical claims
needs a clinician; one making historical causal claims needs a historian.

**14. Existing research.** Does the author already have material: a folder of PDFs, prior
notes, an existing bibliography, a draft? This changes the first chapter's shape
substantially, and it's the question most often forgotten.

**15. Open questions.** Anything the author already knows they'll want a human expert or
lawyer to weigh in on.

## Step 1 (fast path): intake from a pasted Master Book Brief

Same destination as the live interview — the same 15 answers, arrived at from what the
author already wrote instead of drawn out one question at a time. Do not treat a brief as
an excuse to skip judgment; a pasted document still needs reading closely, not rubber-
stamping.

1. **Map the brief onto the 15 interview items one by one.** Most briefs won't use the
   template's exact numbering or headings — match by content, not by section title.
2. **Anything the brief states clearly, use as stated.** Don't re-ask it, and don't
   "improve" it into something the author didn't say — a stated thesis or chapter spine is
   the author's call, not a first draft to workshop.
3. **Anything the brief leaves blank or unclear, propose an answer** the same way the live
   interview does — draft a plausible chapter spine, genre-trap list, or reviewer panel
   from what *is* filled in, per the interview's own guidance above. Don't invent specifics
   the brief gives no basis for (a named flashpoint, a specific genre trap tied to a real
   case) — propose only what the rest of the brief actually supports, and mark anything
   else as a genuine open question instead.
4. **Batch every open question into one message**, the same "one structured pass" the live
   interview uses — never trickle them out one at a time once a brief already exists to
   work from.
5. **Present the full picture back before scaffolding anything**: what came from the brief,
   what was proposed and why, and what's still open. Wait for a real go-ahead, same as
   Step 3 (author approval of scope) always requires — a brief being detailed doesn't lower
   this bar.
6. **Preserve the brief itself.** Once setup proceeds, save the author's pasted text
   verbatim into `00_Book_Control/Master_Book_Brief.md` (template in
   `book_control_templates.md`), along with a short intake log: what was taken as stated,
   what was proposed, and how each open question got resolved. `Book_Bible.md` is the
   living, evolving document from here forward; this file stays a fixed record of the
   original ask, the same way `Source_Registry.md` keeps a source's canonical description
   distinct from every place it's later cited.

A brief does not shortcut **Step 2** (voice capture) unless it included a writing sample or
named a target register (the template's optional section 16) — a thorough brief about what
the book argues is not a substitute for knowing how the author writes. It does not shortcut
**Step 4**'s judgment sections either, unless the brief already drafted them (sections 17-18) —
propose those from the rest of the brief exactly as the live path would, and get them
confirmed like anything else.

## Step 2: capture the voice

Ask for one or two samples of the author's own prose: a published piece, a blog post, an
email they liked, a chapter from a previous book. Write `00_Book_Control/Voice_Profile.md`
describing what you observe, concretely:

- typical sentence length and how much it varies
- paragraph shape; whether they open with claims or with scene
- how formal, how direct, whether they use first person
- characteristic moves (rhetorical questions, short punch sentences, extended analogies)
- vocabulary level and any recurring word choices
- what they conspicuously *don't* do

Without this the voice pass at stage 13 is editing toward generic competence. With it, it's
editing toward the author. If the author has no sample to give, note that and build the
profile from their approved drafts as the book progresses.

If the author instead describes the book as written in a recognizable nonfiction mode rather
than their own natural prose (for example, "I want this to read like sweeping macro-history,"
or names a comparable writer as a touchstone), don't try to capture *their* voice from samples
that don't represent what they're asking for. Set `Voice_Profile.md`'s "Target register" field
instead, and check `humanizer_checklist.md` for a matching named register (or the template for
defining a new one).

## Step 3: scaffold

Create `00_Book_Control/` and populate from
`assets/templates/book_control_templates.md`:

| File | Holds |
|---|---|
| `Book_Bible.md` | Identity, premise, core definitions and distinctions, high-risk topics, style exceptions, book code, structure targets, editorial decisions |
| `Master_Outline.md` | The full chapter list with status and dense per-chapter summaries |
| `Project_Status.md` | Phase, completed work, **open gate debts**, next steps, pre-publication rechecks |
| `Claim_Ledger.md` | Every claim in the book, with IDs, tiers, and both status axes |
| `Source_Registry.md` | Every source, with permanent C-IDs and canonical descriptions |
| `Citation_Audit.md` | Compiled endnotes per chapter, in the project's citation style |
| `Image_Manifest.md` | Every chart, map, diagram, photograph, and piece of cover art, with permanent Image IDs and status |
| `Voice_Profile.md` | From step 2 |

Also fill, if applicable:
- `imprint_profile.md` for a publisher or series with a brand standard.
- `Master_Book_Brief.md` — only if setup came from the fast path above; holds the author's
  pasted brief verbatim plus the intake log. Skip this file entirely for a live-interview
  setup; there's no brief to preserve.

**Set the book code now.** Two to four characters, recorded in the Book Bible, used in every
Claim ID for this book. See `traceability.md`.

Do **not** create chapter folders for the whole book up front. Create each as the chapter is
opened, per the chapter workflow.

## Step 4: fill the Book Bible's judgment sections

Three sections need real thought, not placeholder text:

**Core Definitions.** Every key term the book relies on, defined precisely. Every later
chapter depends on these staying stable, and terminology drift is the most common
whole-manuscript defect.

**Core Distinctions.** Pairs of concepts the book will keep carefully separate. These are
usually the book's actual intellectual contribution. State them precisely enough that a
reviewer could hold a chapter to them.

**Treatment of the book's own commitment.** Every argumentative book argues for something.
State plainly, at least once in the book, that holding its position doesn't by itself make
anyone right, honest, or competent, and that the real safeguards are structural. Decide here
where that goes. See `style_rules.md`.

## Setting up a series

Only when the author confirms a series:

1. Record the series name and its arc in `Master_Outline.md` or a separate series outline.
2. Confirm the **shared** `Source_Registry.md` location. One registry serves the whole
   series; a C-ID assigned in book one means the same source in book four.
3. Note which facts and themes are likely to recur across books ("series seams"), so the
   continuity role knows where to look for cross-book contradictions.
4. Keep voice book-specific. Consistency of fact across a series is mandatory;
   homogenization of prose is not the goal.

## What setup does not do

- It does not verify facts. Nothing gets a status until stage 7 of a chapter.
- It does not create Claim IDs, unless importing material that already has them.
- It does not soften the thesis. Intake records the argument the author wants to make; the
  red team's job is testing it, and that job belongs later.
- It does not write prose.
