import json
from pathlib import Path


def load_questions(path="packs/cardiac questions.prepflow.json"):
    pack_path = Path(path)

    if not pack_path.exists():
        raise FileNotFoundError(
            f"Could not find {pack_path}. Run the compiler first."
        )

    with pack_path.open("r", encoding="utf-8") as file:
        pack = json.load(file)

    if pack.get("format") != "prepflow_pack":
        raise ValueError(f"Invalid PrepFlow pack format: {pack_path}")

    return pack["questions"]