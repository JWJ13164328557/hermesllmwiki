---
type: entity
entity_type: gene
name: "OsbHLH150"
aliases: ["bHLH150", "CSS12b", "OsbHLH150 transcription factor"]
summary: "OsbHLH150 is a rice bHLH-type transcription factor that positively regulates chilling tolerance through the OsMAPK3-OsbHLH150-OsNCED3 phosphorylation cascade, which activates ABA biosynthesis. A natural V471L variant distinguishes cold-tolerant japonica from cold-sensitive indica rice."
status: reviewed
confidence: high
updated: "2026-05-29"
related_papers:
  - "[[rice-chilling-tolerance]]"
  - "[[osbhlh150-rice-chilling-tolera]]"
  - "[[aba-biosynthesis-stress]]"
related_evidence:
  - "[[rice-root-cell-types-10x]]"
  - "[[rice-root-marker-genes]]"
related_synthesis: []
---

# OsbHLH150

## Summary

OsbHLH150 is a bHLH family transcription factor in rice (*Oryza sativa*) that functions as the central regulatory hub of a cold-responsive kinase-TF-enzyme cascade: **OsMAPK3 → OsbHLH150 → OsNCED3 → ABA → chilling tolerance**. Under cold stress, OsMAPK3 phosphorylates OsbHLH150 at three key serine residues (S669, S674, S734), stabilizing the protein and enabling it to directly bind the E-box (CACATG) in the OsNCED3 promoter, driving ABA biosynthesis. A natural SNP at position 1203027368 causes a Val471Leu substitution — the Val allele (japonica) confers strong transactivation activity and cold tolerance, while the Leu allele (indica) impairs activity and causes cold sensitivity. Evidence comes from map-based cloning, knockout, complementation, Y2H, phosphorylation assays, ChIP/LUC, and double-mutant epistasis analysis (Luo et al., 2026, *Plant Communications*).

---

## Biological Roles

### Chilling Tolerance — Positive Regulator

OsbHLH150 acts as a positive regulator of chilling tolerance at both the seedling and booting stages.

Evidence:
- Map-based cloning from CSSL population (Koshihikari × Nona Bokra) identified OsbHLH150 as causal gene for QTL CSS12b
- CRISPR knockout lines show enhanced cold sensitivity
- Overexpression lines show enhanced chilling tolerance
- Complementation restores cold tolerance

Confidence: **Strong** (multiple lines of genetic evidence)

### Transcriptional Activation of ABA Biosynthesis

OsbHLH150 directly binds the OsNCED3 promoter to activate ABA biosynthetic gene expression.

Evidence:
- ChIP and LUC reporter assays confirm direct binding to E-box (CACATG) in OsNCED3 promoter
- Phosphorylated OsbHLH150 shows enhanced transcriptional activation
- OE-OsNCED3 rescues cold-sensitive phenotype of CR-OsbHLH150

Confidence: **Strong** (direct binding + genetic epistasis)

---

## Expression Pattern

### Tissue
Seedling leaves and shoot tissues; expression induced by cold stress

### Subcellular Localization
Nucleus (nuclear localization confirmed)

### Stress Responsiveness
Cold-inducible — expression elevated under chilling stress conditions

### Evidence
- qRT-PCR under cold treatment
- Subcellular localization assay (nuclear)
- Transcriptional activation assay (yeast)

### Caveats
Tissue-level expression across root and reproductive tissues not yet profiled by single-cell or spatial methods. Expression data is bulk-tissue level from the single published study.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| Chilling tolerance — positive regulator | Rice (*O. sativa*) | Seedling shoot | KO + OE + complementation | [[rice-chilling-tolerance]] | Strong |
| Cold-responsive expression | Rice (*O. sativa*) | Seedling shoot | qRT-PCR | [[rice-chilling-tolerance]] | Moderate |
| Physical interaction with OsMAPK3 | Rice (*O. sativa*) | — | Y2H + in vitro pull-down | [[rice-chilling-tolerance]] | Strong |
| Phosphorylation by OsMAPK3 (S669/S674/S734) | Rice (*O. sativa*) | — | In vitro + in vivo kinase assay | [[rice-chilling-tolerance]] | Strong |
| Direct binding to OsNCED3 promoter (E-box) | Rice (*O. sativa*) | — | ChIP + LUC reporter | [[rice-chilling-tolerance]] | Strong |
| V471L variant — transactivation activity difference | Rice (*O. sativa*) | — | Site-directed mutagenesis + reporter assay | [[rice-chilling-tolerance]] | Moderate |
| Haplotype association with cold tolerance | Rice (*O. sativa*) | Seedling | Population genetics (SNP 1203027368) | [[rice-chilling-tolerance]] | Moderate |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| OsMAPK3 | Physical interaction; phosphorylates S669/S674/S734 → stabilizes OsbHLH150 | Y2H + in vitro/in vivo phosphorylation | Strong |
| Cold stress signal | Induces OsbHLH150 expression | qRT-PCR under cold treatment | Moderate |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| OsNCED3 | Direct transcriptional activation via E-box (CACATG) binding | ChIP + LUC + genetic epistasis | Strong |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| OsMAPK3 → OsbHLH150 → OsNCED3 → ABA (linear cascade, no feedback described) | [[rice-chilling-tolerance]] | — |

### Co-expression Modules

