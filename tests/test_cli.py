from __future__ import annotations

import pytest

from tui_template import __version__
from tui_template.cli import build_parser, parse_port


def test_parse_port_accepts_valid_port() -> None:
    assert parse_port("8000") == 8000


@pytest.mark.parametrize("value", ["0", "65536", "abc"])
def test_parse_port_rejects_invalid_port(value: str) -> None:
    with pytest.raises(Exception):
        parse_port(value)


def test_version_argument(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(["--version"])

    assert __version__ in capsys.readouterr().out
