# Front Matter Template

Fill in and save as `Front_Matter.md` in the manuscript folder. Present to the author for
approval before treating it as final. It precedes the Introduction in reading order and
feeds directly into `scripts/build_interior_docx.py`'s `--title`, `--subtitle`, `--author`,
`--publisher`, and `--motto` arguments, so the values here and the values passed to the
script should never diverge.

```markdown
# Front Matter

**Status:** Proposed, awaiting author approval
**Logged:** [date]

---

## Title Page

**[Book Title]**
*[Subtitle]*

[Author Name, in the exact byline form used across the project]

---

## Publisher Imprint

**[Publisher Name]:** *[Motto or tagline, if the project has one]*

[For a self-published title with no imprint, omit this section entirely rather than
inventing a publisher name.]

---

## Copyright Page

[Kept to a simple imprint line until closer to print. Add these as they're finalized:]

- Copyright notice and year
- ISBN
- Edition and printing history
- Rights reserved statement
- Printer or distributor, if required
- Any permissions acknowledgements for quoted or reproduced material

---

**Note:** permissions are easy to leave until too late. If the book reproduces song lyrics,
poetry, substantial prose excerpts, images, or figures from another source, the clearance
work belongs on the pre-publication checklist in `Project_Status.md`, not in the final week.
```
