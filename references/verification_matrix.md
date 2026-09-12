# Verification Matrix: Full Claim-Type Standards

Escalation reference for `verification.md`. Read the section for the claim type in front of
you when the call is genuinely hard: the evidence is mixed, the claim is load-bearing, or a
reviewer is going to push back.

The status definitions and standing rules (source independence, materiality, scope
preservation) are in `verification.md`; the identifier and tier model is in
`traceability.md`. This file is only the per-type evidentiary detail.

---

## 1. Primary-text fact

What an authoritative document literally says.

**Preferred evidence:** authenticated primary text, official government publication,
official court opinion, enrolled statute, original treaty, archival original.

**Verified requires:** one authoritative primary source is ordinarily sufficient for what
the text directly says; exact locator required; authenticity and document version not
materially disputed.

**Additional corroboration required when:** authenticity is disputed, wording differs across
versions, provenance matters, interpretive significance is contested, or current legal
status matters.

**Do not:** require a secondary source to prove unambiguous words that appear in the
authoritative text. And do not treat *interpretation* of the text as identical to the text
itself; those are two claims, and the second is usually `INTERPRETATION_OR_OPINION` or
`CONTESTED_HISTORY`.

---

## 2. Empirical fact

**Preferred evidence:** original dataset, official report, peer-reviewed study, government
statistics, high-quality institutional records.

**Verified requires:** the proposition matches what the source actually measured or
recorded; population and time period correct; no material denominator or base-rate
distortion; methodology adequate for the proposition being asserted; important caveats
preserved.

**Auto-downgrade to PARTIAL when:** the number is approximately remembered but the source
isn't identified; the denominator is unclear; methodology materially limits the claimed
conclusion; or only a secondary report of the figure exists where the original should
reasonably be findable.

**No specific figure on file:** `UNVERIFIED`. Don't draft the number.

---

## 3. Attributed statement

**Preferred evidence, in order:** original recording, transcript, filing, letter, speech,
post, or official statement; then a reliable contemporaneous reproduction where the original
is unavailable; then reputable journalism quoting it, with caution.

**Verified requires:** speaker or author correctly identified; wording faithful; date and
venue correct where material; surrounding context does not materially reverse or qualify the
meaning.

**Direct quotes:** exact wording, locator, `context_intact: true`. Ellipses and brackets must
not alter meaning.

**Paraphrase:** labeled and written as paraphrase; never inside quotation marks.

**Controversial or damaging attribution:** prefer the original source plus independent
corroboration or a contextual source, and route the named-person concern to legal review.

---

## 4. Doctrine or official position

Covers the stated position of any organization, tradition, party, movement, profession, or
institution: religious doctrine, corporate policy, party platform, professional code, an
advocacy group's platform.

**Preferred evidence:** the group's own authoritative source, whatever form that takes in the
domain. A party platform, a board or conference resolution, bylaws, a professional body's
code of ethics, a published corporate policy, an official teaching document, a confession or
catechism, or any comparable recognized institutional statement. Where the meaning is
contested, add reputable scholarly or expert analysis.

**Verified requires:** the specific faction, chapter, branch, administration, local, or
sub-group is scoped; the source's authority *within the group* is understood (a regional
chapter's resolution is not the national body's position, and a prominent member's op-ed is
neither); the claim does not silently universalize one part to the whole; historical
positions are not presented as current without current-status support.

**For internal diversity, use formulations like:**
- "[Organization]'s official statement says..."
- "[Body]'s adopted position holds..."
- "Some [identifiable subgroup] leaders..."
- "Within [movement], a prominent strand argues..."

**Never:** an unscoped "[Group] believes / wants / does..." unless the proposition genuinely
applies across the whole named group and the evidence supports that scope.

**Auto-flag:** `position_overgeneralization`.

---

## 5. Interpretation or opinion

**Status:** `OPINION_NOT_VERIFIABLE` when the proposition is genuinely evaluative. The
underlying factual premises must still be extracted and verified separately.

**Disclosed-basis rule:** opinion should rest on facts disclosed or cited nearby when the
inference is material. This is both an honesty standard and the thing that keeps sharp
criticism defensible.

**Attribution:** if the interpretation belongs to a scholar, court, critic, or institution,
the *existence* of that interpretation is an `ATTRIBUTED_STATEMENT` and is verifiable as such.

