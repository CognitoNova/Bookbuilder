# Cover Design Specification

The front cover, spine, and back cover are a separate deliverable from the interior file
`scripts/build_interior_docx.py` produces. Nothing in this skill generates cover artwork
automatically; that needs an illustrator or an image-generation tool, not a docx script.

This file exists so cover work, whenever and however it happens, follows a documented
standard rather than being redesigned from scratch per book. Where the project has an
imprint with a brand guide, that guide governs and its specifics live in the project's
`Imprint_Profile.md`; this file is the checklist of what a cover has to decide.

## Logo and mark

If the project has a logo, define its clear-space rule (a common convention: clear space
equal to the height of some dominant element of the mark) and its prohibitions: never
distorted, rotated, recolored, or placed on a busy or low-contrast background.

The logo is usually the one visual element that should look identical on every cover, spine,
and title page in a list. Record where the asset file lives so it isn't recreated from
memory each time.

## Front cover system

Decide each of these once, per imprint, and hold them:

- **Background:** a single consistent treatment, usually white or a light brand tint.
- **Title:** a large display serif occupying roughly 50 to 60 percent of the cover's
  vertical space. This is the dominant element. Don't let a subtitle, illustration, or the
  author's name compete with it for size.
- **Series or tagline line:** a small uppercase line at the top, using an approved tagline.
  If a project has more than one approved tagline, record which is allowed where, and
  record any line that is explicitly *not* allowed in print. Web-only lines migrating onto
  covers is a common and avoidable error.
- **Author byline:** the exact form used across the list, in small caps. Record any
  shortened form that is not permitted.
- **Illustration:** a consistent treatment in a consistent position (a lower-third
  monochrome silhouette is one workable system). Whatever the choice, it should be
  restrained enough not to compete with the title.
- **Subtitle:** centered beneath the title.
- **Logo:** centered at the bottom.

## Category colour coding

Some imprints assign each book's accent colour, used in the title treatment and the spine
band, by subject category rather than by launch order. If yours does, the mapping lives in
`Imprint_Profile.md`.

Assigning a title to a category is an editorial judgment, not something to assume silently:
many books plausibly fit more than one category. Confirm with the author per book, then log
the decision in that book's Book Bible and in the imprint profile's title table.

## Spine

Logo at top, title centered, author name beneath, and a colour band at the bottom matching
the book's category colour where the project uses one. Spine width depends on page count and
paper stock; get the final number from the printer rather than estimating.

## Back cover

- A 150 to 250 word synopsis.
- Two or three endorsements once available. **Leave placeholder space rather than inventing
  quotes**, and never draft a blurb in a real person's voice before they've given one.
- A short author bio.
- The logo.
- ISBN and barcode.
- Website and QR code, if used.

## Image style

Whatever the project chooses, write it down: illustration technique, motif range, gradient
tolerance, and what to avoid. A one-line standard ("engraved or vector silhouettes,
restrained motifs, minimal gradients, no photographic realism") is enough to keep six covers
looking like a set. Apply it to cover art and interior figures alike.

## What this skill automates

The build script handles interior pages only: title page, imprint page, table of contents,
chapter text, and back matter. Cover work is applied by hand, through an image tool, or by
briefing a designer. Keep the logo, palette, and typography choices consistent with the
interior so the finished cover matches the book it wraps.
