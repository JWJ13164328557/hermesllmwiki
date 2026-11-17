---
type: evidence
claim: "Canonical heat-shock genes are uniformly upregulated across all root cell types under heat stress"
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
  - seedling
condition:
  - heat stress (37°C)
support:
  - "[[xr-10-1105-tpc-18-00785]]"
supporting_figures:
  - "xr-10-1105-tpc-18-00785#figure-1"
  - "xr-10-1105-tpc-18-00785#figure-2"
experiments:
  - scRNA-seq with heat stress
  - differential expression across cell types
  - HSP gene family analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Heat-Shock Genes Are Uniformly Upregulated Across Root Cell Types

## Claim

Under heat stress (37°C), canonical heat-shock protein (HSP) genes — including HSP70, HSP90, and small HSP families — are uniformly and strongly upregulated across all root cell types, demonstrating a core transcriptional heat-stress response shared by the entire organ.

## Biological Context

The heat-shock response is an ancient, conserved cellular stress program mediated by heat-shock transcription factors (HSFs) that bind heat-shock elements (HSEs) in target gene promoters. Whether all cell types in a multicellular organ respond equivalently, or whether the response is cell-type-specific, was unknown before scRNA-seq.

## Supporting Evidence

| Paper | Stress Condition | HSP Genes Assessed | Key Finding |
|-------|-----------------|-------------------|-------------|
| [[xr-10-1105-tpc-18-00785]] | 37°C, 1 hr | HSP70, HSP90, sHSP families | Uniform upregulation across all 15+ cell types; >10-fold induction common |

## Evidence Quality

**Tier 3** — Spatial Support. Single-cell resolution reveals that the core heat-shock response is pancellular, consistent with bulk RNA-seq data.

### Important Caveats
- Single time point (1 hr); temporal dynamics of the response per cell type not captured
- Only one heat stress regime tested; dose-response unknown
- "Uniform" refers to qualitative upregulation; quantitative fold-changes may vary mildly

## Contradictory Evidence

None challenging the uniformity of canonical HSP induction. Some studies suggest that the magnitude of induction may differ subtly between cell types, but this does not contradict the core claim of shared response.

## Consensus Assessment

**Established** — The pancellular nature of the heat-shock response is consistent with decades of molecular biology and confirmed at single-cell resolution by [[xr-10-1105-tpc-18-00785]].

## Alternative Models

N/A — This is a descriptive observation with strong prior support.

## Open Questions

- Does the uniform response hold at milder heat-stress temperatures (e.g., 30°C, 34°C)?
- Are heat-shock transcription factors (HSFA1a, HSFA2) also uniformly expressed across cell types?
- Does the response magnitude scale with stress duration?

## Next Critical Experiment

Time-course scRNA-seq (0, 15 min, 30 min, 1 hr, 4 hr) at multiple temperatures to resolve cell-type-specific differences in heat-shock response kinetics.
