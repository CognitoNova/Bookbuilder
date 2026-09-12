# Print Layout Specification

The interior design standard: a print-ready file that looks deliberate and consistent throughout, with the same trim size, margin logic, typography, and treatment of chapter openers, quotations, callouts, notes, and images. Use `scripts/build_interior_docx.py` to generate the formatted `.docx` from a compiled manuscript. This file documents the specification the script implements, so the standard is legible on its own and can be re-implemented in another tool (InDesign, Vellum, Atticus) later if needed. Cover and spine design, a separate deliverable, is in `references/cover_design_spec.md`.

## Palette

Colours are project-specific. If the book belongs to a publisher or imprint with a brand standard, they're defined in that project's `Imprint_Profile.md` (see `assets/templates/imprint_profile.md`); use those exact hex values, not approximations. Pass them to the build script with `--primary-color`, `--accent-color`, `--body-color`, and `--callout-bg`; anything not passed falls back to the script's defaults.

For a book with no imprint standard, pick a small palette and hold it:

| Role | Guidance |
|---|---|
| Primary | Chapter titles, headings, primary accents. One colour, used consistently. |
| Accent | Callout labels and any category banding. Used sparingly. |
| Body text | A soft near-black (something like `#222222`) rather than pure black. Easier to read at length and it looks less harsh in print. |
| Callout background | A light tint that stays legible under body text. |

## Typography

A book needs three faces at most:

- **Display** (chapter titles, cover titles): a serif with some personality.
- **Body**: a highly readable serif, sized for long-form reading.
- **Sans support** (running headers, captions, callout labels): a clean sans.

Display and brand fonts are frequently **not** installed in the environment producing a `.docx`. Where a specified font is missing, fall back to a standard serif and **tell the author the substitution happened** rather than letting it pass silently; a LibreOffice preview substituting a font doesn't necessarily reflect what Word will show on the author's own machine. For final print-ready files, install the real fonts rather than relying on fallback.

## Trim size

Two supported sizes. Pick one per book and stay consistent for that title; don't mix within a book.

- **6" x 9"** (default): the standard U.S. trade nonfiction size. Use this unless there's a specific reason not to.
- **5.5" x 8.5"** (alternate/digest): a smaller trim that runs more pages for the same word count. Reasonable for a shorter title or if the author wants a more compact physical object.

## Margins

Print margins need a larger inside (gutter) margin than outside, since the gutter accounts for the binding. The gutter should grow with page count; a book under 150 pages needs less gutter allowance than one over 400.

| Trim size | Top | Bottom | Outside | Inside/Gutter (under 150 pp) | Inside/Gutter (150-400 pp) | Inside/Gutter (400+ pp) |
|---|---|---|---|---|---|---|
| 6" x 9" | 0.75" | 0.75" | 0.5" | 0.75" | 0.875" | 1.0" |
| 5.5" x 8.5" | 0.75" | 0.75" | 0.5" | 0.75" | 0.875" | 1.0" |

Use mirror margins (inside/outside rather than left/right) so facing pages are symmetrical around the spine.

## Type specification

- **Body text**: the project's body serif (see Typography above), in the body-text near-black rather than pure black. 11 to 11.5pt, line spacing 1.15, first-line paragraph indent of 0.2 to 0.25 inches, no extra space between paragraphs (the indent does the separating, matching how print books actually set text, not how word processors default to setting it).
- **Chapter titles**: the project's display face, in the primary colour rather than black. A distinct, larger treatment: an eyebrow line ("CHAPTER SEVEN" or "INTRODUCTION" or "CONCLUSION") in small caps above the title, generous white space, then the chapter's actual title at 22 to 26pt. If the project's imprint profile specifies a logo or crest watermark on chapter openers, the build script does not insert it automatically (it needs the actual asset file); treat it as the finished standard once the asset exists, and note its absence when handing off an interior built without it.
- **Section headings within a chapter** (if a chapter uses them): smaller than the chapter title, bold, in the primary colour, same family as the chapter title for a consistent hierarchy. **No isolated headers**: a section heading must never sit alone at the bottom of a page with its body text pushed to the following page. The build script enforces this with "keep with next" and widow/orphan control on the heading style; if a design tool other than the build script is used, replicate this rule by hand (nudge the heading to the next page rather than leaving it stranded).
- **Running headers**: small caps or italic, 9pt, in the sans support face, book title on verso (left-hand, even) pages and the current chapter's title on recto (right-hand, odd) pages. No running header on a chapter's opening page.
- **Page numbers**: 10pt, positioned at the **outside** of the footer (outer-bottom corner: right on recto/odd pages, left on verso/even pages), not centered. No page number displayed on a chapter's opening page, though it still counts in pagination.

