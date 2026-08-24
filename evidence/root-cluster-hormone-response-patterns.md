---
type: evidence
claim: "Each root cell cluster shows unique hormonal response signatures"
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
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2019-04-004]]"
supporting_figures:
  - "xr-10-1016-j-molp-2019-04-004#figure-4"
  - "xr-10-1016-j-molp-2019-04-004#figure-5"
experiments:
  - scRNA-seq
  - hormone-related gene expression profiling
  - functional category enrichment
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Root Cell Clusters Have Unique Hormonal Signatures

## Claim

The 24 root cell clusters defined by scRNA-seq exhibit distinct expression patterns for hormone biosynthesis, signaling, and response genes — including auxin, cytokinin, gibberellin, ABA, ethylene, and brassinosteroid pathways — indicating cell-type-specific hormonal microenvironments.

## Biological Context

Plant hormones coordinate root development, with auxin establishing positional gradients, cytokinin regulating meristem size, and ABA mediating stress responses. Each hormone's effect depends on cell-type-specific receptor expression, signaling component availability, and downstream transcriptional machinery. scRNA-seq can map this complexity at cell-type resolution.

## Supporting Evidence

| Paper | Hormone Pathways Profiled | Key Findings |
|-------|--------------------------|-------------|
| [[xr-10-1016-j-molp-2019-04-004]] | Auxin, cytokinin, GA, ABA, ethylene, BR | Each cluster has a unique combinatorial hormone gene signature; QC and stem cell clusters show distinct auxin signaling profiles |

## Evidence Quality

**Tier 5** — Pre/Correlative Observations. Hormone pathway activity is inferred from gene expression; hormone concentrations and signaling dynamics are not measured.

### Important Caveats
- Gene expression of biosynthetic enzymes does not directly measure hormone levels
- Signaling component expression does not prove pathway activation
- Many hormone responses are post-translational (e.g., auxin-regulated degradation of Aux/IAA proteins)
- Baseline condition only; no hormone treatments applied to test responsiveness

## Contradictory Evidence

None. The patterns are consistent with known hormone biology (e.g., auxin maximum in QC, cytokinin signaling in vascular cells).

## Consensus Assessment

**Tentative** — The transcriptional signatures are clear and biologically plausible, but functional hormone activity (concentrations, signaling output) remains unmeasured.

## Alternative Models

- **Uniform hormone sensitivity**: All cell types may express core signaling components, with specificity arising from post-translational regulation (partially contradicted by the data)
- **Concentration-driven**: Cell-type specificity may reflect hormone gradients rather than cell-type-intrinsic signaling differences

## Open Questions

- Do hormone-responsive reporter lines confirm the cell-type-specific patterns predicted by scRNA-seq?
- How do hormonal signatures change upon exogenous hormone treatment?
- Which cell clusters are functionally responsive to each hormone in terms of transcriptional output?

## Next Critical Experiment

Treat roots with individual hormones (auxin, cytokinin, ABA, etc.) and perform scRNA-seq at multiple time points to directly measure cell-type-specific transcriptional responses and validate pathway activity predictions.
