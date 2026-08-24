---
type: entity
entity_type: cell-type
name: "Quiescent Center"
aliases: ["QC", "静止中心"]
summary: "The quiescent center is a small group of mitotically inactive cells at the root apical meristem that functions as the organizing center of the stem cell niche, maintaining surrounding initial cells through short-range signals."
status: reviewed
confidence: high
updated: "2026-05-29"
related_papers:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[xr-10-1016-j-devcel-2022-01-008]]"
related_evidence:
  - "[[qc-cells-transcriptionally-distinct]]"
  - "[[arabidopsis-root-has-15-cell-types]]"
related_synthesis: []
---

# Quiescent Center (QC)

## Summary

The QC is a group of ~4 mitotically inactive cells at the heart of the Arabidopsis root apical meristem. It functions as the **stem cell niche organizer**, maintaining surrounding initial cells that give rise to all root tissues. QC identity is marked by WOX5 expression and requires auxin minimum and local signaling.

---

## Defining Features

| Feature | Description |
|---------|-------------|
| **Morphological** | Small, densely cytoplasmic cells; ~4 cells in Arabidopsis |
| **Molecular** | WOX5+, PLT1+, auxin minimum |
| **Functional** | Maintains surrounding stem cells; rarely divides |
| **Spatial** | Center of root apical meristem, surrounded by initial cells |

---

## Marker Genes

| Marker | Species | Evidence | Specificity | Caveats |
|--------|---------|----------|-------------|---------|
| WOX5 | Arabidopsis | scRNA-seq + reporter | high | Also expressed in embryo |
| PLT1 | Arabidopsis | scRNA-seq + reporter | medium | Broader stem cell niche expression |
| AGL42 | Arabidopsis | scRNA-seq | medium | scRNA-seq derived |

---

## Functional Roles

| Role | Evidence Object | Confidence |
|------|----------------|------------|
| Stem cell niche organization | — | Strong (genetic) |
| Maintenance of surrounding initials | — | Strong (genetic) |
| Quiescence enforcement | — | Moderate |

---

## Cell-State Heterogeneity

### Known Substates
Recent scRNA-seq studies suggest QC cells may not be homogeneous — some studies detect transcriptional heterogeneity within the QC population.

### Evidence
- [[qc-cells-transcriptionally-distinct]] — QC forms a distinct cluster but may contain substates
- [[xr-10-1016-j-devcel-2022-01-008]] — Optimal transport analysis shows QC as trajectory origin

### Biological Interpretation
QC heterogeneity may reflect dynamic cell states (quiescence depth, readiness to divide upon stress)

### Alternative Explanations
- Technical noise in low-abundance transcripts from rare cell populations
- Protoplasting-induced transcriptional changes

---

## Cross-Species Conservation

| Species | QC Presence | Key Regulator | Evidence |
|---------|-------------|---------------|----------|
| Arabidopsis | Yes | WOX5 | Multiple studies |
| Rice | Probable | OsWOX5 (putative) | Limited |
| Maize | Probable | Unknown | Limited |

### Conservation Assessment: **Partially conserved** — QC exists across angiosperms but molecular characterization limited to Arabidopsis.

---

## Open Questions

### Question 1: QC heterogeneity — functional or technical?
- **Why It Matters**: If QC contains functional substates, the niche organization model needs revision
- **Missing Evidence**: Spatial transcriptomics at single-cell resolution
- **Suggested Experiment**: Stereo-seq of root tip + QC-specific lineage tracing

### Question 2: What signals maintain QC quiescence?
- **Why It Matters**: Understanding quiescence regulation could enable controlled cell division for regeneration
- **Missing Evidence**: Direct signaling pathway characterization
- **Suggested Experiment**: Single-cell receptor-ligand analysis + genetic perturbation
