---
type: evidence
claim: "Arabidopsis root scRNA-seq identifies 24 putative cell clusters with distinct transcriptional signatures"
claim_type: observation
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2019-04-004]]"
supporting_figures:
  - "xr-10-1016-j-molp-2019-04-004#figure-1"
  - "xr-10-1016-j-molp-2019-04-004#figure-2"
experiments:
  - 10x Genomics scRNA-seq
  - t-SNE clustering
  - marker gene analysis
contradictions:
  - "Fewer clusters (15) reported by [[xr-10-1016-j-devcel-2019-02-022]]"
contradiction_type: resolution-dependent
updated: "2026-05-29"
---

# Arabidopsis Root Has 24 Cell Clusters

## Claim

Unsupervised clustering of Arabidopsis root scRNA-seq data at higher resolution identifies 24 putative cell clusters, each with a distinct transcriptional signature — representing both major cell types and potential sub-states within lineages.

## Biological Context

The 15-cluster annotation (see [[arabidopsis-root-has-15-cell-types]]) captures major cell types. Higher-resolution clustering can reveal biologically meaningful substructure: developmental sub-states within a lineage, rare populations, or transcriptionally distinct microenvironments.

## Supporting Evidence

| Paper | Clusters | Resolution Approach | Notable Subclusters |
|-------|----------|--------------------|--------------------|
| [[xr-10-1016-j-molp-2019-04-004]] | 24 | Higher-resolution t-SNE + clustering | Sub-states within stele, epidermis, and cortex |

## Evidence Quality

**Tier 4** — Correlative Evidence. Higher cluster counts are resolution-dependent; biological validity of subclusters requires independent validation.

### Important Caveats
- Cluster number is a parameter choice, not a biological truth
- Some subclusters may represent technical noise or cell-cycle state rather than distinct cell types
- Different clustering algorithms and parameters yield different cluster counts
- The 15-cluster vs. 24-cluster discrepancy reflects resolution, not contradiction

## Contradictory Evidence

Studies using lower-resolution clustering (e.g., [[xr-10-1016-j-devcel-2019-02-022]]) report ~15 clusters. This is not a genuine contradiction — higher clustering resolution subdivides the same biological groups.

## Consensus Assessment

**Tentative** — 24 clusters are reported in one major study. The optimal cluster number for root scRNA-seq remains unresolved and likely depends on the biological question.

## Alternative Models

- **Optimal at ~15 clusters**: Lower resolution captures major cell types with less risk of over-clustering
- **Continuous spectrum**: No true discrete clusters exist; cells form a continuum better described by trajectories
- **More than 24**: Even higher-resolution clustering or iterative subclustering may reveal further structure

## Open Questions

- Which of the 24 clusters represent true biological entities vs. technical subdivisions?
- Do subclusters correspond to spatial domains within the root?
- What is the optimal resolution for a consensus root cell atlas?

## Next Critical Experiment

Multi-resolution clustering analysis (e.g., clustree) combined with spatial transcriptomics to determine at what resolution clusters map to spatially discrete cell populations.
