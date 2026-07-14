from compiler.diagnostics import DiagnosticSeverity
from compiler.validator import validate_questions


def test_completion_question_does_not_require_choices() -> None:
    question = {
        "chapter": 1,
        "question_number": 1,
        "question_type": "completion",
        "stem": "What is 70 kg in pounds?",
        "choices": [],
        "correct_answers": ["154"],
        "rationale": "One kilogram equals 2.2 pounds.",
    }

    diagnostics = validate_questions([question])

    assert not any(
        diagnostic.message == "no answer choices"
        for diagnostic in diagnostics
    )

def test_validator_rejects_answer_that_points_to_missing_choice() -> None:
    questions = [
        {
            "chapter": 23,
            "question_number": 2,
            "question_type": "multiple_choice",
            "stem": "What is another term for seizure disorder?",
            "choices": [
                {"label": "B", "text": "Enkephalin"},
                {"label": "C", "text": "Narcolepsy"},
                {"label": "D", "text": "Neuropathy"},
            ],
            "correct_answers": ["A"],
            "rationale": "A seizure disorder is also called epilepsy.",
        }
    ]

    diagnostics = validate_questions(questions)

    assert any(
        diagnostic.severity == DiagnosticSeverity.RECOVERABLE
        and diagnostic.message == "correct answer references missing choice"
        for diagnostic in diagnostics
    )
