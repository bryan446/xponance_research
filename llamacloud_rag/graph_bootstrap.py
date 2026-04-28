from __future__ import annotations

import argparse
import json

from .config import get_settings
from .graph_backend import rebuild_graph


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build the finished Neo4j GraphRAG corpus."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and chunk the local corpus without writing to Neo4j.",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Force a full Neo4j graph rebuild even when the corpus hash matches.",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    settings = get_settings()
    summary = rebuild_graph(settings, dry_run=args.dry_run, rebuild=args.rebuild)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
