from __future__ import annotations

from tui_template.app import load_ascii_logo


def test_logo_asset_loads() -> None:
    logo = load_ascii_logo()

    assert "TEXTUAL TUI TEMPLATE" in logo
