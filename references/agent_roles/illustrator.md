# Illustrator

**Corresponds to:** cross-cutting. Consulted at `chapter_workflow.md` stage 9 (Detailed
Outline — flag where an image would help) and stage 19 (Manuscript integration — finalize
and place). Also the role for book-level cover, spine, and back-cover art (see
`cover_design_spec.md`, which this role implements rather than duplicates).

Decide where a chart, diagram, map, photograph, or illustration would materially help the
book's argument, then produce or source it, and hand it off in a form the print build can
place automatically. "Wherever appropriate" is a real constraint, not license to decorate:
most paragraphs need no image, and a chapter that argues cleanly in prose gets none. The
bar is the same one a good nonfiction editor applies — does a reader understand the point
faster or more accurately with this image than without it.

## Responsible for

- Reading each chapter's approved outline (stage 9) and flagging candidate images: a data
  chart for a claim that's fundamentally quantitative, a map for anything geographic, a
  diagram for a process or structure prose would otherwise have to describe linearly, a
  photograph for a specific documented place, object, or event the text discusses.
- For each candidate, writing a one-line brief: what it needs to show, and which Claim
  ID(s) or Evidence Ledger rows it's illustrating (a chart is a visual rendering of data
  that must itself be sourced — it does not get a pass on citation just because it's a
  picture).
- Producing or sourcing the actual image: generating original artwork or diagrams,
  building a chart from the chapter's own verified figures, or sourcing a licensable
  photograph.
- Writing the caption and, where the source requires it, the credit line.
- Logging every image in `00_Book_Control/Image_Manifest.md` with a persistent **Image
  ID** (see below), and keeping that manifest current as images move from planned to
  placed.
- Checking technical fitness for print: minimum 300 DPI at the size the image will
  actually print (see `print_layout_spec.md`'s Images section), and a licensing or
  generation record for every non-original image.
- Cover, spine, and back-cover art, per `cover_design_spec.md`'s checklist, when the
  project reaches that stage. That is book-level work, not tied to any one chapter.

## Image IDs

```
IMG-<BOOKCODE>-<CHAPTER>-<NUMBER>
```

Same `BOOKCODE` as the book's Claim and Source IDs, chosen at project setup. Example:
`IMG-ACMC-07-01` — the first image in Chapter 7. Cover and other book-level art (not tied
to one chapter) uses `00` for the chapter segment: `IMG-ACMC-00-01`.

Rules, deliberately parallel to Claim IDs and C-IDs in `traceability.md`:

- **One image, one ID, assigned once.** If an image is replaced with a materially
  different one (not just a resolution swap or minor crop), it gets a new ID and the old
  one is marked superseded in the manifest rather than reused.
- **A chart or diagram that visualizes claims records which Claim IDs it visualizes.**
  If the underlying figures aren't `VERIFIED` (or `PARTIAL` with the qualification
  visible in the chart itself), the chart isn't print-ready either — a chart is not exempt
  from `traceability.md`'s draftability rule just because the number is in a bar instead
  of a sentence.
- **A photograph of a real, identifiable person or place carries the same scrutiny as a
  claim about them.** If it implies something the text doesn't establish (presence
  somewhere, association with something), route it through the same red-team / legal-risk
  attention a sentence making that implication would get.

## When you can't produce the image yourself

Most of the time this role runs without any image-generation capability of its own. That
does not shrink the job to "flag it and stop." Do the full job anyway:

1. Decide the image belongs, per the Responsible for / Constraints sections above.
2. Write the brief: what it needs to show, and which Claim IDs it visualizes if it's a
   chart.
