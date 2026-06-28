import json
import re
from pathlib import Path


QUESTION_RE = re.compile(r"^\s*\*\*(\d+)\.\*\*\s*(.+)")
CHOICE_RE = re.compile(r"^\s*([a-fA-F])\.\s*(.+)")
ANSWER_RE = re.compile(r"^\s*\*\*Answer:\s*([A-Fa-f,\s]+)\*\*")
RATIONALE_RE = re.compile(r"^\s*\*\*Rationale:\*\*\s*(.+)")
def extract_choices(raw_lines: list[str]) -> list[dict]:
    choices = []

    for line in raw_lines:
        match = CHOICE_RE.match(line)

        if match:
            choices.append({
                "label": match.group(1).upper(),
                "text": match.group(2).strip(),
            })

    return choices

def extract_correct_answers(raw_lines: list[str]) -> list[str]:
    for line in raw_lines:
        match = ANSWER_RE.match(line)

        if match:
            answer_text = match.group(1)
            return re.findall(r"[A-Fa-f]", answer_text.upper())

    return []

def extract_rationale(raw_lines: list[str]) -> str | None:
    for line in raw_lines:
        match = RATIONALE_RE.match(line)

        if match:
            return match.group(1).strip()

    return None

def detect_question_type(raw_lines: list[str]) -> str:
    answer_count = len(extract_correct_answers(raw_lines))

    if answer_count > 1:
        return "sata"

    return "multiple_choice"

def parse_questions(tokens_path: str, output_path: str) -> list[dict]:
    """
    Parser v0.2

    Reads tokenized document data and groups it into question blocks.
    Now extracts answer choices from raw lines.
    """

    tokens_file = Path(tokens_path)
    output_file = Path(output_path)

    with tokens_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        tokens = data["tokens"]

    questions = []
    current_question = None

    for token in tokens:
        if isinstance(token, dict):
            text = token.get("text", "").strip()
        else:
            text = str(token).strip()

        if not text:
            continue

        match = QUESTION_RE.match(text)

        if match:
            if current_question:
                current_question["choices"] = extract_choices(current_question["raw_lines"])
                current_question["correct_answers"] = extract_correct_answers(current_question["raw_lines"])
                current_question["rationale"] = extract_rationale(current_question["raw_lines"])
                current_question["question_type"] = detect_question_type(current_question["raw_lines"])
                questions.append(current_question)

            question_number = int(match.group(1))
            stem_start = match.group(2).strip()

            current_question = {
                "question_number": question_number,
                "stem": stem_start,
                "raw_lines": [text],
                "choices": [],
                "correct_answers": [],
                "question_type": None,
                "rationale": None,
            }
        else:
            if current_question:
                current_question["raw_lines"].append(text)

    if current_question:
        current_question["choices"] = extract_choices(current_question["raw_lines"])
        current_question["correct_answers"] = extract_correct_answers(current_question["raw_lines"])
        current_question["rationale"] = extract_rationale(current_question["raw_lines"])
        current_question["question_type"] = detect_question_type(current_question["raw_lines"])
        questions.append(current_question)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    return questions