**Do not:** disguise evaluative judgment as empirical fact, or assign VERIFIED merely
because a source shares the author's interpretation.

---

## 6. Contested history

**Default:** `PARTIAL`, unless the narrow factual proposition can be verified independently
of the contested interpretation.

**Require:** serious scholarship representing the real interpretive range; the schools of
interpretation recorded; primary evidence where available; clear separation of undisputed
facts from disputed interpretation.

**VERIFIED may apply to:** narrow underlying facts, authentic text, dates, documented acts.

**VERIFIED must not be used to erase:** legitimate scholarly disagreement over meaning,
motive, causation, or significance.

**Publishing standard:** present the range where the dispute is genuine. A book that
flattens a real historical dispute into certainty has handed its critics the easiest
possible attack.

---

## 7. Current law and doctrine

**Preferred evidence, in order:** controlling primary authority; subsequent controlling
cases; current official statutory or regulatory text; an authoritative citator or current
legal research service; high-quality legal scholarship for interpretation.

**Verified requires:** court and jurisdiction correct; holding distinguished from dicta;
procedural posture correct; constitutional claim distinguished from statutory claim;
subsequent treatment checked; `current_status_date` recorded.

**Watch especially for:** cases whose holding is easy to misstate; cases whose basis
(constitutional vs statutory) is easy to conflate; decisions whose court level is easy to
overstate, such as a trial-court ruling described as though it were appellate or
apex-court precedent; and precedent that has been limited, distinguished, or overruled since
the source describing it was written.

The project's own list of controlling authorities goes in the Book Bible's High-Risk Topics.

**If current status is unchecked:** `PARTIAL` or `UNVERIFIED` depending on materiality. Do
not draft as current law.

---

## 8. Causal claim

**Causation requires more than:** sequence, correlation, co-occurrence, plausible motive, or
advocacy preceding enactment.

**Preferred evidence:** a causal research design; a strong documentary chain;
contemporaneous records showing the decision pathway; multiple independent sources where
appropriate.

**Verified requires:** the evidence actually supports causal language; alternative
explanations considered where material; the scope of the causal claim matches the strength
of the evidence.

**If only association is supported, rewrite as:** "was associated with," "coincided with,"
"followed," "was cited by," "advocates argued for."

---

## 9. Motive and state of mind

High scrutiny. This is where argumentative nonfiction most often crosses from strong into
indefensible.

**Preferred evidence:** direct admission; authenticated contemporaneous communication; sworn
testimony; documentary evidence strongly establishing state of mind; an adjudicated factual
finding, carefully characterized.

**Verified requires:** evidence specifically supporting the mental-state proposition.
Conduct alone is never automatically proof of motive.

**Named living person:** route to legal review; potentially HIGH risk depending on the harm
category.

**Safe default:** describe the documented conduct and disclose the basis for any opinion.

> Instead of: "X knowingly lied."
> Prefer, if supported: "X's statement conflicts with the study's published findings. [C-ID]"

The second version is both more defensible and, usually, more damning.

---

## 10. Institutional or organizational action

**Preferred evidence:** the organization's own filing or report; campaign finance records;
lobbying disclosures; court dockets; official statements; audited financials.

**Verified requires:** correct organizational entity; correct date or reporting period;
amount or action accurately characterized; parent, affiliate, chapter, foundation, PAC, and
related entities not conflated.

**Important:** do not impute an organization's action or position to every member or
adherent. That's a scope error and usually an unfair one.

---

## 11. Named-person biographical fact

**Preferred evidence:** official biography, public record, primary document, reliable
institutional source.

**Verified requires:** identity resolved (watch for same-name confusion); time period
correct; current versus historical status distinguished.

**Reputation-affecting fact:** higher corroboration standard; route to legal review.

**Private person:** substantially higher caution than a public figure, on every axis.

---

## Human review does not change evidence

Subject-matter review may set `human_review_status` to APPROVED, HOLD, or REVISE. It does not
retroactively make weak evidence VERIFIED. A VERIFIED claim can still be blocked from publication while
`human_review_status` is PENDING, HOLD, or REVISE. Legal sign-off works the same way: it
clears legal risk, not evidentiary weakness.
