# Atlas Workstation Handoff Specification

**Project:** Atlas Discovery Engine (A.D.E.)\
**Audience:** Atlas Core, Atlas Workstation, Future Atlas Engineering
Chats\
**Status:** Foundational Architecture

------------------------------------------------------------------------

# Purpose

The Atlas Workstation Handoff is the **canonical output** of Atlas
Discovery.

Its purpose is to provide a single, trusted representation of campaign
knowledge that Atlas Workstation can consume.

The user should replace **one file** in Atlas Workstation to update the
website.

------------------------------------------------------------------------

# Core Principle

> **The user manages one file. Atlas manages everything else.**

Atlas may consume many source files internally, but the normal workflow
remains simple.

------------------------------------------------------------------------

# Workflow

``` text
Fantasy Grounds
        │
        ▼
Campaign Snapshot
        │
        ▼
Atlas Discovery Engine
        │
        ▼
Discovery Report
        │
        ▼
Atlas Objects
        │
        ▼
Atlas Workstation Handoff (ONE Markdown File)
        │
        ▼
Atlas Workstation
        │
        ▼
Website
```

------------------------------------------------------------------------

# Source Ownership

Fantasy Grounds owns:

-   Live campaign
-   Mechanics
-   Combat state
-   Character mechanics
-   NPC mechanics

Atlas owns:

-   Discovery Reports
-   Atlas Objects
-   Synchronization Reports
-   Atlas Workstation Handoff
-   Website knowledge

Atlas never becomes the authoritative owner of the live campaign.

------------------------------------------------------------------------

# Engineering Philosophy

Internally, Atlas may read many source artifacts (db.xml, session
snapshots, module state, extension state, future source systems). These
are implementation details.

The user-facing workflow does **not** change.

------------------------------------------------------------------------

# Canonical Output

The Atlas Workstation Handoff should contain stable campaign knowledge,
including:

-   Characters
-   NPCs
-   Locations
-   Organizations
-   Story
-   Encounters
-   Items
-   Images
-   Relationships
-   Discovery metadata

It should not contain parser state, temporary diagnostics, or
implementation details.

------------------------------------------------------------------------

# Future Compatibility

Regardless of whether the source is Fantasy Grounds, D&D Beyond,
Foundry, or another supported system, Atlas produces the same canonical
handoff.

------------------------------------------------------------------------

# Workflow Preservation

Every future architectural proposal should answer:

1.  Does this preserve the single Workstation handoff workflow?
2.  Does the source system remain the owner of mechanics?
3.  Does Atlas continue to learn from snapshots rather than the live
    campaign?
4.  Can the website still be refreshed by replacing one generated
    Markdown file?

If the answer to any of these is **No**, the proposal should be
reconsidered.

------------------------------------------------------------------------

# Atlas Law #1

> **The user manages one file. Atlas manages everything else.**
