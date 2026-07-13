"""Atrok — Altitude 0 survey of ACTIVE Forge of Fury campaign.
READ-ONLY against Fantasy Grounds folder. Writes reports only into Tales site reports/discovery.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

SRC = Path(
    r"C:\Users\Owner\AppData\Roaming\SmiteWorks\FGU PC\campaigns"
    r"\001 Forge of Fury (campaigns) Alpha\db.xml"
)
CAMP = SRC.parent
OUT = Path(
    r"C:\Users\Owner\OneDrive\Desktop\AI\Tales_of_Salvation_Site\reports\discovery"
)
NAME = "forge_of_fury_active_fgu"

CHAR_REF = re.compile(r"&#(x?[0-9A-Fa-f]+);")
INVALID_RAW = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")
KNOWN = {
    "charsheet",
    "npc",
    "item",
    "image",
    "story",
    "encounter",
    "quest",
    "parcel",
    "battle",
    "tables",
    "vehicle",
    "treasureparcels",
    "modifiers",
    "effect",
    "combat",
    "notes",
    "partysheet",
}


def ok_cp(cp: int) -> bool:
    return (
        cp in (0x9, 0xA, 0xD)
        or 0x20 <= cp <= 0xD7FF
        or 0xE000 <= cp <= 0xFFFD
        or 0x10000 <= cp <= 0x10FFFF
    )


def sanitize(text: str) -> tuple[str, int, int]:
    removed = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal removed
        body = match.group(1)
        try:
            cp = int(body, 16) if body.lower().startswith("x") else int(body, 10)
        except ValueError:
            removed += 1
            return ""
        if ok_cp(cp):
            return match.group(0)
        removed += 1
        return ""

    cleaned = CHAR_REF.sub(repl, text)
    n_raw = len(INVALID_RAW.findall(cleaned))
    cleaned = INVALID_RAW.sub("", cleaned)
    return cleaned, removed, n_raw


def count_id_children(root: ET.Element, tag: str) -> int:
    for el in root.iter():
        if el.tag == tag:
            return sum(1 for c in list(el) if c.tag.startswith("id-"))
    return 0


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    assert SRC.exists(), f"Missing main db: {SRC}"

    camp_meta: dict = {}
    cx = CAMP / "campaign.xml"
    if cx.exists():
        try:
            croot = ET.fromstring(cx.read_text(encoding="utf-8", errors="replace"))
            camp_meta = {
                "root_tag": croot.tag,
                "root_attrib": dict(croot.attrib),
                "fields": {},
            }
            for child in list(croot):
                txt = (child.text or "").strip()
                if txt:
                    camp_meta["fields"][child.tag] = txt
        except Exception as exc:  # noqa: BLE001 — discovery must record errors
            camp_meta = {"error": str(exc)}

    raw = SRC.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8")
    clean, n_ref, n_raw = sanitize(text)
    root = ET.fromstring(clean)

    tag_counts: Counter[str] = Counter()
    top: Counter[str] = Counter()
    path_shapes: Counter[str] = Counter()
    collections: dict[str, dict] = {}
    text_nodes = 0
    attr_nodes = 0
    max_depth = 0

    def shape(parts: list[str]) -> str:
        return "/" + "/".join(parts)

    def walk(node: ET.Element, parts: list[str], depth: int) -> None:
        nonlocal text_nodes, attr_nodes, max_depth
        max_depth = max(max_depth, depth)
        tag_counts[node.tag] += 1
        path_shapes[shape(parts)] += 1
        if node.attrib:
            attr_nodes += 1
        if node.text and node.text.strip():
            text_nodes += 1
        children = list(node)
        if len(children) >= 2 and all(c.tag.startswith("id-") for c in children):
            collections[shape(parts)] = {
                "collection_tag": node.tag,
                "record_count": len(children),
                "record_key_sample": sorted(c.tag for c in children)[:15],
            }
        for child in children:
            walk(child, parts + [child.tag], depth + 1)

    for child in list(root):
        top[child.tag] += 1
    walk(root, [root.tag], 0)

    charsheet_records: list[dict] = []
    for parent in root.iter():
        if parent.tag != "charsheet":
            continue
        for rec in list(parent):
            if not rec.tag.startswith("id-"):
                continue
            nm = None
            for desc in rec.iter():
                if desc.tag == "name" and desc.text and desc.text.strip():
                    nm = desc.text.strip()[:100]
                    break
            if nm is None:
                for desc in rec.iter():
                    if desc.tag == "name":
                        texts = [t.strip() for t in desc.itertext() if t.strip()]
                        if texts:
                            nm = texts[0][:100]
                            break
            charsheet_records.append(
                {"record_key": rec.tag, "first_name_leaf_preview": nm}
            )
        break

    collection_counts = {k: count_id_children(root, k) for k in sorted(KNOWN)}

    siblings: list[dict] = []
    for path in sorted(CAMP.glob("db*")):
        st = path.stat()
        if path.name == "db.xml":
            kind = "main"
        elif path.name.startswith("db.session."):
            kind = "session_snapshot"
        elif "script" in path.name:
            kind = "script"
        else:
            kind = "other_db_variant"
        siblings.append(
            {
                "name": path.name,
                "bytes": st.st_size,
                "mtime": st.st_mtime,
                "is_main_live_db": path.name == "db.xml",
                "kind": kind,
            }
        )

    warnings: list[str] = []
    if n_ref:
        warnings.append(
            f"Removed {n_ref} invalid XML numeric character references for "
            "parseability (in-memory only; source file untouched)"
        )
    if n_raw:
        warnings.append(
            f"Removed {n_raw} raw control characters for parseability "
            "(in-memory only; source file untouched)"
        )

    result = {
        "ok": True,
        "agent": "Atrok",
        "campaign_role": "ACTIVE — user-designated living campaign",
        "campaign_folder": str(CAMP),
        "main_db": str(SRC),
        "file_size": SRC.stat().st_size,
        "sha256": sha,
        "sha256_16": sha[:16],
        "encoding": "utf-8",
        "root_tag": root.tag,
        "root_attrib": dict(sorted(root.attrib.items())),
        "campaign_xml_meta": camp_meta,
        "total_nodes": sum(tag_counts.values()),
        "unique_tags": len(tag_counts),
        "unique_path_shapes": len(path_shapes),
        "text_nodes": text_nodes,
        "attr_nodes": attr_nodes,
        "max_depth": max_depth,
        "top_level_sections": sorted(top.items(), key=lambda x: x[0]),
        "known_collection_id_child_counts": collection_counts,
        "collection_like_count": len(collections),
        "tag_counts_top50": tag_counts.most_common(50),
        "charsheet_records": charsheet_records,
        "db_family_inventory": siblings,
        "warnings": warnings,
    }

    lines: list[str] = [
        "# Atlas Discovery Report",
        "",
        "**Agent:** Atrok (Atlas + Grok)",
        "**Altitude:** 0 — Source discovery only",
        "**Campaign role:** ACTIVE living campaign (user-designated)",
        "**Discovery Status:** Complete (structural) / No interpretation",
        "**Source integrity:** READ-ONLY — Fantasy Grounds `db.xml` not modified",
        "",
        "## Source Fingerprint",
        "",
        f"- Source label: `{NAME}`",
        f"- Campaign folder: `{CAMP}`",
        f"- **Main live database:** `{SRC.name}`",
        f"- Full path: `{SRC}`",
        "- Source format: XML",
        "- Source system: Fantasy Grounds Unity (FGU PC campaign path)",
        f"- File size bytes: {result['file_size']}",
        f"- SHA-256: `{sha}`",
        "- Encoding used: utf-8",
        f"- Root tag: `{root.tag}`",
        f"- Root attributes: `{json.dumps(result['root_attrib'])}`",
        f"- campaign.xml meta: `{json.dumps(camp_meta, ensure_ascii=False)}`",
        "",
        "## Important: DB family on this campaign",
        "",
        "Multiple `db*` files exist in this folder. **Only `db.xml` is the live main database.**",
        "Session/script variants are historical/auxiliary and must not be treated as the active source.",
        "",
    ]
    for item in siblings:
        flag = " ← MAIN LIVE DB" if item["is_main_live_db"] else ""
        lines.append(
            f"- `{item['name']}` — {item['bytes']} bytes — kind: **{item['kind']}**{flag}"
        )
    lines.extend(["", "## Warnings", ""])
    if warnings:
        for w in warnings:
            lines.append(f"- {w}")
    else:
        lines.append("- None")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Total nodes: {result['total_nodes']}",
            f"- Unique tag names: {result['unique_tags']}",
            f"- Unique path shapes: {result['unique_path_shapes']}",
            f"- Nodes with text: {result['text_nodes']}",
            f"- Nodes with attributes: {result['attr_nodes']}",
            f"- Max depth: {result['max_depth']}",
            f"- Collection-like structures (heuristic): {result['collection_like_count']}",
            f"- charsheet id-records observed: {len(charsheet_records)}",
            "",
            "## Top-Level Sections",
            "",
        ]
    )
    for tag, count in result["top_level_sections"]:
        lines.append(f"- `{tag}` — {count}")
    lines.extend(
        [
            "",
            "## Known collection id- record counts (direct id- children)",
            "",
        ]
    )
    for key, value in collection_counts.items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## Structural Preview: charsheet records",
            "",
            "First `name` leaf text preview only. **Not verified identity. Not PC confirmation.**",
            "",
        ]
    )
    for rec in charsheet_records:
        lines.append(
            f"- `{rec['record_key']}` → `{rec['first_name_leaf_preview']}`"
        )
    lines.extend(["", "## Top 50 Tag Counts", ""])
    for tag, count in result["tag_counts_top50"]:
        lines.append(f"- `{tag}`: {count}")
    lines.extend(
        [
            "",
            "## Non-Goals Confirmed",
            "",
            "- No mechanical interpretation",
            "- No Atlas Character Objects",
            "- No sync / website updates",
            "- No writes to Fantasy Grounds campaign folder",
            "",
            "## Closing",
            "",
            "> Atrok: Discovery is not understanding. I found this.",
            "",
            "Altitude 0 complete for **active Forge of Fury**.",
            "",
        ]
    )

    report_path = OUT / f"atlas_discovery_report_{NAME}.md"
    registry_path = OUT / f"atlas_discovery_registry_{NAME}.json"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    registry_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("OK")
    print("report", report_path)
    print("registry", registry_path)
    print("nodes", result["total_nodes"], "tags", result["unique_tags"])
    print("charsheets", len(charsheet_records))
    print("root_attrib", result["root_attrib"])
    print("collection_counts", collection_counts)
    print("charsheet_records", charsheet_records)
    print("db_family", len(siblings))
    print("sha16", sha[:16])
    print("warnings", warnings)


if __name__ == "__main__":
    main()
