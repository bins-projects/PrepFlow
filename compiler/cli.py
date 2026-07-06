import json
import sys
from pathlib import Path
from collections import defaultdict

from compiler.docx_reader import read_docx
from compiler.tokenizer import tokenize
from compiler.parser import parse_questions
from compiler.pipeline import compile_questions


def print_validation_failure(problems: list[str]) -> None:
    print()
    print("Validation failed.")
    print(f"Problems found: {len(problems)}")
    print()

    grouped_problems = defaultdict(list)

    for problem in problems:
        if ": " in problem:
            question_label, issue = problem.split(": ", 1)
            grouped_problems[question_label].append(issue)
        else:
            grouped_problems["General"].append(problem)

    for question_label, issues in grouped_problems.items():
        print(question_label)
        for issue in issues:
            print(f"  - {issue}")
        print()

    print()
    print("Compilation aborted.")


def print_deduplication(removed: list[str]) -> None:
    if not removed:
        return

    print()
    print("Deduplication")
    print(f"Questions removed: {len(removed)}")

    for removal in removed:
        print(f"- {removal}")


def compile_docx(source_path: str) -> None:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    raw_document = read_docx(source_path)

    raw_path = output_dir / "01_raw_document.json"
    with raw_path.open("w", encoding="utf-8") as file:
        json.dump(raw_document, file, indent=2, ensure_ascii=False)

    tokenized = tokenize(raw_document)

    token_path = output_dir / "02_tokens.json"
    with token_path.open("w", encoding="utf-8") as file:
        json.dump(tokenized, file, indent=2, ensure_ascii=False)

    question_path = output_dir / "03_questions.json"
    questions = parse_questions(str(token_path), str(question_path))

    result = compile_questions(
        questions,
        pack_id="compiled_pack",
        title=Path(source_path).stem,
    )

    if result.problems:
        print_validation_failure(result.problems)
        sys.exit(1)

    print_deduplication(result.removed)

    print("Loaded document.")
    print(f"Source: {raw_document['source_path']}")
    print(f"Paragraphs: {raw_document['paragraph_count']}")
    print(f"Raw artifact: {raw_path}")
    print()
    print("Tokenized document.")
    print(f"Tokens: {tokenized['token_count']}")
    print(f"Token artifact: {token_path}")
    print()
    print("Parsed questions.")
    print(f"Question blocks: {len(questions)}")
    print(f"Question artifact: {question_path}")
    print()
    print("Validation.")
    print(f"Problems found: {len(result.problems)}")
    print()
    print(f"Canonical questions built: {len(result.questions)}")
    print(f"Pack built: {result.pack.id}")


def compile_json(source_path: str) -> None:
    with open(source_path, "r", encoding="utf-8") as file:
        questions = json.load(file)

    result = compile_questions(
        questions,
        pack_id=Path(source_path).stem,
        title=Path(source_path).stem,
    )

    if result.problems:
        print_validation_failure(result.problems)
        sys.exit(1)

    print_deduplication(result.removed)

    print("Loaded question JSON.")
    print(f"Source: {source_path}")
    print(f"Question blocks: {len(questions)}")
    print()
    print("Validation.")
    print(f"Problems found: {len(result.problems)}")
    print()
    print(f"Canonical questions built: {len(result.questions)}")
    print(f"Pack built: {result.pack.id}")


def main():
    print("PrepFlow Compiler")
    print("Version 0.1")
    print()

    if len(sys.argv) < 2:
        print("Usage:")
        print('python3 -m compiler.cli "path/to/question_bank.docx"')
        print('python3 -m compiler.cli "path/to/questions.json"')
        return

    source_path = sys.argv[1]
    suffix = Path(source_path).suffix.lower()

    if suffix == ".docx":
        compile_docx(source_path)
    elif suffix == ".json":
        compile_json(source_path)
    else:
        print(f"Unsupported source file type: {suffix}")
        sys.exit(1)


if __name__ == "__main__":
    main()