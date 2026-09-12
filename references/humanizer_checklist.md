# The Humanizer: Voice and Style Pass

This is stage 13. It runs after the citation audit (stage 12) and before the drift check (stage 14), so the audit isn't spent on prose about to change and the polish gets verified afterward. Its job is narrow: find and fix the prose patterns that make a chapter recognizable as AI-assisted writing, without touching any claim, source, or piece of evidence. This is a wording pass, not a content pass. If you find yourself wanting to change what a sentence argues rather than how it's phrased, that's a different kind of edit and belongs in an earlier stage, not here.

Read the project's `Voice_Profile.md` before starting. Without it this pass edits toward generic competence rather than toward this author.

## Why this matters

A reader who notices a chapter "sounds like AI" will discount everything in it, including the parts that are rigorously sourced and true. The fix isn't to hide that the writing was assisted, it's to make the prose read the way a careful human writer actually writes: varied, specific, occasionally blunt, willing to end a paragraph on a short sentence.

## Patterns to hunt for

**Repeated hedge phrases.** Watch for the same softening construction showing up more than once or twice across a chapter: "it's worth noting that," "arguably," "in many ways," "to some extent," "it should be said." One use is fine. Three uses in 900 words is a tic. Cut most of them outright; a claim that needs hedging usually just needs a more precise claim, not a softer one.

**Template section transitions.** Watch for every section starting with the same rhetorical move: every paragraph opening with a rhetorical question, every section closing with "ultimately," every transition using "however" or "that said." Vary the opening move paragraph to paragraph the way a human writer naturally does without thinking about it.

**Uniform sentence rhythm.** Long, evenly-paced sentences of similar length back to back read as generated even when they're not. Read a paragraph aloud (or simulate doing so). If every sentence lands with the same cadence, break the rhythm: a short sentence after a long one, a sentence fragment used deliberately, a one-line paragraph for emphasis.

**Duplicated negation-correction constructions.** Watch for the same "not X, but Y" or "this isn't a claim that... it's a claim that..." shape recurring across a chapter. It's a genuinely useful construction for precision, which is exactly why it's overused. Keep it where it's doing real work; vary or cut it elsewhere.

**Over-signaled structure.** Phrases like "first," "moreover," "in conclusion," "as discussed above" that exist to announce the essay's own structure rather than to say something. A human writer's transitions usually do double duty (they connect ideas AND move the argument forward); a purely structural transition is dead weight.

**The three-item list reflex.** Watch for everything arriving in groups of exactly three (three examples, three adjectives, three clauses in a sentence). Real writing is lumpier than that. Two is fine. Four is fine. Vary it.

**Summarizing what was just said before moving on.** A paragraph that ends by restating its own point in slightly different words, right before the next paragraph makes a new point, is padding. Cut the restatement; let the next paragraph's first sentence do the work of moving forward.

## How to do the pass

1. Read the full chapter straight through, out loud if possible, without stopping to fix anything. Note where it drags or where you can predict the next sentence's shape before you read it.
2. Go back through and fix the specific instances you noticed, working sentence level, not paragraph level. Don't rewrite whole paragraphs from scratch; that risks losing precision the draft has already earned through its citation audit.
3. After fixing, re-read once more. If a fix introduced a new repeated pattern, fix that too. This is iterative, not one pass.
4. Confirm nothing about the chapter's actual claims changed. The drift check at stage 14 will diff C-IDs, Claim IDs, proposition meaning, scope qualifiers, and attributions, and the fairness review at stage 15 checks the argument against the Opposition Brief. But a wording change that accidentally strengthens or weakens a claim is cheapest to catch here, by the person who made it, rather than at stage 14 by someone reconstructing what happened.
5. Log in `Fact_Check.md` that the voice pass ran and that no substantive claims changed, so the drift check knows to treat this as a wording-only revision.

## What this pass is not

It is not a request to insert typos, casual grammar errors, or affected imperfection to "seem more human." That's a different kind of fake. The goal is genuinely better, more varied prose, the kind a good human editor would produce, not a performance of humanness layered on top of otherwise-unchanged writing.

## Optional alternate targets: named nonfiction registers

The default target for this pass is always the project's own `Voice_Profile.md` — the author's
actual prose, captured from real samples. That default doesn't change, and for most chapters
it's the right one.

Some books, though, are written in a register that isn't really "this author's natural prose"
so much as a recognizable mode of nonfiction writing: the sweeping, cross-disciplinary
macro-history voice; a scene-first narrative style that opens on a moment before pulling back
to the argument; a plain-spoken, service-journalism directness. If the Book Bible names one of
these as the book's target register, or the author asks for it on a given chapter, run the pass
using the matching agent prompt below instead of, or layered on top of, the generic tic-hunt
earlier in this file.

