# CNC Asset API

A REST API to register and query CNC machines and their operational data, built with FastAPI.

This project is in its early stage. It is the foundation of a larger industrial data pipeline, and it is also a learning project: each milestone adds one production concern (testing, CI, persistence, observability) on top of a small, working service.

## What to expect

Available today:

- `GET /health/live`: liveness probe, returns `{"status": "ok"}`.
- CI on every pull request (lint, format check, type check, tests).

Planned, in order:

- Readiness probe (`/health/ready`) and typed configuration through environment variables.
- CRUD for machines (assets), with validation and a database behind it.
- Structured logging, metrics and tracing.
- Containerization and deployment.

Design decisions are recorded as ADRs in `docs/adr/`.

## Requirements

- [uv](https://docs.astral.sh/uv/) (it installs the right Python version for you)
- `make` (optional, it only wraps the commands below)
- Python 3.13 (managed by uv, see `.python-version`)

## Getting started

```bash
git clone https://github.com/glbilati/cnc-asset-api.git
cd cnc-asset-api
uv sync --locked
```

`uv sync --locked` creates `.venv` and installs the exact versions pinned in `uv.lock`.

## Running the API

```bash
uv run cnc-asset-api
```

The server listens on `http://localhost:8000`. Check that it is up:

```bash
curl http://localhost:8000/health/live
# {"status":"ok"}
```

FastAPI also serves the interactive documentation at `http://localhost:8000/docs`.

## Development

Run everything the CI runs with a single command:

```bash
make check
```

Individual commands:

| Command          | What it does                                           |
| ---------------- | ------------------------------------------------------ |
| `make install`   | Install dependencies from the lockfile                 |
| `make format`    | Format the code and apply safe lint fixes (ruff)       |
| `make lint`      | Check lint and formatting without changing files       |
| `make typecheck` | Run mypy in strict mode                                |
| `make test`      | Run the test suite with coverage                       |
| `make check`     | Lint, type check and tests, same as the CI             |

Without `make`, run the commands directly, for example `uv run pytest`.

## Project layout

```
.
├── src/cnc_asset_api/   # application code
│   ├── api/             # HTTP routers
│   ├── main.py          # create_app() factory
│   └── cli.py           # entrypoint for the cnc-asset-api command
├── tests/               # test suite
├── pyproject.toml       # dependencies and tool configuration
└── uv.lock              # pinned dependency versions
```

## Contributing workflow

1. Create a branch from `main`.
2. Make your change and run `make check`.
3. Open a pull request. The CI must pass before merging.
