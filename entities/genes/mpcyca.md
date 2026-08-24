---
type: entity
entity_type: gene
name: "MpCYCA"
aliases: ["Cyclin A", "MpCYCA cyclin", "Marchantia S-phase cyclin"]
summary: "MpCYCA is the sole S-phase cyclin in Marchantia polymorpha, uniquely driving DNA replication progression in a minimalist cell cycle system. Unlike flowering plants with dozens of cyclins, Marchantia relies on a single non-redundant CYCA whose overexpression causes growth arrest, revealing the need for precise temporal control."
status: reviewed
confidence: high
updated: "2026-05-29"
related_papers:
  - "[[plant-cell-cycle-control]]"
  - "[[cell-cycle-scrna-seq]]"
related_evidence:
  - "[[snRNA-seq-valid-plant-transcriptomics]]"
  - "[[snRNA-seq-additional-plant-cell-subtypes]]"
related_synthesis: []
---

# MpCYCA

## Summary

MpCYCA is the A-type cyclin in *Marchantia polymorpha* (common liverwort) and the **sole S-phase-dominant cyclin** in its minimalist cell cycle system. Single-cell RNA-seq of the vegetative gametophyte (thallus) demonstrated that MpCYCA expression is specific to the S-phase (DNA replication), with minimal overlap with G1 (MpCYCD;1) or G2/M (MpCYCB;1) phases. Fluorescent reporter live imaging confirmed S-phase-specific protein dynamics. Overexpression of MpCYCA causes growth arrest, indicating that S-phase cyclin levels must be tightly controlled — unlike MpCYCD;1, which acts as a proliferation driver. Evidence is from Romani & Haseloff et al. (*The Plant Cell*), integrating scRNA-seq with functional overexpression phenotyping (Romani & Haseloff et al., 2025).

---

## Biological Roles

### S-phase Progression — Non-Redundant Regulator

MpCYCA is the only cyclin dominating the S-phase in Marchantia, driving DNA replication in proliferating cells of the vegetative thallus.

Evidence:
- scRNA-seq: MpCYCA expression specifically enriched in S-phase cells, with clean temporal boundaries
- Live fluorescent reporter: S-phase-specific protein accumulation and localization
- Overexpression phenotype: growth arrest (tight temporal control required)

Confidence: **Strong** (scRNA-seq + live imaging converge)

### Growth Arrest Upon Overexpression

Unlike MpCYCD;1 (which drives proliferation when overexpressed), MpCYCA overexpression causes growth cessation, demonstrating that S-phase cyclin levels must oscillate precisely.

Evidence:
- Overexpression lines show arrested growth phenotype
- Suggests strict temporal window for CYCA function — cannot be constitutively active

Confidence: **Strong** (direct overexpression phenotype)

---

## Expression Pattern

### Tissue
Expressed in proliferating cells of the vegetative thallus (gametophyte), including apical notch meristematic regions and gemma cups.

### Phase Specificity
S-phase-specific — scRNA-seq shows MpCYCA expression marks S-phase cells with minimal overlap with adjacent cell cycle phases.

### Protein Dynamics
- Protein turnover and subcellular localization complement transcriptional regulation to maintain phase specificity
- Fluorescent reporter lines validate S-phase-specific protein accumulation

### Evidence
- scRNA-seq of Marchantia thallus (Romani & Haseloff et al., 2025)
- Live fluorescent reporter imaging

### Caveats
Expression data is from whole-thallus scRNA-seq; tissue-specific or cell-type-specific variation within proliferating cell populations has not been resolved. Spatial transcriptomics data is not available.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| S-phase cyclin — non-redundant | Marchantia | Vegetative thallus | scRNA-seq + live reporter | [[plant-cell-cycle-control]] | Strong |
| S-phase specificity (clean temporal boundaries) | Marchantia | Vegetative thallus | scRNA-seq phase assignment | [[cell-cycle-scrna-seq]] | Strong |
| Overexpression → growth arrest | Marchantia | Vegetative thallus | Genetic (OE phenotyping) | [[plant-cell-cycle-control]] | Strong |
| Protein turnover + localization control | Marchantia | Vegetative thallus | Fluorescent reporter imaging | [[plant-cell-cycle-control]] | Moderate |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| S-phase entry signals | Transcriptional activation at G1/S transition | Inferred from phase-specific expression pattern | Moderate (mechanism uncharacterized) |
| Post-translational control | Protein turnover and subcellular localization restrict activity to S-phase | Fluorescent reporter dynamics | Moderate |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| CDK partners | MpCYCA binds and activates CDKs to drive S-phase progression | Inferred from cyclin-CDK paradigm; specific CDK partners not identified | Low |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| S-phase completion → MpCYCA degradation | Implied by oscillatory expression and growth arrest upon constitutive expression | Moderate |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Proliferating thallus cells | S-phase progression in dividing cells | scRNA-seq | Moderate |
| Not resolved at individual cell-type level | — | — | — |

*Marchantia thallus cell types have not been fully catalogued at single-cell resolution; the scRNA-seq data is organized by cell cycle phase rather than cell type identity.*

