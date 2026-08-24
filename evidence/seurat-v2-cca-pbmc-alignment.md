---
type: evidence
claim: "CCA-based integration aligns PBMC scRNA-seq datasets across resting and stimulated conditions"
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
  - resting
  - IFN-β stimulated
support:
  - "[[xr-10-1038-nbt-4096]]"
supporting_figures:
  - "xr-10-1038-nbt-4096#figure-1"
  - "xr-10-1038-nbt-4096#figure-2"
experiments:
  - CCA integration
  - scRNA-seq
  - alignment benchmarking
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# CCA-Based Integration Aligns PBMC Datasets Across Conditions

## Claim

Canonical Correlation Analysis (CCA)-based data integration, introduced in Seurat v2, successfully aligns PBMC scRNA-seq datasets from resting and IFN-β-stimulated conditions into a shared embedding, preserving cell-type distinctions while removing condition-specific variation.

## Methodological Context

Cross-condition scRNA-seq comparisons require distinguishing biological cell types from condition-induced transcriptional shifts. Seurat v2 uses CCA to identify shared correlation structures across datasets and applies dynamic time warping to align canonical correlation vectors, followed by mutual nearest neighbor (MNN) pairing for robust integration.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-nbt-4096]] | CCA integration | Resting and stimulated PBMC datasets aligned; stimulation-specific expression changes preserved | 2 datasets, multiple cell types |

## Evidence Quality

**Tier 1** — Computational method with biological ground truth (expected cell-type groupings)

## Contradictory Evidence

None. CCA integration outperformed MNN-based methods in preserving cell-type separation.

## Consensus Assessment

**Established** — CCA became the standard framework for scRNA-seq data integration, extended in Seurat v3 and v4.

## Alternative Models

MNN (Haghverdi et al.), Harmony, and LIGER offer alternative integration strategies.

## Open Questions

- At what level of biological divergence does CCA integration fail?
- What is the optimal number of canonical correlation vectors to retain?

## Next Critical Experiment

Systematic benchmark of CCA vs. anchor-based vs. Harmony integration across datasets with varying biological and technical divergence.
