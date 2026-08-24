---
type: evidence
claim: "Pseudotime analysis captures continuous transcriptional progression during endodermis differentiation"
claim_type: association
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - endodermis
development_stage:
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-3"
experiments:
  - pseudotime analysis (Monocle 2)
  - branch expression analysis modeling (BEAM)
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Pseudotime Captures Continuous Endodermis Differentiation

## Claim

Monocle 2 pseudotime analysis of endodermis cells from Arabidopsis root scRNA-seq data reconstructs a continuous transcriptional trajectory from undifferentiated meristematic cells through to mature, Casparian strip-forming endodermis, demonstrating that endodermis differentiation is transcriptionally gradual.

## Biological Context

Endodermis cells are produced by the root meristem and differentiate progressively as they are displaced from the tip. The hallmark of differentiation is lignification forming the Casparian strip. Whether this process involves discrete transcriptional states or smooth progression was unknown before scRNA-seq.

## Supporting Evidence

| Paper | Method | Trajectory Features | Validation |
|-------|--------|---------------------|------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Monocle 2 + BEAM | Single continuous trajectory; branch points at differentiation decisions | Known marker gene progression confirmed (e.g., CASP1–5, MYB36) |

## Evidence Quality

**Tier 4** — Correlative Evidence. Inferred ordering from static transcriptional snapshots; not validated by lineage tracing or live imaging.

### Important Caveats
- Pseudotime assumes a tree-like differentiation topology
- Cannot distinguish real developmental time from other continuous covariates (cell size, stress)
- Monocle 2 ordering sensitive to gene selection parameters

## Contradictory Evidence

None directly. However, other trajectory algorithms (e.g., Monocle 3, Slingshot) may produce subtly different branch topologies.

## Consensus Assessment

**Tentative** — The qualitative conclusion (continuous progression) is robust, but the precise ordering and branch structure depend on algorithm choice and parameters.

## Alternative Models

- **Discrete stage model**: Differentiation occurs in transcriptional jumps between stable states (not supported by current scRNA-seq data but not rigorously excluded)
- **Cycle-influenced**: Pseudotime may conflate cell-cycle state with differentiation stage

## Open Questions

- Is the trajectory reproducible across biological replicates and growth conditions?
- How do trajectory algorithms (Monocle 2 vs. 3 vs. Slingshot vs. scVelo) compare?
- Does RNA velocity analysis confirm the directional flow of differentiation?

## Next Critical Experiment

Compare pseudotime trajectories from three orthogonal algorithms (Monocle 3, Slingshot, scVelo) on the same endodermis data; validate directionality with RNA velocity and spatial transcriptomics.
