import argparse
import json
from pathlib import Path


def make_question_id(question: dict, id_prefix: str) -> str:
    section = question.get("section") or "unknown"
    return (
        f"{id_prefix}-ch{int(question['chapter']):02d}-"
        f"{section}-q{int(question['source_question_number']):03d}"
    )


def convert_question(question: dict, id_prefix: str, source: str) -> dict:
    choices = [
        {"label": label.upper(), "text": text}
        for label, text in sorted(question.get("choices", {}).items())
    ]

    return {
        "id": make_question_id(question, id_prefix),
        "source": source,
        "chapter": question.get("chapter"),
        "chapter_title": question.get("chapter_title"),
        "section": question.get("section"),
        "source_question_number": question.get("source_question_number"),
        "type": question.get("type"),
        "stem": question.get("stem"),
        "choices": choices,
        "correct_answers": [answer.upper() for answer in question.get("answer", [])],
        "rationale": question.get("rationale"),
        "metadata": question.get("metadata"),
    }


def write_pack(
    in_path: Path,
    out_path: Path,
    pack_id: str,
    title: str,
    source: str,
    id_prefix: str,
) -> None:
    questions = json.loads(in_path.read_text(encoding="utf-8"))

    pack = {
        "format": "prepflow_pack",
        "version": "1.0",
        "pack_id": pack_id,
        "title": title,
        "questions": [
            convert_question(question, id_prefix, source)
            for question in questions
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(pack, indent=2), encoding="utf-8")

    print(f"Wrote source module: {out_path}")
    print(f"Questions: {len(pack['questions'])}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-path", default="scratch/pharm_module.json")
    parser.add_argument("--out-path", default="packs/pharmacy.prepflow.json")
    parser.add_argument("--pack-id", default="pharmacy")
    parser.add_argument("--title", default="Pharmacy")
    parser.add_argument("--source", default="pharm")
    parser.add_argument("--id-prefix", default="pharm")
    args = parser.parse_args()

    write_pack(
        in_path=Path(args.in_path),
        out_path=Path(args.out_path),
        pack_id=args.pack_id,
        title=args.title,
        source=args.source,
        id_prefix=args.id_prefix,
    )


if __name__ == "__main__":
    main()
