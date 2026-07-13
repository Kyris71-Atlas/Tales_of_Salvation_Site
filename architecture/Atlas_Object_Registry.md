# Atlas Object Registry

**Project:** Atlas Salvation Alpha\
**Version:** 0.1 Draft\
**Status:** Living Document

------------------------------------------------------------------------

# Purpose

The Atlas Object Registry defines every object Atlas Workstation can
recognize.

It is the bridge between raw Fantasy Grounds data and Atlas knowledge.

The Registry answers four questions for every object:

1.  What is it?
2.  Who owns it?
3.  How does it synchronize?
4.  What does it become?

------------------------------------------------------------------------

# Design Philosophy

> Atlas should understand before it remembers.

Fantasy Grounds records the mechanics.

Atlas understands the relationships.

Atlas Workstation presents the knowledge.

------------------------------------------------------------------------

# Registry

  -------------------------------------------------------------------------------
  Object         Primary Source    Ownership    Synchronization    Generates
  -------------- ----------------- ------------ ------------------ --------------
  Character      Fantasy Grounds   FG Mechanics Auto + Preserve    Character
                                   / Atlas                         Dossier
                                   Meaning                         

  NPC            Fantasy Grounds   FG Mechanics Auto + Preserve    NPC Dossier
                                   / Atlas                         
                                   Meaning                         

  Companion      FG + Atlas        Shared       Auto + Preserve    Companion
                                                                   Dossier

  Item           Fantasy Grounds   FG Mechanics Auto + Preserve    Item Page
                                   / Atlas Lore                    

  Location       Atlas (FG         Atlas        Preserve           Location Page
                 references when                                   
                 available)                                        

  Session        Atlas             Atlas        Manual Summary     Session Report

  Campaign       Atlas             Atlas        Preserve           Campaign
  Highlight                                                        Highlight

  Mystery        Atlas             Atlas        Preserve           Mystery Page

  Evidence       Atlas             Atlas        Preserve           Evidence Panel

  Relationship   Atlas             Atlas        Preserve           Relationship
                                                                   Graph (Future)
  -------------------------------------------------------------------------------

------------------------------------------------------------------------

# Object Discovery Workflow

``` text
Fantasy Grounds Export
        │
        ▼
Character / NPC / Item Records
        │
        ▼
Atlas Object Discovery
        │
        ▼
Identify Object Type
        │
        ▼
Apply Synchronization Rules
        │
        ▼
Generate Atlas Object
        │
        ▼
Publish to Atlas Workstation
```

------------------------------------------------------------------------

# Object Ownership

## Fantasy Grounds Owns

-   Mechanical statistics
-   Character sheets
-   NPC stat blocks
-   Spells
-   Inventory
-   Magic Items
-   Conditions
-   Levels
-   Combat information

## Atlas Owns

-   Story
-   Meaning
-   Campaign Highlights
-   Relationships
-   Mysteries
-   Commentary
-   Confidence
-   Evidence

------------------------------------------------------------------------

# Synchronization Rules

Atlas never changes Fantasy Grounds mechanics.

Atlas enriches those mechanics with campaign knowledge.

If a conflict exists:

1.  Preserve Fantasy Grounds mechanics.
2.  Preserve Atlas narrative.
3.  Report the conflict.
4.  Never silently overwrite either source.

------------------------------------------------------------------------

# Future Registry Objects

These objects are expected to join Atlas as the project grows.

-   Faction
-   Organization
-   Deity
-   Plane
-   Quest
-   Encounter
-   Timeline Event
-   Region
-   Dungeon
-   World Event

------------------------------------------------------------------------

# Guiding Principle

Objects are more important than pages.

Pages may change.

Objects endure.

Every future feature in Atlas Workstation should begin by asking:

> "What object am I looking at?"
