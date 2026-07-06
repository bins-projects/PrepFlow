import json
import sys
from collections import Counter
from pathlib import Path


def load_questions(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        if "questions" in data:
            return data["questions"]

    raise ValueError("Could not locate a questions list in this file.")


def inspect_questions(questions):
    field_counts = Counter()
    question_types = Counter()
    choice_counts = Counter()
    answer_counts = Counter()

    for question in questions:
        for field in question:
            field_counts[field] += 1

        question_types[question.get("question_type", "unknown")] += 1
        choice_counts[len(question.get("choices", []))] += 1
        answer_counts[len(question.get("correct_answers", []))] += 1
        
        missing_answers = [
        question.get("question_number", "Unknown")
        for question in questions
        if len(question.get("correct_answers", [])) == 0
    ]
    print()
    print("PrepFlow Schema Inspector")
    print("=" * 30)
    print()

    print(f"Questions: {len(questions)}")
    print()

    print("Fields")
    print("------")
    for field in sorted(field_counts):
        print(f"{field:20} {field_counts[field]}/{len(questions)}")

    print()
    print("Question Types")
    print("--------------")
    for qtype, count in sorted(question_types.items()):
        print(f"{qtype:20} {count}")

    print()
    print("Choice Counts")
    print("-------------")
    for count, total in sorted(choice_counts.items()):
        print(f"{count} choices{' ':13}{total}")

    print()
    print("Correct Answer Counts")
    print("---------------------")
    for count, total in sorted(answer_counts.items()):
        print(f"{count} answers{' ':12}{total}")
    
    if missing_answers:
        print()
        print("Questions Missing Answers")
        print("-------------------------")
        for number in missing_answers:
            print(f"Question {number}")


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("python tools/schema_inspector.py <questions.json>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    questions = load_questions(path)
    inspect_questions(questions)


if __name__ == "__main__":
    main()