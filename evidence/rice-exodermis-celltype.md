---
type: evidence
claim: "Rice root contains exodermis as a monocot-specific cell type with distinct transcriptional program"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Oryza sativa
tissue:
  - root tip
cell_type:
  - exodermis
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2020-12-014]]"
supporting_figures:
  - "xr-10-1016-j-molp-2020-12-014#figure-1"
  - "xr-10-1016-j-molp-2020-12-014#figure-2"
experiments:
  - scRNA-seq
  - clustering
  - differential expression
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Rice Root Exodermis Has a Distinct Transcriptional Program

## Claim

scRNA-seq identifies the exodermis as a transcriptionally distinct cell type in rice roots, characterized by suberin biosynthesis and Casparian strip-associated gene expression that distinguishes it from the epidermis and outer cortex.

## Biological Context

Monocot roots possess an exodermis — a sub-epidermal layer with Casparian strips that functions as an apoplastic barrier. This cell type is absent in Arabidopsis and represents a monocot-specific innovation for regulating water and solute uptake.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2020-12-014]] | 10x scRNA-seq + clustering | Exodermis forms a distinct cluster with suberin biosynthesis gene expression (CYP86A, GPAT5 orthologs) | 27,469 (Nipponbare) |

## Evidence Quality

**Tier 3** — Spatial Support (cluster identity inferred from known exodermis markers; spatial location of exodermis is well-established anatomically)

## Contradictory Evidence

None. The exodermis is a well-characterized anatomical structure in rice and other monocot roots.

## Consensus Assessment

**Established** — Known anatomical cell type confirmed at transcriptomic level.

## Alternative Models

N/A — This is a descriptive observation confirming a known anatomical cell type.

## Open Questions

- Is exodermis identity specified by the same SHR-SCR pathway that patterns the endodermis?
- Does the exodermis have functionally distinct subpopulations (e.g., short vs long cells)?
- What transcription factors drive exodermis-specific gene expression?

## Next Critical Experiment

CRISPR knockout of candidate exodermis-specific transcription factors to test their role in exodermis differentiation and barrier function.
