.PHONY: install lint format typecheck test check

install:
	uv sync --locked

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff format . --fix

typecheck:
	uv run mypy

test:
	uv run pytest

check: lint typecheck test