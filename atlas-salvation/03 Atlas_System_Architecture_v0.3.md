# Atlas System Architecture

**Project:** Atlas Salvation\
**Version:** 0.3\
**Status:** Living Document

------------------------------------------------------------------------

# Purpose

This document defines the architectural structure of Atlas and the
responsibilities of its major components.

Atlas System Architecture describes **how Atlas operates**. It defines
the major subsystems, the flow of knowledge through those systems, and
the boundaries between discovery, interpretation, and presentation.

------------------------------------------------------------------------

# Core Principle

Atlas is the companion knowledge system for Fantasy Grounds.

Fantasy Grounds records mechanics.

Atlas discovers, understands, remembers, and presents campaign
knowledge.

------------------------------------------------------------------------

# High-Level Workflow

``` text
Fantasy Grounds
        │
        ▼
Atlas Discovery Engine (A.D.E.)
        │
        ▼
Discovery Reports
        │
        ▼
══════ Discovery Closure ══════
        │
        ▼
Atlas Portal
        │
        ▼
Character Dossiers
        │
        ▼
Campaign Knowledge
        │
        ▼
Atlas Workstation
        │
        ▼
Website
```

------------------------------------------------------------------------

# Discovery Engine

The Atlas Discovery Engine (A.D.E.) is responsible for learning from
campaign source material before any knowledge is created.

**Discovery always precedes interpretation.\
Interpretation always precedes knowledge.**

------------------------------------------------------------------------

# Discovery Sources

## Discovery Phase (Phases 1--3)

Sources used to establish evidence.

-   Fantasy Grounds campaign data
-   Atlas Notes
-   Structured campaign records
-   Player Notes (perspective only)

Player Notes are valuable for understanding player intent but are never
treated as campaign canon without supporting evidence.

------------------------------------------------------------------------
## Interpretation Phase (Phase 4)

### Atlas Portal Acquisition

Before interpreting Atlas Portal content, Atlas must acquire the Portal through direct Fantasy Grounds XML traversal.

The Fantasy Grounds adapter must:

- Locate the Atlas Portal index within the campaign `db.xml`.
- Read each linked internal `recordname`.
- Resolve every referenced record against the appropriate XML branch.
- Extract the complete contents of each Portal entry.
- Recursively resolve relevant links contained within Portal entries.
- Report unresolved references rather than silently omitting them.

Semantic search may assist with discovery and navigation, but direct XML traversal is the authoritative method for resolving Fantasy Grounds internal record links.

Portal entries must be read without making assumptions based on their titles. Each entry represents Christopher speaking directly to Atlas from within Fantasy Grounds and may contain campaign context, design discussions, reflections, future ideas, reminders, creative history, or general conversation.

---

### Portal Interpretation

The Atlas Portal is treated as a single interconnected body of contextual knowledge rather than a collection of isolated notes.

Typical Portal sources include:

- Atlas Portal notes
- Collaboration discussions
- Session recaps
- Dungeon Master observations
- Design discussions
- Player reflections

The Portal provides **context**, not **campaign evidence**.

Information contained within the Portal must never overwrite or replace evidence established during Discovery Phases 1–3.

Portal entries may contain:

- observations
- questions
- ideas
- theories
- future plans
- abandoned concepts
- reminders
- design intent
- creative discussion

These entries represent Christopher's thoughts at the time they were written and should not be assumed to describe the current campaign state.

When Portal content introduces new information or appears to conflict with Discovery evidence, Atlas must investigate rather than conclude.

Atlas should ask:

- What do Phases 1–3 say about this?
- Does the Discovery evidence support this statement?
- Is this an idea, or an established fact?

Only Discovery evidence establishes campaign truth.

The Atlas Portal enriches interpretation by providing context, intent, and historical perspective. It may generate questions for Atlas to investigate, but it does not generate facts.
------------------------------------------------------------------------

## Human Validation (Phase 5)

Atlas conducts an interview with the player or Dungeon Master.

Human experience completes discovery.

### Player Interview Philosophy

The purpose of Phase 5 is not to generate a character summary.

Its purpose is to generate thoughtful interview questions that demonstrate Atlas's understanding of the character by combining:

- Discovery evidence (Phases 1–3)
- Atlas Portal context (Phase 4)
- Atlas collaboration insights

These questions should encourage players to reflect on their character's journey and provide meaningful responses for the Tales of Salvation archive.

Interview questions should:

- Be grounded in established campaign evidence.
- Be enriched by contextual understanding from the Atlas Portal.
- Never present Portal content as established fact.
- Invite reflection rather than confirm assumptions.
- Feel natural to readers unfamiliar with Atlas's internal systems.

For public presentation, Atlas must:

- Refer to **The DM** rather than any real-world individual.
- Never reference Atlas, the Discovery Engine, collaboration chats, or internal development.
- Never identify or reference player names.
- Never reveal hidden campaign information or unrevealed Dungeon Master knowledge.
- Write questions as though they come from a knowledgeable campaign historian seeking to better understand the character's story.

The objective is for each player to feel that Atlas genuinely understands their character and asks questions that could only be formed through comprehensive campaign discovery and interpretation.
------------------------------------------------------------------------

# Discovery Closure

Discovery Closure is the architectural boundary between Discovery and
Interpretation.

Once Discovery closes:

-   Discovery evidence is frozen for the current cycle.
-   New contextual information may inform interpretation but may not
    become Discovery evidence.
-   Atlas begins Phase 4 with the Atlas Portal.

This protects the integrity and reproducibility of Discovery.

------------------------------------------------------------------------

# Atlas Portal Acquisition

Before contextual interpretation begins, Atlas acquires the complete
Atlas Portal.

Workflow:

1.  Locate the Atlas Portal index.
2.  Resolve every linked Portal record.
3.  Assemble the complete Portal into a working collection.
4.  Review the complete Portal before focusing on a specific character.
5.  Determine character relevance from the Portal contents, not from
    note titles alone.

The Atlas Portal is treated as an interconnected knowledge graph.

------------------------------------------------------------------------

# Knowledge Layer

The `knowledge/` folder is the canonical memory of Atlas.

Knowledge Objects are created only after Discovery and Interpretation
have been completed and reviewed.

------------------------------------------------------------------------

# Repository Principle

The user manages source files.

Atlas manages discovery, organization, interpretation, and knowledge
generation.

------------------------------------------------------------------------

# Closing Principle

> Atlas learns first.\
> Atlas interprets second.\
> Atlas remembers third.
