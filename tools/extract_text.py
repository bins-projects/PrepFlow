from pathlib import Path
from pypdf import PdfReader


def extract_text(pdf_path: Path) -> str:
    """
    Extract raw text from a PDF.

    This stage should preserve the document text as faithfully as possible.
    Cleaning, normalization, and parsing belong to later stages.
    """
    reader = PdfReader(pdf_path)
    text_parts: list[str] = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)

    return "\n".join(text_parts)


if __name__ == "__main__":
    print("extract_text module ready")