---

## Developmental Context

### Vegetative Gametophyte (Thallus)
MpCYCA function demonstrated in the vegetative thallus — the dominant life stage of Marchantia (haploid gametophyte). Proliferating cells in the apical notch and gemma cups express MpCYCA during S-phase.

### Reproductive Stages
Role of MpCYCA in sexual reproductive structures (antheridiophores, archegoniophores) not specifically characterized.

---

## Stress or Environmental Context

### Normal Proliferation (Primary Context)
MpCYCA characterized under standard growth conditions; role in S-phase under normal cell cycle progression.

### Stress Responses
No data on MpCYCA expression or function under environmental stress (cold, heat, drought, nutrient limitation). Whether the minimalist cell cycle is modulated by stress in Marchantia is unknown.

---

## Cross-Species Conservation

### Arabidopsis
Arabidopsis has multiple A-type cyclins (CYCA1, CYCA2, CYCA3 families) with functional redundancy. No single Arabidopsis CYCA is strictly non-redundant for S-phase. The minimalist MpCYCA represents the ancestral state, while Arabidopsis CYCA redundancy is a derived feature.

### Other Bryophytes
*Physcomitrium patens* (moss) has more CYCA paralogs than Marchantia, suggesting the Marchantia single-copy state is unusually reduced even among bryophytes.

### Conservation Assessment: **Ancestral** — The single CYCA in Marchantia represents the predicted ancestral cyclin complement. Seed plant CYCA expansion is derived.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Transcriptional (scRNA-seq) | Strong | Single-cell resolution, phase-specific pattern |
| Protein (live reporter) | Strong | Protein dynamics validate mRNA data |
| Functional (OE phenotyping) | Strong | Clear overexpression phenotype |
| Biochemical (CDK partners) | Weak | Specific CDK partners not identified |
| Cross-species | Moderate | Phylogenetic inference; no direct ortholog complementation |

**Overall Confidence: High** — MpCYCA S-phase identity and non-redundant function are well-supported by scRNA-seq, live imaging, and overexpression phenotyping from a single comprehensive study. Independent replication and biochemical characterization of CDK interactions are needed.

---

## Contradictions and Context Dependence

### Contradiction 1: Single-study dependence
- **Claim**: MpCYCA is the sole S-phase cyclin with clean phase boundaries.
- **Context**: All evidence from one study (Romani & Haseloff et al., 2025). No independent replication in other Marchantia accessions or related liverwort species.
- **Caveat**: Until independently replicated, the generality of the minimalist model across Marchantia populations remains tentative.

### Context Dependence
- **Life stage**: Only tested in vegetative gametophyte; sporophyte cell cycle regulation unknown.
- **Growth conditions**: Standard laboratory conditions; environmental modulation untested.
- **Genetic background**: Single Marchantia accession (Cam-2 or Tak-1 background).

---

## Open Questions

### Question 1: What CDK partners does MpCYCA use?
- **Why It Matters**: Cyclins function by binding and activating specific CDKs. Identifying CYCA-CDK pairs is essential for a complete mechanistic model.
- **Missing Evidence**: Co-immunoprecipitation, Y2H screen, or in vitro kinase assay for CYCA-CDK interaction.
- **Suggested Experiment**: Y2H screen of Marchantia CDKs against MpCYCA; in vitro kinase assay with candidate CDK partners.

### Question 2: How is S-phase entry transcriptionally controlled?
- **Why It Matters**: Understanding the upstream transcription factors that activate MpCYCA at G1/S transition would reveal how phase boundaries are enforced in the minimalist system.
- **Missing Evidence**: Promoter analysis, transcription factor identification.
- **Suggested Experiment**: Promoter deletion analysis; Y1H screen for MpCYCA promoter-binding TFs.

### Question 3: Is MpCYCA function conserved in other liverwort species?
- **Why It Matters**: Determines whether the minimalist model is unique to Marchantia or conserved across Marchantiophyta.
- **Missing Evidence**: CYCA functional characterization in *Marchantia paleacea* or other liverwort species.
- **Suggested Experiment**: CYCA knockout/complementation in another liverwort species; scRNA-seq comparison.

---

## Key References

1. Romani F. & Haseloff J. et al. (2025). A simple cell-cycle control system in Marchantia polymorpha provides a framework for understanding plant cell proliferation. *The Plant Cell*. — [[plant-cell-cycle-control]] — **Primary evidence for all claims on this page.**

---

## Knowledge Graph Links

### Related Genes
- [[mpcycd1]] — G1 cyclin; drives cell cycle re-entry (upstream in cell cycle)
- [[mpcycb1]] — G2/M cyclin; mitotic entry (downstream in cell cycle)

### Related Concepts
- [[plant-cell-cycle-control]] — Plant cell cycle regulatory framework
- [[cell-cycle-scrna-seq]] — scRNA-seq methodology for cell cycle analysis

### Related Entities
- [[marchantia-polymorpha]] — Host species
- Evidence: [[snRNA-seq-valid-plant-transcriptomics]]
