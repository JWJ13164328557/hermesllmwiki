# Evidence Specification

Version: 1.0

Purpose:

Define how scientific claims are represented, evaluated, tracked, and synthesized across publications.

This specification is the foundation of the knowledge graph layer.

---

# 1 Philosophy

## 1.1 What Is Evidence?

Evidence is not a paper.

Evidence is not a figure.

Evidence is not an entity.

Evidence is:

```text
A Scientific Claim
+
Supporting Observations
+
Supporting Experiments
```

Example:

```text
WOX5 maintains QC identity
```

This is an Evidence Object.

---

## 1.2 Why Evidence Exists

Papers are temporary.

Knowledge persists.

The same biological claim may appear in:

* multiple papers
* multiple species
* multiple technologies

Evidence aggregates all support for a claim.

---

## 1.3 One Evidence = One Claim

Correct:

```text
WOX5 maintains QC identity

PLT1 promotes stem cell maintenance

QC contains transcriptionally distinct states
```

Incorrect:

```text
Root development regulation
```

Too broad.

Evidence must be atomic.

---

# 2 Evidence Hierarchy

Scientific claims are organized into levels.

---

## Level 1 Observation

Direct observation.

Example:

```text
WOX5 transcripts enriched in QC cells.
```

No interpretation.

---

## Level 2 Association

Observed relationship.

Example:

```text
WOX5 expression correlates with QC identity.
```

---

## Level 3 Functional Relationship

Perturbation evidence exists.

Example:

```text
WOX5 is required for QC maintenance.
```

---

## Level 4 Mechanistic Relationship

Causal mechanism identified.

Example:

```text
WOX5 directly regulates PLT1.
```

---

## Level 5 Consensus

Supported by multiple independent studies.

Example:

```text
WOX5 is a core regulator of QC maintenance.
```

---

# 3 Evidence Object Template

## Metadata

```yaml
---
type: evidence

claim:

claim_type:

status:

consensus_level:

confidence:

updated:
---
```

---

## Claim

Single scientific statement.

Example:

```text
WOX5 maintains QC identity
```

---

## Claim Type

Allowed:

```yaml
claim_type:
  observation
  association
  function
  mechanism
  consensus
```

---

## Biological Scope

Must specify context.

```yaml
species:

tissue:

cell_type:

development_stage:

condition:
```

---

Example:

```yaml
species:
  arabidopsis-thaliana

tissue:
  root

cell_type:
  quiescent-center
```

---

# 4 Evidence Sources

Every claim must have source papers.

---

## Supporting Papers

Format:

```yaml
support:
  - [[paper-a]]
  - [[paper-b]]
```

---

## Supporting Figures

Format:

```yaml
supporting_figures:
  - paper-a#figure-2
  - paper-b#figure-4
```

---

## Supporting Experiments

Examples:

```yaml
experiments:
  - scRNA-seq
  - reporter
  - knockout
  - lineage-tracing
```

---

# 5 Evidence Quality Assessment

Purpose:

Determine reliability.

---

## Tier 1

Mechanistic Proof

Examples:

```text
ChIP

CUT&Tag

Reporter Validation

Genetic Rescue
```

Highest confidence.

---

## Tier 2

Functional Validation

Examples:

```text
Mutant phenotype

Overexpression

Knockdown
```

---

## Tier 3

Spatial Support

Examples:

```text
Spatial Transcriptomics

ISH

Reporter
```

---

## Tier 4

Correlative Evidence

Examples:

```text
scRNA-seq

Co-expression

Trajectory inference
```

---

## Tier 5

Speculative

Examples:

```text
Discussion-only claims
```

Not allowed as consensus.

---

# 6 Evidence Strength Score

Calculate:

```text
Evidence Strength
=
Quality
+
Replication
+
Independence
```

---

## Weak

Single paper.

Single method.

---

## Moderate

Multiple experiments.

Single group.

---

## Strong

Multiple groups.

Multiple methods.

---

## Established

Independent replication.

Mechanistic support.

Consensus exists.

---

# 7 Contradiction Tracking

Evidence must record disagreement.

---

## Contradictory Papers

```yaml
contradictions:
  - [[paper-x]]
```

---

## Contradiction Type

```yaml
contradiction_type:
  direct
  contextual
  technical
```

---

### Direct

Claims opposite conclusion.

---

### Contextual

Different species.

Different tissue.

---

### Technical

Different methodology.

---

# 8 Consensus Assessment

Purpose:

Measure field agreement.

---

## Consensus Levels

### Emerging

1–2 papers.

---

### Moderate

Several supporting studies.

---

### Strong

Independent replication.

---

### Established

Widely accepted.

Textbook-level.

---

### Controversial

Significant disagreement.

---

# 9 Alternative Models

Science is not linear.

Every evidence object must include:

```markdown
# Alternative Explanations
```

Example:

```text
Observation:

WOX5 expressed in QC

Interpretation A:

Maintains QC identity

Interpretation B:

Marker only
```

Store both.

---

# 10 Evidence Timeline

Track historical evolution.

---

## Initial Observation

First report.

---

## Validation

Functional confirmation.

---

## Mechanistic Resolution

Causal explanation.

---

## Consensus Formation

Community agreement.

---

Example:

```text
2004
WOX5 identified

2011
Functional validation

2018
Regulatory mechanism

2026
Spatial confirmation
```

---

# 11 Cross-Species Evidence

Required whenever possible.

---

## Arabidopsis

Evidence summary.

---

## Rice

Evidence summary.

---

## Maize

Evidence summary.

---

## Conservation Assessment

```yaml
conservation:
  conserved
  partially-conserved
  unknown
  divergent
```

---

# 12 Knowledge Graph Integration

Every Evidence Object must generate graph edges.

---

## Source Entity

Example:

```text
WOX5
```

---

## Target Entity

Example:

```text
QC identity
```

---

## Relationship

Example:

```text
maintains
```

---

Graph:

```text
WOX5
 ↓
maintains
 ↓
QC identity
```

---

# 13 Open Questions

Every Evidence Object must end with:

---

## What Is Known?

---

## What Is Missing?

---

## What Is Controversial?

---

## What Experiment Would Resolve It?

---

# 14 Evidence Lifecycle

Evidence evolves.

---

## Seed

Single observation.

---

## Emerging

Initial support.

---

## Validated

Functional evidence.

---

## Mechanistic

Mechanism established.

---

## Consensus

Field agreement.

---

## Deprecated

Superseded by stronger evidence.

Never delete.

---

# 15 Agent Rules

The Agent must:

1. Separate observation from interpretation
2. Separate mechanism from correlation
3. Track contradictions
4. Preserve minority evidence
5. Update consensus level
6. Record evidence quality
7. Track historical evolution
8. Link all evidence to source papers
9. Generate graph relationships
10. Never upgrade confidence without evidence

---

# 16 Final Output

Every Evidence Object must contain:

## Claim

## Biological Context

## Supporting Evidence

## Evidence Quality

## Contradictory Evidence

## Consensus Assessment

## Historical Timeline

## Alternative Models

## Knowledge Graph Relationships

## Open Questions

## Next Critical Experiment

Without these sections, the Evidence Object is incomplete.

```
```
