# Book Builder

A complete system for producing serious argumentative nonfiction: a book that takes a
position and survives scrutiny of it. From the first interview about what the book is, to a
print-ready interior file.

This is the merge of two working systems. The **operational layer** (chapter workflow,
control files, style rules, humanizer, print production) comes from a pipeline proven across
31 chapter-length units of a finished book. The **rigor layer** (persistent claim IDs, a
global source registry, claim-type verification standards, citation integrity auditing,
defamation review) comes from a separate editorial control system built for the same
problem. Neither half was complete alone.

## What makes it different

**Every factual proposition is traceable.** Claims get persistent IDs. Sources get permanent
IDs. The link between them survives drafting, polishing, and integration, and a final
manifest proves it end to end. A book that can't show where a fact came from can't defend it.

**The gates are real, and they run where they're cheap.** Red-team review happens before
drafting, not after. Named-person risk gets triaged before a paragraph is written and polished.
Citation auditing happens before the voice pass; a cheap drift check happens after it.

**Rigor scales with consequence.** Claims are tiered. A load-bearing causal accusation gets
independent corroboration and full metadata. An uncontroversial date gets its source checked
and nothing more. The alternative, treating every claim identically, spends the project's
attention in the wrong places.

**Gates are soft while drafting, hard at publication.** Skip a stage for momentum if you
want. It's logged as a debt in `Project_Status.md` and it has to clear before final approval
and before the print build. A skipped gate is deferred, never waived.

## Structure

```text
bookbuilder-v4/
├── SKILL.md                              Routing hub: figure out where the user is first
├── README.md
├── CHANGELOG.md
├── references/
│   ├── project_setup.md                  Book Brief Interview, voice capture, scaffolding
│   ├── chapter_workflow.md               The 20-stage chapter protocol
│   ├── traceability.md                   Claim IDs, C-IDs, tiers, registry, blocking codes
│   ├── verification.md                   The status decision table (always load)
│   ├── verification_matrix.md            Per-claim-type standards (load on demand)
│   ├── style_rules.md                    Universal rules plus per-project house rules
│   ├── humanizer_checklist.md            AI-prose tics and how to fix them
│   ├── consistency_reviewer_role.md      Whole-manuscript pass
│   ├── print_layout_spec.md              Interior design specification
│   ├── cover_design_spec.md              Cover, spine, back cover
│   ├── agent_roles.md                    The 16-role index
│   └── agent_roles/                      One file per role
├── assets/templates/
│   ├── imprint_profile.md                Publisher/series brand profile
│   ├── master_book_brief_template.md     Fill-in brief the author preps and pastes in,
│   │                                     instead of a live setup interview
│   ├── book_control_templates.md         Book Bible, Master Outline, Project Status,
│   │                                     Claim Ledger, Source Registry, Citation Audit,
│   │                                     Image Manifest, Master Book Brief, Voice Profile
│   ├── chapter_folder_templates.md       Per-chapter file skeletons
│   └── front_matter_template.md
└── scripts/
    ├── build_interior_docx.py            Print interior build (whole book)
    └── build_chapter_docx.py             Per-chapter manuscript-format export (post-editing)
```

## The two layers

**The chapter loop** runs once per chapter, twenty stages from Author Input to Manuscript
Integration.

**Book-level work** runs once: project setup, whole-manuscript consistency review, series
continuity, the final citation manifest, the print build.

Don't research an entire book before drafting a word. Research one chapter, write it, review
it, integrate it, open the next.

## The chapter loop at a glance

| Stage | What happens |
|---|---|
| 0 to 3 | Author input, chapter ticket, research plan, **author approves scope** |
| 4 to 5 | Primary-source and scholarly research, including opposing evidence |
| 6 to 7 | Fact extraction (Claim IDs, tiers), fact validation (Evidence Ledger, statuses) |
| 8 | Red team at argument level, plus named-person triage, both pre-draft |
| 9 to 10 | Detailed outline, **author approves outline** |
| 11 | Draft 1: VERIFIED as fact, PARTIAL only with its qualification stated, UNVERIFIED not at all |
| 12 to 14 | Citation audit, voice pass, drift check |
| 15 to 17 | Fairness verification and prose-level red team, legal-risk review, continuity |
| 18 to 19 | **Author final approval**, manuscript integration |

## The status model

Two independent axes, because "the evidence supports this" and "a human approved this" are
different questions and conflating them is how unsupported claims get published.

`verification_status`: VERIFIED · PARTIAL · UNVERIFIED · OPINION_NOT_VERIFIABLE

`human_review_status`: NOT_REQUIRED · PENDING · APPROVED · HOLD · REVISE

Human approval never upgrades evidence. Only the Fact Validator assigns verification status.

## Worked example

Raw sentence:

> Senator John Doe knowingly lied about the study. Studies show that 74 percent of Americans
> oppose the policy.

Extraction separates three propositions:
- Doe made a statement about the study.
- Doe knew the statement was false.
- 74 percent of Americans oppose the policy.

Validation finds:
- statement exists: VERIFIED
- knowing falsity: UNVERIFIED (conduct doesn't establish a mental state)
- the statistic: UNVERIFIED (no poll identified)

So the drafter can't state the latter two as fact. If research then finds the actual poll
reports 61 percent, the claim is rewritten with that figure and a real C-ID. The mental-state
claim goes to legal review and comes back as documented conduct: "Doe's statement conflicts
with the study's published findings. [C0114]"

The result is a stronger criticism, because it rests on something a reader can check.

## Adapting it

Nothing here assumes a topic, a publisher, or a politics. Every project-specific element gets
captured at setup: thesis, target of critique, genre traps, high-risk topics, house style
rules, citation style, required reviewers, imprint and brand, and the author's own voice.

The one rule that doesn't bend: when choosing between making an argument easier and making it
more defensible, choose defensible.
