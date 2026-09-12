#!/usr/bin/env python3
"""
build_interior_docx.py

Build a print-ready .docx interior from a compiled book manuscript, per
bookbuilder/references/print_layout_spec.md. Produces:
  - Title page + imprint/motto page
  - A dynamic TOC field (Word recalculates real page numbers on open/update)
  - Chapters, each starting on its own page, with alternating running headers
    (book title on even/verso pages, chapter title on odd/recto pages) and
    page numbers, suppressed on each chapter's opening page
  - Block quotes, :::callout ... ::: boxes, and :::image ... ::: figures rendered
    distinctly from body text
  - A back-matter Notes section built from an endnote file, if supplied

Usage:
    python build_interior_docx.py \
        --manuscript "Current Manuscript.md" \
        --title "Book Title" \
        --subtitle "Book Subtitle" \
        --author "Author Name" \
        --publisher "Publisher Name" \
        --motto "Publisher motto, if any" \
        --trim 6x9 \
        --notes "Citation_Audit.md" \
        --output "interior.docx"

    Optional, to match a project's brand palette (see the imprint profile):
        --primary-color "#0B2341" --accent-color "#C62828" \
        --body-color "#222222" --callout-bg "#F8F6F2"

Manuscript format expected: one or more chapters, each starting with a
Markdown H1 ("# Chapter Title" / "# Introduction: Title" / "# Conclusion: Title"),
optionally preceded/followed by a metadata block of the form:

If the book groups its chapters into Parts, a Part divider line
("# Part I: The Invisible Colossus") may appear before any chapter it
introduces. It becomes its own divider page (eyebrow + title, no body) and
does not need to precede every chapter -- only where a new Part begins. A
manuscript with no "# Part ..." lines builds exactly as before. Each
chapter/section is optionally preceded/followed by a metadata block of the
form:

    **Status:** ...
    **Citation status:** ...

    ---

which is treated as non-printing metadata and stripped. Body paragraphs are
separated by blank lines. A line starting with "> " is a block quote line.
A block whose every line starts with "- " or "* " is rendered as a bulleted
list. A fenced block:

    :::callout Optional Label
    content
    :::

is rendered as a bordered callout box.

An image is placed with a similar fenced block, produced by the Illustrator role
(references/agent_roles/illustrator.md) and logged in 00_Book_Control/Image_Manifest.md:

    :::image IMG-ACMC-07-01
    path: assets/images/ch07_water_use_by_region.png
    caption: Data center water consumption by region, 2020-2025.
    credit: Source: EPA, 2025 (S-ACMC-041)
    width: 5in
    :::

`path` is required (resolved relative to the manuscript file's directory unless
--images-dir points elsewhere) and `caption` is required; `credit` and `width` are
optional. See references/print_layout_spec.md's Images section for the full spec.

If the Illustrator role planned and briefed an image but had no way to actually produce
it (no image-generation capability available), the block carries a `prompt:` field and
omits `path:` instead:

    :::image IMG-ACMC-07-02
    caption: Conceptual diagram of the "additionality" test applied to a new data center's
      power demand.
    prompt: Clean, minimal editorial diagram in the style of a policy-report infographic --
      two paths from a single "new data center demand" node, one labeled "additional clean
      generation" leading to a green checkmark, one labeled "grid draw only" leading to a
      red flag. No text longer than a few words per label, no photorealistic elements, no
      real logos or people.
    :::

This renders as a dashed placeholder box holding the brief and the full prompt, in the
image's actual reserved position in the manuscript, rather than a blank gap or an invented
picture -- ready for a person or a dedicated image-generation tool to fill in later. A
field's value can run onto following lines (as in `prompt:` above) as long as those lines
don't start with another recognized field name.

Dependencies: python-docx (pip install python-docx --break-system-packages)
Optional: Pillow (pip install Pillow --break-system-packages), for the 300 DPI check on
images -- the build still works without it, just without that one warning.
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

try:
    from PIL import Image as PILImage
except ImportError:
    PILImage = None

TRIM_SIZES = {
    "6x9": (Inches(6), Inches(9)),
    "5.5x8.5": (Inches(5.5), Inches(8.5)),
}

# Gutter (inside margin) scales with page count; this is an estimate made
# before layout, so it's a reasonable default rather than an exact fit.
# Pass --pages to override the bracket if you already know roughly how long
# the finished book will run.
def gutter_for_pages(pages):
    if pages is None or pages < 150:
        return Inches(0.75)
    if pages < 400:
        return Inches(0.875)
    return Inches(1.0)


# Typographic defaults. These are the font *names* embedded in the document,
# which matters even if the machine rendering a preview lacks them and
# substitutes something else: Word on a machine that has the real fonts
# installed (all of these are on Google Fonts) will render them correctly.
# Override with --body-font / --heading-font, or set a project-wide standard in
# the imprint profile.
BODY_FONT = "Source Serif 4"
HEADING_FONT = "Libre Baskerville"
SANS_FONT = "Source Sans 3"

# Default palette. Override per project from the imprint profile's palette
# table; where a project has a brand standard, use its exact hex values rather
# than approximating them.
NAVY = RGBColor(0x0B, 0x23, 0x41)       # Primary: headings and chapter titles
ACCENT_RED = RGBColor(0xC6, 0x28, 0x28)  # Accent: callout labels
CHARCOAL = RGBColor(0x22, 0x22, 0x22)    # Body text: a soft near-black, not pure black
IVORY_HEX = "F8F6F2"                     # callout box background

# Image placement defaults. IMAGES_DIR is set in build() -- either --images-dir or the
# manuscript file's own directory -- and used to resolve a relative `path:` field from a
# :::image ... ::: block. DEFAULT_IMAGE_WIDTH_IN is used when a block omits `width:`; it's
# deliberately narrower than the full text column so a default-sized image doesn't crowd
# the page the way a full-width chart sometimes needs to.
IMAGES_DIR = None
DEFAULT_IMAGE_WIDTH_IN = 4.5
MIN_PRINT_DPI = 300

# Every :::image ... ::: block rendered as an "awaiting generation" placeholder
# (a prompt: field but no usable path: yet) gets logged here, so build() can
# print a single actionable to-do list at the end instead of the warning
# scrolling past on stderr with nothing to check it against afterward.
PENDING_IMAGE_IDS = []


def _parse_hex(value, field):
    """Accept '#0B2341' or '0B2341' and return an RGBColor."""
    v = value.strip().lstrip("#")
    if len(v) != 6 or any(c not in "0123456789abcdefABCDEF" for c in v):
        print(
            f"{field} must be a 6-digit hex colour like '#0B2341', got {value!r}",
            file=sys.stderr,
        )
        sys.exit(2)
    return RGBColor(int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))


# ---------------------------------------------------------------------------
# Manuscript parsing
# ---------------------------------------------------------------------------

# Only lines matching this pattern count as a real chapter opener. This
# deliberately excludes a compiled manuscript file's own document-level H1
# (e.g. "# Current Manuscript"), which is front-matter noise, not a chapter.
# Extend the alternation if a future book's chapters use a different label
# (e.g. "Part I", "Prologue", "Epilogue").
CHAPTER_HEADING_RE = re.compile(
    r"^#\s+((?:Chapter\s+\d+|Introduction|Conclusion|Prologue|Epilogue|Appendix\s+[A-Za-z0-9]+)\s*:?\s*.*?)\s*$",
    re.IGNORECASE,
)
# A Part divider ("# Part I: The Invisible Colossus", "# Part 3: ..."), for a
# book whose chapters are grouped into Parts. Only meaningful in the
# whole-manuscript (strict) parse -- a single chapter file never contains one.
# A manuscript with no Part headings at all behaves exactly as before.
PART_HEADING_RE = re.compile(
    r"^#\s+(Part\s+(?:[IVXLCDM]+|\d+)\s*:?\s*.*?)\s*$",
    re.IGNORECASE,
)
# Any H1 at all. Used only for a single-chapter file (see build_chapter_docx.py),
# where there's no whole-manuscript document title to confuse with a chapter
# heading, so the stricter pattern above isn't needed and would wrongly reject
# a chapter file whose own heading is just "# The Chapter's Actual Title" with
# no "Chapter N:" prefix — which is exactly what chapter_folder_templates.md's
# Draft_2.md / Approved_Chapter.md templates use before chapter_workflow.md's
# stage 19 adds the ordinal prefix on the way into Current_Manuscript.md.
ANY_H1_RE = re.compile(r"^#\s+(.+?)\s*$")
SECTION_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
METADATA_LINE_RE = re.compile(r"^\*\*(Status|Citation status|Gate debts)\:\*\*", re.IGNORECASE)

# Recognized field names inside a :::image ... ::: block. A line beginning
# "<one of these>:" starts a new field; any other line is a continuation of
# whichever field was last set, so a multi-line generation prompt (or a
# caption that itself contains a colon) doesn't get mis-split.
IMAGE_FIELD_NAMES = {"path", "caption", "credit", "width", "prompt"}


def parse_manuscript(text, strict_chapter_headings=True):
    """Split a manuscript file into a list of chapters, optionally
    interleaved with Part dividers.

    Returns a list of dicts. A chapter is
    {"kind": "chapter", "title": str, "blocks": [block, ...]} where each
    block is one of:
      {"type": "para", "text": str}
      {"type": "quote", "text": str}
      {"type": "callout", "label": str, "paras": [str, ...]}
      {"type": "image", "image_id": str, "path": str, "caption": str,
       "credit": str or None, "width": str or None, "prompt": str or None}
      -- "path" is "" (not missing/None) when the image hasn't been produced yet
      and only a "prompt:" field was given; see add_image_block().
    A Part divider (whole-manuscript / strict mode only) is
    {"kind": "part", "title": str} -- it carries no body blocks; a Part
    heading only ever introduces the chapters that follow it.

    `strict_chapter_headings` (default True) requires a chapter heading to
    match CHAPTER_HEADING_RE ("Chapter N: ...", "Introduction: ...", etc.),
    which is what lets a compiled multi-chapter manuscript tell an actual
    chapter opener apart from its own document-level title line; in this
    mode a "# Part ..." line (PART_HEADING_RE) is also recognized and
    emitted as its own divider unit. Pass strict_chapter_headings=False for
    a single-chapter file, where any H1 is unambiguously the chapter title,
    Part headings never appear, and the stricter pattern would silently
    produce zero chapters if that title doesn't happen to start with one of
    those words.
    """
    heading_re = CHAPTER_HEADING_RE if strict_chapter_headings else ANY_H1_RE
    lines = text.split("\n")
    chapters = []
    current = None
    buffer_lines = []
    in_callout = False
    callout_label = ""
    callout_paras = []
    callout_buffer = []
    in_image = False
    image_id = ""
    image_fields = {}
    image_last_key = None

    def flush_para(target_chapter):
        block = "\n".join(buffer_lines).strip()
        buffer_lines.clear()
        if not block:
            return
        if METADATA_LINE_RE.match(block):
            return
        if block == "---":
            return
        if block.startswith("> "):
            quote_text = "\n".join(
                l[2:] if l.startswith("> ") else l for l in block.split("\n")
            )
            target_chapter["blocks"].append({"type": "quote", "text": quote_text})
            return
        block_lines = block.split("\n")
        if block_lines and all(re.match(r"^[\-\*]\s+", l) for l in block_lines):
            items = [re.sub(r"^[\-\*]\s+", "", l) for l in block_lines]
            target_chapter["blocks"].append({"type": "list", "items": items})
        else:
            target_chapter["blocks"].append({"type": "para", "text": block})

    def flush_callout_para():
        block = "\n".join(callout_buffer).strip()
        callout_buffer.clear()
        if block:
            callout_paras.append(block)

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith(":::callout"):
            if current is not None:
                flush_para(current)
            in_callout = True
            callout_label = stripped[len(":::callout"):].strip()
            callout_paras = []
            callout_buffer = []
            continue

        if in_callout and stripped == ":::":
            flush_callout_para()
            if current is not None:
                current["blocks"].append(
                    {"type": "callout", "label": callout_label, "paras": list(callout_paras)}
                )
            in_callout = False
            continue

        if in_callout:
            if stripped == "":
                flush_callout_para()
            else:
                callout_buffer.append(line)
            continue

        if stripped.startswith(":::image"):
            if current is not None:
                flush_para(current)
            in_image = True
            image_id = stripped[len(":::image"):].strip()
            image_fields = {}
            image_last_key = None
            continue

        if in_image and stripped == ":::":
            if current is not None:
                current["blocks"].append({
                    "type": "image",
                    "image_id": image_id,
                    "path": image_fields.get("path", ""),
                    "caption": image_fields.get("caption", ""),
                    "credit": image_fields.get("credit"),
                    "width": image_fields.get("width"),
                    "prompt": image_fields.get("prompt"),
                })
            in_image = False
            continue

        if in_image:
            if stripped == "":
                continue
            key, sep, value = stripped.partition(":")
            key_norm = key.strip().lower()
            if sep and key_norm in IMAGE_FIELD_NAMES:
                image_fields[key_norm] = value.strip()
                image_last_key = key_norm
            elif image_last_key:
                # A continuation line (no recognized "field:" prefix -- e.g. a
                # generation prompt that runs past one line, or a caption
                # containing its own ":"). Append to whichever field was last
                # set, rather than discarding it or misreading it as a new
                # field.
                image_fields[image_last_key] = (image_fields.get(image_last_key, "") + " " + stripped).strip()
            continue

        if strict_chapter_headings:
            part_match = PART_HEADING_RE.match(line)
            if part_match:
                if current is not None:
                    flush_para(current)
                current = None
                chapters.append({"kind": "part", "title": part_match.group(1).strip()})
                continue

        match = heading_re.match(line)
        if match:
            if current is not None:
                flush_para(current)
            current = {"kind": "chapter", "title": match.group(1).strip(), "blocks": []}
            chapters.append(current)
            continue

        if current is None:
            # Front matter / document-title noise before the first real
            # chapter heading (e.g. a compiled manuscript file's own "#
            # Current Manuscript" line, or a "Compiled:" summary line).
            continue

        section_match = SECTION_HEADING_RE.match(line)
        if section_match:
            flush_para(current)
            current["blocks"].append({"type": "heading2", "text": section_match.group(1).strip()})
            continue

        if stripped == "":
            flush_para(current)
        else:
            buffer_lines.append(line)

    if current is not None:
        flush_para(current)

    return chapters


def find_unrecognized_h1_lines(text):
    """Return every H1 line that ANY_H1_RE sees but CHAPTER_HEADING_RE
    doesn't, restricted to lines that appear AFTER the first recognized
    chapter heading. This is the check that catches the exact failure mode
    CHAPTER_HEADING_RE's strictness creates: an unrecognized H1 there
    silently folds into the preceding chapter instead of starting a new
    one -- nothing raises, a chapter just quietly stops being its own
    chapter. A leading document-title H1 before any real chapter (e.g. a
    compiled manuscript's own "# Current Manuscript" line) is legitimate
    front matter, not a mis-formatted chapter, so it's deliberately not
    flagged here -- only what appears once real chapters have started."""
    unrecognized = []
    seen_real_chapter = False
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\n")
        if CHAPTER_HEADING_RE.match(line):
            seen_real_chapter = True
            continue
        if PART_HEADING_RE.match(line):
            continue
        if seen_real_chapter and ANY_H1_RE.match(line):
            unrecognized.append(line.strip())
    return unrecognized


# ---------------------------------------------------------------------------
# Inline markdown emphasis (bold / italic) -> docx runs
# ---------------------------------------------------------------------------

INLINE_EMPHASIS_RE = re.compile(r"(\*\*.+?\*\*|\*[^\*\n]+?\*)")


def add_runs_with_emphasis(paragraph, text, base_size=None, base_name=None):
    """Add `text` to `paragraph` as one or more runs, converting **bold**
    and *italic* markdown spans into real bold/italic runs instead of
    printing the literal asterisks, the way a print-ready page should."""
    parts = INLINE_EMPHASIS_RE.split(text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            run = paragraph.add_run(part)
        if base_size:
            run.font.size = base_size
        if base_name:
            run.font.name = base_name


# ---------------------------------------------------------------------------
# docx field helpers
# ---------------------------------------------------------------------------

def add_field(paragraph, instr_text, cached_text="", bold=False):
    """Insert a Word field code (TOC, PAGE, etc.) into a paragraph."""
    run = paragraph.add_run()
    run.bold = bold
    fldChar_begin = OxmlElement("w:fldChar")
    fldChar_begin.set(qn("w:fldCharType"), "begin")
    fldChar_begin.set(qn("w:dirty"), "true")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = instr_text
    run._r.append(fldChar_begin)
    run._r.append(instrText)

    r_sep = OxmlElement("w:r")
    fldChar_sep = OxmlElement("w:fldChar")
    fldChar_sep.set(qn("w:fldCharType"), "separate")
    r_sep.append(fldChar_sep)
    if cached_text:
        t = OxmlElement("w:t")
        t.text = cached_text
        r_sep.append(t)
    paragraph._p.append(r_sep)

    r_end = OxmlElement("w:r")
    fldChar_end = OxmlElement("w:fldChar")
    fldChar_end.set(qn("w:fldCharType"), "end")
    r_end.append(fldChar_end)
    paragraph._p.append(r_end)


def set_update_fields_on_open(document):
    settings = document.settings.element
    uf = OxmlElement("w:updateFields")
    uf.set(qn("w:val"), "true")
    settings.append(uf)


def set_no_header_footer(section):
    """Suppress header/footer on a section's first page (the chapter opener)."""
    section.different_first_page_header_footer = True
    section.first_page_header.is_linked_to_previous = False
    for p in list(section.first_page_header.paragraphs):
        p.text = ""
    section.first_page_footer.is_linked_to_previous = False
    for p in list(section.first_page_footer.paragraphs):
        p.text = ""


def style_header_paragraph(paragraph, text, alignment):
    paragraph.text = ""
    paragraph.alignment = alignment
    run = paragraph.add_run(text.upper())
    run.font.size = Pt(9)
    run.font.name = SANS_FONT
    run.font.italic = True


def add_page_number_footer(footer, alignment):
    """Brand guide: page numbers sit at the OUTSIDE of the footer, not
    centered, so recto (odd) pages get right alignment and verso (even)
    pages get left alignment."""
    p = footer.paragraphs[0]
    p.text = ""
    p.alignment = alignment
    add_field(p, "PAGE", "1")
    for run in p.runs:
        run.font.size = Pt(10)
        run.font.name = SANS_FONT


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------

def setup_styles(document):
    styles = document.styles

    normal = styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(11)
    normal.font.color.rgb = CHARCOAL
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.first_line_indent = Inches(0.25)
    # Widow/orphan control document-wide: never leave a single line of a
    # paragraph stranded alone at the top or bottom of a page.
    normal.paragraph_format.widow_control = True

    if "Book Body" not in [s.name for s in styles]:
        body = styles.add_style("Book Body", 1)  # WD_STYLE_TYPE.PARAGRAPH
        body.base_style = normal
        body.font.name = BODY_FONT
        body.font.size = Pt(11)
        body.font.color.rgb = CHARCOAL

    if "Book Quote" not in [s.name for s in styles]:
        quote = styles.add_style("Book Quote", 1)
        quote.base_style = normal
        quote.font.size = Pt(10.5)
        quote.font.italic = True
        quote.paragraph_format.left_indent = Inches(0.4)
        quote.paragraph_format.first_line_indent = Inches(0)
        quote.paragraph_format.space_before = Pt(6)
        quote.paragraph_format.space_after = Pt(6)

    if "Chapter Eyebrow" not in [s.name for s in styles]:
        eyebrow = styles.add_style("Chapter Eyebrow", 1)
        eyebrow.base_style = styles["Normal"]
        eyebrow.font.size = Pt(12)
        eyebrow.font.name = HEADING_FONT
        eyebrow.font.color.rgb = ACCENT_RED
        eyebrow.paragraph_format.first_line_indent = Inches(0)
        eyebrow.paragraph_format.space_before = Pt(72)
        eyebrow.paragraph_format.space_after = Pt(6)
        eyebrow.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    if "Section Heading" not in [s.name for s in styles]:
        section_style = styles.add_style("Section Heading", 1)
        section_style.base_style = normal
        section_style.font.size = Pt(13)
        section_style.font.name = HEADING_FONT
        section_style.font.bold = True
        section_style.font.color.rgb = NAVY
        section_style.paragraph_format.first_line_indent = Inches(0)
        section_style.paragraph_format.space_before = Pt(18)
        section_style.paragraph_format.space_after = Pt(6)
        # No isolated headers: never let a section heading sit alone at the
        # bottom of a page with its body text pushed to the next page.
        section_style.paragraph_format.keep_with_next = True
        section_style.paragraph_format.widow_control = True

    # Word's built-in Heading 1 / Heading 2 styles, modified in place rather
    # than custom styles. This matters: the TOC field only scans paragraphs
    # by outline level, and built-in Heading styles are the reliable way to
    # guarantee that level is set, so the table of contents actually finds
    # every entry when the field is updated in Word.
    #
    # Heading 1 (outline level 1) is reserved for Part dividers -- the
    # book's top structural tier, when the manuscript has any. Heading 2
    # (outline level 2) is what chapter titles use, whether or not the book
    # has Parts: a book with no Parts just never populates outline level 1,
    # and its TOC (built with \o "1-2") lists chapters exactly as before.
    h1 = styles["Heading 1"]
    h1.font.size = Pt(32)
    h1.font.name = HEADING_FONT
    h1.font.bold = True
    h1.font.color.rgb = NAVY
    h1.paragraph_format.first_line_indent = Inches(0)
    h1.paragraph_format.space_before = Pt(0)
    h1.paragraph_format.space_after = Pt(36)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    h2 = styles["Heading 2"]
    h2.font.size = Pt(24)
    h2.font.name = HEADING_FONT
    h2.font.bold = True
    h2.font.color.rgb = NAVY
    h2.paragraph_format.first_line_indent = Inches(0)
    h2.paragraph_format.space_before = Pt(0)
    h2.paragraph_format.space_after = Pt(36)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER


def add_callout_box(document, label, paragraphs):
    table = document.add_table(rows=1, cols=1)
    table.autofit = True
    cell = table.cell(0, 0)
    cell.text = ""

    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), IVORY_HEX)
    tcPr.append(shd)

    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "8")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "999999")
        borders.append(el)
    tcPr.append(borders)

    cell_margin = OxmlElement("w:tcMar")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "200")
        el.set(qn("w:type"), "dxa")
        cell_margin.append(el)
    tcPr.append(cell_margin)

    p0 = cell.paragraphs[0]
    if label:
        run = p0.add_run(label.upper())
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = SANS_FONT
        run.font.color.rgb = ACCENT_RED
    for para_text in paragraphs:
        p = cell.add_paragraph()
        p.paragraph_format.first_line_indent = Inches(0)
        add_runs_with_emphasis(p, para_text, base_size=Pt(10.5), base_name=BODY_FONT)
    document.add_paragraph()  # spacing after the box


