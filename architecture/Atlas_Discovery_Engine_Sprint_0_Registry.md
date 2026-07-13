# Atlas Discovery Engine — Sprint 0 Registry Specification

**Project:** Atlas Discovery Engine  
**Component:** Discovery Registry  
**Status:** Implementation Specification  
**Version:** 0.0.1  

---

## Purpose

Sprint 0 establishes the first executable layer of Atlas Core: the **Discovery Layer**.

Its purpose is to examine a source system, beginning with Fantasy Grounds `db.xml`, and describe what exists without interpretation, validation, synchronization, or publication.

This aligns with the operating principle:

> Atlas observes before it understands.

---

## Relationship to Existing Documents

This specification extends the Atlas Discovery Engine Bootstrap and the Atlas Discovery Layer Proposal.

The Bootstrap defines the immediate engineering direction: produce a verified Atlas Character Object from Fantasy Grounds data, beginning with Mantis.

The Discovery Layer Proposal adds a necessary prior step: survey the source system before object discovery begins.

Sprint 0 therefore becomes the required precursor to Sprint 1.

---

# Sprint 0 Goal

Given a Fantasy Grounds `db.xml`, Atlas Discovery Engine produces a deterministic **Discovery Registry** and a human-readable **Discovery Report**.

The system answers only one question:

> What exists inside this source system?

It does not answer:

- What does this mean?
- Is this valid?
- Is this complete?
- Should this become an Atlas Object?
- How should this be synchronized?

---

# Non-Goals

Sprint 0 must not:

- Build Atlas Character Objects
- Interpret Fantasy Grounds mechanics
- Derive ability modifiers, spell DCs, hit points, armor class, or proficiency
- Generate HTML
- Modify source files
- Synchronize websites
- Compare revisions
- Guess missing values
- Validate against the Character Object Specification

---

# Core Rule

## Discovery Never Decides

Discovery records what is present.

If the source contains:

```xml
<strength>17</strength>
```

Discovery may record:

```json
{
  "node_name": "strength",
  "value_preview": "17",
  "path": "/root/charsheet/id-00001/abilities/strength"
}
```

Discovery must not conclude:

```text
Mantis has Strength 17.
```

That conclusion belongs to a later Interpretation layer.

---

# Proposed Pipeline

```text
Source System
      |
      v
Source Loader
      |
      v
Source Fingerprint
      |
      v
Structure Scanner
      |
      v
Discovery Registry
      |
      v
Discovery Report
      |
      v
Object Discovery
```

---

# Component Responsibilities

## 1. Source Loader

The Source Loader accepts a source path and returns a parsed document.

Responsibilities:

- Confirm the file exists
- Confirm it can be read
- Parse XML
- Return the root element
- Report load errors clearly

The loader does not inspect game meaning.

---

## 2. Source Fingerprint

The Source Fingerprint identifies the broad source context.

Minimum fields:

```json
{
  "source_type": "Fantasy Grounds Unity",
  "format": "XML",
  "root_tag": "root",
  "ruleset": null,
  "campaign_name": null,
  "source_file": "db.xml"
}
```

Unknown values are allowed and should remain explicit as `null`.

No guessing.

---

## 3. Structure Scanner

The Structure Scanner walks the XML tree and records observed structures.

Responsibilities:

- Record every unique node name
- Record every unique path shape
- Count occurrences
- Record parent-child relationships
- Record whether nodes contain text
- Record whether nodes contain attributes
- Record whether nodes contain children
- Preserve unknown structures

The scanner does not classify nodes as characters, items, NPCs, or story unless that classification is directly observable from structure naming.

---

## 4. Discovery Registry

The Discovery Registry is the machine-readable internal artifact produced by Sprint 0.

It is the first Atlas internal model.

Recommended top-level structure:

```json
{
  "registry_version": "0.0.1",
  "source_fingerprint": {},
  "summary": {},
  "nodes": [],
  "collections": [],
  "relationships": [],
  "warnings": []
}
```

---

# Discovery Registry Schema

## registry_version

Version of the Discovery Registry format.

Example:

```json
"0.0.1"
```

---

## source_fingerprint

Describes the source system.

Example:

```json
{
  "source_type": "Fantasy Grounds Unity",
  "format": "XML",
  "root_tag": "root",
  "source_file": "db.xml",
  "ruleset": null,
  "campaign_name": null
}
```

---

## summary

High-level observed counts.

