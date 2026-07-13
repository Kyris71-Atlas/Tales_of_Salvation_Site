# Atlas Data Model

**Project:** Atlas Salvation Alpha\
**Version:** 0.2 Draft\
**Status:** Living Document

------------------------------------------------------------------------

# Purpose

The Atlas Data Model defines the major objects within Atlas Salvation,
their sources, ownership, and synchronization behavior.

> **Fantasy Grounds owns mechanics. Atlas owns meaning.**

------------------------------------------------------------------------

# Universal Object Pattern

Every Atlas object answers five questions:

1.  What is it?
2.  Where does its data come from?
3.  Who owns each field?
4.  How does it synchronize?
5.  What page does it generate?

------------------------------------------------------------------------

# Character

**Represents:** A player character.

## Fantasy Grounds owns

-   Name
-   Portrait
-   Race
-   Class / Level
-   Ability Scores
-   AC / HP
-   Saves & Skills
-   Spells
-   Inventory
-   Magic Items
-   Conditions / Curses
-   Mechanical effects

## Atlas owns

-   Campaign Highlights
-   Story Arc
-   Relationships
-   Commentary
-   Evidence
-   Confidence notes

## Synchronization

**Source:** Fantasy Grounds `db.xml`

**Automatic updates** - Replace all mechanical values with current
Fantasy Grounds values. - Never overwrite Atlas commentary or story
sections.

**Conflict handling** - If Fantasy Grounds and Atlas disagree on
mechanics: - Preserve Fantasy Grounds. - Flag the difference for DM
review. - Never silently change or "fix" data.

**Generates** - Character Dossier

------------------------------------------------------------------------

# NPC

Fantasy Grounds owns mechanics.

Atlas owns personality, motives, history, and narrative role.

**Synchronization** - Update mechanics automatically. - Preserve
narrative notes.

Generates: - NPC Dossier

------------------------------------------------------------------------

# Companion

Represents recurring allies that intentionally sit between PC and NPC.

Example: - Brennar Tallowick

**Synchronization** - Same as Character unless Constitution specifies
otherwise.

Generates: - Companion Dossier

------------------------------------------------------------------------

# Item

Fantasy Grounds owns mechanical properties.

Atlas owns history, symbolism, campaign importance, and discovery notes.

**Synchronization** - Update mechanics. - Preserve lore.

Generates: - Item Page

------------------------------------------------------------------------

# Location

Fantasy Grounds may provide map references and encounter links.

Atlas owns descriptions, history, atmosphere, and campaign significance.

Generates: - Location Page

------------------------------------------------------------------------

# Session

Represents one game session.

Fantasy Grounds provides chronological events where available.

Atlas creates: - Summary - Highlights - Narrative - Evidence

Generates: - Session Report

------------------------------------------------------------------------

# Mystery

Represents unanswered questions.

Examples: - Deep Memory - Black Obelisk - Twenty-Six Breaths

Atlas owns Mysteries.

Fantasy Grounds may reference them indirectly but is not the source.

------------------------------------------------------------------------

# Campaign Highlight

Curated by Atlas.

Never automatically generated from mechanics alone.

Examples: - First contact with the Deep Memory - Defeat of Idalla

------------------------------------------------------------------------

# Evidence

Every significant statement should identify its source.

🟢 Verified

🟡 High-confidence inference

🟠 Educated guess

🔴 Speculation

------------------------------------------------------------------------

# Synchronization Philosophy

Synchronization is **alignment**, not automation.

Atlas synchronizes with Fantasy Grounds so mechanical data remains
accurate while preserving Atlas-authored meaning.

The synchronization engine should produce a report before rebuilding
pages.

Example report:

``` text
Character: Mantis

✓ Ability Scores updated
✓ Inventory updated
✓ Spell list updated

Story sections preserved.
No conflicts detected.
```

------------------------------------------------------------------------

# Long-Term Workflow

``` text
Fantasy Grounds Export
        ↓
Updated db.xml
        ↓
Atlas reads the Data Model
        ↓
Objects are synchronized
        ↓
Synchronization Report
        ↓
Website regenerated
```

------------------------------------------------------------------------

This document will evolve as Atlas Workstation grows.
