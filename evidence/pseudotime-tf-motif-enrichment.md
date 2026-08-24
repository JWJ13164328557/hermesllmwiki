---
type: evidence
claim: "Distinct TF binding motifs are enriched in early vs. late pseudotime cells"
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
  - epidermis
development_stage:
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-3"
experiments:
  - pseudotime-dependent gene clustering
  - cis-regulatory motif enrichment
  - TF binding site prediction
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# TF Motif Enrichment Shifts with Pseudotime

## Claim

Genes upregulated early vs. late in pseudotime are enriched for distinct transcription factor binding motifs in their promoters, suggesting that sequential TF activity drives the temporal progression of root cell differentiation.

## Biological Context

Developmental transitions are orchestrated by cascades of transcription factors, each activating the next wave of gene expression. If pseudotime captures true developmental progression, then early-expressed genes should be enriched for motifs of early-acting TFs, and late-expressed genes for late-acting TFs.

## Supporting Evidence

| Paper | Cell Types | Early Motifs | Late Motifs | Proposed Cascade |
|-------|-----------|-------------|-------------|-----------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Endodermis, epidermis | Cell-cycle related TFs (E2F-like) | Differentiation TFs (MYB, NAC, bHLH families) | Proliferation → differentiation switch |

## Evidence Quality

**Tier 5** — Pre/Correlative Observations. Motif enrichment is computational; binding and functional activity not experimentally validated.

### Important Caveats
- Motif enrichment is based on promoter sequence, not actual TF binding (ChIP-seq data lacking)
- Promoter definitions (e.g., 1 kb upstream) are arbitrary
- Many plant TFs recognize similar motifs (e.g., MYB family), reducing specificity
- Motif presence ≠ TF binding ≠ transcriptional regulation

## Contradictory Evidence

None. The pattern is consistent with developmental biology principles, but the specific motif-TF links remain largely unvalidated.

## Consensus Assessment

**Tentative** — The computational pattern is clear, but functional validation is absent. This is a hypothesis-generating observation.

## Alternative Models

- **Motif promiscuity**: Enriched motifs may be bound by multiple TF families, weakening the cascade model
- **Chromatin accessibility**: Motif enrichment may reflect open chromatin regions rather than active TF binding
- **Technical artifact**: Pseudotime ordering may correlate with cell-cycle state, which has its own TF motif signature

## Open Questions

- Which specific TFs bind the enriched motifs in vivo?
- Do early TFs directly activate late TFs (sequential cascade) or act in parallel?
- Is the motif enrichment pattern conserved across cell types?

## Next Critical Experiment

scATAC-seq or ChIP-seq for candidate early and late pseudotime TFs (e.g., E2Fa for early, MYB36 for late endodermis) to validate that predicted motifs correspond to in vivo binding sites.
