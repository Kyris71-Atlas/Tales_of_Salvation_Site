# Blasingdell Town Hub — Grok Build Handoff

## First Things First

Before implementation work, request and read:

1. `data/Atlas_Ground_Truth.md`
2. `architecture/Atlas_System_Architecture.md`

Keep this page integrated with the existing Tales of Salvation site structure, navigation, relative paths, and visual language.

---

## Project Purpose

We are turning the existing **Mining Town of Blasingdell map** into a player-facing **town hub**.

The map should function like walking into town. Players will click clearly visible location markers on the map to enter individual shop and service pages.

This hub supports the party’s upcoming downtime between sessions. Over the next few weeks, players should be able to browse goods and services, buy equipment, sell recovered items, arrange repairs, healing, lodging, and other downtime needs, and review location-specific opportunities before the next live session.

This should not feel like a generic online store or menu screen. It should feel like the party has returned to Blasingdell and is choosing where to walk.

---

## Source Map and Interaction

Use the provided Blasingdell town map as the centerpiece of the hub page.

Do not redesign or replace the map unless Christopher specifically requests it.

Interactive location markers should be:

- easy to notice;
- clearly clickable;
- visually consistent with the fantasy setting;
- modest enough that they do not cover or overpower the map;
- positioned near the corresponding location;
- accompanied by a hover or focus label such as **Enter The Shattered Rune**.

A small doorway, sign, crest, glow, or similar marker fits the intended experience.

Maintain keyboard focus, descriptive labels, and usable links.

---

## First-Wave Active Locations

### The Shattered Rune

Primary magical shop and service destination.

Expected uses:

- buying and selling magical or unusual items;
- identification and magical services;
- Town Portal scrolls;
- spell-related supplies;
- commissions and special requests;
- interactions with Gimble Wandsplice.

### Ironvein Smithy

Primary martial equipment destination.

Expected uses:

- buying and selling weapons;
- buying and selling armor;
- repairs and maintenance;
- custom commissions;
- appraisal of recovered martial gear;
- interactions with Durnan Ironvein.

### The Shrine

Primary healing and religious service destination.

Expected uses:

- healing services;
- blessings;
- restorative services;
- donations and offerings;
- religious supplies or support;
- interactions with Sister Maerith and the Shrine of Chauntea.

### The Pick & Lantern

Primary lodging, food, rumor, and common-room destination.

Expected uses:

- rooms and meals;
- local rumors;
- notices and informal opportunities;
- meeting townsfolk;
- downtime conversation;
- interactions with Marta Two-Tankard.

### Vellbrandt Manor

A refined, patron-facing destination connected to Lady Seraphine Vellbrandt.

Expected uses:

- private requests;
- special commissions;
- rewards or patronage;
- refined or unusual transactions;
- invitations and campaign-facing social business.

Do not expose Lady Seraphine’s hidden role, plans, or affiliations unless Christopher explicitly approves that information for players.

### Stone Hall

Primary civic and official destination.

Expected uses:

- contracts;
- formal rewards;
- claims;
- permits;
- public notices;
- town business;
- official transactions and requests.

---

## Parked Locations

These locations remain visible on the map but should not receive active doors yet.

### Warehouse District

Park this location until later.

Hidden campaign truth: the Warehouse District is operated through the thieves’ guild.

This is **not player knowledge**. Do not reveal or hint at it through page text, tooltips, metadata, comments, navigation, or filenames.

### Greytooth Quarry

Park this location until later.

Greytooth Quarry is connected to **The Cracked Vein**. There is currently no player-facing reason to return, so the hub should not imply that it is open, useful, or awaiting exploration.

It may become active when the campaign creates a reason to reopen that door.

---

## Build Priority

The immediate goal is to get the player commerce loop working.

Recommended order:

1. Town Hub map and six active doors
2. Ironvein Smithy
3. The Shattered Rune
4. The Shrine
5. The Pick & Lantern
6. Stone Hall
7. Vellbrandt Manor

Buying and selling functionality should come before lower-priority atmosphere or lore work.

---

## Location Page Expectations

Each destination page should share a consistent structure while preserving the personality of the location.

Suggested sections:

### Arrival

A short atmospheric introduction that makes the player feel they have entered the location.

### Proprietor or Host

The relevant NPC in the established campaign voice.

### Goods and Services

Clear categories for what is currently available.

### Buying

Current stock, cost, limits, and special conditions.

### Selling

What the proprietor will purchase, preferred item types, exclusions, and offered value.

### Special Requests

Repairs, commissions, identification, healing, lodging, or other location-specific services.

### Current Opportunities

Limited inventory, rumors, notices, favors, or approved campaign hooks.

### Return to Town

A reliable link back to the Blasingdell Town Hub.

Inventory should be easy for Christopher to update between sessions. Items may appear, sell out, change price, or become unavailable as Blasingdell evolves.

---

## Player-Knowledge Boundary

The hub and shop pages are player-facing.

Do not expose DM-only information merely because it exists elsewhere in Atlas, source files, campaign archives, comments, metadata, or prior collaboration.

Specifically:

- do not reveal the Warehouse District’s thieves’ guild control;
- do not reveal Seraphine’s secret role or Stillwake activity;
- do not imply Greytooth Quarry is currently active;
- do not invent inventory, services, prices, secrets, or NPC knowledge without Christopher’s approval.

When information is missing, leave a clear placeholder or ask Christopher rather than filling the gap.

---

## Design Goal

**The Blasingdell Town Hub should let the players walk into town, choose a visible destination on the map, and conduct their downtime business inside a living campaign location rather than through a generic shop menu.**

---

## Current Status

- Town hub concept: approved
- Source map: provided
- Active first-wave locations: confirmed
- Parked locations: confirmed
- Shop inventory and transaction details: still to be supplied or developed one location at a time
- Build approach: one page at a time, preserving integration across the full Tales of Salvation site
- **Scaffold (local):** `town/index.html` hub + six location stubs + Campaign Home link; art/stock placeholders only
- Arrival line: *Catch your breath. The mountain isn't going anywhere.*
- Asset drop folders: `assets/images/forge-of-fury/town/<location>/`
