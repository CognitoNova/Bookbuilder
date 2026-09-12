# Traceability: Claims, Sources, and the Manifest

The promise this system makes is that at the end of the book, every factual proposition in
it can be traced back to a source you can actually check. That promise is only worth
something if the links survive drafting, editing, and polishing. This file defines the
identifiers that make that possible and the audit codes that catch it when they break.

## The chain

Every factual proposition must resolve end to end:

```
Claim ID → [C-ID] → Source Registry entry → source → pinpoint locator → archive/durable copy
```

Any break in that chain is a defect with a name (see Blocking codes below).

## Claim IDs

A **Claim ID** identifies one atomic factual proposition. Format:

```
CL-<BOOKCODE>-<CHAPTER>-<NUMBER>
```

`BOOKCODE` is 2 to 4 characters, chosen at project setup and recorded in the Book Bible.
Use something mnemonic for a standalone book (`HP`, `CMC`) or sequential for a series
(`B1`, `B2`). Example: `CL-B3-06-021`, `CL-HP-12-004`.

Rules:

- **Claim IDs identify propositions, not sentences.** If the prose moves, the ID follows
  the proposition.
- **One proposition, one ID.** A sentence containing three factual propositions produces
  three Claim IDs.
- **Materially changed propositions get a new ID**, with the superseded relationship
  recorded. Don't quietly reuse an ID for something that now says something different.
- **Relationships get recorded** where claims relate: SUPPORTS, NARROWS, BROADENS,
  SUPERSEDES, DUPLICATES.

Claims live in `00_Book_Control/Claim_Ledger.md` at book level, and appear per chapter in
that chapter's `Evidence_Ledger.md`.

## Claim tiers

Not every claim deserves identical scrutiny, and pretending otherwise wastes effort that
should go to the claims that carry the argument. Assign a tier at extraction:

| Tier | What it means | Required treatment |
|---|---|---|
| `LOAD_BEARING` | The argument fails if this is wrong. Central causal claims, the statistics the thesis rests on, reputation-affecting claims about named people, anything a hostile reviewer would target first. | Full metadata. Independent corroboration where practical. Full verification matrix treatment. Never drafted below VERIFIED. |
| `SUPPORTING` | Real evidentiary work, but the chapter survives if it's cut. Context, secondary examples, corroborating figures. | Full metadata. Standard verification. |
| `INCIDENTAL` | Background detail a reader would never dispute. Uncontroversial dates, well-known titles, common-knowledge context. | Short record: claim, source C-ID, locator, status. Skip the statistic/quote metadata blocks unless the claim is actually a statistic or quote. |

Two rules keep this from becoming a loophole:

1. **Tier is about consequence, not confidence.** "I'm sure about this" is not a reason to
   call something incidental. "Nothing breaks if it's wrong" is.
2. **A claim about an identifiable person is never INCIDENTAL**, regardless of how minor it
   seems. Neither is any statistic, any direct quotation, or any claim carrying a
   genre-trap flag.

When in doubt, tier up. The cost of over-documenting one date is trivial; the cost of
under-documenting one load-bearing claim is the book's credibility.

## C-IDs and the Source Registry

A **C-ID** is a permanent global identifier for one source: `C0042`. It is assigned once
and never renumbered, and it stays stable across every book in a project or series.

Registry rules:

- **One source, one C-ID, one canonical description.** The same court opinion described two
  different ways in two chapters is a continuity defect.
- **Reprints, wire copies, syndicated versions, and press-release echoes** are linked as
  `C####-dupN`. They are *not* independent corroboration. Two outlets running the same wire
  story is one source, not two.
- **Book relevance is appended** to an existing entry rather than creating a second ID for
  the same source.
- **Web sources record an archive URL and access date.** A source that can vanish is a
  citation that can rot.
- **Citation renderings are stored on the entry** in the project's chosen style, so the
  endnote list and bibliography can be generated rather than retyped.

The registry lives in `00_Book_Control/Source_Registry.md`. Its entry schema is in
`assets/templates/book_control_templates.md`.

### Joining an existing project

If a book is joining a series that already has a registry, **reuse it**. Do not create a
new one, do not renumber, and do not reconstruct prior entries from memory. Import the
existing file and add to it. Inventing a registry entry for a source you haven't seen is
the single worst thing this system can do, because it produces a citation that looks
verified and isn't.

## The two status axes

