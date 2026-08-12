#!/usr/bin/env python3
"""Install one validated Pack and refresh its generic browser catalog entry."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from compiler.repair import RepairError, load_pack
from pack_catalog import write_catalog


def main() -> None:
    parser = argparse.ArgumentParser(description="Install a validated PrepFlow Pack and refresh the browser catalog")
    parser.add_argument("pack", type=Path, help="Validated Pack file to install")
    parser.add_argument("--packs", type=Path, default=ROOT / "packs")
    parser.add_argument("--catalog", type=Path, default=ROOT / "web" / "data" / "pack-catalog.json")
    args = parser.parse_args()
    source = args.pack.resolve()
    if source.is_symlink() or not source.is_file() or source.suffixes[-2:] != [".prepflow", ".json"]:
        raise SystemExit("Pack must be a real .prepflow.json file")
    try:
        load_pack(source)
    except RepairError as error:
        raise SystemExit(f"Pack is invalid: {error}") from error
    destination = args.packs / source.name
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite installed Pack: {destination.name}")
    args.packs.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    try:
        write_catalog(args.packs, args.catalog)
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    print(destination)
    print(args.catalog)


if __name__ == "__main__":
    main()
