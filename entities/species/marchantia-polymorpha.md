---
type: entity
entity_type: species
name: "Marchantia polymorpha"
aliases: ["地钱", "common liverwort", "M. polymorpha"]
summary: "Marchantia polymorpha is a thalloid liverwort and early-diverging land plant that serves as a minimalist model for plant cell cycle regulation. Its non-redundant core cell cycle gene set — MpCYCD;1 (G1), MpCYCA (S), MpCYCB;1 (G2/M) — enables clean dissection of cyclin-CDK logic without the paralog redundancy of flowering plants."
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

# Marchantia polymorpha

## Summary

*Marchantia polymorpha* (common liverwort) is a bryophyte model organism that occupies a key phylogenetic position as an early-diverging land plant. It is distinguished by a streamlined, non-redundant genome with single-copy core gene families, making it uniquely suited for dissecting fundamental plant biology without paralog interference. Its most distinctive feature is the **minimalist cell cycle system**: only three core cyclins (MpCYCD;1 for G1, MpCYCA for S, MpCYCB;1 for G2/M) control the entire cell division cycle, in contrast to the dozens of cyclins in flowering plants. Single-cell RNA-seq combined with live fluorescent reporter imaging has validated the temporal specificity and non-redundant function of each cyclin (Romani & Haseloff et al., *The Plant Cell*). Its haploid-dominant life cycle and ease of genetic manipulation further enhance its value as an experimental system.

---

## Major Single-Cell Resources

### scRNA-seq of Vegetative Gametophyte (Thallus)

| Resource | Description | Evidence Object |
|---|---|---|
| Marchantia thallus scRNA-seq | Single-cell transcriptome of vegetative gametophyte capturing cell cycle phases | [[cell-cycle-scrna-seq]] |

Key findings from scRNA-seq:
- Cell cycle genes show phase-specific expression with minimal overlap between phases
- Each cell cycle phase is dominated by a single cyclin
- Transcriptional profiles validate the non-redundant model
- Combined with live fluorescent reporters for protein-level validation

### Methodological Integration
- **scRNA-seq + live imaging**: Transcript-level phase assignment validated by protein-level fluorescent reporter dynamics
- **Protein turnover analysis**: Cyclin protein stability and subcellular localization complement mRNA data
- **Overexpression phenotyping**: Functional validation of each cyclin's role

---

## Major Spatial Resources

*No dedicated spatial transcriptomics datasets currently available for Marchantia. The gemma cup and thallus architecture are amenable to spatial approaches but remain unexplored at spatially-resolved transcriptomic resolution.*

---

## Key Tissues Studied

| Tissue | Description | Key Findings | Evidence |
|---|---|---|---|
| Vegetative thallus | Main photosynthetic body; haploid gametophyte | Contains proliferating cells with active cell cycle; scRNA-seq reveals cell cycle phase populations | [[cell-cycle-scrna-seq]] |
| Gemma cups | Asexual reproductive structures on thallus surface | Source of clonal propagules; active cell proliferation | [[plant-cell-cycle-control]] |
| Apical notch | Meristematic region at thallus tip | Site of active cell division; MpCYCD;1-driven proliferation | [[plant-cell-cycle-control]] |

---

## Known Regulatory Programs

### Minimalist Cell Cycle Control

The defining regulatory program of Marchantia is its simplified cell cycle:

| Phase | Cyclin | Function | Overexpression Phenotype |
|---|---|---|---|
| G1 | [[mpcycd1]] | Drives cell cycle re-entry; promotes proliferation and dedifferentiation | Enhanced proliferation |
| S | [[mpcyca]] | S-phase progression | Growth arrest |
| G2/M | [[mpcycb1]] | G2/M transition; mitotic entry | Growth arrest |

### Regulatory Logic
- **Non-redundant**: Each phase controlled by a single cyclin (no paralog compensation)
- **Temporal specificity**: Phase transitions have limited overlap; clean boundaries
- **Dual regulation**: Transcriptional control (mRNA) + post-translational control (protein turnover, subcellular localization) together maintain phase fidelity

### MpCYCD;1 as Proliferation Gatekeeper
- Overexpression sufficient to drive cell cycle re-entry
- Promotes proliferation and dedifferentiation
- Unlike MpCYCA/MpCYCB;1 overexpression (which causes arrest), MpCYCD;1 acts as a positive proliferation driver

---

