---
type: entity
entity_type: gene
name: "MpCYCB;1"
aliases: ["Cyclin B1", "MpCYCB1", "MpCYCB;1 cyclin", "Marchantia M-phase cyclin"]
summary: "MpCYCB;1 is the sole G2/M-phase cyclin in Marchantia polymorpha, uniquely driving mitotic entry in a minimalist cell cycle system. Its overexpression causes growth arrest, indicating that M-phase cyclin levels require strict temporal oscillation — unlike flowering plants where multiple redundant CYCB paralogs buffer this control."
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

# MpCYCB;1

## Summary

MpCYCB;1 is the B-type cyclin in *Marchantia polymorpha* (common liverwort) and the **sole G2/M-phase-dominant cyclin** in its minimalist cell cycle system. Single-cell RNA-seq of the vegetative gametophyte (thallus) revealed that MpCYCB;1 expression is specific to the G2/M phase (mitotic entry), with clean temporal boundaries separating it from G1 (MpCYCD;1) and S (MpCYCA) phases. Live fluorescent reporter imaging confirmed M-phase-specific protein dynamics, including characteristic mitotic localization patterns. Overexpression of MpCYCB;1 causes growth arrest — the same phenotype as MpCYCA OE — indicating that M-phase cyclin levels, like S-phase levels, must oscillate precisely rather than remain constitutively high. Evidence is from Romani & Haseloff et al. (*The Plant Cell*), integrating scRNA-seq with functional overexpression phenotyping (Romani & Haseloff et al., 2025).

---

## Biological Roles

### G2/M Transition and Mitotic Entry — Non-Redundant Regulator

MpCYCB;1 is the single cyclin that dominates the G2/M phase in Marchantia, controlling the critical decision to enter mitosis.

Evidence:
- scRNA-seq: MpCYCB;1 expression specifically enriched in G2/M-phase cells, with clean temporal boundaries
- Live fluorescent reporter: M-phase-specific protein accumulation with characteristic mitotic localization
- Overexpression phenotype: growth arrest (tight temporal control required)

Confidence: **Strong** (scRNA-seq + live imaging converge)

### Growth Arrest Upon Overexpression

Like MpCYCA, constitutive MpCYCB;1 overexpression causes growth cessation. This contrasts with MpCYCD;1, whose overexpression drives proliferation, suggesting that G1 cyclins are permissive for proliferation while S and M cyclins must be temporally restricted.

Evidence:
- Overexpression lines show arrested growth phenotype
- Indicates strict temporal window for CYCB;1 function

Confidence: **Strong** (direct overexpression phenotype)

---

## Expression Pattern

### Tissue
Expressed in proliferating cells of the vegetative thallus (gametophyte), including apical notch meristematic regions and gemma cups.

### Phase Specificity
G2/M-phase-specific — scRNA-seq shows MpCYCB;1 expression marks G2/M cells with minimal overlap with G1 or S phases.

### Protein Dynamics
- G2/M-specific protein accumulation and degradation
- Characteristic subcellular re-localization during mitosis (nuclear envelope breakdown, spindle association)
- Protein turnover critical for mitotic exit

### Evidence
- scRNA-seq of Marchantia thallus (Romani & Haseloff et al., 2025)
- Live fluorescent reporter imaging showing M-phase dynamics

### Caveats
Expression data is from whole-thallus scRNA-seq. Cell-type-specific variation within proliferating populations has not been resolved. Spatial transcriptomics data is not available. The specific CDK partners and degradation machinery (APC/C, cyclin destruction box) have not been characterized in Marchantia.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| G2/M cyclin — non-redundant | Marchantia | Vegetative thallus | scRNA-seq + live reporter | [[plant-cell-cycle-control]] | Strong |
| G2/M specificity (clean temporal boundaries) | Marchantia | Vegetative thallus | scRNA-seq phase assignment | [[cell-cycle-scrna-seq]] | Strong |
| Overexpression → growth arrest | Marchantia | Vegetative thallus | Genetic (OE phenotyping) | [[plant-cell-cycle-control]] | Strong |
| Mitotic subcellular localization | Marchantia | Vegetative thallus | Fluorescent reporter imaging | [[plant-cell-cycle-control]] | Moderate |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| G2/M transition signals | Transcriptional activation at G2/M boundary | Inferred from phase-specific expression pattern | Moderate (mechanism uncharacterized) |
| APC/C-mediated degradation | Ubiquitin-mediated proteolysis at mitotic exit (predicted) | Inferred from conserved eukaryotic mechanism; not directly shown in Marchantia | Low |
| Post-translational control | Protein turnover and subcellular localization restrict activity to M-phase | Fluorescent reporter dynamics | Moderate |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| CDK partners | MpCYCB;1 binds and activates CDKs to drive mitotic entry | Inferred from cyclin-CDK paradigm; specific CDK partners not identified | Low |
| Mitotic machinery | Activation of spindle assembly, chromosome condensation | Implied by mitotic entry function | Low |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| Mitotic exit → MpCYCB;1 degradation | Implied by oscillatory expression; conserved APC/C mechanism predicted | Moderate |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Proliferating thallus cells | G2/M transition and mitotic entry in dividing cells | scRNA-seq | Moderate |
| Not resolved at individual cell-type level | — | — | — |