## Chapter openers

Every chapter starts on a new page. In the finished, print-ready book, chapters conventionally start on a recto (right-hand) page, which sometimes means leaving a blank verso page before it; this is a manual final-layout step most self-publishing tools (Vellum, Atticus, InDesign) handle automatically and isn't something the interior-build script attempts on its own. The script does guarantee every chapter starts on its own new page and suppresses the running header and page number on that first page.

## Table of contents

Build a real, dynamic table of contents, not a hand-typed page-number list. In a Word document this means an actual TOC field tied to the document's heading styles: it updates automatically to the correct page numbers whenever the document is opened or the field is refreshed, so it never drifts out of sync with the actual interior layout the way a manually typed list would the moment a chapter changes length. `scripts/build_interior_docx.py` inserts this automatically; when the file is opened in Word, either it updates on open or the user may need to right-click the TOC and choose "Update Field" (or select the whole document and press F9) once, which recalculates every page number against the real layout.

## Block quotations

Set off from body text: indented 0.4" from the left margin (no right indent needed unless the quote is verse), same or slightly smaller point size (10.5pt), no quotation marks (the indentation itself signals quotation). Attribution, if used, goes on its own line below, right-aligned. If the project's house rules ban the punctuation mark conventionally used to introduce an attribution line, set the attribution as plain "Name, Source" on its own line instead.

## Callout boxes

Used sparingly, for supplementary material that would break the chapter's flow if left inline (a defining quote, a short list of figures, a "worth knowing" aside). Set as a bordered box shaded in the callout background tint, offset from the surrounding text, with a short bold label in the accent colour at the top (e.g., "A CLOSER LOOK" or "KEY NUMBERS"). In the manuscript markdown, mark a callout with a fenced block:

```
:::callout Key Numbers
Content of the callout goes here. Can be multiple paragraphs.
:::
```

The build script detects this fence and renders it as a bordered box rather than body text.

## Footnotes and back-matter notes

This system uses endnotes, not page-bottom footnotes. In-text, a claim needing a citation gets a superscript reference number; the actual note text is compiled per chapter in the book's `Citation_Audit.md` and rendered in the printed book's back matter as a "Notes" section, grouped by chapter, numbering restarting at 1 for each chapter. Don't use Word's native footnote feature for this; keep notes as back matter so the endnote list stays generated from `Citation_Audit.md` rather than hand-maintained in two places.

## Images

Deciding what gets illustrated and producing or sourcing the image is
`references/agent_roles/illustrator.md`'s job, tracked in `00_Book_Control/Image_Manifest.md`
with a persistent `IMG-<BOOKCODE>-<CHAPTER>-<NUMBER>` ID. This section is the print
standard that role's output has to meet, and the manuscript syntax the build script reads.

- Minimum 300 DPI at the size the image will actually print, so it doesn't look soft on the page.
- Place an image at the nearest paragraph break after its first mention in text, not mid-paragraph.
- Every image gets a caption directly below it, smaller italic text, and a credit line if the source requires one.
- Center images on the page unless a specific layout reason calls for a different placement.

**Embedding in the manuscript:** in `Current_Manuscript.md`, mark an image with a fenced
block, the same pattern as a `:::callout ... :::` box:

