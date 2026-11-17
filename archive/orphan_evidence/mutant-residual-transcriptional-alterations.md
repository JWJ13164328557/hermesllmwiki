---
type: evidence
claim: "Epidermis patterning mutants reveal cell-type-specific transcriptional alterations at single-cell resolution"
claim_type: association
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - epidermis
development_stage:
  - seedling
condition:
  - mutant background
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-4"
  - "xr-10-1016-j-devcel-2019-02-022#figure-5"
experiments:
  - scRNA-seq of mutants
  - differential expression analysis
  - cell-type proportion analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Mutants Reveal Cell-Type-Specific Transcriptional Alterations

## Claim

scRNA-seq profiling of root epidermis patterning mutants (e.g., *wer*, *cpc*, *gl2*) reveals that loss of key patterning transcription factors produces cell-type-specific transcriptional alterations, with some cell types showing dramatic reprogramming while others remain largely unaffected.

## Biological Context

The root epidermis is patterned by a network of MYB/bHLH/WD40 transcription factors: WER/GL3/EGL3/TTG1 promote non-hair fate, while CPC/TRY/ETC1 promote hair fate through lateral inhibition. Mutating these factors causes predictable cell-fate transformations. scRNA-seq in mutant backgrounds can reveal the full transcriptomic consequences of these fate switches.

## Supporting Evidence

| Paper | Mutants Profiled | Key Findings |
|-------|-----------------|--------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | *wer*, *cpc*, *gl2* | Cell-type proportions shift; residual cells show altered transcriptomes; non-epidermal cell types largely unchanged |

## Evidence Quality

**Tier 4** — Correlative Evidence. Transcriptional changes are observed but causal mechanisms (direct vs. indirect targets) not resolved.

### Important Caveats
- Mutants may have pleiotropic effects beyond the epidermis
- Single time-point analysis may miss developmental compensation
- scRNA-seq captures steady-state mRNA; does not distinguish primary from secondary transcriptional effects

## Contradictory Evidence

None. The observed transcriptional changes are consistent with known mutant phenotypes.

## Consensus Assessment

**Tentative** — Strongly plausible and consistent with genetic data but limited to a single study without independent replication.

## Alternative Models

- **Cell-fate conversion**: Transcriptional changes reflect complete cell-fate transformation (supported)
- **Partial reprogramming**: Mutant cells exist in hybrid or intermediate states rather than full fate conversions

## Open Questions

- Are the transcriptional changes in mutant residual cells direct targets of the mutated TFs or secondary consequences?
- Do mutant cells adopt stable alternative fates or remain in transcriptional "limbo"?
- How do double and triple mutants compare?

## Next Critical Experiment

scRNA-seq with inducible TF degradation (e.g., auxin-inducible degron) for WER or CPC to capture direct transcriptional targets at high temporal resolution before secondary effects accumulate.
