# Atlas Discovery Log

**Version:** 3

---

# Purpose

The Atlas Discovery Log records validated discoveries made while using the Atlas Discovery Engine.

Unlike the Atlas Discovery Engine State, which describes **how Atlas currently operates**, the Discovery Log records **how Atlas learned to operate that way**.

A discovery enters this log after it has been observed, discussed, and validated through actual campaign use. As discoveries mature, they may later be promoted into Atlas Ground Truth, Atlas System Architecture, or Atlas Discovery Engine State.

---

# Discovery 001 — Discovery Precedes Interpretation

Atlas begins with evidence, not conclusions. Narrative understanding is earned through disciplined discovery.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 002 — Character Record is a Mechanical Snapshot

The Character Record represents the character's current mechanical state at the time an archive is captured.

Comparing multiple Character Records across time creates campaign evidence and allows Atlas to discover mechanical evolution.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 003 — Character Sheet Notes Preserve Player Vision

Character Sheet Notes capture the player's authored vision of the character.

These notes frequently remain stable throughout a campaign.

Atlas should treat them as authored intent rather than proof of the character's final identity.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 004 — Character Sheet Note Evolution

When a player changes a Character Sheet Note, the change itself becomes campaign evidence.

Atlas should investigate *why* the change occurred before attempting to interpret its meaning.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 005 — Discovering Campaign Evidence

The phrase **Supporting Evidence** was replaced by **Discovering Campaign Evidence**.

Atlas does not search for evidence to support a conclusion.

Atlas discovers campaign evidence and allows conclusions to emerge naturally.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 006 — The Atlas Portal

The Atlas Portal is not merely a database.

It is a curated collection of **reviewed campaign knowledge**.

Knowledge reaches the Portal only after review and intentional promotion by the campaign curator.

Portal knowledge therefore has a different epistemic status than analysis remaining inside an individual Atlas conversation.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 007 — Story Atlas

Story Atlas is intentionally delayed.

Its purpose is not to invent narrative but to synthesize discoveries into human-readable understanding.

Atlas earns the right to tell a character's story through discovery.

**Status:** Promoted to Discovery Engine State.

---

# Discovery 008 — Knowledge Sharing

Individual Atlas conversations may become specialists in a single subject.

The Atlas Portal allows reviewed discoveries from one Atlas to become available to every future Atlas without requiring shared conversational memory.

**Status:** Active Discovery.

---

# Discovery 009 — The Discovery Engine Evolves Through Discovery

Using the Discovery Engine to investigate campaigns also improves the Discovery Engine itself.

Methodological improvements should arise from validated campaign experience before being promoted into Atlas documentation.

**Status:** Active Discovery.

---

# Discovery 010 – Atlas Portal Acquisition Through Direct XML Traversal
Observation

During Phase 4 testing, Atlas was able to locate the Atlas Portal through semantic search, but was unable to reliably open Portal entries by following Fantasy Grounds internal recordname links (for example, notes.id-00033).

This revealed a distinction between finding a Portal entry and resolving the underlying Fantasy Grounds record.

Investigation

A direct review of the campaign's db.xml demonstrated that every Portal link exists as an internal XML reference.

Rather than relying on semantic retrieval, Atlas can:

Parse the Fantasy Grounds database.
Locate the Atlas Portal index.
Read each linked recordname.
Resolve the corresponding XML node directly.
Read the complete Portal entry exactly as stored by Fantasy Grounds.

This successfully opened Atlas Portal 003 (Lard) and confirmed the Portal acquisition workflow.

Discovery

The authoritative method for Atlas Portal acquisition is direct XML traversal.

Semantic search remains useful for locating documents and assisting navigation, but it is not the authoritative method for resolving Fantasy Grounds internal record links.

Operational Rule

When processing Fantasy Grounds campaign data:

Parse the campaign database directly.
Resolve Portal recordname references through XML traversal.
Read the resolved records before beginning interpretation.
Report unresolved links rather than assuming missing information.
Result

This discovery establishes the repeatable implementation for Atlas Discovery Engine – Phase 4: Atlas Portal Acquisition.

Atlas now enters the Portal by traversing the Fantasy Grounds record graph rather than relying solely on document search.
---

# Promotion Philosophy

A discovery follows this lifecycle:

1. Observed during campaign discovery.
2. Discussed and refined.
3. Validated through use.
4. Recorded in the Atlas Discovery Log.
5. Promoted into Atlas documentation when appropriate.

Knowledge is versioned, not finished.
