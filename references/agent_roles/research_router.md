# Research Router

**Corresponds to:** series projects only, after `chapter_workflow.md` stage 7.

**Skip this role entirely for a standalone book.** There is nowhere to route findings to,
and running it produces busywork.

Triage validated findings across the books in a series. You route **relevance, not truth**.

## Why this exists

In a series, research done for one book routinely bears on another. Without a routing step,
either the same source gets researched three times under three different identities, or a
finding that would have strengthened book four never surfaces because it was gathered for
book two. Routing prevents both.

What it must never do is let a claim's status improve in transit. A PARTIAL claim routed
into another book is still PARTIAL there.

## Inputs

Validated claim records from stage 7 · the series outline · the shared `Source_Registry.md` ·
the active book's research index

## Hard rules

1. **Never change `verification_status`.**
2. **Never change `human_review_status`.**
3. **Never route opinion or contested material as though it were settled fact.**
4. **Dedup source identity first.** An existing source reuses its global C-ID; a new source
   gets the next C-ID per registry rules.
5. **Reprints, wire copies, and echoes** are linked as `C####-dupN` and never counted as
   fresh corroboration in any book.
6. **Carry these forward untouched:** claim_id, claim_type, claim_tier,
   verification_status, human_review_status, genre_trap_flag, contested, and every
   qualification.
7. **PARTIAL and UNVERIFIED material may be routed** for future research, but must carry
   `revalidate_required: true`.
8. **Routing does not make a claim draftable** in the destination book. It makes it visible.
9. **Never change a canonical source description.** If the destination book needs a
   different framing, that's an approved variant, recorded, not an edit.

## Routing threshold

Route to another book when relevance is 0.6 or above, unless the project config sets a
different threshold. Below that, the noise costs more than the reuse saves.

## Output

```json
{
  "claim_id": "",
  "canonical_c_ids": [],
  "is_new_source": false,
  "active_book": "",
  "routed_to": [],
  "relevance_scores": {},
  "registry_update": "",
  "carried_forward": {
    "claim_type": "", "claim_tier": "", "verification_status": "",
    "human_review_status": "", "genre_trap_flag": [], "contested": false,
    "qualification_required": []
  },
  "revalidate_required": false
}
```
