---
type: evidence
claim: "10x Genomics scRNA-seq resolves all major Arabidopsis root cell types at high resolution"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - all root cell types
development_stage:
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[xr-10-1016-j-molp-2019-04-004]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-1"
  - "xr-10-1104-pp-18-01482#figure-1"
  - "xr-10-1016-j-molp-2019-04-004#figure-1"
experiments:
  - 10x Genomics scRNA-seq
  - UMAP/t-SNE clustering
  - marker gene validation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# 10x scRNA-seq Resolves All Major Arabidopsis Root Cell Types

## Claim

The 10x Genomics droplet-based platform resolves all major Arabidopsis root cell types — including epidermis (hair and non-hair), cortex, endodermis, pericycle, stele, columella, lateral root cap, and quiescent center — as transcriptionally distinct clusters.

## Biological Context

The Arabidopsis root contains ~15 anatomically defined cell types organized in concentric radial layers. Demonstrating that scRNA-seq can faithfully recapitulate this known anatomy is a critical validation step and establishes a baseline for discovery of novel cell states.

## Supporting Evidence

| Paper | Clusters | Cell Types Resolved | Key Finding |
|-------|----------|---------------------|-------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | 15 | All major types + QC | Hair vs. non-hair epidermis split |
| [[xr-10-1104-pp-18-01482]] | 15+ | All major types | Time-course enhances resolution |
| [[xr-10-1016-j-molp-2019-04-004]] | 24 | All types + subclusters | Higher resolution reveals sub-states |

## Evidence Quality

**Tier 3** — Spatial Support (cell-type annotations validated by known marker genes from in situ hybridization and reporter lines)

## Contradictory Evidence

None. All studies identify the same set of major cell types. Variations in cluster number reflect differences in clustering resolution, not genuine disagreement about cell-type identity.

## Consensus Assessment

**Established** — Independently replicated across at least three major studies using independent plant growth, protoplasting, and analysis pipelines.

## Alternative Models

N/A — This is a validation claim rather than a mechanistic one.

## Open Questions

- What is the optimal clustering resolution — when does over-clustering begin?
- Do subclusters represent biologically meaningful cell states or technical noise?
- How many rare cell types remain below detection?

## Next Critical Experiment

Integration of all published root scRNA-seq datasets with a common reference atlas to define consensus cell-type annotations and systematically identify rare populations.
