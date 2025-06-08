.PHONY: clean dev nodev check fix run

clean:
	rm -rf .venv .ruff_cache .mypy_cache

dev:
	uv sync

nodev:
	uv sync --no-dev

check:
	uv run ruff check .
	mypy .

fix:
	uv run ruff check --fix .
	uv run ruff format .

run:
	uv run python bot.py