def _parse_image_width(width_field):
    """Accept '5in', '5', or '5.5in' from a :::image block's `width:` field and
    return inches as a float. Falls back to DEFAULT_IMAGE_WIDTH_IN for anything
    missing or unparseable, rather than raising, since a malformed width shouldn't
    take down the whole build over one figure."""
    if not width_field:
        return DEFAULT_IMAGE_WIDTH_IN
    cleaned = width_field.strip().lower().rstrip("in").strip()
    try:
        return float(cleaned)
    except ValueError:
        print(f"Warning: could not parse image width {width_field!r}; using default.", file=sys.stderr)
        return DEFAULT_IMAGE_WIDTH_IN


def _resolve_image_path(raw_path):
    p = Path(raw_path)
    if p.is_absolute() and p.exists():
        return p
    if IMAGES_DIR is not None:
        candidate = IMAGES_DIR / raw_path
        if candidate.exists():
            return candidate
    if p.exists():
        return p
    # Nothing resolved; return the IMAGES_DIR-joined path (or the raw path) anyway
    # so the caller's existence check reports a sensible attempted location.
    return (IMAGES_DIR / raw_path) if IMAGES_DIR is not None else p


def add_pending_generation_box(document, image_id, caption, prompt):
    """Render the reserved space for an image that's been planned and briefed
    but not yet produced: no dedicated image-generation capability was available
    to the role/session that wrote this block, so instead of inventing a picture
    or silently dropping the slot, it left a bordered placeholder holding the
    exact spot in the manuscript plus everything a person or a dedicated image
    generator needs to fill it -- same principle as SOURCE REQUIRED for an
    unverified claim. Deliberately styled differently from the red
    [MISSING IMAGE] case below: that one is a broken reference (a manifest points
    at a file that should exist and doesn't); this one is an intentional,
    tracked to-do, not a defect."""
    table = document.add_table(rows=1, cols=1)
    table.autofit = True
    cell = table.cell(0, 0)
    cell.text = ""

    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "EFEFEF")
    tcPr.append(shd)

    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "dashed")
        el.set(qn("w:sz"), "8")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "999999")
        borders.append(el)
    tcPr.append(borders)

    cell_margin = OxmlElement("w:tcMar")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "200")
        el.set(qn("w:type"), "dxa")
        cell_margin.append(el)
    tcPr.append(cell_margin)

    p0 = cell.paragraphs[0]
    run = p0.add_run(f"AWAITING IMAGE GENERATION — {image_id}")
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = SANS_FONT
    run.font.color.rgb = ACCENT_RED

    if caption:
        p_cap = cell.add_paragraph()
        p_cap.paragraph_format.first_line_indent = Inches(0)
        p_cap.paragraph_format.space_before = Pt(6)
        run = p_cap.add_run(caption)
        run.italic = True
        run.font.size = Pt(10)
        run.font.name = BODY_FONT

    if prompt:
        p_label = cell.add_paragraph()
        p_label.paragraph_format.first_line_indent = Inches(0)
        p_label.paragraph_format.space_before = Pt(6)
        run = p_label.add_run("Generation prompt:")
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.name = SANS_FONT

        p_prompt = cell.add_paragraph()
        p_prompt.paragraph_format.first_line_indent = Inches(0)
        run = p_prompt.add_run(prompt)
        run.font.size = Pt(9.5)
        run.font.name = BODY_FONT
    document.add_paragraph()  # spacing after the box


