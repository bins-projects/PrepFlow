#!/usr/bin/env python3
"""Refresh the generic web catalog after installing a validated Pack."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pack_catalog import write_catalog


def main() -> None:
    parser = argparse.ArgumentParser(description="Create the web Pack catalog from installed PrepFlow Packs")
    parser.add_argument("--packs", type=Path, default=ROOT / "packs")
    parser.add_argument("--output", type=Path, default=ROOT / "web" / "data" / "pack-catalog.json")
    args = parser.parse_args()
    print(write_catalog(args.packs, args.output))


if __name__ == "__main__":
    main()
