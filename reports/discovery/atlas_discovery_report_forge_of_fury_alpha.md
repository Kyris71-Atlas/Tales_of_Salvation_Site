# Atlas Discovery Report

**Altitude:** 0 — Source discovery only
**Engine mode:** Grok Build agent (resilient parse; atlas_core CLI blocked by invalid FG character refs)
**Discovery Status:** Complete (structural) / No interpretation

## Source Fingerprint

- Source label: `forge_of_fury_alpha`
- Source file: `C:\Users\Owner\OneDrive\Personal\001 Forge of Fury (campaigns) Alpha\db.xml`
- Source format: XML
- Probable source system: Fantasy Grounds-style campaign database (filename `db.xml`)
- File size bytes: 853632
- Content sha256 (first 16 hex): `6feddb778a58c2c1`
- Encoding used: utf-8
- Root tag: `root`
- Root attribute keys: dataversion, release, version

## Warnings

- Removed 16 invalid XML numeric character references for parseability

## Summary

- Total nodes: 15525
- Unique tag names: 400
- Unique path shapes: 12866
- Nodes with text: 9007
- Nodes with attributes: 8688
- Max depth: 9
- Collection-like structures: 154

## Top-Level Sections

- `background` — 1 direct child node(s) with this tag under root
- `battle` — 1 direct child node(s) with this tag under root
- `calendar` — 1 direct child node(s) with this tag under root
- `charsheet` — 1 direct child node(s) with this tag under root
- `class` — 1 direct child node(s) with this tag under root
- `combattracker` — 1 direct child node(s) with this tag under root
- `currencies` — 1 direct child node(s) with this tag under root
- `deathmanager` — 1 direct child node(s) with this tag under root
- `effects` — 1 direct child node(s) with this tag under root
- `encounter` — 1 direct child node(s) with this tag under root
- `feat` — 1 direct child node(s) with this tag under root
- `image` — 1 direct child node(s) with this tag under root
- `item` — 1 direct child node(s) with this tag under root
- `languages` — 1 direct child node(s) with this tag under root
- `location` — 1 direct child node(s) with this tag under root
- `modifiers` — 1 direct child node(s) with this tag under root
- `motd` — 1 direct child node(s) with this tag under root
- `notes` — 1 direct child node(s) with this tag under root
- `npc` — 1 direct child node(s) with this tag under root
- `options` — 1 direct child node(s) with this tag under root
- `partysheet` — 1 direct child node(s) with this tag under root
- `picture` — 1 direct child node(s) with this tag under root
- `quest` — 1 direct child node(s) with this tag under root
- `race` — 1 direct child node(s) with this tag under root
- `settings` — 1 direct child node(s) with this tag under root
- `spell` — 1 direct child node(s) with this tag under root
- `spelltokens` — 1 direct child node(s) with this tag under root
- `temp` — 1 direct child node(s) with this tag under root
- `treasureparcels` — 1 direct child node(s) with this tag under root

## Known FG-like Collection Tag Hits (anywhere in tree)

- `battle`: 1
- `charsheet`: 1
- `encounter`: 1
- `image`: 21
- `item`: 1
- `modifiers`: 1
- `npc`: 2
- `quest`: 1
- `treasureparcels`: 1

## Collection-like Structures (heuristic)

