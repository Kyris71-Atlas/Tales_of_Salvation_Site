"""One-off Altitude 0 survey agent script.
Does not modify atlas_core. Does not modify source db.xml files.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

SOURCES = [
    (
        "forge_of_fury_desktop",
        Path(r"C:\Users\Owner\OneDrive\Desktop\001 Forge of Fury\db.xml"),
    ),
    (
        "forge_of_fury_alpha",
        Path(r"C:\Users\Owner\OneDrive\Personal\001 Forge of Fury (campaigns) Alpha\db.xml"),
    ),
    (
        "avernus_dia_2026",
        Path(
            r"C:\Users\Owner\OneDrive\Desktop\Desktop D&D\Avernus\002 Baldur's Gate DIA 2026\db.xml"
        ),
    ),
]

OUT_DIR = Path(
    r"C:\Users\Owner\OneDrive\Desktop\AI\Tales_of_Salvation_Site\reports\discovery"
)

CHAR_REF = re.compile(r"&#(x?[0-9A-Fa-f]+);")
INVALID_RAW = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")


def _is_xml10_char(codepoint: int) -> bool:
    return (
        codepoint in (0x9, 0xA, 0xD)
        or 0x20 <= codepoint <= 0xD7FF
        or 0xE000 <= codepoint <= 0xFFFD
        or 0x10000 <= codepoint <= 0x10FFFF
    )


KNOWN_COLLECTIONS = {
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
}


def sanitize(text: str) -> tuple[str, int, int]:
    removed_refs = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal removed_refs
        body = match.group(1)
        try:
            codepoint = int(body, 16) if body.lower().startswith("x") else int(body, 10)
        except ValueError:
            removed_refs += 1
            return ""
        if _is_xml10_char(codepoint):
            return match.group(0)
        removed_refs += 1
        return ""

    text2 = CHAR_REF.sub(repl, text)
    n_raw = len(INVALID_RAW.findall(text2))
    text2 = INVALID_RAW.sub("", text2)
    return text2, removed_refs, n_raw


def survey(path: Path) -> dict:
    warnings: list[str] = []
    try:
        raw = path.read_bytes()
    except OSError as e:
        return {
            "ok": False,
            "error": f"Could not read file bytes: {e}",
            "file_size": path.stat().st_size if path.exists() else None,
            "sha256_16": None,
            "encoding_tried": None,
            "warnings": [
                "File may be OneDrive cloud-only / provider offline (not hydrated locally)."
            ],
        }
    sha = hashlib.sha256(raw).hexdigest()[:16]

    text = None
    enc_used = None
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            enc_used = enc
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        text = raw.decode("utf-8", errors="replace")
        enc_used = "utf-8-replace"
        warnings.append("Decoded with replacement characters")

    clean, n_ref, n_raw = sanitize(text)
    if n_ref:
        warnings.append(
            f"Removed {n_ref} invalid XML numeric character references for parseability"
        )
    if n_raw:
        warnings.append(
            f"Removed {n_raw} raw control characters for parseability"
        )

    try:
        root = ET.fromstring(clean)
    except ET.ParseError as e:
        return {
            "ok": False,
            "error": str(e),
            "file_size": path.stat().st_size,
            "sha256_16": sha,
            "encoding_tried": enc_used,
            "warnings": warnings,
        }

    tag_counts: Counter[str] = Counter()
    top_children: Counter[str] = Counter()
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
        if children:
            id_like = [c for c in children if c.tag.startswith("id-")]
            if len(children) >= 2 and len(id_like) == len(children):
                collections[shape(parts)] = {
                    "collection_tag": node.tag,
                    "record_count": len(children),
                    "record_key_sample": sorted(c.tag for c in children)[:12],
                }
            else:
                ct = Counter(c.tag for c in children)
                common_tag, cnt = ct.most_common(1)[0]
                if cnt >= 2 and cnt == len(children):
                    collections[shape(parts)] = {
                        "collection_tag": node.tag,
                        "record_count": cnt,
                        "child_tag": common_tag,
                    }

        for child in children:
            walk(child, parts + [child.tag], depth + 1)

    for child in list(root):
        top_children[child.tag] += 1

    walk(root, [root.tag], 0)

    name_previews: list[dict[str, str]] = []
    for parent in root.iter():
        if parent.tag != "charsheet":
            continue
        for rec in list(parent):
            nm = None
            for desc in rec.iter():
                if desc.tag == "name" and desc.text and desc.text.strip():
                    nm = desc.text.strip()[:80]
                    break
            if nm is not None:
                name_previews.append(
                    {"record_key": rec.tag, "name_text_preview": nm}
                )
        break

    return {
        "ok": True,
        "file_size": path.stat().st_size,
        "sha256_16": sha,
        "encoding": enc_used,
        "root_tag": root.tag,
        "root_attrib_keys": sorted(root.attrib.keys()),
        "top_level_sections": sorted(
            top_children.items(), key=lambda x: (-x[1], x[0])
        ),
        "top_level_unique": sorted(top_children.keys()),
        "tag_counts_top50": tag_counts.most_common(50),
        "unique_tags": len(tag_counts),
        "unique_path_shapes": len(path_shapes),
        "total_nodes": sum(tag_counts.values()),
        "text_nodes": text_nodes,
        "attr_nodes": attr_nodes,
        "max_depth": max_depth,
        "collections": dict(sorted(collections.items(), key=lambda x: x[0])),
        "known_collection_hits": {
            k: tag_counts[k] for k in sorted(KNOWN_COLLECTIONS) if k in tag_counts
        },
        "charsheet_name_previews": name_previews,
        "warnings": warnings,
    }


def render_md(name: str, path: Path, result: dict) -> str:
    lines: list[str] = []
    lines.append("# Atlas Discovery Report")
    lines.append("")
    lines.append("**Altitude:** 0 — Source discovery only")
    lines.append(
        "**Engine mode:** Grok Build agent "
        "(resilient parse; atlas_core CLI blocked by invalid FG character refs)"
    )
    lines.append(
        "**Discovery Status:** Complete (structural) / No interpretation"
    )
    lines.append("")
    lines.append("## Source Fingerprint")
    lines.append("")
    lines.append(f"- Source label: `{name}`")
    lines.append(f"- Source file: `{path}`")
    lines.append("- Source format: XML")
    lines.append(
        "- Probable source system: Fantasy Grounds-style campaign database "
        "(filename `db.xml`)"
    )
    lines.append(f"- File size bytes: {result.get('file_size')}")
    lines.append(
        f"- Content sha256 (first 16 hex): `{result.get('sha256_16')}`"
    )
    if result.get("ok"):
        lines.append(f"- Encoding used: {result.get('encoding')}")
        lines.append(f"- Root tag: `{result.get('root_tag')}`")
        keys = result.get("root_attrib_keys") or []
        key_text = ", ".join(keys) if keys else "(none)"
        lines.append(f"- Root attribute keys: {key_text}")
    lines.append("")
    lines.append("## Warnings")
    lines.append("")
    for w in result.get("warnings") or []:
        lines.append(f"- {w}")
    if not result.get("warnings"):
        lines.append("- None")
    lines.append("")

    if not result.get("ok"):
        lines.append("## Blocking Error")
        lines.append("")
        lines.append(f"- Parse failed: {result.get('error')}")
        lines.append("")
        lines.append("Discovery incomplete for this source.")
        lines.append("")
        return "\n".join(lines) + "\n"

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total nodes: {result['total_nodes']}")
    lines.append(f"- Unique tag names: {result['unique_tags']}")
    lines.append(f"- Unique path shapes: {result['unique_path_shapes']}")
    lines.append(f"- Nodes with text: {result['text_nodes']}")
    lines.append(f"- Nodes with attributes: {result['attr_nodes']}")
    lines.append(f"- Max depth: {result['max_depth']}")
    lines.append(
        f"- Collection-like structures: {len(result['collections'])}"
    )
    lines.append("")
    lines.append("## Top-Level Sections")
    lines.append("")
    for tag, count in result["top_level_sections"]:
        lines.append(
            f"- `{tag}` — {count} direct child node(s) with this tag under root"
        )
    lines.append("")
    lines.append("## Known FG-like Collection Tag Hits (anywhere in tree)")
    lines.append("")
    if result["known_collection_hits"]:
        for tag, count in result["known_collection_hits"].items():
            lines.append(f"- `{tag}`: {count}")
    else:
        lines.append(
            "- None of the common FG collection tag names were observed"
        )
    lines.append("")
    lines.append("## Collection-like Structures (heuristic)")
    lines.append("")
    cols = result["collections"]
    if not cols:
        lines.append("- None detected by current heuristics")
    else:
        for i, (cpath, meta) in enumerate(cols.items()):
            if i >= 40:
                lines.append(
                    f"- … {len(cols) - 40} more collection-like paths omitted"
                )
                break
            extra = meta.get("record_key_sample") or meta.get("child_tag") or ""
            lines.append(
                f"- `{cpath}` — records: {meta.get('record_count')} — "
                f"tag: `{meta.get('collection_tag')}` — detail: {extra}"
            )
    lines.append("")
    lines.append("## Top 50 Tag Counts")
    lines.append("")
    for tag, count in result["tag_counts_top50"]:
        lines.append(f"- `{tag}`: {count}")
    lines.append("")
    lines.append("## Structural Preview: `charsheet` name leaves")
    lines.append("")
    lines.append(
        "Text previews only. **Not** a claim that these are verified "
        "Player Characters."
    )
    lines.append("")
    prev = result.get("charsheet_name_previews") or []
    if not prev:
        lines.append(
            "- No `charsheet` collection with `name` text previews found"
        )
    else:
        for p in prev:
            lines.append(
                f"- record key `{p['record_key']}` → name text preview: "
                f"`{p['name_text_preview']}`"
            )
    lines.append("")
    lines.append("## Non-Goals Confirmed")
    lines.append("")
    lines.append("- No ability modifiers calculated")
    lines.append("- No Atlas Character Objects created")
    lines.append("- No synchronization performed")
    lines.append("- No website content generated")
    lines.append("- Source `db.xml` was not modified")
    lines.append("")
    lines.append("## Closing")
    lines.append("")
    lines.append(
        "> Discovery is not understanding. Discovery is the disciplined "
        "act of looking before deciding."
    )
    lines.append("")
    lines.append("Altitude 0 complete for this source.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, path in SOURCES:
        print("====", name, "====")
        print("exists", path.exists())
        if not path.exists():
            continue
        print("size", path.stat().st_size)
        result = survey(path)
        md = render_md(name, path, result)
        out = OUT_DIR / f"atlas_discovery_report_{name}.md"
        out.write_text(md, encoding="utf-8")
        slim = dict(result)
        if slim.get("ok") and len(slim.get("collections") or {}) > 100:
            items = list(slim["collections"].items())
            slim["collections"] = dict(items[:100])
            slim["collections_omitted"] = len(items) - 100
        reg = OUT_DIR / f"atlas_discovery_registry_{name}.json"
        reg.write_text(json.dumps(slim, indent=2), encoding="utf-8")
        print("ok" if result.get("ok") else "FAIL", "->", out)
        if result.get("ok"):
            print(
                "nodes",
                result["total_nodes"],
                "tags",
                result["unique_tags"],
                "cols",
                len(result["collections"]),
            )
            print("top", result["top_level_unique"][:25])
            print("charsheet previews", result.get("charsheet_name_previews"))
        else:
            print("error", result.get("error"))


if __name__ == "__main__":
    main()
