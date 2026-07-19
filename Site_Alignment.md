# Site Alignment

**Project:** Tales of Salvation  
**Status:** Locked (working model)  
**Audience of this doc:** Humans + Atrok / Atlas instances working on the website  
**Last aligned:** 2026-07-18 (hub order + Witness block)  


This document records product and navigation decisions for the **website**.  
It does not replace `atlas-salvation/` doctrine (Mission, Ground Truth, A.D.E.).  
It explains **how the site presents** play tools vs discovery archive.

**Placement:** Off public paths. Keep `Site_Alignment.md` for humans + Atrok/Atlas (repo / local notes).  
**Do not** link it from player-facing HTML (nav, breadcrumbs, footers, or “for builders” notes on live pages).

---

## 1. Core products

| Product | What it is | Who it’s for |
|---------|------------|--------------|
| **Company Character Sheet (CCS)** | Table-facing play sheet for a **company PC** | Active campaign players |
| **Character Discovery Report / Dossier** | A.D.E. archive page — evidence, story, validation | Archive, ADE, deeper reading |
| **Deep Memory (site hub)** | Vault **entrance** — orientation + **portals** into chambers | Archive visitors + ongoing discovery |
| **Deep Memory chamber** | Per-campaign (or circle) room — dossiers, sessions, companions | Exploring one table’s memory |
| **Campaign Home** | Active table door — last session, sheets, enter Deep Memory | **Primary** visitor path for active play |

**Working model:** CCS and dossier are **dual products**. They link to each other; they are not merged into one page.

---

## 2. Active vs archived campaigns

| | Active | Archived |
|--|--------|----------|
| **Current** | **Forge of Fury** only (Tempest Company) | e.g. Descent into Avernus (Spice Boys); others as added |
| **Play sheets** | **CCS** for company PCs | **Dossiers only** by default; character sheets **upon request** |
| **Discovery** | Dossiers + that campaign’s **Deep Memory chamber** | Dossiers under Deep Memory chambers as grown |

Only the **active** campaign gets Company Character Sheets as a standard product.

---

## 3. Company Character Sheets (CCS)

- **Title “Company Character Sheet” / CCS is unique to Tempest Company** for now.
- CCS exists **only** for **Tempest Company player characters** (the company roster).
- If another campaign becomes **active** later:
  - That table invents its **own party name**.
  - A **new kind of character sheet** may emerge for that company.
  - It is **not** automatically called CCS unless we deliberately reuse the brand.

**Non-company play sheets** (example: **Malcolm Sol Moonstar**) are **not** CCS.  
They are tied to **Deep Memory** (Witness chamber / other tables), not the Tempest company sheet list.

---

## 4. Deep Memory — vault layout (locked direction)

**Vision:** Deep Memory is the home of **Dossier / Discovery Report** pages and related archive (sessions, companions).

### Hybrid language (public copy)

| Word | Meaning | Where it appears |
|------|---------|------------------|
| **Portal** / **chamber door** | Threshold on the **hub** into a **campaign** chamber | Image door cards on site Deep Memory hub |
| **Chamber** | The **room** for one campaign’s memory | Forge / Avernus pages; breadcrumbs; nav |
| **Witness block** | Vault-native section on the **hub** (not a campaign door) | After Three Strands; Sol + circle |

**Do not use “wing”** in public site copy going forward. Fine in old notes until renamed.

**Hub line example:** *Chamber doors into the campaigns Deep Memory keeps.*  
**Landing example:** *Forge chamber* (`forge-of-fury/deep-memory.html` is the template).

### Site hub layout order (locked)

Page: `deep-memory/index.html`  
**Job:** vault entrance — stay small as campaigns grow.