- `/root/charsheet/id-00001/featurelist/id-00002/text` — records: 2 — tag: `text` — detail: p
- `/root/charsheet/id-00001/featurelist/id-00003/text` — records: 16 — tag: `text` — detail: p
- `/root/charsheet/id-00001/featurelist/id-00006/text/table` — records: 6 — tag: `table` — detail: tr
- `/root/charsheet/id-00001/featurelist/id-00006/text/table/tr` — records: 2 — tag: `tr` — detail: td
- `/root/charsheet/id-00001/featurelist/id-00007/text` — records: 20 — tag: `text` — detail: p
- `/root/charsheet/id-00001/featurelist/id-00007/text/p` — records: 4 — tag: `p` — detail: i
- `/root/charsheet/id-00001/inventorylist/id-00001/description/linklist` — records: 2 — tag: `linklist` — detail: link
- `/root/charsheet/id-00001/powers/id-00004/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00005/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00006/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00007/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00008/description/table` — records: 9 — tag: `table` — detail: tr
- `/root/charsheet/id-00001/powers/id-00008/description/table/tr` — records: 2 — tag: `tr` — detail: td
- `/root/charsheet/id-00001/powers/id-00010/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00011/description/table` — records: 6 — tag: `table` — detail: tr
- `/root/charsheet/id-00001/powers/id-00011/description/table/tr` — records: 2 — tag: `tr` — detail: td
- `/root/charsheet/id-00001/powers/id-00012/description` — records: 4 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00015/description` — records: 3 — tag: `description` — detail: p
- `/root/charsheet/id-00001/powers/id-00017/description/p` — records: 4 — tag: `p` — detail: i
- `/root/charsheet/id-00002/featurelist/id-00003/text` — records: 5 — tag: `text` — detail: p
- `/root/charsheet/id-00002/featurelist/id-00004/text` — records: 16 — tag: `text` — detail: p
- `/root/charsheet/id-00002/featurelist/id-00009/text/linklist` — records: 10 — tag: `linklist` — detail: link
- `/root/charsheet/id-00002/featurelist/id-00010/text` — records: 7 — tag: `text` — detail: p
- `/root/charsheet/id-00002/featurelist/id-00011/text` — records: 2 — tag: `text` — detail: p
- `/root/charsheet/id-00002/inventorylist/id-00010/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00004/description` — records: 6 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00005/description` — records: 6 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00006/description` — records: 6 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00008/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00009/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00010/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00011/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00012/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00015/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00016/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00002/powers/id-00017/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00003/inventorylist/id-00001/description/p` — records: 2 — tag: `p` — detail: i
- `/root/charsheet/id-00003/powers/id-00002/description` — records: 2 — tag: `description` — detail: p
- `/root/charsheet/id-00003/powers/id-00004/description` — records: 3 — tag: `description` — detail: p
- `/root/charsheet/id-00003/powers/id-00007/description/p` — records: 2 — tag: `p` — detail: i
- … 114 more collection-like paths omitted

## Top 50 Tag Counts

- `public`: 1575
- `holder`: 1035
- `p`: 1025
- `name`: 770
- `b`: 637
- `td`: 636
- `type`: 380
- `tr`: 302
- `bonus`: 291
- `id-00001`: 289
- `locked`: 289
- `score`: 234
- `link`: 177
- `description`: 174
- `class`: 157
- `id-00002`: 146
- `order`: 144
- `i`: 134
- `level`: 127
- `shortcut`: 127
- `recordname`: 126
- `actions`: 121
- `count`: 117
- `desc`: 114
- `stat`: 106
- `text`: 104
- `max`: 95
- `prepared`: 95
- `misc`: 94
- `total`: 92
- `label`: 92
- `spell_token`: 92
- `weight`: 91
- `cast`: 91
- `group`: 91
- `used`: 90
- `carried`: 85
- `id-00003`: 84
- `prof`: 84
- `cost`: 75
- `linklist`: 75
- `savemodifier`: 72
- `subtype`: 68
- `id-00004`: 65
- `attune`: 64
- `durmod`: 61
- `value`: 61
- `dice`: 58
- `duration`: 57
- `ac`: 56

## Structural Preview: `charsheet` name leaves

Text previews only. **Not** a claim that these are verified Player Characters.

- record key `id-00001` → name text preview: `Sorcerer`
- record key `id-00002` → name text preview: `Cleric`
- record key `id-00003` → name text preview: `Infernal Puzzle Box`
- record key `id-00004` → name text preview: `Fighter`
- record key `id-00005` → name text preview: `Warlock`

## Non-Goals Confirmed

- No ability modifiers calculated
- No Atlas Character Objects created
- No synchronization performed
- No website content generated
- Source `db.xml` was not modified

## Closing

> Discovery is not understanding. Discovery is the disciplined act of looking before deciding.

Altitude 0 complete for this source.

