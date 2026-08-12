import json
from pathlib import Path
import subprocess
import sys

import pytest

from tools.pack_catalog import CATALOG_FORMAT, pack_catalog, write_catalog


def write_pack(path: Path, *, pack_id: str = "pediatrics", title: str = "Pediatrics") -> None:
    path.write_text(json.dumps({
        "format": "prepflow_pack", "version": "1.0", "pack_id": pack_id,
        "title": title,
        "questions": [{
            "id": f"PFQ-{pack_id}-000000001", "chapter": 1,
            "chapter_title": "Growth", "type": "multiple_choice", "stem": "Which?",
            "choices": [{"label": "A", "text": "First"}],
            "correct_answers": ["A"], "rationale": "Because.",
        }],
    }), encoding="utf-8")


def test_catalog_includes_valid_unstyled_pack_with_dynamic_metadata(tmp_path: Path) -> None:
    packs = tmp_path / "packs"; packs.mkdir()
    write_pack(packs / "pediatrics.prepflow.json")

    catalog = pack_catalog(packs)

    assert catalog["format"] == CATALOG_FORMAT
    assert catalog["books"] == [{
        "id": "pediatrics", "title": "Pediatrics",
        "path": "../packs/pediatrics.prepflow.json",
        "question_count": 1, "chapter_count": 1,
    }]


def test_catalog_write_is_metadata_only_and_rejects_invalid_installed_pack(tmp_path: Path) -> None:
    packs = tmp_path / "packs"; packs.mkdir()
    write_pack(packs / "valid.prepflow.json", pack_id="valid")
    destination = tmp_path / "web" / "data" / "pack-catalog.json"
    assert write_catalog(packs, destination) == destination
    assert json.loads(destination.read_text(encoding="utf-8"))["books"][0]["id"] == "valid"
    precache = (tmp_path / "web" / "pack-precache.js").read_text(encoding="utf-8")
    assert "../packs/valid.prepflow.json" in precache

    (packs / "broken.prepflow.json").write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="Invalid installed Pack"):
        pack_catalog(packs)


def test_installer_adds_pack_and_catalog_entry_without_book_specific_ui(tmp_path: Path) -> None:
    source = tmp_path / "pediatrics.prepflow.json"
    write_pack(source)
    packs = tmp_path / "installed"; catalog = tmp_path / "web" / "data" / "pack-catalog.json"

    subprocess.run([
        sys.executable, "tools/install_pack.py", str(source),
        "--packs", str(packs), "--catalog", str(catalog),
    ], check=True)

    assert (packs / source.name).is_file()
    assert json.loads(catalog.read_text(encoding="utf-8"))["books"][0]["id"] == "pediatrics"