| Order | Block | Role |
|-------|--------|------|
| 1 | **Hero** — Deep Memory · *Every campaign is worth keeping* | Vault identity |
| 2 | **What this vault is** | Orientation (background, how the vault works) |
| 3 | **Three Strands of Memory** | Signage: CCS / Discovery Report / Companions — not a roster |
| 4 | **Witness of the Deep Memory** | **Keep as its own block** — vault family, not a campaign (Sol has no campaign). Featured card: who/why, Sol sheet, Portia, optional whisper lore. Not a full phone book. Prefer wording **of**, not “to.” |
| 5 | **Chamber doors** | **Campaign portals only** — image doors into campaign chamber pages (Forge, Avernus, future tables). Status (Active / Archived) + one CTA. **No** full character lists on the hub. |

**On the hub:** orientation + Witness block + campaign chamber doors.  
**Off the hub (lives in campaign chambers):** full Discovery Report lists, companion lists, session indexes for those tables.

Listing every character for every campaign on the hub **does not scale** and is not the long-term layout.

**Witness is not a chamber door in the campaign row.** Sol belongs to the vault’s face. If Witness content grows large later, it may gain its own chamber page *in addition* to the hub block — but it still is **not** treated as a campaign portal.

### Campaign chambers

**Job:** discovery and exploration of **one campaign table’s** memory.

**Layout language:** match **Forge Deep Memory** (`forge-of-fury/deep-memory.html`) — hero/mural, intro, sessions, discovery reports, companions, clear labels.

| Chamber | Scope | Notes |
|---------|--------|--------|
| **Forge** | Tempest Company · Forge of Fury | Template chamber; active table’s archive |
| **Avernus** | Descent into Avernus · Spice Boys | Archived; dossiers only; sheets upon request |

New campaigns get a **new chamber door on the hub** and a **new chamber page** — not a longer hub roster.

### Play path vs vault path (both correct)

**Active players (primary):**
```text
Home
 → Forge Campaign Home (last session · Company Character Sheets · Enter Deep Memory)
 → Forge chamber
```

**Vault visitors:**
```text
Home
 → Deep Memory (site hub)
      ├─ Witness of the Deep Memory (hub block → Sol / Portia)
      └─ Chamber doors → Forge / Avernus / … campaign chambers
```

**Campaign Home** keeps “this week’s breath” and **CCS**.  
**Deep Memory** keeps the stone: Witness on the hub; campaign memory in **chambers**.

As more Discovery Reports are added, they **accumulate in the relevant campaign chamber** (or under Witness if Sol-circle only), not as competing “main” products on the site home, and not as ever-growing lists under every door.

---

## 5. Audience priority

- **Most visitors** will be **active-campaign players** (sheets, last session, table utility).
- A.D.E. / dossiers are essential and growing, but must not be the **only** story the front door tells.
- **Signage:** table utility first; vault second — without hiding ADE.

---

## 6. Navigation principles (agreed)

1. **Clear labels** everywhere: “Company Character Sheet” vs “Discovery Report” / “Dossier”.
2. **Cross-links** on every Tempest PC: Sheet ↔ Discovery Report.
3. **Unified sidebars** so nav never “disappears” (companions: site Deep Memory + campaign chamber + full companion set).
4. **Site home** favors active players; Deep Memory hub is the vault door hall.
5. **Archived campaigns:** e.g. *“Archive campaign — dossiers only. Character sheets upon request.”*
6. **Hub vs chamber:** hub = orientation + Witness block + campaign chamber doors; chamber = full campaign explore page (Forge template).
7. **Witness** stays a **hub block** (not mixed into the campaign door row).
8. **Tempest Company URL / redirect** (old party-hall path): still open — no third competing room if Campaign Home holds CCS and Forge chamber holds archive. Redirect target TBD (Campaign Home vs Forge chamber).

---

## 7. Companions

**Rule:** Companions **always start as NPCs**.

- As they become a bigger part of the story, they may be easier to run on a **Fantasy Grounds Character Sheet** than an NPC stat block.
- That is a **promotion of convenience in FG**, not a promotion to **player character**.
- They remain **NPC companions**.

| Layer | Truth |
|--------|--------|
| Story / Atlas / site | Companion (NPC) |
| Fantasy Grounds | May use a character sheet record for play |
| Site CCS | **Never** — CCS is for Tempest **player** characters only |
| Site placement | Companion pages under **Deep Memory** (chamber of their campaign/circle); light links from active Campaign Home if useful |

