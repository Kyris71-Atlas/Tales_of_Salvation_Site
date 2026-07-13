"""Atlas Structure Scanner.

Responsibility:
    Walk the source tree and record what exists.

Rules:
    - Discovery never decides.
    - Everything gets discovered.
    - Output must be deterministic.
"""

from dataclasses import dataclass, field
import xml.etree.ElementTree as ET


@dataclass
class DiscoveredNode:
    path: str
    tag: str
    child_count: int
    has_text: bool
    attributes: dict[str, str] = field(default_factory=dict)


def scan_xml(root: ET.Element) -> list[DiscoveredNode]:
    """Scan an XML tree and return discovered nodes in deterministic order."""
    discovered: list[DiscoveredNode] = []

    def walk(node: ET.Element, path: str) -> None:
        discovered.append(
            DiscoveredNode(
                path=path,
                tag=node.tag,
                child_count=len(list(node)),
                has_text=bool(node.text and node.text.strip()),
                attributes=dict(sorted(node.attrib.items())),
            )
        )
        for index, child in enumerate(list(node)):
            walk(child, f"{path}/{child.tag}[{index}]")

    walk(root, f"/{root.tag}")
    return discovered
