# Character Object Specification

**Project:** Atlas Salvation Alpha\
**Version:** 0.1 Draft\
**Status:** Living Document

------------------------------------------------------------------------

# Purpose

This specification defines the **Verified Atlas Character Object**.

It is the contract between:

-   Fantasy Grounds
-   Atlas Core
-   Atlas Workstation

The Character Discovery Engine must produce an object that satisfies
this specification before synchronization or website generation can
occur.

------------------------------------------------------------------------

# Guiding Principle

> Atlas understands before it remembers.

A Character Object is not a web page.

It is a trusted representation of one player character.

------------------------------------------------------------------------

# Object Layout

## Identity

  Field        Source            Owner
  ------------ ----------------- -------
  Name         Fantasy Grounds   FG
  Portrait     Fantasy Grounds   FG
  Race         Fantasy Grounds   FG
  Class        Fantasy Grounds   FG
  Subclass     Fantasy Grounds   FG
  Level        Fantasy Grounds   FG
  Background   Fantasy Grounds   FG

------------------------------------------------------------------------

## Mechanics

  Field                Source                                     Owner
  -------------------- ------------------------------------------ -------
  STR                  Fantasy Grounds                            FG
  DEX                  Fantasy Grounds                            FG
  CON                  Fantasy Grounds                            FG
  INT                  Fantasy Grounds                            FG
  WIS                  Fantasy Grounds                            FG
  CHA                  Fantasy Grounds                            FG
  AC                   Fantasy Grounds                            FG
  HP                   Fantasy Grounds                            FG
  Initiative           Fantasy Grounds                            FG
  Speed                Fantasy Grounds                            FG
  Passive Perception   Fantasy Grounds (or verified derivation)   FG

------------------------------------------------------------------------

## Spellcasting

  -----------------------------------------------------------------------
  Field                   Source                  Notes
  ----------------------- ----------------------- -----------------------
  Spellcasting Ability    Fantasy Grounds         Direct

  Spell Save DC           FG if present,          Never guessed
                          otherwise derived from  
                          verified mechanics      

  Spell Attack Bonus      FG if present,          Never guessed
                          otherwise derived       

  Spell List              Fantasy Grounds         Direct
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Inventory

-   Equipment
-   Magic Items
-   Currency

Source: Fantasy Grounds

------------------------------------------------------------------------

## Atlas Narrative

Owned exclusively by Atlas.

-   Campaign Highlights
-   Story Arc
-   Relationships
-   Commentary
-   Evidence
-   Confidence

These fields are **never overwritten** during synchronization.

------------------------------------------------------------------------

## Metadata

  Field                  Source
  ---------------------- -----------------
  Source Campaign        Fantasy Grounds
  Character Record ID    Fantasy Grounds
  Last Synchronization   Atlas
  Verification Status    Atlas

------------------------------------------------------------------------

# Verification Rules

🟢 Verified --- Directly read from Fantasy Grounds.

🟡 High-confidence inference --- Derived from verified mechanics using
published rules.

🟠 Educated guess --- Allowed only outside mechanics and must be
labeled.

🔴 Speculation --- Never used for mechanical values.

------------------------------------------------------------------------

# Acceptance Criteria

A Character Object is complete when:

-   Every mechanical field has a verified source.
-   Every Atlas field has a defined owner.
-   No field has ambiguous ownership.
-   Synchronization can update mechanics without altering narrative.

------------------------------------------------------------------------

# Example

Mantis is the reference implementation for this specification. Future
player characters should conform to the same object layout unless the
Constitution changes.