Example:

```json
{
  "total_nodes": 18420,
  "unique_node_names": 312,
  "unique_paths": 921,
  "top_level_sections": 14,
  "warnings": 0
}
```

---

## nodes

Each discovered node type/path combination.

Example:

```json
{
  "path": "/root/charsheet/id-00001/name",
  "node_name": "name",
  "occurrences": 1,
  "has_text": true,
  "has_attributes": false,
  "has_children": false,
  "text_preview": "Mantis"
}
```

Notes:

- `text_preview` should be limited to a safe preview length.
- Long text should be truncated.
- Discovery should not summarize text.

---

## collections

Collections are repeated structures directly observed in the XML.

Example:

```json
{
  "collection_path": "/root/charsheet",
  "collection_name": "charsheet",
  "record_count": 5,
  "record_keys": [
    "id-00001",
    "id-00002",
    "id-00003"
  ]
}
```

Discovery may identify a collection when a node contains multiple similarly shaped child records.

It must not decide that a collection is semantically complete or valid.

---

## relationships

Relationships are structural references observed in the source.

Example:

```json
{
  "from_path": "/root/charsheet/id-00001/portrait",
  "to_reference": "campaign/portraits/mantis.png",
  "relationship_type": "observed_reference"
}
```

Relationship discovery is observational only.

It does not verify that the referenced target exists unless that is part of a later verification pass.

---

## warnings

Warnings describe discovery concerns without treating them as failures.

Example:

```json
{
  "level": "warning",
  "message": "Large text node truncated in preview.",
  "path": "/root/story/id-00031/text"
}
```

Warnings should be deterministic and repeatable.

---

# Discovery Report

The Discovery Report is the human-readable view of the Discovery Registry.

Minimum report sections:

```text
Atlas Discovery Report
======================

Source Fingerprint
------------------
Source Type: Fantasy Grounds Unity
Format: XML
Root Tag: root
Source File: db.xml
Ruleset: Unknown
Campaign: Unknown

Summary
-------
Total Nodes: 18420
Unique Node Names: 312
Unique Paths: 921
Top-Level Sections: 14
Warnings: 0

Top-Level Sections
------------------
charsheet
npc
item
image
story
quest
reference

Collections Discovered
----------------------
/root/charsheet — 5 records
/root/npc — 148 records
/root/item — 642 records

Warnings
--------
None
```

---

# Determinism Requirements

Discovery must be deterministic.

For the same input file:

- Node ordering must be stable
- Collection ordering must be stable
- Warning ordering must be stable
- Report output must be stable
- Registry output must be stable

Recommended ordering:

1. Path alphabetically
2. Node name alphabetically
3. Record key alphabetically

---

# Initial Command

The first executable command should be:

```bash
atlas discover db.xml
```

Recommended outputs:

```text
/discovery/atlas_discovery_registry.json
/discovery/atlas_discovery_report.md
```

Optional console output:

```text
Atlas Discovery Engine 0.0.1
Source loaded: db.xml
Discovery complete.
Registry: discovery/atlas_discovery_registry.json
Report: discovery/atlas_discovery_report.md
```

---

# Suggested File Layout

```text
atlas-core/
  discovery/
    __init__.py
    loader.py
    fingerprint.py
    scanner.py
    registry.py
    reporter.py
  cli/
    __init__.py
    discover.py
  tests/
    test_discovery_loader.py
    test_structure_scanner.py
    test_registry_determinism.py
```

---

# Acceptance Criteria

Sprint 0 is complete when:

- A Fantasy Grounds `db.xml` can be loaded
- A Discovery Registry JSON file is produced
- A Discovery Report Markdown file is produced
- Top-level XML sections are listed
- Repeated collections are counted
- Unknown structures are preserved
- No Atlas Objects are produced
- No game mechanics are interpreted
- Output is deterministic for the same input

---

# Hand-Off to Sprint 1

Sprint 1 may begin only after Sprint 0 produces a stable Discovery Registry.

Sprint 1 will consume the registry and begin Object Discovery for one target character:

```text
Mantis
```

Sprint 1 will then attempt to produce one Verified Atlas Character Object while preserving source ownership and avoiding guessed mechanical values.

---

# A.D.E. Closing Principle

Discovery is not understanding.

Discovery is the disciplined act of looking before deciding.

Atlas must first be able to say:

> I found this.

Only later may it say:

> I know what this means.
