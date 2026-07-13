# Atlas Discovery Report

**Altitude:** 0 — Source discovery only
**Engine mode:** Grok Build agent (resilient parse; atlas_core CLI blocked by invalid FG character refs)
**Discovery Status:** Complete (structural) / No interpretation

## Source Fingerprint

- Source label: `avernus_dia_2026`
- Source file: `C:\Users\Owner\OneDrive\Desktop\Desktop D&D\Avernus\002 Baldur's Gate DIA 2026\db.xml`
- Source format: XML
- Probable source system: Fantasy Grounds-style campaign database (filename `db.xml`)
- File size bytes: 5614069
- Content sha256 (first 16 hex): `26bd6756d7228f1c`
- Encoding used: utf-8
- Root tag: `root`
- Root attribute keys: dataversion, release, version

## Warnings

- Removed 2 invalid XML numeric character references for parseability

## Summary

- Total nodes: 106917
- Unique tag names: 3066
- Unique path shapes: 82074
- Nodes with text: 63468
- Nodes with attributes: 50344
- Max depth: 10
- Collection-like structures: 1449

## Top-Level Sections

- `MNMStats` — 1 direct child node(s) with this tag under root
- `ShiftedState` — 1 direct child node(s) with this tag under root
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
- `export` — 1 direct child node(s) with this tag under root
- `feat` — 1 direct child node(s) with this tag under root
- `image` — 1 direct child node(s) with this tag under root
- `item` — 1 direct child node(s) with this tag under root
- `languages` — 1 direct child node(s) with this tag under root
- `library` — 1 direct child node(s) with this tag under root
- `location` — 1 direct child node(s) with this tag under root
- `modifiers` — 1 direct child node(s) with this tag under root
- `motd` — 1 direct child node(s) with this tag under root
- `notes` — 1 direct child node(s) with this tag under root
- `npc` — 1 direct child node(s) with this tag under root
- `oldTokenImage` — 1 direct child node(s) with this tag under root
- `options` — 1 direct child node(s) with this tag under root
- `partysheet` — 1 direct child node(s) with this tag under root
- `picture` — 1 direct child node(s) with this tag under root
- `quest` — 1 direct child node(s) with this tag under root
- `race` — 1 direct child node(s) with this tag under root
- `reference` — 1 direct child node(s) with this tag under root
- `savedACArmor` — 1 direct child node(s) with this tag under root
- `savedACDEX` — 1 direct child node(s) with this tag under root
- `savedACShield` — 1 direct child node(s) with this tag under root
- `savedCHR` — 1 direct child node(s) with this tag under root
- `savedCON` — 1 direct child node(s) with this tag under root
- `savedDEX` — 1 direct child node(s) with this tag under root
- `savedINT` — 1 direct child node(s) with this tag under root
- `savedSTR` — 1 direct child node(s) with this tag under root
- `savedWIS` — 1 direct child node(s) with this tag under root
- `settings` — 1 direct child node(s) with this tag under root
- `skill` — 1 direct child node(s) with this tag under root
- `spell` — 1 direct child node(s) with this tag under root
- `spelltokens` — 1 direct child node(s) with this tag under root
- `tables` — 1 direct child node(s) with this tag under root
- `temp` — 1 direct child node(s) with this tag under root
- `treasureparcels` — 1 direct child node(s) with this tag under root
- `update_notifier` — 1 direct child node(s) with this tag under root
- `vehicle` — 1 direct child node(s) with this tag under root

## Known FG-like Collection Tag Hits (anywhere in tree)

- `battle`: 1
- `charsheet`: 1
- `encounter`: 1
- `image`: 402
- `item`: 1
- `modifiers`: 1
- `npc`: 2
- `quest`: 1
- `tables`: 1
- `treasureparcels`: 1
- `vehicle`: 1

## Collection-like Structures (heuristic)

