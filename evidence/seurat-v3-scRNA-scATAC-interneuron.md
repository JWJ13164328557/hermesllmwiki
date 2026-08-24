---
type: evidence
claim: "Anchor-based integration links scRNA-seq and scATAC-seq revealing interneuron chromatin differences"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Mus musculus
tissue:
  - brain (prefrontal cortex)
cell_type:
  - interneurons
development_stage:
  - adult
condition:
  - standard
support:
  - "[[xr-10-1016-j-cell-2019-05-031]]"
supporting_figures:
  - "xr-10-1016-j-cell-2019-05-031#figure-2"
  - "xr-10-1016-j-cell-2019-05-031#figure-4"
experiments:
  - scRNA-seq
  - scATAC-seq
  - anchor-based integration
  - motif enrichment analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Anchor-Based Integration Links scRNA-seq and scATAC-seq for Interneurons

## Claim

Seurat v3's anchor-based integration framework links scRNA-seq and scATAC-seq profiles from mouse prefrontal cortex, revealing that interneuron subtypes have distinct chromatin accessibility landscapes that drive cell-type-specific gene regulatory programs.

## Methodological Context

Integrating scRNA-seq and scATAC-seq is challenging because they measure fundamentally different molecular modalities (transcriptome vs. chromatin accessibility) from separate cells. Seurat v3 identifies cross-modality anchors by correlating gene expression with gene activity scores (derived from ATAC peaks near genes), then transfers labels and imputes across modalities.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-cell-2019-05-031]] | Anchor-based scRNA–scATAC integration | Pvalb, Sst, and Vip interneurons identified with distinct chromatin landscapes; cell-type-specific TF motifs enriched | Multiple interneuron subtypes, ~10K cells total |

## Evidence Quality

**Tier 1** — Computational framework with biological validation (motif enrichment matches known TF regulators)

## Contradictory Evidence

None. Chromatin accessibility differences between interneuron subtypes have been confirmed by independent studies.

## Consensus Assessment

**Established** — Anchor-based integration is the standard Seurat framework for cross-modality analysis.

## Alternative Models

MOFA+, LIGER (online iNMF), and TotalVI offer alternative multi-modal integration frameworks.

## Open Questions

- What is the optimal gene activity scoring method for bridging ATAC to RNA?
- Can anchor-based integration handle more than two modalities simultaneously?

## Next Critical Experiment

Compare anchor-based scRNA–scATAC integration with multiome (simultaneous RNA+ATAC from the same cell) data as ground truth.