def add_image_block(document, block):
    """Render one :::image ... ::: block: the picture itself (centered, sized per
    its `width:` field or DEFAULT_IMAGE_WIDTH_IN), a caption directly below in
    smaller italic text, and a credit line below that if supplied. Per
    references/print_layout_spec.md's Images section. A missing file or an image
    under the 300 DPI print floor at its requested size doesn't halt the build --
    it's flagged loudly (stderr, and a visible placeholder in the document itself
    for a missing file) so it's caught before print, not silently shipped soft.

    A block with a `prompt:` field but no usable `path:` yet is a different case
    from a broken reference: it's an image the Illustrator role planned and
    briefed but couldn't produce itself (no image-generation capability
    available), so the reserved spot renders as a dashed placeholder box holding
    the brief and the full generation prompt, ready for a person or a dedicated
    image tool to fill in -- see add_pending_generation_box()."""
    image_id = block.get("image_id", "")
    raw_path = block.get("path", "")
    caption = block.get("caption", "")
    credit = block.get("credit")
    prompt = block.get("prompt")
    width_in = _parse_image_width(block.get("width"))

    if not raw_path:
        if prompt:
            PENDING_IMAGE_IDS.append(image_id or "(unlabeled image)")
            add_pending_generation_box(document, image_id or "(unlabeled image)", caption, prompt)
            return
        print(f"Warning: {image_id or '(unlabeled image)'} has no path: or prompt: field; skipped.", file=sys.stderr)
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(f"[MISSING IMAGE: {image_id} — no path or prompt given in Image_Manifest.md]")
        run.italic = True
        run.font.size = Pt(10)
        run.font.color.rgb = ACCENT_RED
        return

    resolved = _resolve_image_path(raw_path)
    if not resolved.exists():
        print(f"Warning: {image_id} — image file not found at {resolved} (from path: {raw_path!r}).", file=sys.stderr)
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(f"[MISSING IMAGE: {image_id} — expected at {raw_path}]")
        run.italic = True
        run.font.size = Pt(10)
        run.font.color.rgb = ACCENT_RED
        return

    if PILImage is not None:
        try:
            with PILImage.open(resolved) as im:
                px_width, _ = im.size
            actual_dpi = px_width / width_in if width_in else None
            if actual_dpi is not None and actual_dpi < MIN_PRINT_DPI:
                print(
                    f"Warning: {image_id} is about {actual_dpi:.0f} DPI at the requested "
                    f"{width_in}in width (print floor is {MIN_PRINT_DPI} DPI). It will look "
                    f"soft on the printed page; use a higher-resolution source or a smaller width.",
                    file=sys.stderr,
                )
        except Exception as e:
            print(f"Warning: could not read image dimensions for {image_id} ({resolved}): {e}", file=sys.stderr)

    document.add_picture(str(resolved), width=Inches(width_in))
    document.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    if caption:
        cap_p = document.add_paragraph()
        cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap_p.paragraph_format.first_line_indent = Inches(0)
        cap_p.paragraph_format.space_before = Pt(6)
        cap_p.paragraph_format.space_after = Pt(2) if credit else Pt(12)
        run = cap_p.add_run(caption)
        run.italic = True
        run.font.size = Pt(9.5)
        run.font.name = SANS_FONT

    if credit:
        credit_p = document.add_paragraph()
        credit_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        credit_p.paragraph_format.first_line_indent = Inches(0)
        credit_p.paragraph_format.space_before = Pt(0)
        credit_p.paragraph_format.space_after = Pt(12)
        run = credit_p.add_run(credit)
        run.font.size = Pt(8.5)
        run.font.name = SANS_FONT
        run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)


