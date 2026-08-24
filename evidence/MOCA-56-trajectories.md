---
type: evidence
claim: "Monocle 3 identifies 56 developmental trajectories from ~2 million cells in MOCA"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Mus musculus
tissue:
  - whole embryo
cell_type:
  - multiple developmental lineages
development_stage:
  - E9.5 to E13.5
condition:
  - standard
support:
  - "[[xr-10-1038-s41586-019-0969-x]]"
supporting_figures:
  - "xr-10-1038-s41586-019-0969-x#figure-3"
  - "xr-10-1038-s41586-019-0969-x#figure-4"
experiments:
  - trajectory inference
  - Monocle 3
  - developmental pseudotime
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Monocle 3 Identifies 56 Developmental Trajectories in MOCA

## Claim

Monocle 3 trajectory inference, applied to the ~2 million cells of the Mouse Organogenesis Cell Atlas (MOCA), identifies 56 distinct developmental trajectories corresponding to major organ lineages and cell-type differentiation pathways during organogenesis.

## Methodological Context

Trajectory inference algorithms reconstruct developmental lineages by ordering cells along pseudotime based on transcriptional similarity. Monocle 3 uses UMAP for dimensionality reduction followed by principal graph-based trajectory reconstruction, enabling it to handle the scale and complexity of the MOCA dataset.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-s41586-019-0969-x]] | Monocle 3 trajectory inference | 56 trajectories identified, including 40 major organ lineages; branching points correspond to known fate decisions | ~2M cells |

## Evidence Quality

**Tier 2** — Computational inference with biological plausibility (known developmental lineages confirmed)

## Contradictory Evidence

None. Trajectories broadly recapitulate known developmental biology.

## Consensus Assessment

**Established** — Widely cited demonstration of large-scale trajectory inference.

## Alternative Models

RNA velocity, Waddington-OT, and CellRank are alternative trajectory/pseudotime methods.

## Open Questions

- How many of the 56 trajectories represent truly independent lineages vs. branches within the same lineage?
- Can these trajectories be ordered in absolute developmental time?

## Next Critical Experiment

Validate predicted trajectory branch points using lineage tracing (e.g., barcoding or inducible Cre) in mouse embryos.
