---
type: evidence
claim: "Arabidopsis root cell types exhibit distinct genome-wide chromatin accessibility landscapes"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - epidermis
  - cortex
  - endodermis
  - stele
  - columella
development_stage:
  - seedling
condition:
  - standard
support:
  - "[[xr-10-1016-j-molp-2021-01-001]]"
supporting_figures:
  - "xr-10-1016-j-molp-2021-01-001#figure-1"
  - "xr-10-1016-j-molp-2021-01-001#figure-2"
experiments:
  - scATAC-seq
  - chromatin accessibility
  - differential peak analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Root Cell Types Exhibit Distinct Chromatin Accessibility Landscapes

## Claim

Single-cell ATAC-seq of Arabidopsis roots reveals that each major cell type exhibits a distinct genome-wide chromatin accessibility landscape, with differential accessibility at genes corresponding to cell-type-specific functions and transcription factor binding motifs.

## Methodological Context

Chromatin accessibility (measured by ATAC-seq) reflects the regulatory potential of genomic regions. In multicellular organisms, cell-type-specific gene expression is regulated in part by differential chromatin accessibility at promoters and enhancers. Plant single-cell ATAC-seq extends this paradigm by resolving chromatin landscapes at cell-type resolution in root tissues.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2021-01-001]] | scATAC-seq | Distinct chromatin landscapes for each root cell type; cell-type-specific TF motifs enriched in accessible regions | Multiple root cell types |

## Evidence Quality

**Tier 3** — Observational genomics with motif enrichment validation

## Contradictory Evidence

None. Cell-type-specific chromatin accessibility is a broadly reproduced finding in multicellular organisms.

## Consensus Assessment

**Established** — Cell-type-specific chromatin accessibility is a fundamental feature of root cell identity.

## Alternative Models

Gene regulatory network models (GRNs) that integrate chromatin accessibility with TF expression.

## Open Questions

- How much of the chromatin landscape is determined by lineage vs. position?
- Which chromatin differences are causal for cell identity vs. consequential?

## Next Critical Experiment

CRISPR-based perturbation of cell-type-specific accessible regions to test functional roles in cell-type specification.
