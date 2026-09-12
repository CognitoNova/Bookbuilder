# Imprint Profile Template

Fill this only when a book belongs to a publisher, imprint, or series with its own brand
standard. A one-off self-published title doesn't need it; the Book Bible's Project Identity
section is enough.

When it does apply, this file is the master copy. Copy the Imprint section into each book's
own Book Bible so the publisher and motto are visible locally, but change them here first if
they ever change.

Save as `00_Book_Control/Imprint_Profile.md`, or in a shared location if several books use it.

---

```markdown
# Imprint Profile: [Publisher / Imprint Name]

Source of truth: [the official brand guide, and its version, if one exists]
Last updated: [date]

## Mission

[What this imprint publishes and why, in one or two sentences.]

## Brand Personality

[A short list of adjectives that should be recognizable in the finished object.]

## Imprint

**Publisher:** [Name]
**Primary tagline / motto:** *[Tagline]*
**Secondary tagline:** *[If one exists, and where it's allowed to appear instead]*
**Author byline:** *[Exact form used on covers and title pages. Note any shortened form that
is NOT permitted, if that has been a problem before.]*

[If a tagline is restricted to certain media (a web-only line that must not appear in print,
for example), say so explicitly here. That distinction is easy to lose and expensive to
catch after a cover is designed.]

## Palette

Use exact values, not approximations.

| Name | Hex | Use |
|---|---|---|
| [Primary] | `#______` | [Chapter titles, headings, primary accents] |
| [Secondary] | `#______` | [Accent, callout labels, category band] |
| [Tertiary] | `#______` | [Links and cross-references where the medium supports colour] |
| [Background] | `#______` | [Cover and callout-box background] |
| [Body text] | `#______` | [Body text; often a soft near-black rather than pure black] |
| [Reserved] | `#______` | [Sparingly: awards or premium editions only] |

## Typography

- **Display** (chapter and cover titles): [Font], fallback [Font]
- **Body:** [Font], fallback [Font]
- **Sans support** (running headers, captions, callout labels): [Font], fallback [Font]

Brand fonts are frequently not installed in the environment producing a `.docx`. Where they
aren't, fall back gracefully and **tell the author a substitution happened** rather than
letting it pass silently. For final print-ready files, install the real fonts rather than
relying on substitution.

## Logo

[Name and description of the mark, where the asset file lives, and the usage rules: never
distorted, rotated, recolored, or placed on a low-contrast background. Note any watermark or
crest treatment expected on chapter openers, and whether the build script can apply it.]

## Trim Size

**Default:** [e.g. 6" x 9"]
**Alternate:** [e.g. 5.5" x 8.5"]

Pick one per book and stay consistent within that title.

## Category Colour Coding

[If the imprint colour-codes titles by subject, the mapping. Confirm each title's category
with the author rather than assuming; many titles plausibly fit more than one.]

| Category | Colour |
|---|---|
| | |

## Titles

| # | Title | Category | Status |
|---|---|---|---|
| 1 | | | |

[Update the Status column as each book progresses. It's the fastest way to see where the
whole list stands.]

## What Every Title Shares

- The chapter workflow and the role structure.
- The universal style rules, plus this imprint's house rules.
- The print interior specification and its build script.
- This imprint and motto in the front matter.
- The palette, typography, and logo rules above.
- The same control-file and chapter-folder structure, so a project opened years apart still
  works the same way.

## What Each Title Defines for Itself

- Its own title, subtitle, thesis, book code, and outline.
- Its own Core Definitions, Core Distinctions, and Treatment-of-its-own-commitment statement.
- Its own High-Risk Topics and genre traps.
- Its own trim size choice, held consistent within the book.
- Its own editorial decisions.
```