*Marchantia thallus cell types have not been fully catalogued at single-cell resolution; the scRNA-seq data is organized by cell cycle phase rather than cell type identity.*

---

## Developmental Context

### Vegetative Gametophyte (Thallus)
MpCYCB;1 function demonstrated in the vegetative thallus — the dominant haploid life stage. Proliferating cells in the apical notch and gemma cups express MpCYCB;1 during G2/M.

### Reproductive Stages
Role of MpCYCB;1 in sexual reproductive structures (antheridiophores, archegoniophores) and meiosis not characterized.

---

## Stress or Environmental Context

### Normal Proliferation (Primary Context)
MpCYCB;1 characterized under standard growth conditions; role in mitotic entry under normal cell cycle progression.

### Stress Responses
No data on MpCYCB;1 expression or function under environmental stress. Whether cell cycle arrest under stress involves MpCYCB;1 downregulation is unknown.

---

## Cross-Species Conservation

### Arabidopsis
Arabidopsis has multiple B-type cyclins (CYCB1;1, CYCB1;2, CYCB1;3, CYCB2;1-4, CYCB3;1) with extensive functional redundancy. CYCB1;1 is commonly used as a G2/M marker in Arabidopsis but is not strictly non-redundant. The minimalist MpCYCB;1 represents the ancestral state.

### Other Bryophytes
*Physcomitrium patens* (moss) has more CYCB paralogs than Marchantia, suggesting the single-copy state is unusually reduced.

### Other Eukaryotes
B-type cyclins (mitotic cyclins) are deeply conserved across eukaryotes (animal Cyclin B, yeast Clb1-4). The Marchantia single-copy state is the simplest known among land plants.

### Conservation Assessment: **Ancestral** — The single CYCB in Marchantia represents the predicted ancestral cyclin complement. B-type cyclin expansion in seed plants is derived, though B-type cyclin multiplicity is common across eukaryotes.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Transcriptional (scRNA-seq) | Strong | Single-cell resolution, phase-specific pattern |
| Protein (live reporter) | Strong | Protein dynamics and subcellular localization validated |
| Functional (OE phenotyping) | Strong | Clear overexpression phenotype |
| Biochemical (CDK partners, degradation) | Weak | Not characterized in Marchantia |
| Cross-species | Moderate | Phylogenetic inference; conserved mitotic cyclin function |

**Overall Confidence: High** — MpCYCB;1 G2/M identity and non-redundant function are well-supported by scRNA-seq, live imaging, and overexpression phenotyping. Independent replication, CDK partner identification, and degradation mechanism characterization are needed.

---

## Contradictions and Context Dependence

### Contradiction 1: Single-study dependence
- **Claim**: MpCYCB;1 is the sole G2/M cyclin with clean phase boundaries.
- **Context**: All evidence from one study (Romani & Haseloff et al., 2025). No independent replication.
- **Caveat**: Generality across Marchantia accessions and growth conditions remains tentative.

### Context Dependence
- **Life stage**: Only tested in vegetative gametophyte; sporophyte and meiotic cell cycle regulation unknown.
- **Growth conditions**: Standard laboratory conditions; environmental modulation untested.
- **Genetic background**: Single Marchantia accession.

---

## Open Questions

### Question 1: What CDK partners does MpCYCB;1 use?
- **Why It Matters**: M-phase CDK (CDKB in plants) identification is critical for a complete mechanistic model of mitotic entry in the minimalist system.
- **Missing Evidence**: Co-IP or Y2H identification of CYCB;1-CDK pairs.
- **Suggested Experiment**: Y2H screen of Marchantia CDKs against MpCYCB;1; in vitro kinase assay.

### Question 2: What is the degradation mechanism at mitotic exit?
- **Why It Matters**: CYCB degradation via APC/C is conserved across eukaryotes, but the specific machinery in Marchantia is uncharacterized.
- **Missing Evidence**: APC/C component identification; CYCB destruction box characterization.
- **Suggested Experiment**: Mutagenesis of putative destruction box; co-IP with APC/C components; cycloheximide chase assay.

### Question 3: How does the G2 DNA damage checkpoint interface with MpCYCB;1?
- **Why It Matters**: Understanding whether the minimalist system retains checkpoint control would reveal whether checkpoints are ancestral or derived.
- **Missing Evidence**: DNA damage response in Marchantia; CYCB;1 regulation under genotoxic stress.
- **Suggested Experiment**: DNA damage treatment (bleomycin, HU) + CYCB;1 reporter dynamics; checkpoint gene characterization.

---

## Key References

1. Romani F. & Haseloff J. et al. (2025). A simple cell-cycle control system in Marchantia polymorpha provides a framework for understanding plant cell proliferation. *The Plant Cell*. — [[plant-cell-cycle-control]] — **Primary evidence for all claims on this page.**

---

## Knowledge Graph Links

### Related Genes
- [[mpcycd1]] — G1 cyclin; drives proliferation (upstream in cell cycle)
- [[mpcyca]] — S-phase cyclin; DNA replication (upstream in cell cycle)

### Related Concepts
- [[plant-cell-cycle-control]] — Plant cell cycle regulatory framework
- [[cell-cycle-scrna-seq]] — scRNA-seq methodology for cell cycle analysis

### Related Entities
- [[marchantia-polymorpha]] — Host species
- Evidence: [[snRNA-seq-valid-plant-transcriptomics]]
