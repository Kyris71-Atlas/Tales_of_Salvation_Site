# Atlas Discovery Report Specification

**Version:** 0.2\
**Status:** Approved Draft

## Purpose

A Discovery Report is **not** a Knowledge Object.

It documents what Atlas discovered, how it discovered it, and the
evidence supporting those discoveries before promotion into the
`knowledge/` layer.

Repository location:

``` text
reports/
└── discovery/
```

## Discovery Philosophy

Atlas always follows this workflow:

1.  Discover
2.  Verify
3.  Analyze
4.  Review
5.  Promote

Shared understanding precedes automation.

## Standard Report Layout

### Header

``` text
==================================================
Atlas Discovery Engine
Discovery Report ####

Version
Subject
Date
Discovery Status
==================================================
```

### Discovery Scope

Document:

-   Source systems searched
-   Discovery profile
-   Search limitations
-   Objects examined

### Discovery Summary

Summarize:

-   Objects examined
-   High-priority discoveries
-   Related sources located
-   Readiness for analysis

This section answers:

> What did Atlas find?

### Evidence

Each discovery should contain:

-   Evidence ID
-   Source
-   Object
-   Relationship
-   Status
-   Notes

Evidence remains objective.

### Relationship Graph

Record discovered relationships before interpretation.

### Analysis

Performed only after evidence gathering.

May include:

-   Patterns
-   Potential significance
-   Supporting observations
-   Questions

Every analytical statement should be traceable to evidence.

### Confidence

-   Canonical Fact
-   Curated DM Knowledge
-   Player Perspective
-   Atlas Observation
-   Atlas Inference

### Provenance

Record where information originated:

-   Fantasy Grounds
-   Atlas Note
-   Player Note
-   Campaign Knowledge
-   Legacy Documentation
-   Session History

### Open Questions

Record uncertainty instead of hiding it.

### Review Checklist

-   Evidence complete
-   Relationships verified
-   Confidence assigned
-   Provenance recorded
-   Assumptions identified
-   Open questions retained

## Promotion Rule

``` text
Discovery
    ↓
Review
    ↓
Campaign Knowledge
    ↓
Atlas Workstation
```

A Discovery Report is never promoted automatically.

## Closing Principle

> Discovery answers what Atlas found.

> Knowledge answers what Atlas remembers.
