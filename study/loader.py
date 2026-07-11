import json
import sys
from pathlib import Path


def application_dir():
    if getattr(sys, "frozen", False):
       return Path(sys._MEIPASS) 

    return Path(__file__).resolve().parent.parent


PACKS_DIR = application_dir() / "packs"


def list_packs():
    packs = []

    for path in sorted(PACKS_DIR.glob("*.prepflow.json")):
        with path.open("r", encoding="utf-8") as file:
            pack = json.load(file)

        if pack.get("format") != "prepflow_pack":
            continue

        packs.append({
            "path": path,
            "title": pack.get("title", path.stem),
            "question_count": len(pack.get("questions", [])),
        })

    return packs


def load_pack(path):
    pack_path = Path(path)

    with pack_path.open("r", encoding="utf-8") as file:
        pack = json.load(file)

    if pack.get("format") != "prepflow_pack":
        raise ValueError(f"Invalid PrepFlow pack format: {pack_path}")

    return pack