# Hermes Agent Instructions for Plant Single-Cell Knowledge Base

## 1. Core Mission

Hermes maintains this knowledge base as a research knowledge system, not as a simple literature note repository.

The goal is to transform:

```text
Raw Literature
    ↓
Paper Analysis
    ↓
Evidence Objects
    ↓
Entity Knowledge
    ↓
Relationships
    ↓
Synthesis
    ↓
Hypotheses
    ↓
Research Programs
```

Every update must preserve source traceability.

---

## 2. Mandatory Reading Before Any Task

Before modifying the knowledge base, Hermes must read:

```text
wiki/schema.md
wiki/schema/paper-specification.md
wiki/schema/evidence-specification.md
wiki/schema/entity-specification.md
wiki/schema/synthesis-specification.md
wiki/schema/research-program-specification.md
wiki/schema/hermes-agent-operational-protocol.md
```

If any file is missing, Hermes must report it before proceeding.

---

## 3. Golden Rule

No knowledge may be added unless it can be traced through:

```text
Claim
    ↓
Evidence Object
    ↓
Paper Page
    ↓
Raw Literature
```

Unsupported statements are not allowed.

Hypotheses must be clearly marked as hypotheses.

Interpretations must not be stored as facts.

---

## 4. Ingest Rule

When ingesting a paper, Hermes must not only summarize it.

Hermes must create or update:

```text
papers/
evidence/
entities/
relationships/
synthesis/
hypotheses/
research-programs/
index.md
log.md
```

At minimum, every paper ingest must produce:

* one detailed paper page
* multiple evidence objects
* updated entity pages
* updated relationship pages
* updated log entry

---

## 5. Paper Analysis Standard

Every paper page must include:

```text
Metadata
Scientific Context
Research Questions
Experimental Logic
Figure-by-Figure Analysis
Evidence Extraction
Knowledge Graph Extraction
Critical Evaluation
Research Insight
Future Research Opportunities
```

A paper page is incomplete if it only contains a summary.

---

## 6. Evidence Standard

Every major claim must become an Evidence Object.

One evidence page equals one scientific claim.

Each Evidence Object must include:

```text
Claim
Biological Context
Supporting Evidence
Evidence Quality
Contradictory Evidence
Consensus Assessment
Alternative Models
Open Questions
Next Critical Experiment
```

---

## 7. Entity Standard

Entity pages are evidence hubs, not encyclopedia pages.

When updating an entity, Hermes must include:

```text
Biological Roles
Expression Pattern
Functional Evidence Matrix
Regulatory Network
Cell-Type Associations
Cross-Species Conservation
Contradictions
Open Questions
Knowledge Graph Links
```

---

## 8. Synthesis Standard

Synthesis pages must answer:

```text
What does the field currently believe?
```

They must include:

```text
Historical Evolution
Current Consensus
Core Biological Questions
Evidence Synthesis
Regulatory Network
Competing Models
Knowledge Gaps
Future Directions
Hypotheses
Research Program Links
```

---

## 9. Research Program Standard

Research Program pages must answer:

```text
What should we do next?
```

They must include:

```text
Problem Definition
Big Questions
Knowledge Map
Hypothesis Portfolio
Critical Knowledge Gaps
Experimental Roadmap
Dataset Roadmap
Technology Roadmap
Risk Assessment
Milestones
Impact Analysis
```

---

## 10. Anti-Hallucination Rules

Hermes must never:

* infer mechanism from correlation without labeling it
* treat scRNA-seq expression as functional proof
* treat trajectory inference as lineage proof
* treat co-expression as direct regulation
* generalize Arabidopsis findings to all plants without evidence
* convert speculation into consensus
* delete contradictory evidence
* modify raw/ files

---

## 11. Logging Rule

Every operation must update:

```text
wiki/log.md
```

Each log entry must include:

```markdown
## YYYY-MM-DD

### Added

### Updated

### Evidence Created

### Entities Updated

### Relationships Updated

### Synthesis Updated

### Open Questions

### Notes
```

---

## 12. Final Check Before Completion

Before finishing any task, Hermes must verify:

* all new claims have sources
* all evidence links resolve
* all entity pages are linked
* all contradictions are preserved
* index.md is updated
* log.md is updated
* no raw/ file was modified

If any check fails, Hermes must report the incomplete items.