## Comparison With Other Species

### Arabidopsis thaliana
- **Cyclin complexity**: Arabidopsis has ~50 cyclin genes with extensive redundancy; Marchantia has a compact set
- **Cell cycle analysis**: Paralog redundancy in Arabidopsis complicates functional dissection; Marchantia enables clean single-gene analysis
- **Life cycle**: Arabidopsis is diploid-dominant; Marchantia is haploid-dominant, simplifying genetic analysis

### Other Bryophytes
- *Physcomitrium patens* (moss): Also has a relatively streamlined genome but with more cyclin paralogs than Marchantia
- Marchantia represents the most reduced, ancestral-like state among experimentally tractable land plants

### Seed Plants
- Seed plant cyclin-CDK complexity is a **derived feature**; Marchantia retains the ancestral simplicity
- The minimalist Marchantia system provides a **prototype** for engineering simplified growth control in crops

---

## Knowledge Biases

### Well-Characterized
- Cell cycle gene complement and phase-specific expression
- Gemma-based clonal propagation and transformation
- Phylogenetic position as early-diverging land plant

### Under-Characterized
- Spatial transcriptomics of thallus development
- Environmental stress responses (cold, drought, heat) at single-cell resolution
- Hormonal signaling networks beyond auxin/cytokinin
- Cell-type atlas of the full thallus (only cell cycle phases profiled)
- Comparison with other Marchantia species (M. paleacea, M. polymorpha subspecies)
- Root/rhizoid development at single-cell level

---

## Open Questions

### Question 1: How is the minimalist cell cycle wired at the cis-regulatory level?

- **Why It Matters**: Understanding how three cyclins are temporally regulated with clean phase transitions could reveal fundamental principles of cell cycle control.
- **Missing Evidence**: Promoter/enhancer analysis of MpCYCD;1, MpCYCA, MpCYCB;1; transcription factors driving phase transitions.
- **Suggested Experiment**: ATAC-seq + ChIP-seq across cell cycle phases; identify master TFs for each cyclin.

### Question 2: Does the minimalist cell cycle model hold in all Marchantia tissues?

- **Why It Matters**: scRNA-seq was performed on whole thalli; tissue-specific cell cycle regulation (e.g., in gemma cups vs. apical notch vs. rhizoids) may differ.
- **Missing Evidence**: Tissue-specific or spatially-resolved cell cycle profiling.
- **Suggested Experiment**: Spatial transcriptomics of thallus cross-sections; tissue-specific cell cycle reporter lines.

### Question 3: How evolutionarily stable is the minimalist cyclin set?

- **Why It Matters**: Understanding why Marchantia retained a minimalist set while seed plants expanded cyclins can illuminate the evolutionary pressures driving gene family expansion.
- **Missing Evidence**: Genome-wide cyclin-CDK surveys across Marchantiophyta (liverworts) and hornworts.
- **Suggested Experiment**: Comparative genomics of cyclin-CDK families across 20+ bryophyte genomes.

### Question 4: Can the minimalist system be ported to crops for growth engineering?

- **Why It Matters**: If the Marchantia cyclin logic is portable, it could simplify growth control engineering in crops.
- **Missing Evidence**: Heterologous expression of Marchantia cyclins in Arabidopsis/rice; functional complementation.
- **Suggested Experiment**: Express MpCYCD;1 in Arabidopsis cycd triple mutant; assess rescue and proliferation phenotypes.

---

## Key References

1. Romani F. & Haseloff J. et al. (2025). A simple cell-cycle control system in Marchantia polymorpha provides a framework for understanding plant cell proliferation. *The Plant Cell*. — [[plant-cell-cycle-control]] — **Primary single-cell and cell cycle evidence.**

2. [[cell-cycle-scrna-seq]] — Single-cell RNA-seq methodological application in Marchantia.

---

## Knowledge Graph Links

### Related Genes
- [[mpcycd1]] — G1 cyclin; drives proliferation and cell cycle re-entry
- [[mpcyca]] — S-phase cyclin
- [[mpcycb1]] — G2/M cyclin; mitotic entry

### Related Concepts
- [[plant-cell-cycle-control]] — Plant cell cycle regulatory framework
- [[cell-cycle-scrna-seq]] — Single-cell RNA-seq for cell cycle analysis

### Related Entities
- Cell cycle evidence: [[snRNA-seq-valid-plant-transcriptomics]]
