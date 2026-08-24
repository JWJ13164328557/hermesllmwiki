---
type: evidence
claim: "mRNA in situ hybridization validates scRNA-seq-identified cell-type markers in maize ears"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Zea mays
tissue:
  - developing ear
cell_type:
  - inflorescence meristem
  - spikelet pair meristem
  - floral meristem
development_stage:
  - early reproductive
condition:
  - field-grown
support:
  - "[[xr-10-1016-j-devcel-2020-12-015]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2020-12-015#figure-2"
experiments:
  - mRNA in situ hybridization
  - scRNA-seq
  - marker gene validation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# In Situ Hybridization Validates scRNA-seq Markers in Maize Ears

## Claim

mRNA in situ hybridization of computationally predicted marker genes confirms their cell-type-specific expression patterns in developing maize ears, providing spatial validation of scRNA-seq cluster annotations.

## Biological Context

scRNA-seq identifies clusters computationally, but spatial validation is essential to confirm that these clusters correspond to anatomically defined cell types. In situ hybridization of predicted markers is the gold standard for validation.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2020-12-015]] | In situ hybridization of scRNA-seq-derived markers | Markers for IM (e.g., KN1), SPM (e.g., FEA4), and FM (e.g., ZAG1) show expected spatial patterns | ~12,500 (scRNA-seq) |

## Evidence Quality

**Tier 2** — Spatial Validation (direct in situ confirmation of marker expression in intact tissue)

## Contradictory Evidence

None. Marker expression patterns are consistent with prior knowledge and scRNA-seq predictions.

## Consensus Assessment

**Established** — Multiple markers validated across major meristem domains.

## Alternative Models

N/A — Validation experiment confirms computational predictions.

## Open Questions

- Are there markers whose in situ pattern differs from scRNA-seq prediction?
- What is the minimum number of markers needed to define a cell type unambiguously?
- Can combinatorial marker expression further refine cell-type boundaries?

## Next Critical Experiment

Multiplexed single-molecule FISH to simultaneously validate multiple markers and quantify co-expression boundaries at cellular resolution.
