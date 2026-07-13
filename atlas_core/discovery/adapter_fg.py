"""Fantasy Grounds Discovery Adapter.

Responsibility:
    Convert Fantasy Grounds XML into an Atlas Discovery Registry.

This adapter is Fantasy Grounds focused, but Atlas Core should not be locked
into Fantasy Grounds as the only future source system.
"""

from pathlib import Path
from .loader import load_xml
from .fingerprint import fingerprint_xml_root
from .scanner import scan_xml
from .registry import build_registry, DiscoveryRegistry


def discover_fantasy_grounds_xml(path: str | Path) -> DiscoveryRegistry:
    """Run the Sprint 0 discovery pipeline for a Fantasy Grounds XML file."""
    document = load_xml(path)
    root = document.getroot()
    fingerprint = fingerprint_xml_root(root.tag)
    nodes = scan_xml(root)
    return build_registry(fingerprint, nodes)
