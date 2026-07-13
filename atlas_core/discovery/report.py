"""Atlas Discovery Report Generator.

Responsibility:
    Render a human-readable report from a Discovery Registry.
"""

from .registry import DiscoveryRegistry


def generate_markdown_report(registry: DiscoveryRegistry) -> str:
    """Generate a deterministic Markdown Discovery Report."""
    lines: list[str] = []
    fp = registry.fingerprint

    lines.append("# Atlas Discovery Report")
    lines.append("")
    lines.append("## Source Fingerprint")
    lines.append("")
    lines.append(f"- Source System: {fp.source_system}")
    lines.append(f"- Source Format: {fp.source_format}")
    lines.append(f"- Confidence: {fp.confidence}")
    lines.append("")
    lines.append("## Fingerprint Notes")
    lines.append("")
    for note in fp.notes:
        lines.append(f"- {note}")
    lines.append("")
    lines.append("## Discovered Tag Counts")
    lines.append("")
    for tag, count in registry.tag_counts.items():
        lines.append(f"- {tag}: {count}")
    lines.append("")
    lines.append("## Discovery Summary")
    lines.append("")
    lines.append(f"- Total Nodes: {len(registry.nodes)}")
    lines.append("")
    lines.append("Discovery does not interpret, validate, synchronize, or create Atlas Objects.")

    return "\n".join(lines) + "\n"
