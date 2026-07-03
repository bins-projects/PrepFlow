from pathlib import Path
import json
import re
from pypdf import PdfReader

SOURCE_FILE = Path("source_banks/pharm_test_bank.pdf")
OUTPUT_FILE = Path("output/pharm_questions.json")

CHAPTER_RE = re.compile(r"^Chapter\s+(\d{2}):\s+(.+)$", re.IGNORECASE | re.MULTILINE)
SECTION_RE = re.compile(
    r"\b(MULTIPLE CHOICE|MULTIPLE RESPONSE|COMPLETION|ORDERING)\b",
    re.IGNORECASE,
)
QUESTION_START_RE = re.compile(r"(?m)^\s*(\d+)\.\s+(?![A-H]\s*$)(?=[A-Z])")
CHOICE_RE = re.compile(r"^\s*([a-f])\.\s+(.+)", re.IGNORECASE)
ANS_RE = re.compile(r"\bANS:\s*(.+)")
OBJ_RE = re.compile(r"\bOBJ:\s*(.+)")
NCLEX_RE = re.compile(r"\bNCLEX:\s*(.+)")
KEY_RE = re.compile(r"\b(KEY|MSC):\s*(.+)")


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


def detect_question_type(section_name: str, body: str) -> str:
    section_name = section_name.lower()

    if "ordering" in section_name:
        return "ordered"

    if re.search(
        r"(place the events|prioritize|appropriate sequence|correct order|in what order)",
        body,
        re.IGNORECASE,
    ):
        return "ordered"

    if "multiple response" in section_name:
        return "sata"

    if "completion" in section_name:
        return "completion"

    return "mc"


def split_sections(chapter_text: str) -> list[dict]:
    matches = list(SECTION_RE.finditer(chapter_text))
    sections = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(chapter_text)

        sections.append(
            {
                "name": match.group(1).upper(),
                "text": chapter_text[start:end],
            }
        )

    return sections


def split_question_blocks(section_text: str) -> list[dict]:
    matches = list(QUESTION_START_RE.finditer(section_text))
    blocks = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section_text)

        blocks.append(
            {
                "number": int(match.group(1)),
                "text": section_text[start:end].strip(),
            }
        )

    return blocks


def clean_text(value: str | None) -> str | None:
    if not value:
        return None

    return re.sub(r"\s+", " ", value).strip()


def extract_field(pattern: re.Pattern, text: str) -> str | None:
    match = pattern.search(text)
    if not match:
        return None

    return clean_text(match.group(1))


def strip_answer_metadata(text: str) -> str:
    markers = ["ANS:", "DIF:", "OBJ:", "TOP:", "KEY:", "MSC:", "NCLEX:"]
    cut_points = []

    for marker in markers:
        index = text.find(marker)
        if index != -1:
            cut_points.append(index)

    if not cut_points:
        return text.strip()

    return text[: min(cut_points)].strip()


def parse_choices(question_text: str) -> tuple[str, dict]:
    clean_question_text = strip_answer_metadata(question_text)
    lines = clean_question_text.splitlines()

    prompt_lines = []
    choices = {}
    current_choice = None

    for line in lines:
        choice_match = CHOICE_RE.match(line)

        if choice_match:
            current_choice = choice_match.group(1).lower()
            choices[current_choice] = choice_match.group(2).strip()
            continue

        if current_choice and line.strip():
            choices[current_choice] += " " + line.strip()
        else:
            prompt_lines.append(line.strip())

    prompt = clean_text(" ".join(prompt_lines))

    choices = {key: clean_text(value) for key, value in choices.items()}

    return prompt, choices


def extract_rationale(text: str) -> str | None:
    ans_match = ANS_RE.search(text)
    if not ans_match:
        return None

    after_ans = text[ans_match.end() :]

    stop_markers = ["DIF:", "OBJ:", "TOP:", "KEY:", "MSC:", "NCLEX:"]
    stop_points = []

    for marker in stop_markers:
        index = after_ans.find(marker)
        if index != -1:
            stop_points.append(index)

    rationale = after_ans[: min(stop_points)].strip() if stop_points else after_ans.strip()

    return clean_text(rationale)


def parse_question(chapter: dict, section_name: str, block: dict) -> dict:
    body = block["text"]

    prompt, choices = parse_choices(body)

    question = {
    "id": (
        f"pharm-ch{chapter['chapter']}-"
        f"{section_name.lower().replace(' ', '-')}-"
        f"q{block['number']}"
    ),    
        "source": "pharm_test_bank",
        "chapter": chapter["chapter"],
        "chapter_title": chapter["title"],
        "question_number": block["number"],
        "question_type": detect_question_type(section_name, body),
        "prompt": prompt,
        "choices": choices,
        "correct_answer": extract_field(ANS_RE, body),
        "rationale": extract_rationale(body),
                "is_valid": bool(
            prompt
            and extract_field(ANS_RE, body)
            and extract_rationale(body)
        ),
        "objective": extract_field(OBJ_RE, body),
        "nclex_category": extract_field(NCLEX_RE, body),
        "metadata": {
            "section": section_name,
            "raw_available": True,
            "raw_text": body,
        },
    }
    return question


def build_questions(chapters: list[dict]) -> list[dict]:
    questions = []

    for chapter in chapters:
        sections = split_sections(chapter["text"])

        for section in sections:
            blocks = split_question_blocks(section["text"])

            for block in blocks:
                questions.append(parse_question(chapter, section["name"], block))

    return questions


def main():
    print("PrepFlow pharm Production Importer")
    print("------------------------------------")
    print()

    if not SOURCE_FILE.exists():
        print(f"Source file not found: {SOURCE_FILE}")
        return

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    full_text = read_pdf_text(SOURCE_FILE)
    chapters = split_chapters(full_text)
    questions = build_questions(chapters)
    type_counts = {}
    missing_answers = 0
    missing_rationales = 0
    seen_ids = set()
    duplicate_ids = []
    invalid_questions = 0
    for question in questions:
        qtype = question["question_type"]
        type_counts[qtype] = type_counts.get(qtype, 0) + 1

        if not question["correct_answer"]:
            missing_answers += 1

        if not question["rationale"]:
            missing_rationales += 1
            if not question["is_valid"]:
                invalid_questions += 1
            if question["id"] in seen_ids:
                duplicate_ids.append(question["id"])
            else:
                seen_ids.add(question["id"])
    print(f"Source: {SOURCE_FILE}")
    print(f"Characters extracted: {len(full_text):,}")
    print(f"Chapters found: {len(chapters)}")
    print(f"Questions parsed: {len(questions)}")
    print(f"Question types: {type_counts}")
    print(f"Missing answers: {missing_answers}")
    print(f"Missing rationales: {missing_rationales}")
    print(f"Duplicate IDs: {len(duplicate_ids)}")
    print(f"Invalid questions: {invalid_questions}")
    print()

    for question in questions[:5]:
        print(f"{question['id']}")
        print(f"  Type: {question['question_type']}")
        print(f"  Prompt: {question['prompt']}")
        print(f"  Answer: {question['correct_answer']}")
        print()

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(questions, file, indent=2, ensure_ascii=False)

    print(f"Questions written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()