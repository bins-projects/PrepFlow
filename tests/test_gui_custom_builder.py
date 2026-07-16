import json

import pytest

import study.save_state as save_state
from study.gui import PrepFlowApp
from study.selection import ChapterSelection


def _make_app() -> PrepFlowApp:
    app = PrepFlowApp.__new__(PrepFlowApp)
    app.builder_selections = []
    app.builder_check_variables = {}
    app.builder_subjects = []
    app.builder_card_count_labels = {}
    app.builder_active_pack_id = None
    app.current_pack_id = "fundamentals"
    app.current_frame = None
    return app


def _make_pack(pack_id: str, title: str, questions: list[dict]) -> dict:
    return {"pack_id": pack_id, "title": title, "questions": questions}


def test_two_chapters_from_one_pack_are_selected() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)
    app._toggle_builder_selection("fundamentals", 2, "Advanced", True)

    assert app._selected_count_for_category("fundamentals") == 2
    assert [selection.chapter for selection in app.builder_selections] == [1, 2]


def test_selections_are_preserved_after_category_switching() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)
    app._toggle_builder_selection("pharmacy", 1, "Dosage", True)
    app._toggle_builder_selection("fundamentals", 2, "Advanced", True)

    assert app._selected_count_for_category("fundamentals") == 2
    assert app._selected_count_for_category("pharmacy") == 1


def test_global_clear_quiz_clears_every_selection() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)
    app._toggle_builder_selection("pharmacy", 1, "Dosage", True)
    app._clear_builder()

    assert app.builder_selections == []


def test_builder_summary_uses_user_facing_category_names() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)
    app._toggle_builder_selection("pharmacy", 1, "Dosage", True)

    summary = app._builder_summary_text()

    assert "Fundamentals" in summary
    assert "Pharm" in summary
    assert "Chapter 1: Intro" in summary
    assert "Chapter 1: Dosage" in summary


