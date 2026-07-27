#!/usr/bin/env python3
"""Read-only QA scanner for PrepFlow JSON Packs."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


CONTAMINATION_PATTERNS = {
    "NURSINGTB contamination": re.compile(
        r"N\s*U\s*R\s*S\s*I\s*N\s*G\s*T\s*B(?:\s*\.?\s*C\s*O\s*M)?",
        re.IGNORECASE,
    ),
    "download/distribution marker": re.compile(
        r"downloaded by|distribution of this document|powered by tcpdf",
        re.IGNORECASE,
    ),
    "marketplace marker": re.compile(
        r"stuvia|marketplace|want to earn",
        re.IGNORECASE,
    ),
    "edition metadata": re.compile(
        r"\b\d+(?:st|nd|rd|th)\s+edition\b",
        re.IGNORECASE,
    ),
    "test-bank metadata": re.compile(
        r"\b(?:NCLEX|cognitive level|client needs|integrated process|"
        r"content area|difficulty level|page reference)\b",
        re.IGNORECASE,
    ),
}

TEXT_PATTERNS = {
    "repeated word": re.compile(r"\b([A-Za-z]{2,})\s+\1\b", re.IGNORECASE),
    "space before punctuation": re.compile(r"\s+[,.!?;:]"),
    "multiple spaces": re.compile(r" {2,}"),
    "space inside parentheses": re.compile(r"\(\s+|\s+\)"),
    "detached taxonomy word": re.compile(
        r"(?:^|[.!?]\s+)(Analyzing|Applying|Understanding|Remembering)\s*$",
        re.IGNORECASE,
    ),
    "possible split suffix": re.compile(
        r"\b[A-Za-z]{4,}\s+(?:s|ed|ing|ly|tion|ment|ness|ity|al|ous|ive)\b"
    ),
    "possible broken web text": re.compile(
        r"\b[A-Z]{1,4}(?:\s+[A-Z]{1,4}){2,}\b"
    ),
    "abrupt ending": re.compile(
        r"\b(?:and|or|the|a|an|to|of|for|with|because|which|that|"
        r"analyzing|applying|understanding|remembering)\s*$",
        re.IGNORECASE,
    ),
}

QUESTION_KEYS = ("questions", "items")
ID_KEYS = ("id", "question_id", "uid")
STEM_KEYS = ("stem", "question", "text", "prompt")
CHOICE_KEYS = ("choices", "answers", "options")
CORRECT_KEYS = (
    "correct",
    "correct_answer",
    "correct_answers",
    "answer",
    "answers_correct",
)
RATIONALE_KEYS = ("rationale", "explanation", "feedback")


def first_present(mapping: dict[str, Any], keys: tuple[str, ...]) -> tuple[str | None, Any]:
    for key in keys:
        if key in mapping:
            return key, mapping[key]
    return None, None


def locate_questions(pack: Any) -> list[Any]:
    if isinstance(pack, list):
        return pack

    if isinstance(pack, dict):
        for key in QUESTION_KEYS:
            value = pack.get(key)
            if isinstance(value, list):
                return value

        for value in pack.values():
            if isinstance(value, dict):
                found = locate_questions(value)
                if found:
                    return found

    return []


def compact(text: str, limit: int = 280) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1] + "…"


def question_id(question: dict[str, Any], index: int) -> str:
    for key in ID_KEYS:
        value = question.get(key)
        if value not in (None, ""):
            return str(value)
    return f"QUESTION-{index:04d}"


def chapter_name(question: dict[str, Any]) -> str:
    for key in ("chapter", "chapter_title", "section", "module"):
        value = question.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def iter_text(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from iter_text(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_text(child, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def normalize_choice_labels(choices: Any) -> list[str]:
    labels: list[str] = []

    if isinstance(choices, list):
        for index, choice in enumerate(choices):
            if isinstance(choice, dict):
                label = (
                    choice.get("label")
                    or choice.get("id")
                    or choice.get("key")
                    or chr(65 + index)
                )
            else:
                label = chr(65 + index)
            labels.append(str(label))
    elif isinstance(choices, dict):
        labels.extend(str(key) for key in choices.keys())

    return labels


def normalize_correct_answers(value: Any) -> list[str]:
    if value is None:
        return []

    if isinstance(value, list):
        return [str(item) for item in value]

    if isinstance(value, (str, int, float)):
        return [str(value)]

    return []


def add_finding(
    findings: list[dict[str, Any]],
    *,
    category: str,
    rule: str,
    severity: str,
    qid: str,
    index: int,
    chapter: str,
    path: str,
    text: str,
    detail: str,
) -> None:
    findings.append(
        {
            "category": category,
            "rule": rule,
            "severity": severity,
            "question_id": qid,
            "question_index": index,
            "chapter": chapter,
            "path": path,
            "detail": detail,
            "text": text,
            "excerpt": compact(text),
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--json-report", type=Path, required=True)
    args = parser.parse_args()

    with args.pack.open("r", encoding="utf-8") as handle:
        pack = json.load(handle)

    questions = locate_questions(pack)

    if not questions:
        raise SystemExit("Could not locate a questions list in the Pack.")

    findings: list[dict[str, Any]] = []
    scanned_text_fields = 0

    seen_ids: dict[str, int] = {}
    normalized_stems: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

    for index, raw_question in enumerate(questions, start=1):
        if not isinstance(raw_question, dict):
            add_finding(
                findings,
                category="Structure",
                rule="question is not an object",
                severity="high",
                qid=f"QUESTION-{index:04d}",
                index=index,
                chapter="",
                path=f"$.questions[{index - 1}]",
                text=str(raw_question),
                detail="Question entry is not a JSON object.",
            )
            continue

        qid = question_id(raw_question, index)
        chapter = chapter_name(raw_question)
        base_path = f"$.questions[{index - 1}]"

        if qid in seen_ids:
            add_finding(
                findings,
                category="Structure",
                rule="duplicate question ID",
                severity="high",
                qid=qid,
                index=index,
                chapter=chapter,
                path=f"{base_path}.id",
                text=qid,
                detail=f"Also used by question {seen_ids[qid]}.",
            )
        else:
            seen_ids[qid] = index

        stem_key, stem = first_present(raw_question, STEM_KEYS)
        choice_key, choices = first_present(raw_question, CHOICE_KEYS)
        correct_key, correct = first_present(raw_question, CORRECT_KEYS)
        rationale_key, rationale = first_present(raw_question, RATIONALE_KEYS)

        if not isinstance(stem, str) or not stem.strip():
            add_finding(
                findings,
                category="Structure",
                rule="missing stem",
                severity="high",
                qid=qid,
                index=index,
                chapter=chapter,
                path=base_path,
                text="",
                detail="No usable question stem was found.",
            )
        else:
            normalized = re.sub(r"[^a-z0-9]+", " ", stem.lower()).strip()
            if normalized:
                normalized_stems[normalized].append((index, qid))

        if not isinstance(choices, (list, dict)) or len(choices) < 2:
            add_finding(
                findings,
                category="Structure",
                rule="missing or insufficient choices",
                severity="high",
                qid=qid,
                index=index,
                chapter=chapter,
                path=f"{base_path}.{choice_key or 'choices'}",
                text=str(choices),
                detail="Question has fewer than two answer choices.",
            )

        labels = normalize_choice_labels(choices)
        correct_values = normalize_correct_answers(correct)

        if not correct_values:
            add_finding(
                findings,
                category="Structure",
                rule="missing correct answer",
                severity="high",
                qid=qid,
                index=index,
                chapter=chapter,
                path=f"{base_path}.{correct_key or 'correct'}",
                text=str(correct),
                detail="No correct answer value was found.",
            )

        if len(correct_values) != len(set(correct_values)):
            add_finding(
                findings,
                category="Structure",
                rule="duplicate correct answers",
                severity="high",
                qid=qid,
                index=index,
                chapter=chapter,
                path=f"{base_path}.{correct_key or 'correct'}",
                text=json.dumps(correct_values),
                detail="Correct-answer list contains duplicate values.",
            )

        if labels and correct_values:
            normalized_labels = {label.strip().upper() for label in labels}
            for answer in correct_values:
                answer_norm = answer.strip().upper()

                if answer_norm.isdigit():
                    numeric = int(answer_norm)
                    valid_numeric = 0 <= numeric < len(labels) or 1 <= numeric <= len(labels)
                    if valid_numeric:
                        continue

                if answer_norm not in normalized_labels:
                    add_finding(
                        findings,
                        category="Structure",
                        rule="correct answer not found in choices",
                        severity="high",
                        qid=qid,
                        index=index,
                        chapter=chapter,
                        path=f"{base_path}.{correct_key or 'correct'}",
                        text=answer,
                        detail=f"Available choice labels: {labels}",
                    )

        if not isinstance(rationale, str) or not rationale.strip():
            add_finding(
                findings,
                category="Structure",
                rule="missing rationale",
                severity="medium",
                qid=qid,
                index=index,
                chapter=chapter,
                path=f"{base_path}.{rationale_key or 'rationale'}",
                text="",
                detail="No usable rationale was found.",
            )

        for relative_path, text in iter_text(raw_question, base_path):
            scanned_text_fields += 1

            for rule, pattern in CONTAMINATION_PATTERNS.items():
                if pattern.search(text):
                    add_finding(
                        findings,
                        category="Contamination",
                        rule=rule,
                        severity="high",
                        qid=qid,
                        index=index,
                        chapter=chapter,
                        path=relative_path,
                        text=text,
                        detail="Known source or extraction contamination detected.",
                    )

            for rule, pattern in TEXT_PATTERNS.items():
                if pattern.search(text):
                    severity = "medium"
                    if rule in {"possible broken web text", "abrupt ending"}:
                        severity = "high"

                    add_finding(
                        findings,
                        category="Text",
                        rule=rule,
                        severity=severity,
                        qid=qid,
                        index=index,
                        chapter=chapter,
                        path=relative_path,
                        text=text,
                        detail="Pattern requires human review against the original source.",
                    )

    for normalized, occurrences in normalized_stems.items():
        if len(occurrences) > 1:
            indexes = [item[0] for item in occurrences]
            ids = [item[1] for item in occurrences]

            for index, qid in occurrences:
                add_finding(
                    findings,
                    category="Duplication",
                    rule="exact normalized duplicate stem",
                    severity="medium",
                    qid=qid,
                    index=index,
                    chapter="",
                    path=f"$.questions[{index - 1}]",
                    text=normalized,
                    detail=f"Matching question indexes: {indexes}; IDs: {ids}",
                )

    counts_by_category = Counter(item["category"] for item in findings)
    counts_by_rule = Counter(item["rule"] for item in findings)
    counts_by_severity = Counter(item["severity"] for item in findings)
    affected_questions = {item["question_id"] for item in findings}

    report_data = {
        "pack": str(args.pack),
        "question_count": len(questions),
        "text_fields_scanned": scanned_text_fields,
        "finding_count": len(findings),
        "affected_question_count": len(affected_questions),
        "counts_by_category": dict(sorted(counts_by_category.items())),
        "counts_by_severity": dict(sorted(counts_by_severity.items())),
        "counts_by_rule": dict(sorted(counts_by_rule.items())),
        "findings": findings,
    }

    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(
        json.dumps(report_data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [
        f"# Fundamentals Pack QA Audit",
        "",
        "> Read-only scan. The original Pack was not modified.",
        "",
        "## Summary",
        "",
        f"- Pack: `{args.pack}`",
        f"- Questions scanned: **{len(questions)}**",
        f"- Text fields scanned: **{scanned_text_fields}**",
        f"- Questions with findings: **{len(affected_questions)}**",
        f"- Total findings: **{len(findings)}**",
        "",
        "### Findings by severity",
        "",
    ]

    for severity, count in sorted(counts_by_severity.items()):
        lines.append(f"- {severity}: {count}")

    lines.extend(["", "### Findings by category", ""])

    for category, count in sorted(counts_by_category.items()):
        lines.append(f"- {category}: {count}")

    lines.extend(["", "### Findings by rule", ""])

    for rule, count in counts_by_rule.most_common():
        lines.append(f"- {rule}: {count}")

    lines.extend(["", "## Detailed findings", ""])

    if not findings:
        lines.append("No findings.")
    else:
        for number, item in enumerate(findings, start=1):
            lines.extend(
                [
                    f"### {number}. {item['question_id']} — {item['rule']}",
                    "",
                    f"- Severity: **{item['severity']}**",
                    f"- Category: {item['category']}",
                    f"- Question index: {item['question_index']}",
                    f"- Chapter: {item['chapter'] or 'Not recorded'}",
                    f"- JSON path: `{item['path']}`",
                    f"- Detail: {item['detail']}",
                    "",
                    "```text",
                    item["excerpt"],
                    "```",
                    "",
                ]
            )

    args.report.write_text("\n".join(lines), encoding="utf-8")

    print()
    print("Fundamentals Pack audit complete.")
    print(f"Questions scanned:       {len(questions)}")
    print(f"Text fields scanned:     {scanned_text_fields}")
    print(f"Questions with findings: {len(affected_questions)}")
    print(f"Total findings:          {len(findings)}")
    print()
    print("Findings by severity:")
    for severity, count in sorted(counts_by_severity.items()):
        print(f"  {severity}: {count}")
    print()
    print(f"Markdown report: {args.report}")
    print(f"JSON ledger:     {args.json_report}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
