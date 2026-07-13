"""Atlas Discovery Loader.

Responsibility:
    Load a source file and return a parsed document representation.

Rules:
    - No interpretation.
    - No normalization.
    - No Atlas Object creation.
"""

from pathlib import Path
import xml.etree.ElementTree as ET


def load_xml(path: str | Path) -> ET.ElementTree:
    """Load an XML file and return an ElementTree document."""
    source_path = Path(path)
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")
    if not source_path.is_file():
        raise ValueError(f"Source path is not a file: {source_path}")
    return ET.parse(source_path)