def add_title_page(document, title, subtitle, author):
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(180)
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(28)
    run.font.name = HEADING_FONT
    run.font.color.rgb = NAVY

    if subtitle:
        p2 = document.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(18)
        run2 = p2.add_run(subtitle)
        run2.italic = True
        run2.font.size = Pt(14)
        run2.font.name = BODY_FONT

    p3 = document.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.paragraph_format.space_before = Pt(72)
    run3 = p3.add_run(author)
    run3.font.size = Pt(14)
    run3.font.name = BODY_FONT


def add_imprint_page(document, publisher, motto):
    """Publisher name and motto render as a single centered line,
    "Publisher Name: Motto", rather than a two-line treatment with the motto
    italicised beneath the name. If no motto is supplied, only the publisher
    name is set."""
    document.add_page_break()
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(300)
    run = p.add_run(publisher)
    run.bold = True
    run.font.size = Pt(13)
    run.font.name = BODY_FONT
    run.font.color.rgb = NAVY

    if motto:
        run_sep = p.add_run(": ")
        run_sep.bold = True
        run_sep.font.size = Pt(13)
        run_sep.font.name = BODY_FONT
        run_sep.font.color.rgb = NAVY

        run2 = p.add_run(motto)
        run2.italic = True
        run2.font.size = Pt(13)
        run2.font.name = BODY_FONT
        run2.font.color.rgb = NAVY