- `/root/ShiftedState` — records: 2414 — tag: `ShiftedState` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007', 'id-00008', 'id-00009', 'id-00010', 'id-00011', 'id-00012']
- `/root/background` — records: 3 — tag: `background` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/background/id-00003/text/linklist` — records: 4 — tag: `linklist` — detail: link
- `/root/battle/category` — records: 2 — tag: `category` — detail: ['id-00025', 'id-00036']
- `/root/battle/category/id-00025/npclist` — records: 8 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007', 'id-00008']
- `/root/battle/category/id-00036/npclist` — records: 5 — tag: `npclist` — detail: ['id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006']
- `/root/battle/category/id-00036/npclist/id-00002/maplink` — records: 4 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004']
- `/root/battle/category/id-00036/npclist/id-00003/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/category/id-00036/npclist/id-00004/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00001/npclist` — records: 7 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007']
- `/root/battle/id-00001/npclist/id-00001/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00001/npclist/id-00004/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00002/npclist` — records: 2 — tag: `npclist` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00003/npclist` — records: 5 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00006']
- `/root/battle/id-00004/npclist` — records: 8 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007', 'id-00008']
- `/root/battle/id-00005/npclist` — records: 6 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006']
- `/root/battle/id-00006/npclist` — records: 6 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006']
- `/root/battle/id-00006/npclist/id-00002/maplink` — records: 4 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004']
- `/root/battle/id-00006/npclist/id-00003/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00006/npclist/id-00004/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00006/npclist/id-00005/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00006/npclist/id-00006/maplink` — records: 6 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006']
- `/root/battle/id-00007/npclist` — records: 4 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004']
- `/root/battle/id-00008/npclist` — records: 5 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005']
- `/root/battle/id-00009/npclist` — records: 2 — tag: `npclist` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00010/npclist` — records: 8 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007', 'id-00013']
- `/root/battle/id-00010/npclist/id-00001/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00011/npclist/id-00001/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00012/npclist` — records: 3 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00012/npclist/id-00001/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00012/npclist/id-00003/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00013/npclist` — records: 5 — tag: `npclist` — detail: ['id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00007']
- `/root/battle/id-00014/npclist/id-00001/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- `/root/battle/id-00015/npclist` — records: 4 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00005']
- `/root/battle/id-00016/npclist` — records: 4 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00005']
- `/root/battle/id-00016/npclist/id-00002/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00017/npclist` — records: 7 — tag: `npclist` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006', 'id-00007']
- `/root/battle/id-00017/npclist/id-00001/maplink` — records: 2 — tag: `maplink` — detail: ['id-00001', 'id-00002']
- `/root/battle/id-00017/npclist/id-00002/maplink` — records: 6 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003', 'id-00004', 'id-00005', 'id-00006']
- `/root/battle/id-00017/npclist/id-00003/maplink` — records: 3 — tag: `maplink` — detail: ['id-00001', 'id-00002', 'id-00003']
- … 1409 more collection-like paths omitted

## Top 50 Tag Counts

- `public`: 6779
- `name`: 6385
- `holder`: 5965
- `p`: 5752
- `type`: 3136
- `td`: 2737
- `id`: 2587
- `locked`: 2503
- `b`: 2301
- `bonus`: 1922
- `link`: 1859
- `id-00001`: 1683
- `class`: 1628
- `score`: 1464
- `layer`: 1228
- `parentid`: 1228
- `desc`: 1178
- `points`: 1123
- `i`: 1091
- `text`: 1058
- `recordname`: 1020
- `tr`: 975
- `matrix`: 974
- `description`: 955
- `id-00002`: 952
- `occluder`: 847
- `level`: 835
- `count`: 748
- `shortcut`: 738
- `stat`: 699
- `linklist`: 696
- `h`: 680
- `actions`: 676
- `bitmap`: 663
- `prof`: 655
- `total`: 651
- `isidentified`: 631
- `misc`: 622
- `order`: 611
- `record`: 605
- `max`: 571
- `source`: 566
- `id-00003`: 563
- `weight`: 547
- `token`: 530
- `used`: 522
- `carried`: 520
- `prepared`: 468
- `cost`: 462
- `cast`: 460

## Structural Preview: `charsheet` name leaves

Text previews only. **Not** a claim that these are verified Player Characters.

- record key `id-00001` → name text preview: `Infernal Puzzle Box`
- record key `id-00002` → name text preview: `Cleric`
- record key `id-00003` → name text preview: `Paladin`
- record key `id-00004` → name text preview: `0, My druid group is in conflict with these Shadow Druids in the Cloakwood fores`
- record key `id-00005` → name text preview: `Rogue`
- record key `id-00006` → name text preview: `Ranger`
- record key `id-00007` → name text preview: `Monk`
- record key `id-00008` → name text preview: `Sorcerer`
- record key `id-00009` → name text preview: `Ranger`
- record key `id-00010` → name text preview: `Druid`
- record key `id-00011` → name text preview: `Wizard`
- record key `id-00012` → name text preview: `Retainer`
- record key `id-00013` → name text preview: `Retainer`
- record key `id-00014` → name text preview: `Fighter`
- record key `id-00015` → name text preview: `Fighter`
- record key `id-00016` → name text preview: `Lulu`
- record key `id-00017` → name text preview: `Artificer`
- record key `id-00018` → name text preview: `Fighter`
- record key `id-00019` → name text preview: `Homunculus: Artificer level`
- record key `id-00020` → name text preview: `Cleric`
- record key `id-00021` → name text preview: `Monk`
- record key `id-00022` → name text preview: `Quotes: I don't hate uou, I am simply disapointed. You turned into everything th`
- record key `id-00023` → name text preview: `x A Space x`
- record key `id-00024` → name text preview: `Ranger`
- record key `id-00025` → name text preview: `Warlock`
- record key `id-00026` → name text preview: `Defender`
- record key `id-00027` → name text preview: `Warlock`
- record key `id-00028` → name text preview: `Fighter`
- record key `id-00029` → name text preview: `Bard`
- record key `id-00030` → name text preview: `Retainer`
- record key `id-00031` → name text preview: `Fighter`

## Non-Goals Confirmed

- No ability modifiers calculated
- No Atlas Character Objects created
- No synchronization performed
- No website content generated
- Source `db.xml` was not modified

## Closing

> Discovery is not understanding. Discovery is the disciplined act of looking before deciding.

Altitude 0 complete for this source.

