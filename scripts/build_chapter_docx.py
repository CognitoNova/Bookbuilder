#!/usr/bin/env python3
"""
build_chapter_docx.py

Export ONE chapter as a standard-manuscript-format .docx, for handing off to
a copyeditor or line editor. This is deliberately not the same output as
build_interior_docx.py: that script produces the finished, trim-sized,
typeset print interior for the whole book; this one produces a plain,
double-spaced working manuscript page for a single chapter, the format an
editor actually expects to mark up or track-change, per
references/humanizer_checklist.md and chapter_workflow.md stage 19.

Run this once a chapter's file is ready to hand off. `Approved_Chapter.md`
(the stage-19 output, after author final approval) is the intended input for
a genuinely final draft; `Draft_2.md` (stage 13, post-voice-pass) also works
if you want post-editing to start before the remaining review gates finish.

Usage:
    python build_chapter_docx.py \
        --chapter "Approved_Chapter.md" \
        --book-title "Book Title" \
        --author "Author Name" \
        --notes "../../00_Book_Control/Citation_Audit.md" \
        --output "Chapter 7 - Editing Draft.docx"

Citations: if --notes is given, this looks up the chapter's own section in
the book's Citation_Audit.md (a "## <Chapter Title>" heading, matching the
chapter's own H1) and renders it as numbered endnotes at the END of this
chapter's document. That placement is deliberate, not a formatting
shortcut: Amazon KDP's own text guidelines say endnotes belong "at the end
of the chapter or book," and this system's print interior (built by
build_interior_docx.py) already compiles every chapter's notes into the
book's back matter as a "Notes" section grouped by chapter. This file's
end-of-chapter notes are that same content, scoped to one chapter, so an
editor can see the sourcing without it interrupting the prose above; the
final KDP submission still gets its endnotes from the book-level build, not
from this file.

Chapter file format expected: an optional metadata block (Status /
Citation status / Gate debts lines, as chapter_folder_templates.md's
Draft_2.md and Approved_Chapter.md produce), then a single Markdown H1 with
the chapter's own title (no "Chapter N:" prefix needed here -- unlike the
compiled manuscript, there's only one chapter in this file, so there's no
ambiguity to resolve), then body paragraphs, block quotes ("> "), bulleted
lists, "## " section headings, ":::callout Label ... :::" boxes, and
":::image ... :::" figures, same as the whole-manuscript format (see
references/print_layout_spec.md). Images render at a smaller working-draft
size here, not fitted to the print trim size, since this file is for
copyediting, not final layout.

Dependencies: python-docx (pip install python-docx --break-system-packages)
"""

import argparse
import sys
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Reuse the manuscript parser and inline-emphasis renderer rather than
# reimplementing markdown handling a second time. This script's own look
# (fonts, colors, layout) is set independently below; it does not touch the
# print interior's module-level style globals.
import build_interior_docx as interior


def extract_chapter_notes(notes_text, chapter_title):
    """Pull this chapter's own section out of a compiled Citation_Audit.md:
    the block between a "## <chapter title>" heading and the next "## " or
    "---" boundary. Matching is case-insensitive and tolerant of the
    chapter's title appearing with or without a "Chapter N:" prefix, since
    Citation_Audit.md's own heading may use either depending on when it was
    compiled. Returns a list of citation lines, or an empty list if no
    matching section is found."""
    target = chapter_title.strip().lower()
    lines = notes_text.split("\n")
    collected = []
    capturing = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            heading = stripped[3:].strip().lower()
            # Match on the whole heading, or on the tail after a "Chapter N:"
            # prefix, so "## Chapter 7: The Concrete Foundations" still
            # matches a chapter file titled just "The Concrete Foundations".
            tail = heading.split(":", 1)[-1].strip()
            capturing = heading == target or tail == target
            continue
        if stripped == "---":
            capturing = False
            continue
        if capturing and stripped:
            collected.append(stripped)
    return collected


def setup_manuscript_styles(document, font, font_size, line_spacing):
    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = font
    normal.font.size = Pt(font_size)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = line_spacing
    normal.paragraph_format.first_line_indent = Inches(0.5)
    normal.paragraph_format.widow_control = True

    if "MS Quote" not in [s.name for s in styles]:
        quote = styles.add_style("MS Quote", 1)
        quote.base_style = normal
        quote.font.size = Pt(font_size)
        quote.paragraph_format.left_indent = Inches(0.5)
        quote.paragraph_format.first_line_indent = Inches(0)
        quote.paragraph_format.line_spacing = 1.0
        quote.paragraph_format.space_before = Pt(6)
        quote.paragraph_format.space_after = Pt(6)

    if "MS Section Heading" not in [s.name for s in styles]:
        heading = styles.add_style("MS Section Heading", 1)
        heading.base_style = normal
        heading.font.bold = True
        heading.font.size = Pt(font_size)
        heading.paragraph_format.first_line_indent = Inches(0)
        heading.paragraph_format.line_spacing = 1.0
        heading.paragraph_format.space_before = Pt(18)
        heading.paragraph_format.space_after = Pt(6)
        heading.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        heading.paragraph_format.keep_with_next = True


def add_manuscript_header(section, author, book_title):
    """Standard manuscript convention: a running header reading
    "Author / Short Title / #", not the print interior's alternating
    book-title/chapter-title headers, since this is a single-chapter
    working file, not a bound book."""
    header = section.header
    header.is_linked_to_previous = False
    p = header.paragraphs[0]
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(f"{author} / {book_title} / ")
    run.font.size = Pt(10)
    interior.add_field(p, "PAGE", "1")
    for run in p.runs:
        run.font.size = Pt(10)


