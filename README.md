# TUI App Template

This repository is a GitHub template for Python Textual TUI apps. It is based on the common structure used by SerialHub and EZProto:

- `src/` package layout
- terminal mode and browser mode through `textual-serve`
- packaged ASCII logo asset
- local app-state storage with an environment-variable override
- pytest and Ruff checks
- Linux and Windows PyInstaller release builds

The starter UI intentionally shows one widget: a logo panel. Replace the template name, package name, ASCII logo, and app behavior with your own domain code.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
tui-template
```

Browser mode:

```bash
tui-template --web
```

Run checks:

```bash
python -m ruff check src tests
python -m pytest
python -m compileall src tests
```

## Rename Checklist

1. Rename `src/tui_template` to your package name.
2. Update `pyproject.toml`:
   - `project.name`
   - `project.description`
   - `project.scripts`
   - `tool.setuptools.dynamic.version`
   - `tool.setuptools.package-data`
3. Update imports and package constants in `src/<package>/`.
4. Replace `src/<package>/assets/logo.txt`.
5. Update `.github/workflows/release.yml` `APP_NAME` and package paths.
6. Mark the GitHub repository as a template in repository settings.

## Local Data

App data is stored in the platform user-data directory. Override it during development:

```bash
TUI_TEMPLATE_DATA_DIR=/tmp/tui-template-data tui-template
```

## Omarchy TUI Shortcut

After installing the command locally, create an Omarchy launcher:

```bash
omarchy-tui-install "TUI Template" "tui-template" tile "/path/to/icon.png"
```

The shortcut creation step does not install the app. The command must already be available.
