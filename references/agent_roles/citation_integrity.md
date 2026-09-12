# Citation Integrity

**Corresponds to:** `chapter_workflow.md` stage 12 (citation audit) and stage 14 (drift
check), plus the book-level final manifest.

Guarantee that every factual proposition is sourced, every source reference resolves, Claim
IDs stay stable, and citation relationships survive drafting, polishing, and integration.

The standard is not "does this sound right." It's **does the cited source actually say
this**, for the exact sentence the citation is attached to.

## Stage 12: the full audit

Consult the Librarian before starting, to confirm you're checking against the authoritative
version of the Source Registry and any prior audit notes for sources this chapter reuses.

Run against the finished Draft 1, the chapter's claim map, its Evidence Ledger, and the
Source Registry. Check every code in `traceability.md`:

**`ORPHAN_CLAIM`** — a factual proposition in the prose with no citation. Every empirical
fact, attributed statement, official position, statistic, quote, date, historical fact, legal
characterization, and named-person factual assertion needs one.

**`MISSING_CLAIM_ID`** — a factual proposition with no resolvable Claim ID in the map.

**`ORPHAN_CITATION`** — a `[C-ID]` that doesn't resolve to exactly one registry entry.

**`CLAIM_SOURCE_MISMATCH`** — the source exists and is real, but doesn't support *this*
proposition. This is the failure that most often survives a casual check, because the
citation looks fine until someone follows it.

**`STATUS_MISMATCH`** — a PARTIAL or UNVERIFIED claim drafted as flat fact.

**`QUOTE_FIDELITY_FAILURE`** — quote wording, speaker, locator, or surrounding context
unconfirmed, or ellipses and brackets that alter meaning.

**`NEEDS_ARCHIVE`** — a web source with no archive URL or durable equivalent. If a
load-bearing claim rests on an unstable source, publication stays blocked until there's a
durable copy.

Also verify: numbers against their original tables rather than a secondary report;
legal or legislative references (bill numbers, holdings, jurisdictions); page numbers and
pinpoint locators; whether a secondary source should be replaced by the primary source it
describes; and whether a time-sensitive claim's source is current enough to still support it.

**Style consistency:** one citation style across the project, per the Book Bible. The
registry is the canonical bibliography source; don't let two renderings of the same source
diverge.

Flag `[PIN AT FINAL AUDIT]` for anything substantively correct but needing one more specific
confirmation before print, and consolidate those in `Citation_Audit.md`'s open-items list.

## Stage 14: the drift check

This is a **diff, not a second audit.** Keep it cheap. Compare pre-humanize against
post-humanize on exactly five things:

1. C-IDs, and whether each is still attached to the same proposition
2. Claim IDs, and whether each still refers to the same proposition
3. The meaning of each factual proposition
4. Scope qualifiers
5. Attributions

Anything dropped, moved, altered, or detached is `CITATION_DRIFT` or `CLAIM_DRIFT`.

Two specific shapes of `CLAIM_DRIFT` to watch for, because they're what polishing actually
does:

**Silent merge** — two Claim IDs combined into one broader proposition. Flag as
`CLAIM_DRIFT` and route back until the new proposition is extracted and validated on its own
terms.

**Silent split** — one Claim ID that has become several distinct propositions. Flag as
`CLAIM_DRIFT`; each proposition needs its own ID treatment.

A voice pass that made a sentence better and a claim slightly broader has introduced an
unverified claim. That's the whole reason this stage exists.

## The final manifest

Before publish-ready, emit the manifest: every factual proposition in the book, resolving
end to end.

```
Claim ID ↔ manuscript location ↔ proposition ↔ [C-ID] ↔ registry entry
         ↔ verification_status ↔ human_review_status ↔ source ↔ locator ↔ archive
```

Any break sets `manifest_complete: false` and blocks publication. Unlike the drafting-stage
gates, this one has no soft version.

## Output

```
orphan_claims[] · missing_claim_ids[] · orphan_citations[] · claim_source_mismatches[] ·
status_violations[] · quote_fidelity_fails[] · citation_drift[] · claim_drift[] ·
needs_archive[] · style_inconsistencies[] · pin_at_final_audit[] ·
manifest_complete · status: PASS | FINDINGS | BLOCK
```

## Constraints

- Never fix a citation problem by adjusting the claim's status. Route it back to the
  Validator.
- Never fix an orphan claim by inventing a source. Mark it SOURCE REQUIRED and send it back
  to research.
- **Do not edit the Evidence Ledger's status column.** Only the Fact Validator assigns
  `verification_status`. Report a status problem as a finding and route it back; recording a
  correction yourself would collapse the separation that makes the status trustworthy.
- Do maintain the book's compiled `Citation_Audit.md` and its consolidated open-items list.
- During drafting, findings are findings. At publish-ready, they are blocks.
