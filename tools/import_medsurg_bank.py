from pathlib import Path
import json
import re
from pypdf import PdfReader

SOURCE_FILE = Path("source_banks/medsurg_test_bank.pdf")
OUTPUT_FILE = Path("output/medsurg_inventory.json")

CHAPTER_RE = re.compile(r"^Chapter\s+(\d{2}):\s+(.+)$", re.IGNORECASE | re.MULTILINE)
SECTION_RE = re.compile(r"^(MULTIPLE CHOICE|MULTIPLE RESPONSE|COMPLETION)$", re.IGNORECASE | re.MULTILINE)
QUESTION_RE = re.compile(r"\n\s*(\d+)\.\s+")
ANSWER_RE = re.compile(r"\bANS:\s*([A-Z,\s]+|[A-Za-z ]+)")
CHOICE_RE = re.compile(r"^([a-f])\.\s+(.+)", re.IGNORECASE)


def read_pdf_text(path: Path) -> str:
    reader = PdfReader(path)
    text_parts = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)

    return "\n".join(text_parts)


def split_chapters(full_text: str) -> list[dict]:
    matches = list(CHAPTER_RE.finditer(full_text))
    chapters = []

    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(full_text)

        chapters.append(
            {
                "chapter": match.group(1),
                "title": match.group(2).strip(),
                "text": full_text[start:end],
            }
        )

    return chapters


def count_question_starts(text: str) -> int:
    return len(QUESTION_RE.findall(text))


def detect_sections(text: str) -> dict:
    return {
        "multiple_choice": bool(re.search(r"\bMULTIPLE CHOICE\b", text, re.IGNORECASE)),
        "multiple_response": bool(re.search(r"\bMULTIPLE RESPONSE\b", text, re.IGNORECASE)),
        "completion": bool(re.search(r"\bCOMPLETION\b", text, re.IGNORECASE)),
        "ordered": bool(re.search(r"(Place the events|Prioritize|appropriate sequence|correct order)", text, re.IGNORECASE)),
    }


def build_inventory(chapters: list[dict]) -> list[dict]:
    inventory = []

    for chapter in chapters:
        text = chapter["text"]
        sections = detect_sections(text)

        inventory.append(
            {
                "chapter": chapter["chapter"],
                "title": chapter["title"],
                "question_starts_found": count_question_starts(text),
                "has_multiple_choice": sections["multiple_choice"],
                "has_multiple_response": sections["multiple_response"],
                "has_completion": sections["completion"],
                "has_ordered": sections["ordered"],
            }
        )

    return inventory


def main():
    print("PrepFlow Med-Surg Importer")
    print("--------------------------")
    print()

    if not SOURCE_FILE.exists():
        print(f"Source file not found: {SOURCE_FILE}")
        return

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    full_text = read_pdf_text(SOURCE_FILE)
    chapters = split_chapters(full_text)
    inventory = build_inventory(chapters)

    print(f"Source: {SOURCE_FILE}")
    print(f"Characters extracted: {len(full_text):,}")
    print(f"Chapters found: {len(chapters)}")
    print()

    for item in inventory[:10]:
        print(f"Chapter {item['chapter']}: {item['title']}")
        print(f"  Question starts found: {item['question_starts_found']}")
        print(f"  MC section: {item['has_multiple_choice']}")
        print(f"  SATA section: {item['has_multiple_response']}")
        print(f"  Completion section: {item['has_completion']}")
        print(f"  Ordered detected: {item['has_ordered']}")
        print()

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=2)

    print(f"Inventory written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()