Claims carry two independent status fields. Conflating them is a category error that lets
"someone approved it" masquerade as "the evidence supports it."

**`verification_status`** answers: does the evidence support this proposition?

- `VERIFIED` — evidence appropriate to the claim type supports it; qualifiers preserved.
- `PARTIAL` — some support, but incomplete, disputed, indirect, stale, or inadequately scoped.
- `UNVERIFIED` — evidence missing, or the cited source doesn't actually support the claim.
- `OPINION_NOT_VERIFIABLE` — genuinely evaluative; its factual premises still get verified separately.

**`human_review_status`** answers: has a required human cleared this for publication?

- `NOT_REQUIRED` · `PENDING` · `APPROVED` · `HOLD` · `REVISE`

A claim can be `VERIFIED` + `PENDING`: the evidence is good, but the manuscript stays
blocked until the required reviewer signs off. A claim can be `PARTIAL` + `APPROVED`: a
human is fine with how it's handled, and it still may not be drafted as flat fact.

**Human approval never upgrades evidence.** Legal sign-off doesn't either.

### Reading an older ledger

If a project has ledgers written on a single five-level scale, map them like this rather
than rewriting the old files:

| Older scale | verification_status | Notes |
|---|---|---|
| Verified | `VERIFIED` | |
| Supported with qualification | `PARTIAL` | Populate `qualification_required` with the specific qualification |
| Disputed | `PARTIAL` | Set `contested: true`; present the range |
| Inference | `UNVERIFIED` if a factual inference; `OPINION_NOT_VERIFIABLE` if evaluative | Decide which by asking whether evidence could settle it |
| Unverified: do not publish | `UNVERIFIED` | |

New work uses the two-axis model. Old ledgers can be read through this table without being
migrated.

## Draftability

A factual proposition may be **drafted as fact** only when `verification_status = VERIFIED`.

- `PARTIAL` may be drafted only with its qualification stated in the prose.
- `UNVERIFIED` may not be drafted as fact at all. Not hedged, not softened. Either find the
  source or cut the claim.
- `OPINION_NOT_VERIFIABLE` may be drafted as opinion when its factual premises are
  disclosed and cited.

If no specific figure is on file, the number is UNVERIFIED and does not go in the prose.
A remembered statistic is not a statistic.

## Blocking codes

The citation audit (stage 12) and drift check (stage 14) emit these. Each names a specific
break in the chain.

| Code | Meaning |
|---|---|
| `ORPHAN_CLAIM` | A factual proposition in the prose with no citation |
| `MISSING_CLAIM_ID` | A factual proposition with no resolvable Claim ID |
| `ORPHAN_CITATION` | A `[C-ID]` that doesn't resolve to exactly one registry entry |
| `CLAIM_SOURCE_MISMATCH` | The cited source is real but doesn't support *this* proposition |
| `STATUS_MISMATCH` | A PARTIAL or UNVERIFIED claim drafted as fact |
| `QUOTE_FIDELITY_FAILURE` | Quote wording, speaker, locator, or context unconfirmed |
| `CITATION_DRIFT` | A C-ID dropped, moved, or detached from its proposition during editing |
| `CLAIM_DRIFT` | A proposition broadened, narrowed, merged, or split during editing |
| `NEEDS_ARCHIVE` | A web source with no durable copy |
| `MANIFEST_INCOMPLETE` | The final manifest has an unresolved row |

During drafting these are findings to fix. At publish-ready they are absolute blocks.

## Genre-trap flags

Claims touching these categories get extra scrutiny at validation regardless of tier. The
generic set:

`disputed_quote` · `current_law_holding` · `contested_history` ·
`position_overgeneralization` · `statistic` · `causal_claim` · `motive_state_of_mind`

Each project adds its own specifics at setup (named cases, statutes, disputed events,
organizations whose positions are easy to overstate). Those live in the Book Bible's
High-Risk Topics section.

## The final manifest

Before publish-ready, emit the citation manifest. Every factual proposition in the book gets
a row resolving the full chain:

```
Claim ID ↔ manuscript location ↔ proposition ↔ [C-ID] ↔ registry entry
         ↔ verification status ↔ human review status ↔ source ↔ locator ↔ archive
```

Any break sets `manifest_complete: false` and blocks publication. This is the one gate with
no soft version: the manifest is the artifact that backs the book's central promise, and a
manifest with holes in it is worse than no manifest, because it claims a rigor the book
doesn't have.
