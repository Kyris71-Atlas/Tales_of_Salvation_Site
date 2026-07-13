# Mantis Synchronization Map

**Project:** Atlas Salvation Alpha\
**Milestone:** 004 -- Trust Through Synchronization\
**Status:** Prototype

------------------------------------------------------------------------

# Purpose

This document defines how **one Fantasy Grounds character** becomes
**one Atlas Character Dossier**.

Mantis is the reference implementation. Every future character should
follow the same pattern.

------------------------------------------------------------------------

# Source of Truth

  Layer             Owner
  ----------------- -------------------
  Mechanics         Fantasy Grounds
  Story & Meaning   Atlas
  Presentation      Atlas Workstation

------------------------------------------------------------------------

# Synchronization Map

  --------------------------------------------------------------------------------------
  Fantasy Grounds Atlas Object              Website        Owner          Sync Rule
                                            Section                       
  --------------- ------------------------- -------------- -------------- --------------
  Name            Character.Name            Page Title     FG             Replace

  Portrait        Character.Portrait        Hero Panel     FG             Replace

  Race            Character.Race            Identity       FG             Replace

  Class / Level   Character.ClassLevel      Identity       FG             Replace

  Ability Scores  Character.Abilities       Character Card FG             Replace

  AC              Character.Combat.AC       Character Card FG             Replace

  HP              Character.Combat.HP       Character Card FG             Replace

  Spell List      Character.Spells          Magic          FG             Replace

  Inventory       Character.Inventory       Equipment      FG             Replace

  Magic Items     Character.Items           Equipment      FG             Replace

  Campaign        Character.Highlights      Story          Atlas          Preserve
  Highlights                                                              

  Relationships   Character.Relationships   Story          Atlas          Preserve

  Atlas           Character.Commentary      Story          Atlas          Preserve
  Commentary                                                              

  Evidence        Character.Evidence        Evidence Panel Atlas          Preserve
  --------------------------------------------------------------------------------------

------------------------------------------------------------------------

# Synchronization Rules

## Replace Automatically

-   Mechanical values
-   Character statistics
-   Spell changes
-   Inventory changes
-   Magic item changes
-   Portrait reference

## Preserve

-   Story
-   Campaign Highlights
-   Relationships
-   Commentary
-   Confidence Notes

## If a Conflict Exists

1.  Fantasy Grounds wins for mechanics.
2.  Atlas wins for meaning.
3.  Never silently overwrite Atlas-authored story.
4.  Produce a Synchronization Report before publishing.

------------------------------------------------------------------------

# Expected Workflow

``` text
Export db.xml
      ↓
Atlas reads Character
      ↓
Compare against existing Atlas object
      ↓
Generate Synchronization Report
      ↓
DM Review
      ↓
Publish updated Character Dossier
```

------------------------------------------------------------------------

# Success Criteria

Atlas correctly detects mechanical changes made to Mantis without
altering Atlas-authored narrative content.

If this succeeds, the same pattern can be applied to every Player
Character, Companion, NPC, Item, and Location.