def add_toc_page(document):
    document.add_page_break()
    heading = document.add_paragraph()
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = heading.add_run("Contents")
    run.bold = True
    run.font.size = Pt(20)
    run.font.name = HEADING_FONT
    run.font.color.rgb = NAVY
    heading.paragraph_format.space_after = Pt(24)

    toc_p = document.add_paragraph()
    add_field(
        toc_p,
        'TOC \\o "1-2" \\h \\z \\u',
        "Right-click here and choose \"Update Field\" (or press Ctrl+A "
        "then F9) to build the table of contents with live page numbers.",
    )


def restart_page_numbering(section, start=1):
    """Reset page numbering to `start` from this section forward. Used once,
    on the first chapter's section, so the front matter (title/imprint/TOC)
    doesn't count into the body's page 1."""
    sectPr = section._sectPr
    pgNumType = OxmlElement("w:pgNumType")
    pgNumType.set(qn("w:start"), str(start))
    sectPr.append(pgNumType)


def add_chapter(document, book_title, chapter, running_header_alignment):
    # Every chapter gets its own section (not just the ones after the
    # first), so the front-matter section stays exclusively front matter
    # with no running header bleeding into it.
    section = document.add_section(WD_SECTION.NEW_PAGE)

    section.header.is_linked_to_previous = False
    style_header_paragraph(section.header.paragraphs[0], chapter["title"], running_header_alignment["odd"])

    section.even_page_header.is_linked_to_previous = False
    style_header_paragraph(section.even_page_header.paragraphs[0], book_title, running_header_alignment["even"])

    section.footer.is_linked_to_previous = False
    add_page_number_footer(section.footer, WD_ALIGN_PARAGRAPH.RIGHT)  # recto/odd: outside = right
    section.even_page_footer.is_linked_to_previous = False
    add_page_number_footer(section.even_page_footer, WD_ALIGN_PARAGRAPH.LEFT)  # verso/even: outside = left

    set_no_header_footer(section)

    eyebrow = document.add_paragraph(style="Chapter Eyebrow")
    eyebrow.add_run(chapter["title"].split(":")[0].upper() if ":" in chapter["title"] else "")
    title_p = document.add_paragraph(style="Heading 2")
    title_p.add_run(chapter["title"])

    for block in chapter["blocks"]:
        if block["type"] == "para":
            p = document.add_paragraph(style="Book Body")
            add_runs_with_emphasis(p, block["text"])
        elif block["type"] == "quote":
            p = document.add_paragraph(style="Book Quote")
            add_runs_with_emphasis(p, block["text"])
        elif block["type"] == "callout":
            add_callout_box(document, block.get("label", ""), block["paras"])
        elif block["type"] == "image":
            add_image_block(document, block)
        elif block["type"] == "heading2":
            p = document.add_paragraph(block["text"], style="Section Heading")
        elif block["type"] == "list":
            for item in block["items"]:
                p = document.add_paragraph(style="List Bullet")
                p.paragraph_format.first_line_indent = Inches(0)
                add_runs_with_emphasis(p, item, base_size=Pt(11), base_name=BODY_FONT)

    return section


