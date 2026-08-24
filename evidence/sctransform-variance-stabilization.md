---
type: evidence
claim: "Pearson residuals from regularized negative binomial regression remove technical variation while preserving biological heterogeneity"
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
  - "[[xr-10-1186-s13059-019-1874-1]]"
supporting_figures:
  - "xr-10-1186-s13059-019-1874-1#figure-1"
  - "xr-10-1186-s13059-019-1874-1#figure-2"
experiments:
  - scRNA-seq normalization
  - variance stabilization
  - benchmarking
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# sctransform Variance Stabilization Removes Technical Variation

## Claim

sctransform uses Pearson residuals from a regularized negative binomial regression model to normalize scRNA-seq data, effectively removing technical variation (sequencing depth effects, mitochondrial content) while preserving biologically meaningful heterogeneity in gene expression.

## Methodological Context

scRNA-seq data exhibits a mean-variance relationship driven by both technical (sampling) noise and biological heterogeneity. Traditional log-normalization fails to fully remove this dependency. sctransform models UMI counts as negative binomial, estimates gene-specific parameters via regularization, and computes Pearson residuals that are independent of sequencing depth for well-measured genes.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1186-s13059-019-1874-1]] | sctransform benchmarking | Pearson residuals produce normalized data with minimal depth-dependence; preserves biological variation better than log-normalization | Multiple scRNA-seq datasets |

## Evidence Quality

**Tier 1** — Statistical framework with comprehensive benchmarking

## Contradictory Evidence

None. sctransform is the default normalization method in Seurat v3+.

## Consensus Assessment

**Established** — sctransform is a widely adopted scRNA-seq normalization method.

## Alternative Models

Log-normalization, scran pooling-based size factors, and Dino (normalized residuals from zero-inflated models).

## Open Questions

- Is the negative binomial assumption appropriate for all UMI-based scRNA-seq technologies?
- How well does sctransform handle batch effects in the residuals?

## Next Critical Experiment

Compare sctransform with alternative variance-stabilizing transformations for integration tasks across diverse single-cell technologies.
