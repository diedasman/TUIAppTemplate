from __future__ import annotations

import argparse
from collections.abc import Sequence

from tui_template import __version__
from tui_template.app import TemplateApp
from tui_template.web import DEFAULT_WEB_HOST, DEFAULT_WEB_PORT, run_web_app


def parse_port(value: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Port must be an integer.") from exc

    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535.")
    return port


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tui-template", description="Template Textual TUI app")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Serve the Textual app in a local browser instead of the terminal",
    )
    parser.add_argument(
        "--host",
        default=DEFAULT_WEB_HOST,
        help=f"Host to bind in web mode (default: {DEFAULT_WEB_HOST})",
    )
    parser.add_argument(
        "--port",
        type=parse_port,
        default=DEFAULT_WEB_PORT,
        help=f"Port to bind in web mode (default: {DEFAULT_WEB_PORT})",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.web:
        run_web_app(host=args.host, port=args.port)
        return 0

    TemplateApp().run()
    return 0
