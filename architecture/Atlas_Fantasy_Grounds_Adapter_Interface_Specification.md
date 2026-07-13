# Atlas Fantasy Grounds Adapter Interface Specification

**Version:** 0.1  
**Status:** Draft  
**Owner:** Atlas Discovery Engine  
**Primary Source System:** Fantasy Grounds Unity  
**Future Source Systems:** Deferred

---

## Purpose

This document defines the first adapter interface for Atlas Core, focused on **Fantasy Grounds Unity** as the primary source system.

The goal is not to create a universal adapter framework yet.

The goal is to build a clean, reliable Fantasy Grounds adapter that produces Atlas Discovery artifacts without locking Atlas permanently to Fantasy Grounds.

---

## Scope

This specification applies to:

- Fantasy Grounds campaign `db.xml`
- Fantasy Grounds-style XML structures
- Discovery Registry generation
- Discovery Report generation
- Source fingerprint extraction

This specification does **not** apply yet to:

- D&D Beyond
- Foundry VTT
- Roll20
- PDFs
- Website publication
- Character Object validation
- Synchronization

Those systems may be considered later, but they are not part of the current implementation focus.

---

## Guiding Principle

> Build for Fantasy Grounds now. Avoid decisions that make other adapters impossible later.

Atlas should remain grounded in the real source system currently in use: Fantasy Grounds.

Future compatibility is preserved through clean boundaries, not premature abstraction.

---

## Adapter Responsibility

The Fantasy Grounds Adapter has one responsibility:

> Convert Fantasy Grounds source data into Atlas Discovery artifacts.

It does not interpret campaign meaning.

It does not build Atlas Character Objects.

It does not validate mechanics.

It does not synchronize with websites.

It does not modify the Fantasy Grounds source file.

---

## Input

Primary input:

```text
Fantasy Grounds db.xml
```

Optional future inputs:

```text
Fantasy Grounds module XML
Fantasy Grounds export XML
Fantasy Grounds campaign folder
```

Only `db.xml` is required for Sprint 0.

---

## Output

The adapter produces:

```text
Discovery Registry
Discovery Report
Source Fingerprint
Warnings
Unknown Object Records
```

The adapter does not produce:

```text
Atlas Character Object
HTML
Website content
Synchronization map
Mechanical validation result
```

---

## Adapter Boundary

The adapter boundary is intentionally narrow.

```text
Fantasy Grounds db.xml
        │
        ▼
Fantasy Grounds Adapter
        │
        ▼
Discovery Registry
        │
        ▼
Atlas Core
```

Everything above the adapter is source-specific.

Everything below the adapter should be source-neutral whenever practical.

---

## Required Adapter Operations

### 1. Load Source

The adapter must load the Fantasy Grounds XML file.

It should verify:

- File exists
- File is readable
- XML is well-formed
- Root node can be identified

Failure to load the source is a blocking error.

---

### 2. Fingerprint Source

The adapter should identify available source-level metadata.

Possible fields include:

```yaml
source_system: Fantasy Grounds Unity
source_format: XML
ruleset: 5E
campaign_name: unknown or discovered
root_node: root
file_name: db.xml
```

The adapter must not guess metadata that cannot be discovered.

If a field cannot be determined, it should be marked as unknown.

---

### 3. Scan Structure

The adapter must walk the XML tree and record structural information.

For each discovered node type, record:

```yaml
node_name:
path:
occurrence_count:
parent_path:
child_node_names:
has_text_value:
has_attributes:
```

The scan must be deterministic.

Given the same source file, the same registry should be produced.

---

### 4. Identify Collections

The adapter should identify probable collections based on structure.

Examples:

```text
charsheet
npc
item
image
story
encounter
quest
parcel
```

This is structural identification only.

The adapter may say:

```text
A collection-like node named charsheet exists.
```

It may not say:

```text
This is the official player character list and Mantis is valid.
```

That belongs to Object Discovery and Validation.

---

### 5. Record Unknowns

Unknown structures must be recorded, not ignored.

Each unknown record should include:

```yaml
node_name:
path:
occurrence_count:
parent_path:
example_children:
notes:
```

