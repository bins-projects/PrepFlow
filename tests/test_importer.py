from pathlib import Path

import pytest

from compiler.importer import (
    ImportRequest,
    detect_source_type,
    extract_source,
    validate_request,
)


def test_detect_source_type_accepts_pdf() -> None:
    assert detect_source_type(Path("book.PDF")) == "pdf"


def test_detect_source_type_rejects_unknown_format() -> None:
    with pytest.raises(ValueError, match="Unsupported source file type"):
        detect_source_type(Path("book.epub"))


def test_validate_request_rejects_invalid_pack_id() -> None:
    request = ImportRequest(
        source_path=Path("book.pdf"),
        pack_id="Medical Surgical!",
        title="Medical-Surgical",
    )

    with pytest.raises(ValueError, match="Pack ID"):
        validate_request(request)


def test_extract_source_writes_raw_artifact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = tmp_path / "book.pdf"
    source.write_bytes(b"placeholder")

    monkeypatch.setattr(
        "compiler.importer.read_pdf",
        lambda path: "Chapter 1\nExample extracted text",
    )

    request = ImportRequest(
        source_path=source,
        pack_id="example-book",
        title="Example Book",
        workspace_root=tmp_path / "imports",
    )

    result = extract_source(request)

    assert result.source_type == "pdf"
    assert result.raw_text == "Chapter 1\nExample extracted text"
    assert result.raw_artifact.read_text(
        encoding="utf-8"
    ) == result.raw_text
    assert result.raw_artifact == (
        tmp_path / "imports" / "example-book" / "01_raw.txt"
    )