def test_mixed_pack_question_construction_keeps_duplicate_ids_across_packs() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)
    app._toggle_builder_selection("pharmacy", 1, "Dosage", True)

    packs = [
        _make_pack(
            "fundamentals",
            "Fundamentals of Nursing",
            [
                {"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
            ],
        ),
        _make_pack(
            "pharmacy",
            "Pharmacy",
            [
                {"id": "Q1", "chapter": 1, "chapter_title": "Dosage", "type": "mc"},
            ],
        ),
    ]

    questions = app._build_selected_questions(packs)

    assert [(question["_pack_id"], question["id"]) for question in questions] == [
        ("fundamentals", "Q1"),
        ("pharmacy", "Q1"),
    ]


def test_single_category_regression_keeps_selection_scoped() -> None:
    app = _make_app()

    app._toggle_builder_selection("fundamentals", 1, "Intro", True)

    packs = [
        _make_pack(
            "fundamentals",
            "Fundamentals of Nursing",
            [
                {"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
                {"id": "Q2", "chapter": 2, "chapter_title": "Advanced", "type": "mc"},
            ],
        ),
    ]

    questions = app._build_selected_questions(packs)

    assert [question["id"] for question in questions] == ["Q1"]


def test_start_studying_shuffles_new_session_and_resume_preserves_order(monkeypatch) -> None:
    app = _make_app()
    app.block_size_variable = type("BlockSize", (), {"get": lambda self: "3", "set": lambda self, value: None})()
    app._show_question_screen = lambda: setattr(app, "question_screen_shown", True)
    app.show_home_screen = lambda: setattr(app, "home_screen_called", True)
    app.builder_selections = [ChapterSelection("fundamentals", 1, "Intro")]

    shuffled = []

    def fake_shuffle(items):
        shuffled.append(list(items))
        items[:] = list(reversed(items))

    monkeypatch.setattr("study.session.random.shuffle", fake_shuffle)
    monkeypatch.setattr("study.gui.list_packs", lambda: [{"path": "pack.json", "title": "Fundamentals", "question_count": 1}])
    monkeypatch.setattr(
        "study.gui.load_pack",
        lambda path: {
            "pack_id": "fundamentals",
            "title": "Fundamentals of Nursing",
            "questions": [
                {"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
                {"id": "Q2", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
                {"id": "Q3", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
            ],
        },
    )

    app._start_studying({"pack_id": "fundamentals"})

    assert len(shuffled) == 1
    assert [question["id"] for question in app.session.questions] == ["Q3", "Q2", "Q1"]

    ordered_questions = [{"id": "Q2", "_pack_id": "fundamentals"}, {"id": "Q3", "_pack_id": "fundamentals"}]
    app.session.questions = ordered_questions
    app.session.current_index = 0

    state = {
        "version": 2,
        "session": {
            "selected_packs": [{"pack_id": "fundamentals", "path": "pack.json"}],
            "question_order": [
                {"pack_id": "fundamentals", "question_id": "Q2"},
                {"pack_id": "fundamentals", "question_id": "Q3"},
            ],
            "current_question": None,
            "review_question_refs": [],
            "missed_question_refs": [],
            "current_index": 0,
            "block_size": 15,
            "review_mode": False,
            "score": {"first_attempt_correct": 0, "first_attempt_missed": 0, "review_corrected": 0, "completed": 0},
            "block_correct": 0,
            "block_missed": 0,
        },
    }

    monkeypatch.setattr("study.gui.load_session", lambda: state)

    app._resume_saved_session()

    assert app.session.questions[0]["id"] == "Q2"
    assert app.session.questions[1]["id"] == "Q3"


def test_block_size_validation_rejects_invalid_values(monkeypatch) -> None:
    app = _make_app()
    app.block_size_variable = type("BlockSize", (), {"get": lambda self: "", "set": lambda self, value: None})()

    messages = []

    def fake_showerror(title, message, parent=None):
        messages.append((title, message))

    monkeypatch.setattr("study.gui.messagebox.showerror", fake_showerror)

    assert app._validate_block_size(3) is None
    assert messages[-1][1] == "Please enter a block size."

    app.block_size_variable = type("BlockSize", (), {"get": lambda self: "abc", "set": lambda self, value: None})()
    assert app._validate_block_size(3) is None
    assert messages[-1][1] == "Block size must be a whole number."

    app.block_size_variable = type("BlockSize", (), {"get": lambda self: "4", "set": lambda self, value: None})()
    assert app._validate_block_size(3) is None
    assert messages[-1][1] == "Block size cannot exceed the number of selected questions (3)."

    app.block_size_variable = type("BlockSize", (), {"get": lambda self: "2", "set": lambda self, value: None})()
    assert app._validate_block_size(3) == 2


def test_initial_category_resolution_uses_real_pack_id(monkeypatch) -> None:
    app = _make_app()
    app.builder_subjects = [
        {
            "pack_id": "fundamentals",
            "display_name": "Fundamentals",
            "pack_info": {"path": "fundamentals.json"},
        },
        {
            "pack_id": "pharmacy",
            "display_name": "Pharm",
            "pack_info": {"path": "pharmacy.json"},
        },
    ]

    resolved = app._resolve_subject_pack_id({"display_name": "Pharm", "pack_info": {"path": "pharmacy.json"}})

    assert resolved == "pharmacy"


def test_resume_uses_current_pack_path_when_saved_path_is_stale(tmp_path, monkeypatch) -> None:
    save_path = tmp_path / ".prepflow" / "session.json"
    save_path.parent.mkdir(parents=True)
    save_path.write_text(
        json.dumps(
            {
                "version": 2,
                "session": {
                    "selected_packs": [{"pack_id": "fundamentals", "path": "stale.json"}],
                    "question_order": [{"pack_id": "fundamentals", "question_id": "Q1"}],
                    "current_question": {"pack_id": "fundamentals", "question_id": "Q1"},
                    "review_question_refs": [],
                    "missed_question_refs": [],
                    "current_index": 0,
                    "block_size": 15,
                    "review_mode": False,
                    "score": {"first_attempt_correct": 0, "first_attempt_missed": 0, "review_corrected": 0, "completed": 0},
                    "block_correct": 0,
                    "block_missed": 0,
                },
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(save_state, "SAVE_DIRECTORY", save_path.parent)
    monkeypatch.setattr(save_state, "SAVE_PATH", save_path)

    monkeypatch.setattr(
        "study.gui.list_packs",
        lambda: [{"path": "current.json", "title": "Fundamentals", "question_count": 1}],
    )

    def fake_load_pack(path):
        if path == "stale.json":
            raise FileNotFoundError("stale path")
        if path == "current.json":
            return {
                "pack_id": "fundamentals",
                "title": "Fundamentals of Nursing",
                "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"}],
            }
        raise FileNotFoundError(path)

    monkeypatch.setattr("study.gui.load_pack", fake_load_pack)

    app = _make_app()
    app._show_question_screen = lambda: setattr(app, "question_screen_shown", True)

    app._resume_saved_session()

    assert getattr(app, "question_screen_shown", False) is True
    assert save_path.exists()


def test_restore_session_state_preserves_order_and_queues_across_packs() -> None:
    app = _make_app()

    packs = [
        _make_pack(
            "fundamentals",
            "Fundamentals of Nursing",
            [
                {"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
                {"id": "Q2", "chapter": 1, "chapter_title": "Intro", "type": "mc"},
            ],
        ),
        _make_pack(
            "pharmacy",
            "Pharmacy",
            [
                {"id": "Q3", "chapter": 1, "chapter_title": "Dosage", "type": "mc"},
            ],
        ),
    ]

    state = {
        "selected_packs": [
            {"pack_id": "fundamentals", "path": "fundamentals.json"},
            {"pack_id": "pharmacy", "path": "pharmacy.json"},
        ],
        "question_order": [
            {"pack_id": "fundamentals", "question_id": "Q2"},
            {"pack_id": "pharmacy", "question_id": "Q3"},
            {"pack_id": "fundamentals", "question_id": "Q1"},
        ],
        "current_question": {"pack_id": "pharmacy", "question_id": "Q3"},
        "review_question_refs": [{"pack_id": "fundamentals", "question_id": "Q2"}],
        "missed_question_refs": [{"pack_id": "pharmacy", "question_id": "Q3"}],
        "current_index": 2,
        "block_size": 10,
        "review_mode": True,
        "score": {"first_attempt_correct": 1, "first_attempt_missed": 1, "review_corrected": 0, "completed": 2},
        "block_correct": 1,
        "block_missed": 1,
    }

    restored = app._restore_session_state(state, packs)

    assert [question["id"] for question in restored["ordered_questions"]] == ["Q2", "Q3", "Q1"]
    assert restored["current_question"]["id"] == "Q3"
    assert [question["id"] for question in restored["review_questions"]] == ["Q2"]
    assert [question["id"] for question in restored["missed_questions"]] == ["Q3"]
    assert restored["block_size"] == 10
    assert restored["review_mode"] is True


def test_resume_rejects_missing_pack_and_missing_question(tmp_path, monkeypatch):
    save_path = tmp_path / ".prepflow" / "session.json"
    save_path.parent.mkdir(parents=True)
    save_path.write_text(
        json.dumps(
            {
                "version": 2,
                "session": {
                    "selected_packs": [{"pack_id": "does-not-exist", "path": "missing.json"}],
                    "question_order": [{"pack_id": "does-not-exist", "question_id": "Q1"}],
                    "current_question": {"pack_id": "does-not-exist", "question_id": "Q1"},
                    "review_question_refs": [],
                    "missed_question_refs": [],
                    "current_index": 0,
                    "block_size": 15,
                    "review_mode": False,
                    "score": {"first_attempt_correct": 0, "first_attempt_missed": 0, "review_corrected": 0, "completed": 0},
                    "block_correct": 0,
                    "block_missed": 0,
                },
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(save_state, "SAVE_DIRECTORY", save_path.parent)
    monkeypatch.setattr(save_state, "SAVE_PATH", save_path)

    app = _make_app()
    app.show_home_screen = lambda: setattr(app, "home_called", True)

    app._resume_saved_session()

    assert getattr(app, "home_called", False) is True
    assert not save_path.exists()


def test_resume_rejects_missing_question_reference(tmp_path, monkeypatch):
    save_path = tmp_path / ".prepflow" / "session.json"
    save_path.parent.mkdir(parents=True)
    save_path.write_text(
        json.dumps(
            {
                "version": 2,
                "session": {
                    "selected_packs": [{"pack_id": "fundamentals", "path": "fundamentals.json"}],
                    "question_order": [{"pack_id": "fundamentals", "question_id": "missing"}],
                    "current_question": {"pack_id": "fundamentals", "question_id": "missing"},
                    "review_question_refs": [],
                    "missed_question_refs": [],
                    "current_index": 0,
                    "block_size": 15,
                    "review_mode": False,
                    "score": {"first_attempt_correct": 0, "first_attempt_missed": 0, "review_corrected": 0, "completed": 0},
                    "block_correct": 0,
                    "block_missed": 0,
                },
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(save_state, "SAVE_DIRECTORY", save_path.parent)
    monkeypatch.setattr(save_state, "SAVE_PATH", save_path)

    app = _make_app()
    app.show_home_screen = lambda: setattr(app, "home_called", True)

    def fake_load_pack(path):
        return {"pack_id": "fundamentals", "title": "Fundamentals of Nursing", "questions": [{"id": "Q1", "chapter": 1, "chapter_title": "Intro", "type": "mc"}]}

    monkeypatch.setattr("study.gui.load_pack", fake_load_pack)

    app._resume_saved_session()

    assert getattr(app, "home_called", False) is True
    assert not save_path.exists()
