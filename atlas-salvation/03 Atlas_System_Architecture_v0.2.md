# Atlas System Architecture

**Project:** Atlas Salvation\
**Version:** 0.2\
**Status:** Living Document

------------------------------------------------------------------------

# Purpose

This document defines the architectural structure of Atlas and the
responsibilities of its major components.

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

Discovery always precedes knowledge.

## Discovery Sources

A.D.E. prioritizes sources in the following order:

1.  Atlas Notes

    -   Curated communication from the Dungeon Master to Atlas.
    -   Primary discovery entry point.

2.  Fantasy Grounds source data

    -   Characters
    -   NPCs
    -   Items
    -   Story entries
    -   Quests
    -   Images
    -   Other records

3.  Campaign Knowledge

4.  Player Notes

    -   Used to understand player perspective.
    -   Valuable for story and character insight.
    -   Never treated as campaign canon without supporting evidence.

------------------------------------------------------------------------

# Knowledge Layer

The `knowledge/` folder is the canonical memory of Atlas.

Knowledge Objects are created only after discovery and review.

------------------------------------------------------------------------

# Repository Principle

The user manages source files.

Atlas manages discovery, organization, and knowledge generation.

------------------------------------------------------------------------

# Closing Principle

> Atlas learns first. Atlas remembers second.