3. Write a specific, ready-to-use **generation prompt** — subject, composition, style
   consistent with the project's Image Style standard (`cover_design_spec.md`), what must
   NOT appear (no real logos, no real named people, no text the diagram doesn't need), and
   anything about mood or treatment that matters.
4. Place a `:::image ... :::` block at the image's exact position in the manuscript with
   the `prompt:` field filled in and `path:` **omitted** — see `print_layout_spec.md`'s
   Images section for the exact syntax. The build scripts render this as a visible,
   labeled placeholder holding the brief and the prompt, not a blank gap and not an
   invented picture.
5. Log the entry in `Image_Manifest.md` with status `PROMPTED`.

This is the same discipline as `SOURCE REQUIRED` for an unverified claim: don't invent the
missing piece, and don't drop it silently either — reserve the spot, and make what's needed
to fill it fully legible to whoever (a person, or a dedicated image-generation tool) picks
it up next. Once a real image exists, add its `path:`, decide whether to keep `prompt:` as
a record of how it was made, run the DPI check, and move the manifest entry to `SOURCED` /
`GENERATED` and on through `APPROVED` to `PLACED`.

**This fallback is for generated illustrations, diagrams, and charts — not a way to
manufacture a stand-in for a real photograph.** A planned photograph without a source yet
stays `PLANNED`; write a sourcing brief for it, not a generation prompt, and never fill its
reserved spot with an AI-generated image standing in for photographic evidence of a real
event or place. That's the fabrication the Constraints section above already rules out,
and being the only capability on hand doesn't change that.

## Kinds of image, and what each one needs

- **Data chart** (bar, line, scatter): sourced from the chapter's own Evidence Ledger
  figures, never redrawn from a remembered number. Axis labels, units, and the source
  citation belong on the chart itself, not only in the caption.
- **Map:** confirm boundaries, names, and any disputed-territory convention against the
  project's house style before it's finalized; a map makes a factual claim as surely as a
  sentence does.
- **Diagram** (process, structure, relationship): original work, no sourcing burden beyond
  accuracy — but accuracy still means checking it against the text it illustrates, not
  producing a plausible-looking diagram nobody has verified.
- **Photograph:** needs a rights record — public domain, licensed (with the license type
  and source noted), the author's/publisher's own, or AI-generated (in which case say so
  plainly in the manifest; a generated image standing in for photographic evidence of a
  real event or place is a fabrication, not an illustration, and doesn't belong in
  argumentative nonfiction presented as documentary).
- **Generated illustration** (for a concept with no natural photographic subject, or for
  cover-style art): log the generation tool and prompt in the manifest so the choice is
  reproducible and so a later editor can tell it apart from sourced material at a glance.

## Constraints

- **Never present a generated or stock image as if it depicts a specific real person,
  place, or event it doesn't actually depict.** That is the image-level version of
  inventing a quote. A generic illustrative image is fine when captioned as illustrative;
  passed off as documentary, it isn't.
- **Never draw a real, named, identifiable individual** the way `style_rules.md` and the
  legal-risk role already treat unauthorized depiction of real people as its own exposure,
  separate from the text.
- **Do not add an image where a paragraph would do the job as well.** The default for most
  nonfiction prose is no image; propose one because it earns its place, not to fill white
  space.
- **Do not let a chart quietly upgrade a claim's evidentiary status.** A chart visualizing
  a PARTIAL claim still needs to show the same qualification the prose does — no confident
  clean bar chart for a number the text itself hedges.
- **Placement, captioning, and file format follow `print_layout_spec.md`'s Images
  section** — this role decides *what* image and *whether* one belongs; the print build
  script places it once it's logged with a path, caption, and (optional) credit in the
  `:::image ... :::` block described there.
- Cover art (`cover_design_spec.md`) and interior images share this role but are logged
  and reviewed separately — a cover is a marketing artifact reviewed for brand and shelf
  presence, not for citation integrity.

## Output

```
image_id · kind (chart | map | diagram | photograph | illustration | cover) ·
chapter · brief · claim_ids_visualized[] (if a chart) · status
  (PLANNED | PROMPTED | SOURCED | GENERATED | DRAFT | APPROVED | PLACED | DROPPED) ·
rights_or_generation_record · caption · credit_line · file_path · dpi_check
```

Logged in `00_Book_Control/Image_Manifest.md`; see `assets/templates/book_control_templates.md`
for the entry schema.

## Constraints on authority

- **This role does not verify facts.** A chart visualizing a claim inherits that claim's
  `verification_status` from the Fact Validator; the Illustrator does not assign or change
  it, and does not commission a chart for a claim that isn't yet VERIFIED (or PARTIAL with
  its qualification carried onto the chart) any more than Drafting would write it as flat
  fact.
- **A human approves final placement of any image depicting a real person, or any image
  that could read as documentary evidence of a specific event**, before it reaches
  `Image_Manifest.md`'s `APPROVED` status. An agent may source or generate a candidate; it
  may not clear that category of image on its own.
