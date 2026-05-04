# Template Guide

This template keeps the reusable pieces from SerialHub and EZProto while avoiding app-specific domain logic.

## Included Patterns

- `cli.py`: argument parser with `--version`, `--web`, `--host`, and `--port`.
- `web.py`: browser mode using `textual-serve`.
- `storage.py`: JSON app-state persistence in a platform data directory.
- `app.py`: Textual application shell with a packaged ASCII logo.
- `.github/workflows/ci.yml`: lint and test workflow.
- `.github/workflows/release.yml`: Linux and Windows standalone builds.

## Suggested First Edits

Rename the package, update the command name, and replace the logo before adding domain features. Keep the initial tests passing while you grow the application.
