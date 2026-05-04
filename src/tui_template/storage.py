from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from platformdirs import user_data_dir

APP_NAME = "TUITemplate"
ENV_DATA_DIR = "TUI_TEMPLATE_DATA_DIR"
APP_STATE_FILE_NAME = "app_state.json"
DEFAULT_THEME = "textual-dark"


@dataclass(slots=True)
class AppState:
    theme: str = DEFAULT_THEME
    last_opened_at: str = ""
    events: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "theme": self.theme or DEFAULT_THEME,
            "last_opened_at": self.last_opened_at,
            "events": self.events[-50:],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AppState:
        raw_events = data.get("events", [])
        events = [event for event in raw_events if isinstance(event, dict)][-50:]
        return cls(
            theme=str(data.get("theme") or DEFAULT_THEME),
            last_opened_at=str(data.get("last_opened_at") or ""),
            events=events,
        )


def current_timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def get_data_dir() -> Path:
    custom = (os.environ.get(ENV_DATA_DIR) or "").strip()
    if custom:
        path = Path(custom).expanduser()
    else:
        path = Path(user_data_dir(appname=APP_NAME, appauthor=False))

    path.mkdir(parents=True, exist_ok=True)
    return path


def app_state_path() -> Path:
    return get_data_dir() / APP_STATE_FILE_NAME


def load_app_state() -> AppState:
    path = app_state_path()
    if not path.exists():
        state = AppState(last_opened_at=current_timestamp())
        save_app_state(state)
        return state

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return AppState(last_opened_at=current_timestamp())

    state = AppState.from_dict(data)
    state.last_opened_at = current_timestamp()
    save_app_state(state)
    return state


def save_app_state(state: AppState) -> None:
    path = app_state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
