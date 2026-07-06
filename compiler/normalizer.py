def normalize_question(question: dict) -> dict:
    """
    Normalize supported legacy question dictionary formats into one
    compiler input schema.

    Canonical compiler input fields:

    - id
    - source
    - chapter
    - chapter_title
    - question_number
    - question_type
    - stem
    - choices
    - correct_answers
    - rationale
    - metadata
    """

    correct_answer = question.get("correct_answers")

    if correct_answer is None:
        correct_answer = question.get("correct_answer")

    if isinstance(correct_answer, str):
        correct_answers = [correct_answer]
    elif isinstance(correct_answer, list):
        correct_answers = correct_answer
    elif correct_answer is None:
        correct_answers = []
    else:
        correct_answers = [str(correct_answer)]

    return {
        "id": question.get("id"),
        "source": question.get("source"),
        "chapter": question.get("chapter"),
        "chapter_title": question.get("chapter_title"),
        "question_number": question.get("question_number"),
        "question_type": question.get("question_type"),
        "stem": question.get("stem") or question.get("prompt") or "",
        "choices": question.get("choices") or {},
        "correct_answers": correct_answers,
        "rationale": question.get("rationale") or "",
        "metadata": question.get("metadata") or {},
    }


def normalize_questions(questions: list[dict]) -> list[dict]:
    """
    Normalize a list of supported question dictionaries.
    """

    return [normalize_question(question) for question in questions]