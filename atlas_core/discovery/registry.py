"""Atlas Discovery Registry.

Responsibility:
    Store discovered observations in a stable intermediate structure.

The registry is consumed by reports and later interpretation stages.
"""

from dataclasses import dataclass, field
from collections import Counter
from .fingerprint import SourceFingerprint
from .scanner import DiscoveredNode


@dataclass
class DiscoveryRegistry:
    fingerprint: SourceFingerprint
    nodes: list[DiscoveredNode]
    tag_counts: dict[str, int] = field(default_factory=dict)


def build_registry(fingerprint: SourceFingerprint, nodes: list[DiscoveredNode]) -> DiscoveryRegistry:
    """Build a Discovery Registry from fingerprint and scanned nodes."""
    counts = Counter(node.tag for node in nodes)
    return DiscoveryRegistry(
        fingerprint=fingerprint,
        nodes=nodes,
        tag_counts=dict(sorted(counts.items())),
    )
