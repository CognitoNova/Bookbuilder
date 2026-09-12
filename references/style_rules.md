# Style Rules

Two kinds of rule live here. The **universal rules** apply to any argumentative nonfiction
book and are always in force. The **house rules** are project-specific and get recorded in
each book's Book Bible at setup.

If a project needs an exception to a universal rule, log it explicitly in that book's Book
Bible rather than quietly drifting from the standard.

---

# Universal rules

## Causation and motive

Don't make claims about any named individual's, official's, or institution's private motive
or state of mind. Report documented actions and their own public statements.

If two explanations for someone's behaviour exist and neither is provable, present both
without picking a winner. "The transactional explanation... the strategic explanation... this
book holds both without ranking them" is the right shape. "He really did it because..." is
not.

This isn't only an accuracy safeguard. It's what keeps a book out of libel territory: a
documented action is defensible, a claimed motive usually isn't. It's also, in practice, more
persuasive. Showing what someone did and letting the reader draw the inference lands harder
than asserting what they were thinking.

## Fairness and evenhandedness

When the argument could read as one-sided, actively look for a comparable case on the other
side rather than letting the omission stand. Patterns that work:

- Pair opposing figures' documented behaviour on the same kind of claim, held to an
  identical test.
- Give a skeptic and an advocate on a contested empirical question comparable space and the
  same standard of evidence, rather than more space to whichever side the book favours.
- Where a case study leans heavily toward criticizing one side, look for a mirror-image case
  on the other, even a smaller or less dramatic one, so the underlying claim about the
  mechanism stays honest.
- If a genuinely comparable pairing doesn't exist and the only available comparison is
  weaker or more contested, **say so and use a different pairing** rather than forcing a
  false balance. Log the rejected option and why, so the decision is visible.

Fairness here means equal standards of evidence, not equal time. The book is allowed its
conclusion.

## Scope discipline

Never attribute a position to an entire group, tradition, party, profession, or movement
unless the evidence genuinely supports that scope. Specify the faction, chapter,
administration, local, denomination, or identifiable sub-group actually responsible.

"Some [subgroup] leaders argued..." is a defensible sentence. "[Whole group] believes..." is
usually neither accurate nor necessary, and it hands a critic the easiest possible rebuttal.

## Acronyms

The first time an acronym or initialism appears **in a chapter**, spell it out with the
acronym in parentheses: "the Centers for Disease Control and Prevention (CDC)." After that,
the acronym alone is fine for the rest of that chapter. This resets per chapter; don't
assume a reader remembers something spelled out three chapters ago.

## Treatment of the book's own core commitment

Every argumentative book argues for something. Don't let that commitment slide into an
implication that holding it makes someone a better person.

State plainly, at least once, that the book's position doesn't by itself guarantee good
character, good judgment, or good governance, and that people who share its starting premise
can still be wrong, corrupt, or cruel. The safeguards a book like this should point to are
structural: transparent institutions, accountability, evidence, and limits on power, not the
correctness of any one worldview.

Where this appears is decided at setup and recorded in the Book Bible.

## Personal narrative boundaries

A chapter that is explicitly the author's own story, usually an Introduction or Conclusion,
is governed by different rules. The author's prose is not rewritten unprompted. Fact-check
any factual claims it makes (statistics, dates, quotes), but leave voice and structure alone
unless the author asks. When they do ask, propose exact replacement text with enough
surrounding original quoted that placement is unambiguous, and wait for explicit sign-off.

## Legal and factual caution

Treat all of these as requiring a full legal-risk review rather than a light one: named
living controversial figures, active or recent litigation, discrimination-adjacent subject
matter, current-events material naming specific officials or institutions, allegations of
illegality, and medical-harm claims.

**Never name or identify a minor**, even indirectly, regardless of how the source material
names them. No exceptions.

When in doubt about whether something is high-risk, treat it as high-risk. An unnecessary
review costs little; a skipped one can cost the book.

## Confidence matches evidence

The prose must never imply more confidence than the claim's `verification_status` supports.
A PARTIAL claim written as flat fact is a defect even when the claim happens to be true,
because the book has then made an assertion it can't back.

---

# House rules

These are project-specific. Record the project's choices in its Book Bible at setup, and
apply them during drafting rather than as a cleanup pass afterward.

Common house rules worth deciding explicitly:

- **Punctuation prohibitions.** Many projects ban a specific mark outright, most often the
  em dash. If yours does, it's a hard rule, not a preference to weigh against others.
- **Numbers and dates.** Spelled out versus numerals, date format, "percent" versus the
  symbol.
- **Serial comma.** Pick one and hold it.
- **Quotation and attribution format.** How block quotes are set off, how in-text
  attribution reads.
- **Citation style.** Chicago, Bluebook, or house. Affects the registry's stored renderings.
- **Terms of art.** Preferred and banned framings, recorded in the Book Bible's Core
  Definitions.

## Enforcing a character-level house rule

Any rule about a specific character can and should be checked mechanically after every write,
not by eye at the end of a chapter. For example, a project banning the em dash:

```bash
grep -c "—" "path/to/file.md"
```

Anything other than `0` or no-match means the file still contains one. Fix it immediately.
Catching one is a five-second fix; catching forty at the end of a book is an editing project.

Run the check on every new file and every edit, including control files and outlines, not
just chapter prose.

If a chapter quotes a source that itself contains the banned character, either choose a
different real quotation or, where exact wording must be preserved for accuracy, note it
explicitly as a verbatim-quotation exception rather than silently breaking the rule.