def build(args):
    interior.IMAGES_DIR = Path(args.images_dir) if args.images_dir else Path(args.chapter).parent
    interior.PENDING_IMAGE_IDS.clear()
    chapter_text = Path(args.chapter).read_text(encoding="utf-8")
    chapters = interior.parse_manuscript(chapter_text, strict_chapter_headings=False)

    if not chapters:
        print(
            f"No chapter heading found in {args.chapter} (expected a Markdown H1). Nothing to build.",
            file=sys.stderr,
        )
        sys.exit(1)
    if len(chapters) > 1:
        print(
            f"Warning: {args.chapter} contains {len(chapters)} H1 headings; "
            f"exporting only the first ('{chapters[0]['title']}'). A chapter "
            "file should contain exactly one chapter.",
            file=sys.stderr,
        )
    chapter = chapters[0]

    document = Document()
    setup_manuscript_styles(document, args.font, args.font_size, args.line_spacing)

    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    add_manuscript_header(section, args.author, args.book_title)

    title_p = document.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.first_line_indent = Inches(0)
    title_p.paragraph_format.line_spacing = 1.0
    title_p.paragraph_format.space_after = Pt(6)
    run = title_p.add_run(chapter["title"])
    run.bold = True
    run.font.size = Pt(args.font_size + 4)
    title_p.paragraph_format.space_after = Pt(24)

    for block in chapter["blocks"]:
        if block["type"] == "para":
            p = document.add_paragraph()
            interior.add_runs_with_emphasis(p, block["text"], base_size=Pt(args.font_size), base_name=args.font)
        elif block["type"] == "quote":
            p = document.add_paragraph(style="MS Quote")
            interior.add_runs_with_emphasis(p, block["text"], base_size=Pt(args.font_size), base_name=args.font)
        elif block["type"] == "callout":
            # Reuse the print interior's shaded callout box, but in
            # grayscale rather than brand color, since this is a plain
            # working manuscript, not the typeset book.
            saved = (interior.NAVY, interior.ACCENT_RED, interior.IVORY_HEX, interior.BODY_FONT, interior.SANS_FONT)
            interior.NAVY = RGBColor(0, 0, 0)
            interior.ACCENT_RED = RGBColor(0, 0, 0)
            interior.IVORY_HEX = "F2F2F2"
            interior.BODY_FONT = args.font
            interior.SANS_FONT = args.font
            try:
                interior.add_callout_box(document, block.get("label", ""), block["paras"])
            finally:
                interior.NAVY, interior.ACCENT_RED, interior.IVORY_HEX, interior.BODY_FONT, interior.SANS_FONT = saved
        elif block["type"] == "image":
            # Smaller default width than the print interior uses, since this is a
            # working manuscript page, not the final typeset column.
            saved_width = interior.DEFAULT_IMAGE_WIDTH_IN
            interior.DEFAULT_IMAGE_WIDTH_IN = 3.5
            try:
                interior.add_image_block(document, block)
            finally:
                interior.DEFAULT_IMAGE_WIDTH_IN = saved_width
        elif block["type"] == "heading2":
            document.add_paragraph(block["text"], style="MS Section Heading")
        elif block["type"] == "list":
            for item in block["items"]:
                p = document.add_paragraph(style="List Bullet")
                p.paragraph_format.first_line_indent = Inches(0)
                p.paragraph_format.line_spacing = args.line_spacing
                interior.add_runs_with_emphasis(p, item, base_size=Pt(args.font_size), base_name=args.font)

    if args.notes:
        notes_text = Path(args.notes).read_text(encoding="utf-8")
        note_lines = extract_chapter_notes(notes_text, chapter["title"])
        if note_lines:
            document.add_page_break()
            heading = document.add_paragraph()
            heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
            heading.paragraph_format.first_line_indent = Inches(0)
            heading.paragraph_format.line_spacing = 1.0
            heading.paragraph_format.space_after = Pt(18)
            run = heading.add_run("Notes")
            run.bold = True
            run.font.size = Pt(args.font_size + 2)
            for line in note_lines:
                p = document.add_paragraph()
                p.paragraph_format.first_line_indent = Inches(-0.3)
                p.paragraph_format.left_indent = Inches(0.3)
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = Pt(6)
                interior.add_runs_with_emphasis(p, line, base_size=Pt(args.font_size - 1), base_name=args.font)
        else:
            print(
                f"Note: no section matching chapter title '{chapter['title']}' found in "
                f"{args.notes}; exported without endnotes.",
                file=sys.stderr,
            )

    document.save(args.output)
    print(f"Wrote {args.output} ('{chapter['title']}').")
    if interior.PENDING_IMAGE_IDS:
        print(
            f"Note: {len(interior.PENDING_IMAGE_IDS)} image(s) in this chapter are reserved "
            "but not yet produced: " + ", ".join(interior.PENDING_IMAGE_IDS),
            file=sys.stderr,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--chapter", required=True, help="Path to the chapter file (Approved_Chapter.md or Draft_2.md).")
    parser.add_argument("--book-title", required=True, help="Used in the running header, e.g. 'Book Title'.")
    parser.add_argument("--author", required=True, help="Used in the running header.")
    parser.add_argument("--notes", default=None, help="Path to the book's Citation_Audit.md, to pull this chapter's endnotes.")
    parser.add_argument("--images-dir", default=None, help="Directory a :::image ... ::: block's relative path: field resolves against (default: this chapter file's own directory).")
    parser.add_argument("--font", default="Times New Roman", help="Body font (default: Times New Roman, the standard manuscript-format convention).")
    parser.add_argument("--font-size", type=int, default=12, help="Body font size in points (default: 12).")
    parser.add_argument("--line-spacing", type=float, default=2.0, help="Body line spacing (default: 2.0, i.e. double-spaced).")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    build(args)


if __name__ == "__main__":
    main()
