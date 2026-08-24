---
type: evidence
claim: "Optimal transport mathematical framework infers developmental trajectories superior to pseudotime"
claim_type: method
status: reviewed
consensus_level: emerging
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - root developmental lineages
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2022-01-008]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2022-01-008#figure-2"
experiments:
  - optimal transport
  - trajectory inference
  - scRNA-seq
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Optimal Transport Framework Infers Developmental Trajectories

## Claim

An optimal transport mathematical framework applied to scRNA-seq data infers developmental trajectories in the Arabidopsis root with higher accuracy and biological interpretability than standard pseudotime algorithms, by leveraging prior knowledge of spatial tissue organization.

## Biological Context

Pseudotime algorithms (Monocle, Slingshot) infer differentiation trajectories from transcriptomic similarity alone. In structured tissues like the root, incorporating spatial constraints via optimal transport can improve trajectory inference by respecting known tissue architecture.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2022-01-008]] | Optimal transport (Waddington-OT) | Inferred trajectories match known root developmental lineages (e.g., endodermis-cortex initial → differentiated endodermis); outperforms pseudotime in spatial coherence | Organ-scale |

## Evidence Quality

**Tier 3** — Spatial Support (trajectories validated against known root developmental biology and spatial organization)

## Contradictory Evidence

None. Optimal transport trajectories are consistent with known developmental lineages.

## Consensus Assessment

**Emerging** — Single study demonstrates superiority; broader adoption and benchmarking against diverse pseudotime methods needed.

## Alternative Models

Standard pseudotime methods may perform adequately for simple linear trajectories; the advantage of optimal transport may be most pronounced in complex, spatially structured tissues.

## Open Questions

- How sensitive is optimal transport to the choice of cost function?
- Does the method generalize to less spatially structured tissues?
- Can it handle branching trajectories with similar accuracy?

## Next Critical Experiment

Benchmark optimal transport against 5+ pseudotime methods across diverse tissues and species using ground-truth lineage tracing data.