Unknown nodes are not failures.

They are discovery results.

---

### 6. Produce Discovery Registry

The adapter must produce the internal Discovery Registry described in the Sprint 0 Registry Specification.

The registry is the machine-readable output of discovery.

---

### 7. Produce Discovery Report

The adapter must produce the human-readable Discovery Report described in the Discovery Report Specification.

The report is for review, debugging, and trust-building.

---

## Non-Responsibilities

The Fantasy Grounds Adapter must not:

- Calculate ability modifiers
- Validate spell save DCs
- Determine source ownership of character fields
- Decide whether a character is complete
- Normalize race, class, item, or spell names
- Generate website pages
- Compare revisions
- Modify `db.xml`
- Infer missing mechanical values
- Interpret narrative meaning

These responsibilities belong to later Atlas Core stages.

---

## Mantis Sprint Relationship

Sprint 1 remains focused on producing one Verified Atlas Character Object for Mantis.

However, Sprint 1 should not begin by directly parsing Mantis.

The correct sequence is:

```text
Sprint 0:
Discover Fantasy Grounds source
Produce Discovery Registry
Produce Discovery Report

Sprint 1:
Use Discovery Registry
Locate Mantis candidate record
Extract raw character data
Build Atlas Character Object
Validate Character Object
```

This prevents Mantis parsing from becoming tightly coupled to raw XML traversal.

---

## Fantasy Grounds First Policy

For the current phase, Atlas may use Fantasy Grounds-specific knowledge where useful.

Examples:

- Common Fantasy Grounds node names
- Known 5E ruleset structures
- `charsheet` as a likely character collection
- `npc`, `item`, `image`, and `story` as known table-like structures

However, that knowledge should remain inside the Fantasy Grounds Adapter.

Atlas Core should consume the Discovery Registry rather than reaching back into Fantasy Grounds XML.

---

## Future Adapter Readiness

Atlas is not required to support other source systems now.

However, the Fantasy Grounds adapter should avoid choices that would make future adapters impossible.

Examples of acceptable future-safe decisions:

- Use `source_system` as a field.
- Record source paths generically.
- Preserve raw source references.
- Keep Discovery Registry independent from XML-specific APIs.

Examples of over-engineering to avoid now:

- Abstract base classes for hypothetical adapters.
- Complex plugin systems.
- Multi-source merge logic.
- D&D Beyond assumptions.
- Foundry-specific terminology.

---

## Determinism Requirements

The adapter must produce stable output.

Given the same input file:

- Collections should appear in consistent order.
- Node paths should be normalized consistently.
- Counts should be repeatable.
- Unknowns should be reported consistently.
- Report formatting should be stable.

This supports version control, debugging, and future comparison tools.

---

## Error Handling

Errors should be explicit and classified.

### Blocking Errors

Examples:

- File missing
- XML malformed
- Source cannot be read
- Root node missing

Blocking errors prevent discovery from completing.

### Warnings

Examples:

- Expected common Fantasy Grounds collection missing
- Unknown high-level node discovered
- Empty collection discovered
- Source metadata unavailable

Warnings do not prevent report generation.

---

## Minimum Sprint 0 Adapter Success Criteria

The first working Fantasy Grounds Adapter is successful when it can:

1. Load a Fantasy Grounds `db.xml`.
2. Identify basic source metadata.
3. Walk the XML tree.
4. List discovered top-level structures.
5. Count major collections.
6. Record unknown structures.
7. Produce a Discovery Registry.
8. Produce a Discovery Report.
9. Make no mechanical guesses.
10. Leave the source file unchanged.

---

## A.D.E. Position

Fantasy Grounds is the active source system.

Fantasy Grounds deserves the full engineering focus of Sprint 0 and Sprint 1.

Future systems should remain possible, but they should not distort the current design.

Atlas should prove itself against one real source before generalizing to others.

---

## Closing Principle

> The Fantasy Grounds Adapter observes the source. Atlas Core decides what to do with the observation.

That boundary protects Atlas from becoming a fragile parser and allows it to mature into a source-aware discovery system.
