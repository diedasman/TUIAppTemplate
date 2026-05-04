from __future__ import annotations

import json

from tui_template.storage import AppState, app_state_path, get_data_dir, load_app_state, save_app_state


def test_storage_uses_env_override(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TUI_TEMPLATE_DATA_DIR", str(tmp_path))

    assert get_data_dir() == tmp_path


def test_app_state_round_trip(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TUI_TEMPLATE_DATA_DIR", str(tmp_path))

    save_app_state(AppState(theme="textual-light", events=[{"message": "created"}]))
    state = load_app_state()

    assert state.theme == "textual-light"
    assert json.loads(app_state_path().read_text(encoding="utf-8"))["events"][0]["message"] == "created"