```
:::image IMG-ACMC-07-01
path: assets/images/ch07_water_use_by_region.png
caption: Data center water consumption by region, 2020-2025.
credit: Source: EPA, 2025 (S-ACMC-041)
width: 5in
:::
```

`path` is required and resolved relative to the manuscript file's own directory unless
`scripts/build_interior_docx.py` is given `--images-dir` to point somewhere else (useful
when images live in a shared assets folder rather than beside the manuscript). `caption`
is required; `credit` and `width` are optional (`width` defaults to a size that fits the
page's text column at the trim size in use). The build script embeds the image, centers
it, sets the caption in smaller italic text directly below it, adds the credit line if
present, and — when the Pillow library is available in the build environment — checks the
image's actual pixel dimensions against the requested print width and warns rather than
silently producing a soft image if it falls under 300 DPI.

This same block, with the actual picture rendered smaller, also works in a single-chapter
file bound for `scripts/build_chapter_docx.py` (the post-editing export); there it's shown
at a working-draft size with its caption, not fitted to the print trim size, since that
file's job is copyediting, not final layout.

**When the image can't be produced yet:** the Illustrator role is often working without any
image-generation capability of its own. When that's the case, it still does its job in
full — deciding an image belongs there, writing the brief, and writing a specific,
ready-to-use generation prompt — and reserves the image's exact position in the manuscript
rather than leaving a gap or inventing a picture no one asked for. Omit `path:` and add
`prompt:` instead:

```
:::image IMG-ACMC-07-02
caption: Conceptual diagram of the "additionality" test applied to a new data center's
  power demand.
prompt: Clean, minimal editorial diagram in the style of a policy-report infographic --
  two paths from a single "new data center demand" node, one labeled "additional clean
  generation" leading to a green checkmark, one labeled "grid draw only" leading to a red
  flag. No text longer than a few words per label, no photorealistic elements, no real
  logos or people.
:::
```

A field's value can continue onto following lines, as shown above, as long as those lines
don't themselves start with `path:`, `caption:`, `credit:`, or `width:`.

The build scripts render this as a dashed placeholder box in that exact spot, holding the
brief and the full prompt — visibly a reserved to-do, not a broken reference, and distinct
from the red `[MISSING IMAGE]` warning a block gets when neither `path:` nor `prompt:`
resolves to anything (that case is a defect in the manuscript or manifest, not a planned
gap). The build's final output also lists every still-pending image by ID, so the list of
outstanding prompts is always visible at build time, not just buried in one page of a
600-page interior. Once a real image exists — generated from the prompt by whatever tool is
available, or sourced some other way — add its `path:`, drop or keep `prompt:` as a record
of how it was made, and update the entry's status in `Image_Manifest.md`.

**The prompt-only fallback is for generated illustrations, diagrams, and charts, not a way
to manufacture a substitute for a real photograph.** `references/agent_roles/illustrator.md`
already treats an AI-generated image standing in for photographic evidence of a real event
or place as a fabrication, not an illustration. A planned photograph the role can't source
stays `PLANNED` (or gets a sourcing brief, not a generation prompt) until an actual
photograph is available — it does not get a generated stand-in just because generation
happens to be the only capability on hand.

## Front and back matter order

1. Title page (title, subtitle, author)
2. Imprint/copyright page (publisher name and motto, if any, on a single centered line, plus copyright notice and edition info as those become available)
3. Table of contents
4. Introduction
5. Numbered chapters, in order, grouped under their Parts if the book uses them
6. Conclusion
7. Notes (endnotes, grouped by chapter)
8. Acknowledgments, if any (not automated by the build script; add manually)

## Consistency across a series

Where several books share an imprint, they use this same specification. Each title specifies only its own trim size and supplies its own compiled manuscript and front matter; margins, typography, chapter-opener treatment, TOC mechanics, block quote and callout formatting, and back-matter structure stay identical. That consistency is what makes a set of books read as one publisher's list rather than a pile of separate projects.
