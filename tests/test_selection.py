import pytest

from study.selection import (
    ChapterSelection,
    QuestionRef,
    aggregate_questions,
    build_loaded_question_lookup,
    build_question_lookup,
    normalize_chapter_selections,
)


def test_malformed_identifiers_are_rejected() -> None:
    with pytest.raises(ValueError):
        ChapterSelection(pack_id="", chapter=1, chapter_title="Intro")

    with pytest.raises(ValueError):
        ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="")

    with pytest.raises(ValueError):
        QuestionRef(pack_id="fundamentals", question_id="")

    with pytest.raises(TypeError):
        ChapterSelection(pack_id="fundamentals", chapter=True, chapter_title="Intro")


def test_overlapping_chapter_numbers_across_packs_are_supported() -> None:
    selections = normalize_chapter_selections(
        [
            ChapterSelection(pack_id="fundamentals", chapter=3, chapter_title="Nursing"),
            ChapterSelection(pack_id="pharmacy", chapter=3, chapter_title="Pharmacology"),
        ]
    )

    assert len(selections) == 2
    assert selections[0].chapter == selections[1].chapter == 3


def test_duplicate_question_ids_across_packs_are_preserved() -> None:
    refs = [
        QuestionRef(pack_id="fundamentals", question_id="q1"),
        QuestionRef(pack_id="pharmacy", question_id="q1"),
    ]

    lookup = build_question_lookup(refs)

    assert lookup[("fundamentals", "q1")].pack_id == "fundamentals"
    assert lookup[("pharmacy", "q1")].pack_id == "pharmacy"


def test_two_chapters_from_the_same_pack_are_allowed() -> None:
    selections = normalize_chapter_selections(
        [
            ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro"),
            ChapterSelection(pack_id="fundamentals", chapter=2, chapter_title="Advanced"),
        ]
    )

    assert [selection.chapter for selection in selections] == [1, 2]


def test_exact_duplicate_chapter_selection_is_rejected() -> None:
    with pytest.raises(ValueError):
        normalize_chapter_selections(
            [
                ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro"),
                ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro"),
            ]
        )


def test_duplicate_pack_ids_are_rejected() -> None:
    with pytest.raises(ValueError):
        build_loaded_question_lookup(
            [
                {"pack_id": "fundamentals", "questions": []},
                {"pack_id": "fundamentals", "questions": []},
            ]
        )


def test_iterable_pack_input_uses_real_pack_field() -> None:
    lookup = build_loaded_question_lookup(
        [{"pack_id": "fundamentals", "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Intro"}]}]
    )

    assert lookup[("fundamentals", "Q1")]["id"] == "Q1"


def test_mapping_pack_input_uses_real_pack_field() -> None:
    lookup = build_loaded_question_lookup(
        {"fundamentals": {"pack_id": "fundamentals", "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Intro"}]}}
    )

    assert lookup[("fundamentals", "Q1")]["id"] == "Q1"


def test_mapping_key_conflicts_with_internal_pack_id() -> None:
    with pytest.raises(ValueError):
        build_loaded_question_lookup(
            {"pharmacy": {"pack_id": "fundamentals", "questions": []}}
        )


def test_chapter_title_whitespace_is_normalized() -> None:
    refs = aggregate_questions(
        [{"pack_id": "fundamentals", "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "  Intro  "}]}],
        [ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro")],
    )

    assert [ref.question_id for ref in refs] == ["Q1"]


def test_aggregate_questions_from_two_packs() -> None:
    packs = [
        {
            "pack_id": "fundamentals",
            "questions": [
                {"id": "Q1", "chapter": 1, "chapter_title": "Intro"},
                {"id": "Q2", "chapter": 2, "chapter_title": "Intro"},
            ],
        },
        {
            "pack_id": "pharmacy",
            "questions": [
                {"id": "Q10", "chapter": 1, "chapter_title": "Dosage"},
            ],
        },
    ]

    selections = [
        ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro"),
        ChapterSelection(pack_id="pharmacy", chapter=1, chapter_title="Dosage"),
    ]

    refs = aggregate_questions(packs, selections)

    assert [ref.question_id for ref in refs] == ["Q1", "Q10"]


def test_reference_order_is_deterministic_before_shuffle() -> None:
    refs = aggregate_questions(
        [
            {
                "pack_id": "fundamentals",
                "questions": [
                    {"id": "Q1", "chapter": 1, "chapter_title": "Intro"},
                    {"id": "Q2", "chapter": 1, "chapter_title": "Intro"},
                ],
            },
            {
                "pack_id": "pharmacy",
                "questions": [
                    {"id": "Q3", "chapter": 1, "chapter_title": "Dosage"},
                ],
            },
        ],
        [
            ChapterSelection(pack_id="fundamentals", chapter=1, chapter_title="Intro"),
            ChapterSelection(pack_id="pharmacy", chapter=1, chapter_title="Dosage"),
        ],
    )

    assert [ref.question_id for ref in refs] == ["Q1", "Q2", "Q3"]


def test_actual_question_lookup_is_keyed_by_pack_and_question_id() -> None:
    lookup = build_loaded_question_lookup(
        [
            {
                "pack_id": "fundamentals",
                "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Intro"}],
            },
            {
                "pack_id": "pharmacy",
                "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Dosage"}],
            },
        ]
    )

    assert lookup[("fundamentals", "Q1")]["chapter_title"] == "Intro"
    assert lookup[("pharmacy", "Q1")]["chapter_title"] == "Dosage"


def test_malformed_pack_and_question_identifiers_are_rejected() -> None:
    with pytest.raises(ValueError):
        build_loaded_question_lookup([{"pack_id": "", "questions": []}])

    with pytest.raises(ValueError):
        build_loaded_question_lookup([{"pack_id": "fundamentals", "questions": [{"id": "", "chapter": 1}]}])
