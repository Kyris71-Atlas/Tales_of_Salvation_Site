"""Atlas Source Fingerprint.

Responsibility:
    Identify the source system and basic source metadata.

For Sprint 0, this is intentionally conservative and Fantasy Grounds focused.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceFingerprint:
    source_system: str
    source_format: str
    confidence: str
    notes: list[str]


def fingerprint_xml_root(root_tag: str) -> SourceFingerprint:
    """Create a basic fingerprint from an XML root tag."""
    if root_tag == "root":
        return SourceFingerprint(
            source_system="Fantasy Grounds Unity",
            source_format="XML",
            confidence="probable",
            notes=["Root tag is 'root', matching common Fantasy Grounds campaign XML structure."],
        )

    return SourceFingerprint(
        source_system="Unknown",
        source_format="XML",
        confidence="low",
        notes=[f"Unrecognized XML root tag: {root_tag}"],
    )
