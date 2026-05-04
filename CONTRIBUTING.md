# Contributing

## Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Checks

```bash
python -m ruff check src tests
python -m pytest
python -m compileall src tests
```

Keep changes focused and add tests for behavior that can regress.