def add_part_divider(document, book_title, part, running_header_alignment):
    """A standalone divider page for a Part heading: eyebrow ("PART I") plus
    main title, vertically dropped down the page, no body text. Gets its own
    section like a chapter does, so page numbering and running headers
    continue correctly, but the divider page itself carries neither (same
    treatment as a chapter's own opening page)."""
    section = document.add_section(WD_SECTION.NEW_PAGE)

    section.header.is_linked_to_previous = False
    style_header_paragraph(section.header.paragraphs[0], book_title, running_header_alignment["odd"])
    section.even_page_header.is_linked_to_previous = False
    style_header_paragraph(section.even_page_header.paragraphs[0], book_title, running_header_alignment["even"])

    section.footer.is_linked_to_previous = False
    add_page_number_footer(section.footer, WD_ALIGN_PARAGRAPH.RIGHT)
    section.even_page_footer.is_linked_to_previous = False
    add_page_number_footer(section.even_page_footer, WD_ALIGN_PARAGRAPH.LEFT)

    set_no_header_footer(section)

    title = part["title"]
    if ":" in title:
        eyebrow_text, main_text = title.split(":", 1)
        eyebrow_text = eyebrow_text.strip()
        main_text = main_text.strip()
    else:
        eyebrow_text, main_text = "", title

    eyebrow = document.add_paragraph(style="Chapter Eyebrow")
    eyebrow.paragraph_format.space_before = Pt(240)
    if eyebrow_text:
        eyebrow.add_run(eyebrow_text.upper())

    title_p = document.add_paragraph(style="Heading 1")
    title_p.add_run(main_text if main_text else title)

    return section