| Module | Dataset | Evidence | Confidence |
|---|---|---|
| Cold-responsive ABA biosynthesis module | Bulk RNA under cold stress | Co-regulation of OsMAPK3, OsbHLH150, OsNCED3 under cold | Moderate |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Not yet characterized at single-cell resolution | — | — | — |

*Cell-type-specific expression of OsbHLH150 has not been profiled by scRNA-seq or spatial transcriptomics. Current evidence is at the whole-seedling level.*

---

## Developmental Context

### Seedling Stage
Function established at seedling stage — main phenotype scored for chilling tolerance. Overexpression also improves tolerance at booting stage.

### Evidence
- Seedling cold stress assays (Luo et al., 2026)
- Booting stage cold tolerance assay

### Gaps
Role in germination, reproductive development, or grain filling under cold stress not examined.

---

## Stress or Environmental Context

### Chilling Stress (Primary Context)
OsbHLH150 expression and phosphorylation are cold-induced. The entire OsMAPK3-OsbHLH150-OsNCED3 cascade is activated by low temperature.

### Other Abiotic Stresses
Role under drought, salt, or heat stress not yet investigated.

### Hormonal Context
Functions within ABA biosynthesis pathway as upstream activator of OsNCED3.

---

## Cross-Species Conservation

### Arabidopsis
Putative bHLH orthologs exist, but functional conservation in cold tolerance not established. Arabidopsis cold tolerance primarily via CBF/DREB pathway, not ABA-bHLH cascade.

### Rice (Other Subspecies)
- **Japonica** (Koshihikari): OsbHLH150-Val471 → strong transactivation → cold tolerant
- **Indica** (Nona Bokra): OsbHLH150-Leu471 → weak transactivation → cold sensitive

### Other Cereals
No direct ortholog functional characterization in maize, wheat, or barley.

### Conservation Assessment: **Divergent** — The OsMAPK3-OsbHLH150-OsNCED3 cascade appears rice-specific, though individual components (MAPK, bHLH TF, NCED) are broadly conserved. The cold-specific regulatory wiring may be a rice adaptation.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Genetic (KO, OE, complementation) | Strong | Multiple independent lines |
| Biochemical (Y2H, phosphorylation, ChIP) | Strong | Multiple assay types, reproducible |
| Population genetics (haplotype, SNP) | Moderate | Single population; needs broader validation |
| Expression (qRT-PCR) | Moderate | Bulk tissue only; no scRNA-seq |
| Cross-species | Weak | Only tested in rice |

**Overall Confidence: High** — The core mechanism is well-supported by genetic and biochemical evidence from a single comprehensive study. Independent replication and single-cell/spatial validation are needed.

---

## Contradictions and Context Dependence

### Contradiction 1: Single-study dependence
- **Claim**: OsMAPK3-OsbHLH150-OsNCED3 is the primary cold tolerance cascade in rice.
- **Context**: All evidence from one study (Luo et al., 2026). No independent replication yet.
- **Caveat**: Until independently replicated, the effect size and generality across rice varieties remain tentative.

### Context Dependence
- **Developmental stage**: Shown at seedling and booting; not tested at germination or grain filling.
- **Stress type**: Only tested under chilling; drought/salt response unknown.
- **Genetic background**: Mainly tested in japonica (Koshihikari) background; indica introgression promising but limited.

---

## Open Questions

### Question 1: What other targets does OsbHLH150 regulate besides OsNCED3?

- **Why It Matters**: The cold tolerance phenotype may involve additional downstream targets beyond ABA biosynthesis.
- **Missing Evidence**: ChIP-seq or DAP-seq genome-wide binding profile.
- **Suggested Experiment**: ChIP-seq under cold vs. control conditions to identify full target repertoire.

### Question 2: Is the OsMAPK3-OsbHLH150-OsNCED3 module conserved in other cereals?

- **Why It Matters**: Determines translational potential for wheat, maize, barley breeding.
- **Missing Evidence**: Ortholog functional characterization in other Poaceae.
- **Suggested Experiment**: Test bHLH150 ortholog complementation in rice mutants; cold assay in orthologous CRISPR lines in wheat/maize.

### Question 3: What is the cell-type-specific expression pattern of OsbHLH150?

- **Why It Matters**: Tissue-level expression data cannot resolve which cell types mediate cold sensing and ABA production.
- **Missing Evidence**: scRNA-seq or spatial transcriptomics of rice seedling under cold stress.
- **Suggested Experiment**: 10x scRNA-seq of cold-treated rice shoot apex; spatial transcriptomics (Stereo-seq) to localize expression.

---

## Key References

1. Luo J. et al. (2026). Natural variation in OsbHLH150 confers chilling tolerance in rice by increasing ABA biosynthesis. *Plant Communications*. DOI: [10.1016/j.xplc.2026.101919](https://doi.org/10.1016/j.xplc.2026.101919) — [[rice-chilling-tolerance]] — **Primary evidence for all claims on this page.**

---

## Knowledge Graph Links

### Related Genes
- [[osmapk3-rice]] — Upstream kinase; phosphorylates OsbHLH150
- [[osnced3-rice]] — Downstream target; ABA biosynthesis rate-limiting enzyme

### Related Pathways
- [[aba-biosynthesis-stress]] — ABA biosynthesis and stress response

### Related Entities
- [[guangxi-university-luo-lab]] — Research group
- [[rice-chilling-tolerance]] — Paper concept
