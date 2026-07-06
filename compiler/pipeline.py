from dataclasses import dataclass

from compiler.models import Pack
from compiler.validator import validate_questions
from compiler.deduplicator import deduplicate_questions
from compiler.builder import build_pack, build_questions


@dataclass
class CompilationResult:
    pack: Pack | None
    problems: list[str]
    removed_duplicates: list[str]


def compile_questions(
    questions: list[dict],
    *,
    pack_id: str,
    title: str,
) -> CompilationResult:
    """
    Compile parsed question dictionaries into a canonical PrepFlow Pack.
    """

    problems = validate_questions(questions)

    if problems:
        return CompilationResult(
            pack=None,
            problems=problems,
            removed_duplicates=[],
        )

    result = deduplicate_questions(questions)

    canonical_questions = build_questions(result.questions)

    pack = build_pack(
        canonical_questions,
        pack_id=pack_id,
        title=title,
    )

    return CompilationResult(
        pack=pack,
        problems=[],
        removed_duplicates=result.removed,
    )