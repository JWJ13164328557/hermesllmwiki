# Hermes Agent Operational Protocol

Version: 1.0

Purpose:

Define the operational workflow for Hermes Agent when maintaining the Plant Single-Cell Research Operating System.

This protocol ensures that literature ingestion produces traceable, reusable, and synthesis-ready knowledge.

---

# 1. Core Principle

Hermes Agent must never treat a paper as the final knowledge unit.

A paper is only the entry point.

The required transformation is:

```text
Raw Literature
    ↓
Paper Page
    ↓
Evidence Objects
    ↓
Entity Updates
    ↓
Relationship Updates
    ↓
Synthesis Updates
    ↓
Hypothesis Updates
    ↓
Research Program Updates
```

---

# 2. Global Rules

Hermes Agent must always:

1. Preserve source traceability.
2. Distinguish observation from interpretation.
3. Distinguish correlation from mechanism.
4. Distinguish hypothesis from consensus.
5. Preserve contradictions.
6. Avoid unsupported generalization.
7. Update knowledge incrementally.
8. Log all modifications.
9. Prefer wikilinks over plain text names.
10. Never modify `raw/`.

---

# 3. Ingest Workflow

## Step 1. Read Raw Literature

Input:

```text
raw/articles/*.md
```

Actions:

* identify title, DOI, PMID, journal, year
* identify biological system
* identify methods
* identify main figures
* identify key claims
* identify datasets
* identify major entities

Output:

```text
paper draft
```

---

## Step 2. Create Paper Page

Path:

```text
papers/{year}-{first-author}-{short-title}.md
```

Paper page must follow:

```text
Paper Analysis Specification
```

Minimum required sections:

* metadata
* scientific context
* research questions
* experimental logic
* figure analysis
* evidence extraction
* knowledge extraction
* critical evaluation
* research insight
* future opportunities

---

## Step 3. Extract Evidence Objects

For each key claim:

1. Determine whether the claim is atomic.
2. Determine claim type.
3. Determine biological scope.
4. Identify supporting figures.
5. Assign evidence quality.
6. Check whether a matching evidence object already exists.
7. Create or update evidence page.

Path:

```text
evidence/{claim-slug}.md
```

---

## Step 4. Update Entities

For every entity involved in the paper:

* gene
* protein
* pathway
* cell type
* tissue
* species
* dataset
* lab

Actions:

1. Create missing entity page.
2. Add evidence-backed claims.
3. Update evidence matrix.
4. Add expression pattern only if supported.
5. Add functional role only if supported.
6. Add contradictions when present.
7. Add open questions when unresolved.

---

## Step 5. Update Relationships

For every entity-to-entity relationship:

```text
Entity A
    ↓
relationship
Entity B
```

Actions:

1. Identify relationship type.
2. Determine context.
3. Determine evidence support.
4. Determine confidence.
5. Create or update relationship page.

Supported relationship types:

```text
activates
represses
interacts_with
expressed_in
marks
required_for
sufficient_for
correlates_with
maintains
promotes
inhibits
```

---

## Step 6. Update Synthesis Pages

If the paper affects a broader topic, update relevant synthesis pages.

Examples:

```text
synthesis/root-stem-cell-niche.md
synthesis/cell-fate-transition.md
synthesis/spatial-patterning.md
```

Update:

* current consensus
* evidence synthesis
* regulatory network
* competing models
* knowledge gaps
* future directions

Do not update synthesis with weak claims unless clearly labeled as emerging or speculative.

---

## Step 7. Update Hypotheses

If the paper suggests a testable hypothesis:

1. Create hypothesis page if new.
2. Link supporting evidence.
3. Define prediction.
4. Define validation experiment.
5. Define failure condition.
6. Assign priority.

Path:

```text
hypotheses/{hypothesis-slug}.md
```

---

## Step 8. Update Research Programs

If the paper affects a long-term research agenda:

* update knowledge map
* update hypothesis portfolio
* update critical gaps
* update experimental roadmap
* update dataset roadmap
* update milestone status

Path:

```text
research-programs/{program-slug}.md
```

---

## Step 9. Update Index and Log

Always update:

```text
index.md
log.md
```

Log entry must include:

```markdown
## YYYY-MM-DD

### Added

### Updated

### Evidence Created

### Entity Updates

### Relationship Updates

### Synthesis Updates

### Open Questions
```

---

# 4. Claim Classification Protocol

Hermes must classify every extracted claim.

## Observation

Directly observed result.

Example:

```text
WOX5 transcripts are enriched in QC cells.
```

## Association

Correlation or co-occurrence.

Example:

```text
WOX5 expression correlates with QC identity.
```

## Function

Perturbation-supported biological role.

Example:

```text
WOX5 is required for QC maintenance.
```

## Mechanism

Causal relationship with mechanistic support.

Example:

```text
WOX5 directly activates PLT1.
```

## Hypothesis

Testable but unresolved claim.

Example:

```text
WOX5 may directly regulate PLT1.
```

---

# 5. Confidence Upgrade Rules

Hermes may upgrade confidence only when evidence improves.

## Low to Medium

Allowed when:

* multiple observations exist
* or one functional experiment exists

## Medium to High

Allowed when:

* independent studies support the claim
* multiple methods support the claim
* contradictions are absent or context-resolved

## High to Consensus

Allowed when:

* independent replication exists
* mechanistic or functional validation exists
* synthesis page supports consensus

---

# 6. Contradiction Handling

When contradiction appears:

Hermes must not overwrite the older claim.

Instead:

1. Add contradiction to evidence page.
2. Add context difference.
3. Add technical difference.
4. Add note to synthesis page.
5. Add unresolved question if needed.

Contradiction types:

```text
direct
contextual
technical
interpretational
```

---

# 7. Anti-Hallucination Rules

Hermes must never:

* infer a mechanism from correlation without labeling it
* generalize Arabidopsis findings to all plants without evidence
* treat scRNA-seq expression as functional proof
* treat trajectory inference as lineage proof
* treat co-expression as direct regulation
* treat discussion speculation as established fact
* create unsupported consensus
* delete minority evidence

---

# 8. Minimum Output Per Paper

For each ingested paper, Hermes must produce or update:

```text
1 paper page
3–20 evidence objects
all relevant entity pages
all relevant relationship pages
at least one synthesis page if topic-relevant
log.md
index.md
```

If fewer than 3 evidence objects are produced, Hermes must explain why.

---

# 9. Quality Gates

A paper ingest is complete only when:

* Paper page follows Paper Specification
* All major figures are analyzed
* Key claims are converted to Evidence Objects
* Entities are linked
* Relationships are extracted
* Contradictions are checked
* Synthesis pages are updated when relevant
* Open questions are recorded
* Index and log are updated

---

# 10. Final Rule

Hermes must always preserve the chain:

```text
Claim
    ↓
Evidence Object
    ↓
Paper Page
    ↓
Raw Literature
```

If this chain is broken, the knowledge cannot be accepted.
