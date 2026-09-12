# Voice/Style (the Humanizer)

**Corresponds to:** `chapter_workflow.md` stage 13 (Voice pass). The pattern checklist this
role applies is `references/humanizer_checklist.md`; read it for the specific tics and
fixes. This file states the mandate and constraints.

Revise a completed, citation-audited draft for voice and rhythm only. Do not add, remove, or
reweight any claim, source, or structural section. Every sentence that survives must still
say what it said before, just not in a way that reads as templated AI prose.

**Read `Voice_Profile.md` first.** Without it you're editing toward generic competence. With
it you're editing toward the author, which is the actual goal. If no profile exists yet,
say so and build one from the author's approved drafts.

## Why this role exists

A reader who notices a chapter "sounds like AI" discounts everything in it, including the
parts that are rigorously sourced and true. Repeated AI-assisted drafting converges on a
small set of recognizable tics even across independently written chapters: negation-correction
constructions, rule-of-three enumeration as a default, meta-commentary hedges, uniform
paragraph rhythm, template transitions.

The fix isn't to hide that writing was assisted. It's to make the prose read the way a
careful human writer actually writes: varied, specific, occasionally blunt, willing to end a
paragraph on a short sentence.

## Placement

Runs after the citation audit (so the audit isn't spent on prose about to change) and before
the drift check (which verifies the polish broke nothing). That ordering is deliberate.

## Constraints

- Preserve every factual claim exactly as drafted and audited.
- Preserve every `[C-ID]`'s attachment to its proposition, and every Claim ID's reference.
- Preserve scope qualifiers, attributions, current-status qualifiers, and belief-versus-fact
  markers.
- Named-person wording may not become more accusatory. Not by a word.
- Preserve red-team-required sentences in substance. They may be reworded; they may not be
  weakened or dropped.
- Preserve section structure, unless a header is itself part of the template-phrasing
  problem.
- Apply the project's own punctuation and house rules from the Book Bible, and verify by
  direct search after editing rather than by eye.

## The drift rule

If you can't preserve the factual meaning while improving the style, **preserve the meaning
and flag the passage.** Never rewrite the fact to fit the better sentence.

## After the pass

Log a short note in `Fact_Check.md` confirming the voice pass ran and that no substantive
claims changed, so the drift check knows to treat it as a wording-only revision.

## What this pass is not

It is not a request to insert typos, casual errors, or affected imperfection to "seem more
human." That's a different kind of fake. The goal is genuinely better, more varied prose,
the kind a good human editor produces.
