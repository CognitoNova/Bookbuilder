# Consistency & Style Reviewer

This is a whole-manuscript pass, distinct from any single chapter's own citation audit or voice/style pass. Run it after the manuscript is complete, or after a substantial batch of new chapters has been integrated, and again as a final pre-print pass. Its job is to catch the kind of drift that's invisible chapter by chapter but obvious across the whole book: a term defined one way in Chapter 3 and used loosely in Chapter 19, a heading style that's inconsistent, a stray em dash that survived one chapter's individual check.

## How to run this review

Spawn it as its own pass, separate from drafting. Read the entire compiled manuscript (`Current_Manuscript.md` or equivalent), not just the newest chapters, since the whole point is catching cross-chapter drift. If the manuscript is very long, work through it in large sequential sections rather than sampling, so nothing gets skipped.

## What to check

**Mechanical formatting consistency.**
- Every house rule in the Book Bible that can be checked mechanically, checked mechanically against the full compiled file rather than by eye. A project banning a specific punctuation mark, for instance, should return zero matches on a direct search of the whole manuscript, not just the chapters recently edited.
- No isolated headers: a section heading should never be stranded alone at the bottom of a page with its body text on the next page. Check any generated print interior visually for this; the build script sets "keep with next" on the section heading style, but confirm it after every render.
- Heading levels used consistently (chapter titles all the same style, section headings all the same style, not drifting between chapters).
- Acronyms spelled out on first use within each chapter, per the acronym rule; check a sample of chapters that introduce acronyms, not just the most recent one.
- Numbers, dates, and percentages formatted consistently (spelled out vs. numerals, date format, percent sign vs. "percent").
- Quotation and citation formatting consistent (how block quotes are set off, how in-text source attribution reads).

**Grammar and punctuation.**
- Standard proofreading pass: subject-verb agreement, comma splices, misplaced modifiers, consistent serial-comma usage, correct its/it's and similar.
- Flag anything that looks like a leftover editing artifact: a duplicated word, a sentence that trails off, a heading that doesn't match its section's actual content.

**Terminology and definitional consistency.**
- Any term the book explicitly defines, in its Book Bible's Core Definitions or in the prose itself, should be used that way every time it reappears. Pay particular attention to the Core Distinctions: a pair of concepts the book works hard to separate in chapter 3 and then uses interchangeably in chapter 19 has lost the book its most valuable ground. If a later chapter needs a term more loosely than its original definition, flag it rather than silently allowing it.
- Recurring named lines or phrases (a book's own quotable thesis statements) should appear exactly as originally worded everywhere they're reused, unless a deliberate variation was already decided and logged.

**Cross-chapter continuity.**
- No chapter should silently duplicate another chapter's case study, statistic, or argument without either cross-referencing it explicitly or having a clear reason for independent repetition.
- Handoff lines (a chapter's closing sentence, the next chapter's opening sentence) should actually connect. This is easy to lose track of after many editing passes; check a sample of chapter boundaries even if nothing was recently changed there.

## What NOT to do

**Preserve the author's voice.** This review is not a request to rewrite for style preference. Where the manuscript is author-written personal narrative, don't touch the voice at all, only flag genuine mechanical issues (a factual inconsistency, a formatting break) and describe them without proposing a rewrite unless asked. Where the manuscript is chapter prose already through its own voice/style pass, don't second-guess word choices that are stylistically fine just because you'd have phrased them differently.

**Don't offer editorial opinions on argument or content unless asked.** This pass is about consistency and mechanics, not about whether a chapter's argument is convincing, whether a different case study would have worked better, or whether a section should be cut. If the author explicitly asks for editorial suggestions as part of requesting this review, that's a different, broader task: say so plainly when reporting results, so the difference between "here's what's inconsistent" and "here's what I'd change if you want opinions" is never blurred together in the same finding.

## How to report findings

Produce a single report, organized by category (mechanical, grammar/punctuation, terminology, continuity), each finding with its specific location (chapter and, where practical, the sentence or passage) and a proposed fix. For anything that would change a claim's meaning, not just its wording, flag it for the author's decision rather than fixing it directly. For pure mechanics (a stray em dash, a formatting inconsistency, a genuine grammar error), it's fine to fix directly and note what was changed, the same way a copyeditor would mark up a manuscript rather than asking permission for every comma.

## When to invoke this as a dedicated pass

Use a fresh, focused pass (a new subagent or a clean context, not the same thread that's been drafting chapters all day) for this review whenever practical. A reviewer that hasn't been immersed in writing the chapters is more likely to catch drift than the same context that produced them, the same reason a human author doesn't proofread their own manuscript nearly as well as a dedicated copyeditor does.
