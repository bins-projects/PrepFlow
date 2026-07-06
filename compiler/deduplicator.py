from dataclasses import dataclass


@dataclass
class DeduplicationResult:
    questions: list[dict]
    removed: list[str]


def deduplicate_questions(questions: list[dict]) -> DeduplicationResult:
    """
    Remove duplicate parsed question dictionaries before canonical building.

    Rules:
    - Keep the first occurrence.
    - Remove later questions with duplicate question numbers.
    - Remove later questions with duplicate stems.
    - Report every removal.
    - Do not repair missing source data.
    """

    deduplicated = []
    removed = []

    seen_numbers = {}
    seen_stems = {}

    for question in questions:
        number = question.get("question_number", "Unknown")
        stem = (question.get("stem") or "").strip()

        if number in seen_numbers:
            original_number = seen_numbers[number]
            removed.append(
                f"Question {number}: removed duplicate question number "
                f"(original: Question {original_number})"
            )
            continue

        if stem and stem in seen_stems:
            original_number = seen_stems[stem]
            preview = stem[:120]
            removed.append(
                f"Question {number}: removed duplicate question text "
                f"(original: Question {original_number}; stem: {preview!r})"
            )
            continue

        seen_numbers[number] = number

        if stem:
            seen_stems[stem] = number

        deduplicated.append(question)

    return DeduplicationResult(
        questions=deduplicated,
        removed=removed,
    )