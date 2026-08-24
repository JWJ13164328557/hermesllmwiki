# Entity Specification

Version: 2.0

Purpose:

Define how biological entities are represented, updated, evaluated, and connected within the Plant Single-Cell Research Operating System.

Entity pages are not encyclopedic descriptions.

Entity pages are evidence-centered knowledge hubs.

---

# 1. Philosophy

## 1.1 What Is an Entity?

An entity is a biological or research object that repeatedly appears across papers and evidence objects.

Examples:

```text
WOX5
PLT1
SHR
SCR
Quiescent Center
Endodermis
Arabidopsis thaliana
Root Apical Meristem
```

An entity page should answer:

```text
What is known about this object?

What evidence supports that knowledge?

In what biological context is it true?

What remains unknown?
```

---

## 1.2 What an Entity Is Not

An entity page is not:

* a glossary entry
* a Wikipedia-style description
* a paper summary
* a loose collection of notes

It must not simply say:

```text
WOX5 is a transcription factor involved in root development.
```

Instead, it must organize all evidence around:

* biological roles
* expression patterns
* regulatory relationships
* functional evidence
* cross-species conservation
* contradictions
* open questions

---

# 2. Entity Categories

Entities are organized by type:

```text
entities/
├── genes/
├── proteins/
├── pathways/
├── cell-types/
├── tissues/
├── species/
├── datasets/
└── labs/
```

---

# 3. General Entity Metadata

Every entity page must include:

```yaml
---
type: entity

entity_type:

name:
aliases:

summary:

status:
confidence:

updated:

related_papers:
related_evidence:
related_relationships:
related_synthesis:
---
```

---

## 3.1 entity_type Values

Allowed values:

```yaml
entity_type:
  - gene
  - protein
  - pathway
  - cell-type
  - tissue
  - species
  - dataset
  - lab
```

---

## 3.2 Status Values

```yaml
status:
  - seed
  - draft
  - reviewed
  - stable
  - deprecated
```

---

## 3.3 Confidence Values

```yaml
confidence:
  - low
  - medium
  - high
  - mixed
```

Use `mixed` when evidence depends strongly on species, tissue, condition, or method.

---

# 4. Gene Entity Template

Path:

```text
entities/genes/wox5.md
```

---

## Required Sections

```markdown
# Summary

# Biological Roles

# Expression Pattern

# Functional Evidence Matrix

# Regulatory Network

# Cell-Type Associations

# Developmental Context

# Stress or Environmental Context

# Cross-Species Conservation

# Evidence Strength

# Contradictions and Context Dependence

# Open Questions

# Key References

# Knowledge Graph Links
```

---

## 4.1 Summary

One concise paragraph.

Must include:

* main function
* strongest evidence
* known context
* unresolved uncertainty

Example:

```text
WOX5 is a root stem cell niche regulator best supported in Arabidopsis quiescent center maintenance. Evidence is strongest for its role in QC identity and stem-cell organization, while direct downstream targets and cross-species conservation remain incompletely resolved.
```

---

## 4.2 Biological Roles

Group by function.

Example:

```markdown
## Biological Roles

### QC Maintenance

Evidence:
- [[evidence/wox5-maintains-qc-identity]]

Confidence:
Strong

### Stem Cell Organization

Evidence:
- [[evidence/wox5-regulates-root-stem-cell-niche]]

Confidence:
Moderate
```

---

## 4.3 Expression Pattern

Separate observation from interpretation.

```markdown
## Expression Pattern

### Tissue

Root apical meristem

### Cell Type

Quiescent center

### Developmental Stage

Seedling root

### Evidence

- scRNA-seq
- Reporter
- Spatial transcriptomics

### Caveats

Transcript dropout may underestimate expression in scRNA-seq.
```

---

## 4.4 Functional Evidence Matrix

Required table:

```markdown
| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| QC maintenance | Arabidopsis | Root | Mutant + reporter | [[wox5-maintains-qc-identity]] | Strong |
```

