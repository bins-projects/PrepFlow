"""Build the browser-safe catalog for installed PrepFlow Packs.

The static web runtime cannot enumerate the repository's ``packs`` directory.
This module is deliberately metadata-only: it validates installed Pack files and
emits their titles, chapter counts, and relative URLs without duplicating their
questions into ``web/data``.
"""
from __future__ import annotations

import json
import hashlib
from pathlib import Path

from compiler.repair import RepairError, load_pack


CATALOG_FORMAT = "prepflow_pack_catalog"
CATALOG_VERSION = "1.0"

# Decoration is optional.  A Pack absent from this table is still a complete,
# selectable book in the generic UI.
DECORATIONS = {
    "fundamentals": {"theme": "fundamentals", "art": "images/quiz-builder/books/fundamentals-closed.png"},
    "pharmacy": {"theme": "pharm", "art": "images/quiz-builder/books/pharm-closed.png?v=20260727-pharm-2"},
    "medical_surgical": {"theme": "med-surg", "art": "images/quiz-builder/books/medsurg-closed.png"},
}


def pack_catalog(pack_directory: Path) -> dict:
    """Return a deterministic catalog for every valid installed Pack."""
    books = []
    seen_ids: set[str] = set()
    for path in sorted(pack_directory.glob("*.prepflow.json"), key=lambda item: item.name.casefold()):
        try:
            pack = load_pack(path)
        except RepairError as error:
            raise ValueError(f"Invalid installed Pack {path.name}: {error}") from error
        pack_id = pack["pack_id"]
        title = pack.get("title")
        questions = pack["questions"]
        if pack_id in seen_ids:
            raise ValueError(f"Duplicate installed Pack ID: {pack_id}")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Installed Pack {path.name} is missing a title")
        if not questions:
            raise ValueError(f"Installed Pack {path.name} has no questions")
        if pack.get("version") != "1.0":
            raise ValueError(f"Installed Pack {path.name} has an unsupported version")

        chapters: dict[tuple[int | None, str], int] = {}
        for question in questions:
            if not isinstance(question, dict):
                raise ValueError(f"Installed Pack {path.name} has an invalid question")
            chapter = question.get("chapter")
            chapter_title = question.get("chapter_title") or "Untitled Chapter"
            if chapter is not None and (not isinstance(chapter, int) or chapter < 1):
                raise ValueError(f"Installed Pack {path.name} has an invalid chapter number")
            if not isinstance(chapter_title, str):
                raise ValueError(f"Installed Pack {path.name} has an invalid chapter title")
            chapters[(chapter, chapter_title)] = chapters.get((chapter, chapter_title), 0) + 1

        book = {
            "id": pack_id,
            "title": title.strip(),
            "path": f"../packs/{path.name}",
            "question_count": len(questions),
            "chapter_count": len(chapters),
        }
        book.update(DECORATIONS.get(pack_id, {}))
        books.append(book)
        seen_ids.add(pack_id)
    return {"format": CATALOG_FORMAT, "version": CATALOG_VERSION, "books": books}


def write_catalog(pack_directory: Path, destination: Path) -> Path:
    catalog = pack_catalog(pack_directory)
    destination.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    destination.write_text(serialized, encoding="utf-8")
    # Imported by the service worker. Updating this file is part of a service
    # worker update check, so a catalog change creates a fresh Pack cache for
    # offline use instead of depending on a student opening each new book once.
    cache_version = hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]
    precache_path = destination.parent.parent / "pack-precache.js"
    precache_path.write_text(
        "self.PREPFLOW_PACK_PRECACHE = "
        + json.dumps({"version": cache_version, "urls": [book["path"] for book in catalog["books"]]}, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )
    return destination
