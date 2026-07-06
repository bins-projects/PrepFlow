def validate_questions(questions: list[dict]) -> list[str]:
    """
    Validate parsed legacy question dictionaries.

    This validator checks the parser output before the compiler converts
    questions into canonical PrepFlow Question objects.
    """

    problems = []
    seen_stems = {}
    seen_numbers = {}

    for question in questions:
        number = question.get("question_number", "Unknown")
        stem = (question.get("stem") or "").strip()

        if number in seen_numbers:
            original_number = seen_numbers[number]
            problems.append(
                f"Question {number}: duplicate question number "
                f"(original: Question {original_number})"
            )
        else:
            seen_numbers[number] = number

        if stem:
            if stem in seen_stems:
                original_number = seen_stems[stem]
                preview = stem[:120]
                problems.append(
                    f"Question {number}: duplicate question text "
                    f"(original: Question {original_number}; stem: {preview!r})"
                )
            else:
                seen_stems[stem] = number

        if not stem:
            problems.append(f"Question {number}: missing stem")

        if not question.get("choices"):
            problems.append(f"Question {number}: no answer choices")

        if not question.get("correct_answers"):
            problems.append(f"Question {number}: missing correct answer")

        if not question.get("rationale"):
            problems.append(f"Question {number}: missing rationale")

        if not question.get("question_type"):
            problems.append(f"Question {number}: missing question type")

    return problems