---

## 4.5 Regulatory Network

Separate upstream and downstream.

```markdown
## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|

### Co-expression Modules

| Module | Dataset | Evidence | Confidence |
|---|---|---|
```

---

## 4.6 Cell-Type Associations

```markdown
| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Quiescent center | Marker/regulator | [[...]] | Strong |
```

---

## 4.7 Cross-Species Conservation

Required when evidence exists.

```markdown
## Cross-Species Conservation

### Arabidopsis

### Rice

### Maize

### Other Species

### Conservation Assessment

conserved / partially conserved / divergent / unknown
```

---

## 4.8 Contradictions and Context Dependence

Record:

* conflicting claims
* species differences
* tissue differences
* developmental-stage differences
* technology-dependent disagreement

Never delete contradictions.

---

## 4.9 Open Questions

Each open question should include:

```markdown
### Question

### Why It Matters

### Missing Evidence

### Suggested Experiment

### Priority
```

---

# 5. Cell-Type Entity Template

Path:

```text
entities/cell-types/quiescent-center.md
```

---

## Required Sections

```markdown
# Summary

# Defining Features

# Marker Genes

# Functional Roles

# Developmental Origin

# Spatial Location

# Cell-State Heterogeneity

# Regulatory Programs

# Cross-Species Conservation

# Evidence Matrix

# Open Questions
```

---

## 5.1 Defining Features

Separate:

```text
Morphological definition
Molecular definition
Functional definition
Spatial definition
```

---

## 5.2 Marker Genes

```markdown
| Marker | Species | Evidence | Specificity | Caveats |
|---|---|---|---|---|
```

Specificity values:

```text
high
medium
low
context-dependent
```

---

## 5.3 Cell-State Heterogeneity

Required for single-cell studies.

```markdown
## Cell-State Heterogeneity

### Known Substates

### Evidence

### Biological Interpretation

### Alternative Explanations

### Missing Validation
```

---

# 6. Pathway Entity Template

Path:

```text
entities/pathways/shr-scr-pathway.md
```

---

## Required Sections

```markdown
# Summary

# Core Components

# Biological Function

# Input Signals

# Output Effects

# Regulatory Logic

# Tissue and Cell-Type Context

# Evidence Matrix

# Cross-Species Conservation

# Open Questions
```

---

## 6.1 Regulatory Logic

Must describe:

```text
activation
repression
feedback
threshold behavior
gradient behavior
spatial restriction
temporal dynamics
```

---

# 7. Tissue Entity Template

Path:

```text
entities/tissues/root-apical-meristem.md
```

---

## Required Sections

```markdown
# Summary

# Anatomical Definition

# Major Cell Types

# Developmental Zones

# Spatial Organization

# Key Regulatory Programs

# Major Datasets

# Cross-Species Comparison

# Open Questions
```

---

# 8. Species Entity Template

Path:

```text
entities/species/arabidopsis-thaliana.md
```

---

## Required Sections

```markdown
# Summary

# Major Single-Cell Resources

# Major Spatial Resources

# Key Tissues Studied

# Known Regulatory Programs

# Comparison With Other Species

# Knowledge Biases

# Open Questions
```

---

# 9. Entity Update Rules

When ingesting a paper, the Agent must:

1. Identify all entities mentioned in key findings.
2. Create missing entity pages.
3. Update existing entity pages only with traceable evidence.
4. Add new evidence objects before adding claims to entity pages.
5. Update functional evidence matrices.
6. Update regulatory relationships.
7. Add contradictions instead of overwriting old claims.
8. Update `updated` date.
9. Add links to related papers and evidence.
10. Log all changes.

---

# 10. Entity Completion Criteria

An entity page is complete only if it contains:

* summary
* biological role
* evidence matrix
* biological scope
* relationship links
* contradiction tracking
* open questions
* source-backed claims
* knowledge graph links

Without evidence links, an entity page is incomplete.
