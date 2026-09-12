# Agent Roles

The chapter workflow's stages each belong to a named specialist role. Run a stage as its own
dedicated pass (a subagent, or a fresh context) whenever practical. A reviewer that hasn't
been immersed in producing the work is more likely to catch what the work missed, which is
the same reason authors don't proofread their own manuscripts well.

Full instructions for each role are in `agent_roles/`.

## The 16 roles

| Role | File | Workflow stage |
|---|---|---|
| Editorial Director | `editorial_director.md` | Cross-cutting; owns stage 19 and the control files |
| Librarian | `librarian.md` | Cross-cutting; consulted before stages 2, 4, 5, 6, 11, 12, 17 |
| Illustrator | `illustrator.md` | Cross-cutting; consulted at stage 9 (flag candidates), finalizes at stage 19; also cover/spine art |
| Research Planning | `research_planning.md` | 2 (Research Plan) |
| Primary Source | `primary_source.md` | 4 (Primary-source research) |
| Scholarly Evidence | `scholarly_evidence.md` | 5 (Scholarly research) |
| Fact Extractor | `fact_extractor.md` | 6 (Fact extraction) |
| Fact Validator | `fact_validator.md` | 7 (Fact validation) |
| Red Team | `red_team.md` | 8 (argument level), 15 (prose level and fairness) |
| Chapter Architect | `chapter_architect.md` | 9 (Detailed Outline) |
| Drafting | `drafting.md` | 11 (Draft 1) |
| Voice/Style | `voice_style.md` | 13 (Voice pass) |
| Citation Integrity | `citation_integrity.md` | 12 (audit), 14 (drift), and the final manifest |
| Legal Risk | `legal_risk.md` | 8 (named-person triage), 16 (full review) |
| Continuity | `continuity.md` | 17 (book, and series where applicable) |
| Research Router | `research_router.md` | Series projects only; after stage 7 |

Three roles are cross-cutting rather than tied to one stage. The **Editorial Director** owns
the whole workflow and the book's control files. The **Librarian** is consulted before any
research-, drafting-, or review-heavy stage, to prevent duplicate work and surface what the
project already knows. The **Illustrator** is consulted at stage 9 to flag where a chart,
map, diagram, or photograph would help a chapter's argument, and again at stage 19 to
finalize and place whatever was approved — most chapters need no image at all, and deciding
that is as much this role's job as producing one.

One role is conditional. The **Research Router** exists only for series projects; a
standalone book has nowhere to route findings to and skips it entirely.

## Separation of authority

The roles are deliberately constrained so that no single one can move a claim from "someone
asserted this" to "the book states this as fact." The constraints that matter:

- **Only the Fact Validator assigns `verification_status`.** Not the researcher who found
  the source, not the router, not the drafter who needs the claim, not a continuity pass,
  not a human reviewer.
- **Only a human clears `human_review_status`** where review is required. An agent may
  prepare the record; it may not sign off on its own work.
- **The Researcher, Extractor, and Router never verify.** They gather, atomize, and triage.
- **The Humanizer never changes meaning.** It changes wording.
- **The Legal Risk role flags risk; it is not a lawyer** and its review is not legal advice.
- **The Illustrator does not verify facts or upgrade a claim's evidentiary status by
  charting it.** A chart inherits its underlying claim's `verification_status` from the
  Fact Validator; it does not acquire a cleaner one for being visual. A human, not an
  agent, clears any image depicting a real identifiable person before it's marked
  `APPROVED` in the Image Manifest.

These separations are the reason the system's output is trustworthy. Collapsing two roles
into one pass to save time collapses the check along with it.

## How this relates to the whole-manuscript passes

The Continuity role works chapter by chapter as each chapter reaches stage 17. It's distinct
from `consistency_reviewer_role.md`, which is a separate whole-manuscript pass run after the
full manuscript or a substantial batch is complete, and from `humanizer_checklist.md`, which
is the pattern checklist the Voice/Style role applies rather than a role definition itself.
