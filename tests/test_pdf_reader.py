from pathlib import Path

import pytest

from compiler.pdf_reader import read_pdf


def test_pdf_reader_rejects_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.pdf"

    with pytest.raises(FileNotFoundError):
        read_pdf(missing)


def test_pdf_reader_rejects_non_pdf_file(tmp_path: Path) -> None:
    source = tmp_path / "source.txt"
    source.write_text("example", encoding="utf-8")

    with pytest.raises(ValueError, match="Expected a PDF"):
        read_pdf(source)
