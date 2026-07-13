"""Command-line entry point for Atlas Discovery Engine Sprint 0."""

from pathlib import Path
import argparse
from discovery.adapter_fg import discover_fantasy_grounds_xml
from discovery.report import generate_markdown_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Atlas Discovery Engine - Fantasy Grounds Sprint 0")
    parser.add_argument("source", help="Path to Fantasy Grounds db.xml")
    parser.add_argument("--out", help="Optional path for Markdown report output")
    args = parser.parse_args()

    registry = discover_fantasy_grounds_xml(args.source)
    report = generate_markdown_report(registry)

    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
