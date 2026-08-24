---
type: evidence
claim: "UMAP yields highest reproducibility in clustering organization across repeated single-cell analyses"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - multiple
tissue:
  - multiple
cell_type:
  - multiple
development_stage:
  - multiple
condition:
  - standard
support:
  - "[[xr-10-1038-nbt-4314]]"
supporting_figures:
  - "xr-10-1038-nbt-4314#figure-2"
  - "xr-10-1038-nbt-4314#figure-3"
experiments:
  - dimensionality reduction
  - reproducibility assessment
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# UMAP Yields Highest Reproducibility in Single-Cell Clustering

## Claim

UMAP yields the highest reproducibility in clustering organization across repeated single-cell analyses when compared to t-SNE, PCA, and other dimensionality reduction methods, as measured by preservation of neighborhood relationships across independent runs.

## Methodological Context

Stochastic dimensionality reduction methods can produce different visual layouts and downstream clustering results when run multiple times on the same data. Method reproducibility is assessed by quantifying how consistently the local neighborhood structure (k-nearest neighbor overlap) is preserved across independent runs.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-nbt-4314]] | UMAP reproducibility benchmark | UMAP had highest kNN preservation across repeated runs vs. t-SNE, PCA, LargeVis, TriMap, scvis | Multiple single-cell datasets |

## Evidence Quality

**Tier 1** — Systematic empirical benchmarking with quantitative reproducibility metrics

## Contradictory Evidence

None. UMAP's reproducibility advantage is consistent across datasets.

## Consensus Assessment

**Established** — UMAP is preferred when reproducible embeddings are required for downstream analysis.

## Alternative Models

PCA is deterministic and fully reproducible but preserves less biological structure.

## Open Questions

- How does setting random seeds affect biological conclusions downstream?
- Are there cases where t-SNE's greater per-run variability captures meaningful biological uncertainty?

## Next Critical Experiment

Quantify how UMAP reproducibility translates to reproducibility of differential expression and gene set enrichment results.
