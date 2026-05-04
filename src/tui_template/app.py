from __future__ import annotations

from importlib.resources import files

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Static

from tui_template.storage import AppState, load_app_state, save_app_state


def load_ascii_logo() -> str:
    try:
        return (
            files("tui_template")
            .joinpath("assets")
            .joinpath("logo.txt")
            .read_text(encoding="utf-8")
            .strip()
        )
    except (FileNotFoundError, ModuleNotFoundError, OSError):
        return "TUI TEMPLATE"


class LogoPanel(Static):
    """Single starter widget that displays the packaged logo text."""


class TemplateApp(App[None]):
    CSS_PATH = "app.tcss"
    TITLE = "TUI Template"
    SUB_TITLE = "Starter Textual application"

    BINDINGS = [
        Binding("ctrl+t", "toggle_theme", "Theme"),
        Binding("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.state: AppState = load_app_state()

    def compose(self) -> ComposeResult:
        with Container(id="app-shell"):
            yield LogoPanel(load_ascii_logo(), id="logo-panel")

    def on_mount(self) -> None:
        self.theme = self.state.theme

    def action_toggle_theme(self) -> None:
        self.theme = "textual-light" if self.theme == "textual-dark" else "textual-dark"
        self.state.theme = self.theme
        save_app_state(self.state)
