def validate_questions(questions: list[dict]) -> list[str]:
    """
    Validate normalized legacy question dictionaries.

    This validator checks normalized compiler input before the compiler
    converts questions into canonical PrepFlow Question objects.
    """

    problems = []
    seen_stems = {}
    seen_numbers = {}

    for question in questions:
        number = question.get("question_number", "Unknown")
        chapter = question.get("chapter", "Unknown")
        label = f"Chapter {chapter}, Question {number}"
        number_key = (chapter, number)

        stem = (question.get("stem") or "").strip()

        if number_key in seen_numbers:
            original_label = seen_numbers[number_key]
            problems.append(
                f"{label}: duplicate question number "
                f"(original: {original_label})"
            )
        else:
            seen_numbers[number_key] = label

        if stem:
            if stem in seen_stems:
                original_label = seen_stems[stem]
                preview = stem[:120]
                problems.append(
                    f"{label}: duplicate question text "
                    f"(original: {original_label}; stem: {preview!r})"
                )
            else:
                seen_stems[stem] = label

        if not stem:
            problems.append(f"{label}: missing stem")

        if not question.get("choices"):
            problems.append(f"{label}: no answer choices")

        if not question.get("correct_answers"):
            problems.append(f"{label}: missing correct answer")

        if not question.get("rationale"):
            problems.append(f"{label}: missing rationale")

        if not question.get("question_type"):
            problems.append(f"{label}: missing question type")

    return problems