def add_notes_backmatter(document, notes_text, book_title):
    section = document.add_section(WD_SECTION.NEW_PAGE)
    section.header.is_linked_to_previous = False
    style_header_paragraph(section.header.paragraphs[0], book_title, WD_ALIGN_PARAGRAPH.CENTER)
    section.even_page_header.is_linked_to_previous = False
    style_header_paragraph(section.even_page_header.paragraphs[0], book_title, WD_ALIGN_PARAGRAPH.CENTER)
    section.footer.is_linked_to_previous = False
    add_page_number_footer(section.footer, WD_ALIGN_PARAGRAPH.RIGHT)
    section.even_page_footer.is_linked_to_previous = False
    add_page_number_footer(section.even_page_footer, WD_ALIGN_PARAGRAPH.LEFT)
    set_no_header_footer(section)

    heading = document.add_paragraph()
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = heading.add_run("Notes")
    run.bold = True
    run.font.size = Pt(20)
    run.font.name = HEADING_FONT
    run.font.color.rgb = NAVY
    heading.paragraph_format.space_after = Pt(18)

    for line in notes_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            p = document.add_paragraph()
            run = p.add_run(stripped[3:])
            run.bold = True
            run.font.size = Pt(13)
            run.font.name = HEADING_FONT
            run.font.color.rgb = NAVY
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Inches(0)
            # No isolated headers: keep each per-chapter Notes subheading
            # glued to the first line of notes that follows it.
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.widow_control = True
        elif stripped.startswith("#"):
            continue
        elif stripped == "---":
            continue
        else:
            p = document.add_paragraph(style="Book Body")
            p.paragraph_format.first_line_indent = Inches(0)
            add_runs_with_emphasis(p, stripped, base_size=Pt(9.5), base_name=BODY_FONT)

    return section


