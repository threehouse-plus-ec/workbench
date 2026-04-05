# Workbench Blueprint — Breakwater Dossier and Essay Method

**Endorsement Marker:** Local candidate framework — T(h)reehouse +EC stewardship. No external endorsement implied.

**Status:** Active  
**Version:** 0.1.0  
**Classification:** Coastline (method definition)  
**Licence:** CC BY-SA 4.0

---

## 1. Purpose

This document describes the standard method for developing a topic through the Breakwater→Evidence→Essay pipeline. Each topic folder in this repository follows this structure.

---

## 2. Topic folder anatomy

```
topic-name/
├── breakwater/          Claim Analysis Ledger entries
│   ├── CL-YYYY-NNN.md  Individual ledger entry
│   └── ...
├── references/          Source notes, evidence, supporting data
│   ├── ref-001.md       Individual reference note
│   └── ...
└── essay/               Sail drafts, commentary, synthesis
    ├── draft.md         Working draft
    └── ...
```

The three sub-folders represent distinct epistemic layers:

- **Breakwater** — purely descriptive measurement of claims. No routing, ranking, or aggregation. Outputs are classifications: COMPATIBLE, UNDERDETERMINED, or INCONSISTENT.
- **References** — evidence notes, source extracts, data summaries. Raw material that feeds both Breakwater entries and essay drafts.
- **Essay** — interpretive synthesis (Sail). Draws on Breakwater findings and reference material to develop a position or narrative.

---

## 3. Breakwater entry protocol

Each Breakwater entry follows the Claim Analysis Ledger schema (v1.0-rc, core frozen):

1. **Claim** — State the claim under analysis. One claim per entry.
2. **Predictions** — What observable consequences follow if the claim is true?
3. **Constraints** — What external coastlines or established results bound the analysis?
4. **Comparison** — Confront predictions with available evidence.
5. **Classification** — Three-value verdict:
   - **COMPATIBLE** — Evidence consistent with the claim within stated constraints.
   - **UNDERDETERMINED** — Evidence insufficient to decide. Requires a Discriminant Condition (what measurement or evidence would resolve it) plus a feasibility flag.
   - **INCONSISTENT** — Evidence contradicts the claim.
6. **No post-verdict text.** The entry ends at the classification.

Additional metadata per entry:

- **Selection mode:** REQUEST (specific claim submitted for analysis) or SWEEP (systematic scan of a domain).
- **Domain:** The field or topic area.
- **Scope:** Optional narrowing of the analysis boundary.

---

## 4. Reference note protocol

Each reference note captures one source or piece of evidence:

- **Source** — Full citation or URL.
- **Date accessed** — When the source was consulted.
- **Key content** — Summary of relevant findings or data (in the author's own words, not verbatim reproduction).
- **Relevance** — Which Breakwater entry or essay section this supports.
- **Quality note** — Brief assessment of source reliability, methodology, or limitations.

---

## 5. Essay drafting protocol

Essays are Sails — interpretive works that draw on Breakwater findings and reference material. They follow the Harbour epistemology: maps, not territory.

Standard structure:

1. **Endorsement Marker** — Always first. Declares stewardship and scope.
2. **Opening** — Frame the question. State what is at stake.
3. **Breakwater summary** — What the claim analysis found. Reference specific CL entries.
4. **Synthesis** — The interpretive move. Connect findings to broader context.
5. **Open questions** — What remains unresolved. Link to UNDERDETERMINED entries where applicable.
6. **Constraints acknowledged** — What this essay does not attempt to address.

---

## 6. Workflow sequence

The typical development sequence for a topic:

1. **Gather references** — Populate `references/` with source notes.
2. **Run Breakwater** — Write ledger entries in `breakwater/` analysing key claims.
3. **Draft essay** — Synthesise findings in `essay/`, citing Breakwater entries and references.
4. **Iterate** — New evidence may trigger new Breakwater entries, which update the essay.

This is not strictly linear. References may be added at any stage. A Breakwater entry may reveal the need for additional sources. The folder structure keeps each layer visible and independently versioned.

---

## 7. Frontmatter convention

Every `.md` file uses YAML frontmatter for metadata:

```yaml
---
title: "Human-readable title"
date: 2026-04-05
status: draft | active | frozen
type: breakwater | reference | essay
topic: topic-folder-name
---
```

The `status` field controls rendering:

- **draft** — Rendered with a visible "DRAFT" marker on the page.
- **active** — Rendered normally.
- **frozen** — Rendered with a "FROZEN" marker; content is archived and should not be edited.

---

## 8. Naming conventions

- Topic folders: lowercase, hyphens, descriptive (`lunar-exploration`, `clock-unification`).
- Breakwater entries: `CL-YYYY-NNN.md` (e.g. `CL-2026-004.md`).
- Reference notes: `ref-NNN.md` (e.g. `ref-001.md`).
- Essay drafts: descriptive names (`draft.md`, `synthesis.md`, `response-to-X.md`).

---

## 9. Anti-patterns

- **Never aggregate Breakwater verdicts** into a single score or ranking.
- **Never route** — Breakwater measures claims; it does not recommend actions.
- **Never import Breakwater verdicts into essay text as authority** — cite them as evidence, not as conclusions.
- **Self-reference exclusion** — A Breakwater entry cannot analyse claims made by the Breakwater system itself.
- **No post-verdict commentary** in Breakwater entries. The classification is the final word.

---

*T(h)reehouse +EC. The emblem is the seed; the network is its recursive unfolding.*
