---
type: evidence
claim: "Quiescent center cells are transcriptionally distinct and detectable by droplet-based scRNA-seq"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - quiescent-center
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[xr-10-1016-j-devcel-2022-01-008]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-1"
experiments:
  - scRNA-seq
  - marker gene validation
  - WOX5 reporter
contradictions: []
updated: "2026-05-29"
---

# QC Cells Are Transcriptionally Distinct

## Claim

The quiescent center (QC) — a rare population of ~4 cells in the Arabidopsis root tip — forms a distinct transcriptional cluster in scRNA-seq data, demonstrating that droplet-based methods can capture even extremely rare cell types.

## Biological Context

The QC is the organizing center of the root stem cell niche. It maintains surrounding stem cells through short-range signals. Prior to scRNA-seq, the QC transcriptome was inaccessible by bulk methods due to its extremely low cell number. scRNA-seq provided the first transcriptome-wide view of QC identity.

## Supporting Evidence

| Paper | QC Detection | Key QC Markers |
|-------|-------------|----------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Distinct cluster | WOX5, PLT1, novel markers |
| [[xr-10-1104-pp-18-01482]] | Distinct subpopulation | WOX5 |
| [[xr-10-1016-j-devcel-2022-01-008]] | Distinct cluster in atlas | WOX5, QC-specific TFs |

## Evidence Quality

**Tier 3** — Spatial Support (scRNA-seq with WOX5 reporter validation)

## Contradictory Evidence

Some studies report QC cells split into subclusters, suggesting internal heterogeneity — but this does not contradict the core claim.

## Consensus Assessment

**Established** — QC transcriptional identity confirmed across multiple studies.

## Alternative Models

The QC may contain transcriptionally dynamic states (not a homogeneous population), but this is complementary rather than contradictory.

## Open Questions

- What is the functional significance of QC transcriptional heterogeneity?
- How does QC transcriptome change during stress or regeneration?

## Next Critical Experiment

Single-cell multi-omics (scRNA-seq + scATAC-seq) of QC cells to link transcriptional identity to chromatin state.
