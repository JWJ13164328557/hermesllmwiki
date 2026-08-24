---
type: evidence
claim: "Cell-type-specific marker genes are defined for both rice cultivars at single-cell resolution"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Oryza sativa
tissue:
  - root tip
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2020-12-014]]"
supporting_figures:
  - "xr-10-1016-j-molp-2020-12-014#figure-2"
experiments:
  - scRNA-seq
  - differential expression
  - marker gene identification
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Cell-Type-Specific Marker Genes Defined for Rice Cultivars

## Claim

Differential expression analysis of scRNA-seq data from two rice cultivars identified robust cell-type-specific marker gene sets, providing a monocot reference for root cell-type annotation and functional genomics.

## Biological Context

Marker genes are essential for cell-type annotation in scRNA-seq studies. Defining these for rice — a major crop with a root system architecturally distinct from Arabidopsis — enables functional genomics and genetic studies in monocots.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2020-12-014]] | Differential expression (Wilcoxon rank-sum) | Marker genes identified for each cluster; known markers validated (e.g., OsSCR for endodermis, OsSHR for stele) | 27,469 + ~10,000 |

## Evidence Quality

**Tier 3** — Spatial Support (informed by known spatial expression patterns of marker genes from literature)

## Contradictory Evidence

None. Marker gene sets are consistent with known rice root expression patterns and orthology with Arabidopsis.

## Consensus Assessment

**Established** — Marker genes validated against published in situ hybridization data and Arabidopsis orthologs.

## Alternative Models

N/A — Marker gene identification is a standard descriptive output of scRNA-seq.

## Open Questions

- What proportion of rice-specific markers lack Arabidopsis orthologs?
- Are there markers that distinguish the exodermis from the epidermis?
- How many markers overlap between Nipponbare and Azucena cultivars?

## Next Critical Experiment

High-throughput in situ hybridization or spatial transcriptomics to validate the full set of predicted marker genes across all rice root cell types.
