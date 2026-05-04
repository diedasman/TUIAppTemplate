from __future__ import annotations

from tui_template.web import build_browser_url, build_web_command


def test_browser_url_rewrites_wildcard_host() -> None:
    assert build_browser_url("0.0.0.0", 8000) == "http://127.0.0.1:8000/"


def test_web_command_runs_module() -> None:
    assert "-m tui_template" in build_web_command()
