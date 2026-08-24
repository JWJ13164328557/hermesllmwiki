---
type: evidence
claim: "DESeq2 fold change shrinkage improves stability and interpretability of DEG estimates"
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
  - "[[xr-10-1186-s13059-014-0550-8]]"
supporting_figures:
  - "xr-10-1186-s13059-014-0550-8#figure-1"
  - "xr-10-1186-s13059-014-0550-8#figure-3"
experiments:
  - differential expression analysis
  - LFC shrinkage
  - variance estimation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# DESeq2 Fold Change Shrinkage Improves DEG Stability

## Claim

DESeq2's fold change shrinkage (log2 fold change shrinkage using an empirical Bayes prior) reduces the variance of log fold change estimates for genes with low counts or high dispersion, improving the stability and interpretability of differentially expressed gene (DEG) rankings.

## Methodological Context

In RNA-seq differential expression analysis, log fold change estimates for lowly expressed genes are noisy and often inflated. DESeq2 addresses this with zero-centered normal or adaptive shrinkage priors that pull noisy LFC estimates toward zero, proportional to their uncertainty. This prevents low-count genes from dominating DEG lists by false-positive large fold changes.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1186-s13059-014-0550-8]] | LFC shrinkage | Shrinkage reduces false positives in DEG ranking; improves gene set enrichment analysis results by preventing low-count gene inflation | Multiple RNA-seq datasets |

## Evidence Quality

**Tier 1** — Statistical framework with extensive empirical validation

## Contradictory Evidence

None. LFC shrinkage is widely adopted in RNA-seq analysis and endorsed by best-practice guidelines.

## Consensus Assessment

**Established** — DESeq2 is the most widely used tool for bulk RNA-seq differential expression.

## Alternative Models

edgeR (quasi-likelihood), limma-voom, and Wilcoxon-based methods for comparative analysis.

## Open Questions

- Is the normal prior appropriate for all data types, or should the prior be data-driven?
- Does LFC shrinkage benefit single-cell pseudobulk differential expression?

## Next Critical Experiment

Compare DESeq2 LFC shrinkage with Bayesian hierarchical models (e.g., apeglm) for single-cell pseudobulk DEG analysis.
