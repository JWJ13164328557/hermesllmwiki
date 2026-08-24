---
type: evidence
claim: "Hundreds of cell-type-specific marker genes identified by 10x scRNA-seq in Arabidopsis root"
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
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[xr-10-1016-j-molp-2019-04-004]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-1"
  - "xr-10-1104-pp-18-01482#figure-2"
  - "xr-10-1016-j-molp-2019-04-004#figure-2"
experiments:
  - differential expression analysis
  - marker gene identification
  - cluster annotation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Hundreds of Cell-Type-Specific Marker Genes Identified

## Claim

Differential expression analysis of 10x scRNA-seq data from Arabidopsis roots identifies hundreds of cell-type-specific marker genes, many of which are novel and expand the molecular toolkit for root cell-type identification beyond classical reporters.

## Biological Context

Prior to scRNA-seq, Arabidopsis root cell types were identified primarily by morphology and a small set of well-characterized marker genes (e.g., WOX5 for QC, SHR/SCR for endodermis, CO2 for cortex). scRNA-seq enables unbiased, transcriptome-wide identification of genes enriched in each cell type, dramatically expanding the marker repertoire.

## Supporting Evidence

| Paper | Marker Genes Identified | Novel Markers | Key Categories |
|-------|------------------------|---------------|----------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Hundreds per cell type | Many novel | TFs, transporters, cell wall enzymes, signaling peptides |
| [[xr-10-1104-pp-18-01482]] | Hundreds per type | Many novel | Time-resolved markers, stress-responsive genes |
| [[xr-10-1016-j-molp-2019-04-004]] | Hundreds per cluster | Many novel | Ion transporters, hormone-related genes |

## Evidence Quality

**Tier 4** — Correlative Evidence. Marker gene status is defined by statistical enrichment in scRNA-seq data; spatial validation by in situ hybridization or reporter lines is limited to a small subset.

### Important Caveats
- Marker gene lists are threshold-dependent and vary between studies
- Many "markers" may show expression in multiple cell types at lower levels
- Protoplasting may alter expression of some genes
- Post-transcriptional regulation not captured

## Contradictory Evidence

Marker gene lists show substantial overlap across studies for well-characterized genes but can differ for lowly-expressed or stress-responsive candidates. This reflects methodological differences rather than contradictions.

## Consensus Assessment

**Tentative** — The qualitative finding (many cell-type-specific genes exist) is robust, but quantitative gene lists require meta-analysis and spatial validation.

## Alternative Models

N/A — this is an observation, not a mechanistic model.

## Open Questions

- What fraction of identified markers are functionally required for cell-type identity?
- Which novel markers are most specific and robust across growth conditions?
- How many markers are conserved across plant species?

## Next Critical Experiment

Large-scale spatial validation of top 50 novel markers per cell type using multiplexed in situ hybridization (e.g., MERFISH, HybISS) or high-throughput reporter lines.
