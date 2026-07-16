"""Strict selection and question-reference models for the custom quiz builder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping


def _normalize_text(value: Any, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    if not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


@dataclass(frozen=True, slots=True)
class ChapterSelection:
    """A chapter selection scoped to a single Pack."""

    pack_id: str
    chapter: int | str | None
    chapter_title: str

    def __init__(self, pack_id: str, chapter: int | str | None, chapter_title: str) -> None:
        if isinstance(chapter, bool) or (
            chapter is not None and not isinstance(chapter, (int, str))
        ):
            raise TypeError("chapter must be an int, str, or None")

        if isinstance(chapter, str) and not chapter.strip():
            raise ValueError("chapter must be a non-empty string")

        object.__setattr__(self, "pack_id", _normalize_text(pack_id, "pack_id"))
        object.__setattr__(self, "chapter", chapter)
        object.__setattr__(self, "chapter_title", _normalize_text(chapter_title, "chapter_title"))


@dataclass(frozen=True, slots=True)
class QuestionRef:
    """A question reference scoped to a single Pack."""

    pack_id: str
    question_id: str

    def __init__(self, pack_id: str, question_id: str) -> None:
        object.__setattr__(self, "pack_id", _normalize_text(pack_id, "pack_id"))
        object.__setattr__(self, "question_id", _normalize_text(question_id, "question_id"))


def _coerce_chapter_selection(value: ChapterSelection | Mapping[str, Any]) -> ChapterSelection:
    if isinstance(value, ChapterSelection):
        return value

    if not isinstance(value, Mapping):
        raise TypeError("chapter selection must be a ChapterSelection or mapping")

    if not {"pack_id", "chapter", "chapter_title"}.issubset(value.keys()):
        raise ValueError("chapter selection must provide pack_id, chapter, and chapter_title")

    return ChapterSelection(
        pack_id=value["pack_id"],
        chapter=value["chapter"],
        chapter_title=value["chapter_title"],
    )


def _coerce_question_ref(value: QuestionRef | Mapping[str, Any]) -> QuestionRef:
    if isinstance(value, QuestionRef):
        return value

    if not isinstance(value, Mapping):
        raise TypeError("question reference must be a QuestionRef or mapping")

    if not {"pack_id", "question_id"}.issubset(value.keys()):
        raise ValueError("question reference must provide pack_id and question_id")

    return QuestionRef(pack_id=value["pack_id"], question_id=value["question_id"])


def normalize_chapter_selections(
    selections: Iterable[ChapterSelection | Mapping[str, Any]] | None,
) -> tuple[ChapterSelection, ...]:
    """Normalize a list of chapter selections into strict ChapterSelection objects."""
    if selections is None:
        return ()

    if isinstance(selections, (str, bytes)):
        raise TypeError("selections must be an iterable of chapter selections")

    normalized: list[ChapterSelection] = []
    seen_keys: set[tuple[str, int | str | None, str]] = set()

    for selection in selections:
        chapter_selection = _coerce_chapter_selection(selection)
        selection_key = (
            chapter_selection.pack_id,
            chapter_selection.chapter,
            chapter_selection.chapter_title,
        )
        if selection_key in seen_keys:
            raise ValueError("duplicate chapter selections are not allowed")
        seen_keys.add(selection_key)
        normalized.append(chapter_selection)

    return tuple(normalized)


def build_question_lookup(
    question_refs: Iterable[QuestionRef | Mapping[str, Any]],
) -> dict[tuple[str, str], QuestionRef]:
    """Build a lookup keyed by (pack_id, question_id)."""
    lookup: dict[tuple[str, str], QuestionRef] = {}

    for question_ref in question_refs:
        ref = _coerce_question_ref(question_ref)
        key = (ref.pack_id, ref.question_id)
        if key in lookup:
            raise ValueError("duplicate question references are not allowed")
        lookup[key] = ref

    return lookup


def _resolve_pack_id(pack: Mapping[str, Any], mapping_key: Any = None) -> str:
    if not isinstance(pack, Mapping):
        raise TypeError("pack entries must be mappings")

    if mapping_key is not None:
        if not isinstance(mapping_key, str) or not mapping_key.strip():
            raise ValueError("pack_id must be a non-empty string")
        normalized_mapping_key = mapping_key.strip()
    else:
        normalized_mapping_key = None

    for field_name in ("id", "pack_id"):
        raw_pack_id = pack.get(field_name)
        if isinstance(raw_pack_id, str) and raw_pack_id.strip():
            resolved_pack_id = raw_pack_id.strip()
            if normalized_mapping_key is not None and normalized_mapping_key != resolved_pack_id:
                raise ValueError("mapping key conflicts with pack internal ID")
            return resolved_pack_id

    raise ValueError("pack_id must be a non-empty string")


def build_loaded_question_lookup(
    packs: Mapping[str, Mapping[str, Any]] | Iterable[Mapping[str, Any]],
) -> dict[tuple[str, str], Mapping[str, Any]]:
    """Build a lookup of actual loaded questions keyed by (pack_id, question_id)."""
    lookup: dict[tuple[str, str], Mapping[str, Any]] = {}
    seen_pack_ids: set[str] = set()

    if isinstance(packs, Mapping):
        for mapping_key, pack in packs.items():
            pack_id = _resolve_pack_id(pack, mapping_key=mapping_key)
            if pack_id in seen_pack_ids:
                raise ValueError("duplicate Pack IDs are not allowed")
            seen_pack_ids.add(pack_id)

            questions = pack.get("questions")
            if not isinstance(questions, list):
                raise TypeError("Pack questions must be a list")

            for question in questions:
                if not isinstance(question, Mapping):
                    raise TypeError("Pack questions must be mappings")

                question_id = question.get("id")
                if not isinstance(question_id, str) or not question_id.strip():
                    raise ValueError("question id must be a non-empty string")

                key = (pack_id, question_id.strip())
                if key in lookup:
                    raise ValueError("duplicate question references are not allowed")
                lookup[key] = question
    else:
        for pack in packs:
            pack_id = _resolve_pack_id(pack)
            if pack_id in seen_pack_ids:
                raise ValueError("duplicate Pack IDs are not allowed")
            seen_pack_ids.add(pack_id)

            questions = pack.get("questions")
            if not isinstance(questions, list):
                raise TypeError("Pack questions must be a list")

            for question in questions:
                if not isinstance(question, Mapping):
                    raise TypeError("Pack questions must be mappings")

                question_id = question.get("id")
                if not isinstance(question_id, str) or not question_id.strip():
                    raise ValueError("question id must be a non-empty string")

                key = (pack_id, question_id.strip())
                if key in lookup:
                    raise ValueError("duplicate question references are not allowed")
                lookup[key] = question

    return lookup


def aggregate_questions(
    packs: Mapping[str, Mapping[str, Any]] | Iterable[Mapping[str, Any]],
    selections: Iterable[ChapterSelection | Mapping[str, Any]],
) -> list[QuestionRef]:
    """Aggregate actual questions from loaded Packs using selected chapter keys."""
    normalized_selections = normalize_chapter_selections(selections)

    if isinstance(packs, Mapping):
        pack_index = {}
        for mapping_key, pack in packs.items():
            pack_id = _resolve_pack_id(pack, mapping_key=mapping_key)
            if pack_id in pack_index:
                raise ValueError("duplicate Pack IDs are not allowed")
            pack_index[pack_id] = pack
    else:
        pack_index = {}
        for pack in packs:
            pack_id = _resolve_pack_id(pack)
            if pack_id in pack_index:
                raise ValueError("duplicate Pack IDs are not allowed")
            pack_index[pack_id] = pack

    aggregated: list[QuestionRef] = []

    for selection in normalized_selections:
        if selection.chapter is None:
            raise ValueError("chapter=None is not supported in this milestone")

        pack = pack_index.get(selection.pack_id)
        if pack is None:
            raise ValueError(f"Pack {selection.pack_id!r} was not found")

        questions = pack.get("questions")
        if not isinstance(questions, list):
            raise TypeError("Pack questions must be a list")

        for question in questions:
            if not isinstance(question, Mapping):
                raise TypeError("Pack questions must be mappings")

            question_id = question.get("id")
            if not isinstance(question_id, str) or not question_id.strip():
                raise ValueError("question id must be a non-empty string")

            question_chapter = question.get("chapter")
            question_chapter_title = _normalize_text(question.get("chapter_title"), "chapter_title")
            if (
                question_chapter == selection.chapter
                and question_chapter_title == selection.chapter_title
            ):
                aggregated.append(
                    QuestionRef(
                        pack_id=selection.pack_id,
                        question_id=question_id.strip(),
                    )
                )

    return aggregated