def build(args):
    global BODY_FONT, HEADING_FONT, SANS_FONT, NAVY, ACCENT_RED, CHARCOAL, IVORY_HEX, IMAGES_DIR
    PENDING_IMAGE_IDS.clear()
    manuscript_path = Path(args.manuscript)
    IMAGES_DIR = Path(args.images_dir) if args.images_dir else manuscript_path.parent
    if args.body_font:
        BODY_FONT = args.body_font
    if args.heading_font:
        HEADING_FONT = args.heading_font
    if args.sans_font:
        SANS_FONT = args.sans_font
    if args.primary_color:
        NAVY = _parse_hex(args.primary_color, "--primary-color")
    if args.accent_color:
        ACCENT_RED = _parse_hex(args.accent_color, "--accent-color")
    if args.body_color:
        CHARCOAL = _parse_hex(args.body_color, "--body-color")
    if args.callout_bg:
        _parse_hex(args.callout_bg, "--callout-bg")  # validate
        IVORY_HEX = args.callout_bg.strip().lstrip("#").upper()

    manuscript_text = manuscript_path.read_text(encoding="utf-8")
    chapters = parse_manuscript(manuscript_text)
    if not chapters:
        print("No chapters found (expected Markdown H1 headings). Nothing to build.", file=sys.stderr)
        sys.exit(1)

    unrecognized = find_unrecognized_h1_lines(manuscript_text)
    if unrecognized and not args.allow_unrecognized_headings:
        print(
            "Found H1 line(s) that don't match a recognized chapter heading "
            "(\"Chapter N: ...\", \"Introduction: ...\", \"Conclusion: ...\", "
            "\"Prologue: ...\", \"Epilogue: ...\", or \"Appendix A: ...\"). Left as-is, each of these "
            "silently merges into the PRECEDING chapter instead of starting a "
            "new one -- a chapter can vanish into its neighbor with no error "
            "and no visible sign in the output:",
            file=sys.stderr,
        )
        for line in unrecognized:
            print(f"    {line!r}", file=sys.stderr)
        print(
            "Fix the heading in Current_Manuscript.md (chapter_workflow.md stage 19 expects "
            "\"# Chapter <N>: <Title>\" when a chapter is appended), or pass "
            "--allow-unrecognized-headings if this is deliberate.",
            file=sys.stderr,
        )
        sys.exit(1)

    width, height = TRIM_SIZES[args.trim]
    gutter = gutter_for_pages(args.pages)

    document = Document()
    setup_styles(document)
    set_update_fields_on_open(document)

    section0 = document.sections[0]
    section0.page_width = width
    section0.page_height = height
    section0.top_margin = Inches(0.75)
    section0.bottom_margin = Inches(0.75)
    section0.left_margin = Inches(0.5)  # outside; mirror margins below
    section0.right_margin = Inches(0.5)
    section0.gutter = gutter
    document.settings.odd_and_even_pages_header_footer = True

    sectPr = section0._sectPr
    mirror = OxmlElement("w:mirrorMargins")
    sectPr.append(mirror)

    add_title_page(document, args.title, args.subtitle, args.author)
    if args.publisher or args.motto:
        add_imprint_page(document, args.publisher, args.motto)
    add_toc_page(document)

    running_header_alignment = {
        "odd": WD_ALIGN_PARAGRAPH.RIGHT,
        "even": WD_ALIGN_PARAGRAPH.LEFT,
    }

    for i, unit in enumerate(chapters):
        if unit.get("kind") == "part":
            sec = add_part_divider(document, args.title, unit, running_header_alignment=running_header_alignment)
        else:
            sec = add_chapter(document, args.title, unit, running_header_alignment=running_header_alignment)
        # propagate trim size / margins to each new section
        sec.page_width = width
        sec.page_height = height
        sec.top_margin = Inches(0.75)
        sec.bottom_margin = Inches(0.75)
        sec.left_margin = Inches(0.5)
        sec.right_margin = Inches(0.5)
        sec.gutter = gutter
        sec_sectPr = sec._sectPr
        mirror2 = OxmlElement("w:mirrorMargins")
        sec_sectPr.append(mirror2)
        if i == 0:
            # Body page numbering starts fresh at 1; the front-matter
            # section (title/imprint/TOC) isn't counted into it.
            restart_page_numbering(sec, start=1)

    if args.notes:
        notes_text = Path(args.notes).read_text(encoding="utf-8")
        sec = add_notes_backmatter(document, notes_text, args.title)
        sec.page_width = width
        sec.page_height = height
        sec.top_margin = Inches(0.75)
        sec.bottom_margin = Inches(0.75)
        sec.left_margin = Inches(0.5)
        sec.right_margin = Inches(0.5)
        sec.gutter = gutter
        sec_sectPr = sec._sectPr
        mirror3 = OxmlElement("w:mirrorMargins")
        sec_sectPr.append(mirror3)

    document.save(args.output)
    chapter_count = sum(1 for u in chapters if u.get("kind") != "part")
    part_count = sum(1 for u in chapters if u.get("kind") == "part")
    image_count = sum(
        1 for u in chapters if u.get("kind") != "part" for b in u.get("blocks", []) if b["type"] == "image"
    )
    part_note = f", {part_count} parts" if part_count else ""
    image_note = f", {image_count} images" if image_count else ""
    print(f"Wrote {args.output} ({chapter_count} chapters{part_note}{image_note}).")
    if PILImage is None and image_count:
        print(
            "Note: Pillow isn't installed, so images were placed without a DPI check. "
            "pip install Pillow --break-system-packages to enable it.",
            file=sys.stderr,
        )
    if PENDING_IMAGE_IDS:
        print(
            f"\n{len(PENDING_IMAGE_IDS)} image(s) are reserved but not yet produced "
            "(placeholder boxes with a generation prompt were placed for each): "
            + ", ".join(PENDING_IMAGE_IDS)
            + ". Run each prompt through an image generator or source the real image, "
            "update its path: in Current_Manuscript.md and its status in "
            "00_Book_Control/Image_Manifest.md, then rebuild.",
            file=sys.stderr,
        )
    print("Open in Word and update the Table of Contents field (Ctrl+A, then F9) "
          "if it doesn't refresh automatically on open.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manuscript", required=True, help="Path to the compiled manuscript markdown file.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", required=True)
    parser.add_argument("--publisher", default="", help="Publisher or imprint name. Omit for a self-published title with no imprint.")
    parser.add_argument("--motto", default="", help="Publisher motto or tagline, if the project has one.")
    parser.add_argument("--trim", choices=list(TRIM_SIZES.keys()), default="6x9")
    parser.add_argument("--pages", type=int, default=None, help="Estimated final page count, to pick the right gutter width.")
    parser.add_argument("--body-font", default=None, help=f"Override the body font (default: {BODY_FONT}).")
    parser.add_argument("--heading-font", default=None, help=f"Override the display/heading font (default: {HEADING_FONT}).")
    parser.add_argument("--sans-font", default=None, help=f"Override the brand sans-serif support font used in running headers, page numbers, and callout labels (default: {SANS_FONT}).")
    parser.add_argument("--primary-color", default=None, help="Hex colour for chapter titles and headings (default: #0B2341).")
    parser.add_argument("--accent-color", default=None, help="Hex colour for callout labels and accents (default: #C62828).")
    parser.add_argument("--body-color", default=None, help="Hex colour for body text; use a soft near-black rather than pure black (default: #222222).")
    parser.add_argument("--callout-bg", default=None, help="Hex fill for callout box backgrounds (default: #F8F6F2).")
    parser.add_argument("--notes", default=None, help="Path to an endnote compilation (e.g. Citation_Audit.md) for the back-matter Notes section.")
    parser.add_argument("--images-dir", default=None, help="Directory a :::image ... ::: block's relative path: field resolves against (default: the manuscript file's own directory). Use this when images live in a shared assets folder rather than beside the manuscript.")
    parser.add_argument("--allow-unrecognized-headings", action="store_true", help="Skip the check for an H1 that won't be recognized as its own chapter and will silently merge into the preceding one. Only pass this if you've confirmed by hand that every chapter is intact.")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    build(args)


if __name__ == "__main__":
    main()
