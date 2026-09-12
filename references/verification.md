# Verification: The Decision Table

This is the working reference for assigning `verification_status`. It covers the great
majority of calls. When a call is genuinely hard, or a claim type needs its full
evidentiary standard spelled out, escalate to `verification_matrix.md`.

**The question is never "how many sources do we have."** It's "what kind of claim is this,
what evidence would actually prove it, and does what we have meet that standard?"
Verification is a judgment about evidentiary fit, not source accumulation.

## Step 1: classify the claim

Mis-typing a contested interpretation as an empirical fact is the most consequential error
available at this stage. Take the classification seriously.

| Type | It looks like | Verified requires |
|---|---|---|
| `PRIMARY_TEXT_FACT` | What a statute, opinion, treaty, or archival document literally says | One authoritative primary source, exact locator. More if authenticity or version is disputed. |
| `EMPIRICAL_FACT` | Rates, counts, measured outcomes, documented events and actions | Authoritative original source; proposition matches what was actually measured; population and period correct; caveats preserved |
| `ATTRIBUTED_STATEMENT` | "X said..." / "The organization stated..." | Speaker correct, wording faithful, date and venue right where material, context doesn't reverse the meaning |
| `DOCTRINE_OR_POSITION` | The stated position of any organization, tradition, party, or movement | The group's own authoritative source; scope specified; no silent universalizing |
| `INTERPRETATION_OR_OPINION` | Evaluative or normative judgments | Not verifiable as such. Status is `OPINION_NOT_VERIFIABLE`; premises verified separately |
| `CONTESTED_HISTORY` | Disputed motives, origins, or significance | Default `PARTIAL`. Narrow underlying facts can be VERIFIED; disputed meaning stays a range |
| `CURRENT_LAW` | What the law currently is or requires | Court and jurisdiction right, holding distinguished from dicta, subsequent treatment checked, `current_status_date` recorded |
| `CAUSAL_CLAIM` | "X caused Y" | Evidence that actually supports causation, not sequence or correlation |
| `MOTIVE_STATE_OF_MIND` | "Knowingly," "intentionally," "lied," "corruptly" | Evidence specifically supporting the mental state. Conduct alone never suffices |
| `INSTITUTIONAL_ACTION` | An organization funded, adopted, filed, or lobbied | Correct entity (not a parent, affiliate, PAC, or chapter conflated), correct period, action accurately characterized |
| `PERSON_BIOGRAPHICAL` | Office held, vote cast, affiliation | Identity resolved, period correct, current vs historical distinguished. Higher bar if reputation-affecting |

## Step 2: assign status

**`VERIFIED`** — all of:
- evidence is appropriate to the claim type
- the source authority is sufficient for what's being asserted
- the proposition matches what the evidence actually says
- material qualifiers are preserved
- required current-status checks are done
- no unresolved contradiction that would change the claim's truth

**`PARTIAL`** — any of:
- support exists but is incomplete, indirect, disputed, or stale
- the claim is inadequately scoped relative to its evidence
- contested history where the interpretation is genuinely open
- current legal status not fully checked
- a material qualification is unresolved

**`UNVERIFIED`** — any of:
- evidence is missing
- the cited source doesn't support the proposition
- a number has no identified source
- a quotation can't be confirmed
- the claim rests on an inference the evidence doesn't establish

**`OPINION_NOT_VERIFIABLE`** — the proposition is genuinely evaluative. Its factual premises
are extracted and verified separately.

## Step 3: apply the standing rules

**Source independence.** Two sources are independent only if they don't derive the
proposition from the same underlying reporting, wire copy, press release, or dataset
interpretation. An AP story plus a paper reprinting it is one source. Three sites copying
the same statistic without original methodology is one source. Record duplicates as
`C####-dupN` and don't count them as corroboration.

**Lean is metadata, not a truth score.** Record a source's perspective where relevant.
Don't treat "one from each side" as a mechanical resolution of a factual dispute, and don't
downgrade primary evidence because of who published it.

**Materiality scales rigor.** Increase scrutiny when a claim is central to the thesis,
surprising, reputation-affecting, legally consequential, statistically precise, politically
contested, historically disputed, or likely to be the first thing a critic quotes. A
peripheral date needs less corroboration than a central causal accusation. This is what the
claim tiers in `traceability.md` operationalize.

**Preserve scope.** "Some [subgroup] leaders..." must never become "[Whole group]...". This
is the single most common way an otherwise accurate chapter becomes indefensible.

**Don't upgrade association to causation** rhetorically. If only association is supported,
write "was associated with," "coincided with," "followed," or "was cited by."

**Conduct is not motive.** Instead of "X knowingly lied," write what's actually supported:
"X's statement conflicts with the study's published findings. [C-ID]" That preserves the
criticism without inventing a mental state, and it's the version that survives review.

## Step 4: flag for human review

Set `human_review_status: PENDING` and record the reason when a claim:
- touches a High-Risk Topic from the Book Bible
- involves a reputation-affecting assertion about an identifiable person
- rests on contested expert interpretation the project's reviewers should weigh in on
- makes a legal characterization the project's legal reviewer should confirm

Verification and human review are independent. Assign both; don't let either substitute for
the other.

## Statistics: the required capture

Any claim carrying a number records all of these, with missing fields left explicitly
missing rather than inferred:

publisher or pollster · year or field dates · population · sample size (n) ·
margin of error where applicable · exact question wording where material ·
comparison baseline where material

Auto-downgrade to `PARTIAL` if the figure is approximately remembered without an identified
source, the denominator is unclear, methodology materially limits the claimed conclusion, or
only a secondary report exists where the original should reasonably be findable.

No specific figure on file means `UNVERIFIED`, and the number does not go in the prose.

## Quotes: the required capture

exact quoted text · speaker or author · original source · pinpoint locator ·
surrounding context · whether ellipses or brackets are present

Ellipses and brackets must not alter meaning. A paraphrase is labeled as a paraphrase and
never sits inside quotation marks. If the surrounding context materially qualifies or
reverses what the quote appears to say, the quote is not usable as-is.