A register is defined by its craft techniques, not by naming a specific living writer as the
target. Two reasons for that, and both matter: a technique-based definition transfers ("blend
disciplines, anchor abstractions in analogy, vary sentence rhythm") in a way that "sound like
this particular person" doesn't, and asking an agent to write *in a named author's distinct
voice* is a meaningfully different instruction than asking it to *use the moves that voice is
known for* — the first invites recognizable mimicry of one person's brand, the second describes
a craft pattern several writers in a tradition share. Where a register below is closely
associated with a particular writer, that's noted for recognizability, but the instruction
itself never names them.

**It still operates inside this pass's constraints, whichever register is used.** Nothing here
licenses touching a claim, a C-ID, a scope qualifier, or an attribution. The mandate in
`agent_roles/voice_style.md` still governs: preserve every factual claim exactly as drafted and
audited, preserve red-team-required sentences in substance, and flag rather than rewrite
anything where style and factual meaning pull in different directions. Any register that leans
on rhetorical questions needs active supervision on that specific point — a rhetorical question
is a style device, not a new claim, and it must never imply an assertion the chapter hasn't
actually sourced.

**Record the choice.** If a chapter or a whole book is run through a named register, note it in
`Voice_Profile.md`'s "Target register" field (or `Project_Status.md` if no voice profile exists
yet) so later chapters and the whole-manuscript consistency review treat it as the intended
register rather than as drift.

### Macro-synthesis nonfiction

The popular-science / macro-history mode most associated with writers like Yuval Noah Harari:
it zooms out from a specific event or institution to what it reveals about human history,
cognition, or social organization, and moves freely across disciplines to get there.

**When this fits:** big-idea nonfiction that deliberately widens its lens; books whose premise
is cross-disciplinary synthesis (biology, history, economics, philosophy in the same
paragraph); chapters that lean on analogy to make an abstract or institutional concept
graspable.

**When it doesn't:** memoir or first-person narrative, technical or policy-heavy chapters where
precision matters more than sweep, legal-sensitive sections where a provocative rhetorical
question could read as an unsupported accusation, or any project whose Book Bible specifies a
different house register. Don't reach for this just because a chapter feels dry; the standard
checklist earlier in this file usually fixes that.

Use this as the system prompt for a dedicated subagent doing the pass, with the chapter's
audited draft as the input text:

```
You are an expert non-fiction editor specializing in popular science and macro-history. Your
task is to revise draft text into engaging, thought-provoking, accessible narrative
non-fiction, using these techniques:

* Macro-Perspective & Synthesis: Blend disciplines (biology, history, economics, philosophy)
  seamlessly. Frame specific events or narrow topics within the broader context of human
  evolution and large-scale historical shifts.

* Concrete Analogies: Anchor abstract, complex, or institutional concepts using highly
  relatable, everyday examples (e.g., explaining shared societal myths by comparing them to
  corporate structures or legal fictions).

* Provocative Inquiry: Periodically deploy sharp, rhetorical questions that challenge the
  reader's deeply held assumptions about human nature, progress, or societal norms. Never let
  a rhetorical question imply a factual assertion the draft doesn't already support.

* Declarative Clarity: Write in clear, authoritative, direct sentences. Strip robotic
  transitions (e.g., "Furthermore," "In conclusion," "It is important to note").

* Objective, Curious Tone: Maintain a detached, observant narrative voice fascinated by human
  behavior. Avoid moralizing, overly emotional language, or flowery adjectives.

Formatting constraint: severely limit em-dashes. Don't lean on them for pacing, subordinate
clauses, or tangential thoughts; restructure with commas, colons, or separate sentences.

Input text: [the audited chapter draft]

Output only the revised text. No preamble, no explanation of what changed.
```

Two of this prompt's own instructions are already load-bearing rules elsewhere in the pipeline,
worth knowing rather than treating as coincidence: the em-dash restriction lines up with
whatever punctuation rules the project's Book Bible sets under `style_rules.md`, and "strip
robotic transitions" is the same complaint stage 13 already exists to fix (see "Template
section transitions" and "Over-signaled structure" earlier in this file). Running this agent
doesn't exempt the chapter from the rest of this checklist; the two overlap more than they
conflict.

### Adding another register

The pattern above generalizes. To define a new one:

1. **Name it by its techniques**, not by a person ("macro-synthesis nonfiction," not a byline).
2. **List 4-6 concrete craft moves** a reader would actually recognize, the way "Concrete
   Analogies" and "Provocative Inquiry" are concrete above rather than "engaging" or "vivid."
3. **State when it fits and when it doesn't.** Every register is wrong for some chapter; say so
   explicitly rather than leaving it to be discovered mid-pass.
4. **Note any formatting constraints** the register implies, and check them against
   `style_rules.md` for conflicts with the project's house rules.
5. **Write the agent prompt from the craft moves directly**, the way the block above turns each
   bullet into an instruction. Keep the same closing shape: input is the audited draft, output
   is revised text only.

This keeps the mechanism reusable rather than tying it to one voice: the next register a book
needs (scene-first narrative, plain-spoken service nonfiction, whatever a project's Book Bible
calls for) gets added the same way, without redesigning this section.