Examples: Brennar Tallowick, Thrain’s Rug of Smothering, Red, Portia Dzuth — different story weight, same **class**: companions.

Optional mechanical snapshot on a companion page is fine; the page stays labeled **Companion**.

---

## 8. Sol / Witness circle

- **Witness of the Deep Memory** is a **dedicated block on the site Deep Memory hub** (after Three Strands, before campaign chamber doors).
- **Malcolm Sol Moonstar** and related companions (e.g. Portia) live under that Witness home, not under Tempest CCS.
- Sol is not a Forge company PC and **does not get a campaign chamber door** (he has no campaign).
- Sol’s public play sheet is **not** CCS.
- Quiet vault easter eggs (e.g. near-invisible “whisper” copy) are allowed as deliberate craft — not accidental contrast bugs on primary headings.

---

## 9. A.D.E. vs website

| | |
|--|--|
| **`atlas-salvation/`** | Doctrine: mission, truth, phases, covenant |
| **This file** | How the **website** splits play tools vs archive |
| **Discovery reports** (internal / Deep Memory) | May record player names for Atlas continuity |
| **Public HTML pages** | No “played by [player name]” on the face of the page |

**Privacy:** Player names may remain in **behind-the-scenes** notes and discovery reports so Atlas/Atrok know who plays whom. They should **not** appear on public character pages as “played by …”.

---

## 10. Change control

- Prefer **local hard drive** work until humans **align on a GitHub push**.
- Do not assume every local edit is live.
- Incomplete is allowed; **misleading completeness** (empty discovery dressed as full story) is not.

---

## 11. One-page map

```text
Site Home  →  mostly active players
    │
    ├─► Forge Campaign Home (active)
    │      ├─ Last session
    │      ├─ Company Character Sheets (Tempest CCS only)
    │      └─ Enter Deep Memory → Forge chamber
    │
    └─► Deep Memory (site hub — vault entrance)
           │
           ├─ 1. Hero: Deep Memory · Every campaign is worth keeping
           ├─ 2. What this vault is
           ├─ 3. Three Strands of Memory
           ├─ 4. Witness of the Deep Memory   ← hub block (not a campaign door)
           │       └─ Sol sheet · Portia · whisper lore as crafted
           └─ 5. Chamber doors (campaigns only — image portals)
                  ├─► Forge chamber    (template: forge-of-fury/deep-memory.html)
                  └─► Avernus chamber  (dossiers, companions; no CCS)
```

---

## 12. Open items (implementation / later decisions)

| Item | Status |
|------|--------|
| **Deep Memory hub order** (hero → vault → strands → Witness block → campaign doors) | **Implemented** on `deep-memory/index.html` (local) |
| **Thin hub** — remove full campaign character lists; image chamber doors | **Implemented** (local); refine door art anytime |
| **Keep Witness hub block** (do not fold into campaign door row) | **Implemented** (local) |
| **Avernus chamber** to Forge layout language | **Implemented** (`descent-into-avernus/deep-memory.html` + spice-boys-banner) |
| **Rename public “wing” → chamber / chamber door / portal** | Direction **locked**; sweep copy when implementing hub |
| **Sidebar template field list** | Open |
| **Tempest Company URL / redirect** | Open (think through; no third hall if Home → Campaign Home → chamber works) |
| **Future active campaign sheet brand name(s)** | Open |

---

## Closing

CCS for the **company at the table**.  
Deep Memory **hub** for orientation, the **Witness**, and **campaign chamber doors**.  
Deep Memory **chambers** for each campaign’s **dossiers and the stone**.  
Companions as **NPCs** who may wear an FG sheet without becoming PCs.  
Only **Tempest** wears the name **Company Character Sheet** until a new active company earns its own.

When in doubt about the **site**, return here.  
When in doubt about **discovery**, return to `atlas-salvation/`.
