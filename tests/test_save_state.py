import json

import study.save_state as save_state


def use_temporary_save_location(tmp_path, monkeypatch):
    save_directory = tmp_path / ".prepflow"
    save_path = save_directory / "session.json"

    monkeypatch.setattr(save_state, "SAVE_DIRECTORY", save_directory)
    monkeypatch.setattr(save_state, "SAVE_PATH", save_path)

    return save_path


def test_version_2_round_trip(tmp_path, monkeypatch):
    save_path = use_temporary_save_location(tmp_path, monkeypatch)

    save_state.save_session({"question_index": 8})

    payload = json.loads(save_path.read_text(encoding="utf-8"))
    assert payload["version"] == 2
    assert payload["session"] == {"question_index": 8}
    assert save_state.load_session() == {"question_index": 8}


def test_version_1_save_is_ignored(tmp_path, monkeypatch):
    save_path = use_temporary_save_location(tmp_path, monkeypatch)
    save_path.parent.mkdir(parents=True)
    save_path.write_text(
        json.dumps({"version": 1, "session": {"question_index": 2}}),
        encoding="utf-8",
    )

    assert save_state.load_session() is None
    assert save_state.has_saved_session() is False


def test_malformed_and_unknown_versions_return_none(tmp_path, monkeypatch):
    save_path = use_temporary_save_location(tmp_path, monkeypatch)
    save_path.parent.mkdir(parents=True)

    save_path.write_text("not valid json", encoding="utf-8")
    assert save_state.load_session() is None

    save_path.write_text(json.dumps({"version": 99, "session": {"question_index": 1}}), encoding="utf-8")
    assert save_state.load_session() is None


def test_delete_saved_session(tmp_path, monkeypatch):
    save_path = use_temporary_save_location(tmp_path, monkeypatch)

    save_state.save_session({"question_index": 2})
    assert save_path.exists()

    save_state.delete_saved_session()

    assert not save_path.exists()
    assert save_state.load_session() is None
