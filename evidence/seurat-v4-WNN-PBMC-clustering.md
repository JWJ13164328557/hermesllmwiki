---
type: evidence
claim: "WNN analysis of 211K CITE-seq PBMCs with 228 antibodies resolves immune cell states superior to transcriptome-only"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Homo sapiens
tissue:
  - peripheral blood
cell_type:
  - PBMCs
development_stage:
  - adult
condition:
  - standard
support:
  - "[[xr-10-1016-j-cell-2021-04-048]]"
supporting_figures:
  - "xr-10-1016-j-cell-2021-04-048#figure-1"
  - "xr-10-1016-j-cell-2021-04-048#figure-2"
  - "xr-10-1016-j-cell-2021-04-048#figure-3"
experiments:
  - CITE-seq
  - WNN analysis
  - multimodal clustering
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# WNN Analysis of 211K CITE-seq PBMCs Resolves Immune Cell States

## Claim

Seurat v4's weighted nearest neighbor (WNN) analysis of 211,000 CITE-seq PBMCs profiled with 228 antibodies defines a joint multimodal neighborhood graph that resolves immune cell states with greater granularity and biological interpretability than transcriptome-only clustering.

## Methodological Context

CITE-seq simultaneously measures transcriptomes and surface protein expression in single cells. WNN constructs a single neighborhood graph by learning cell-specific modality weights from the agreement between RNA-based and protein-based distance metrics, enabling clustering that respects both modalities rather than defaulting to one.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-cell-2021-04-048]] | WNN on CITE-seq | 31 immune subsets identified; protein data separated CD4+ T cell memory/naive subsets; WNN outperformed RNA-only in cluster stability | 211K cells, 228 antibodies |

## Evidence Quality

**Tier 1** — Computational framework with biological validation (known surface markers confirm cluster identity)

## Contradictory Evidence

None. WNN consistently outperformed single-modality clustering in this dataset.

## Consensus Assessment

**Established** — WNN is the recommended Seurat framework for CITE-seq and multi-modal single-cell data.

## Alternative Models

TotalVI, MOFA+, and multi-omics factor analysis offer alternative multi-modal integration approaches.

## Open Questions

- What is the optimal weighting strategy when modalities have vastly different feature counts?
- Can WNN be extended to three or more modalities?

## Next Critical Experiment

Benchmark WNN against alternative multi-modal integration methods using multiome (RNA+ATAC+protein) datasets with known ground truth.
