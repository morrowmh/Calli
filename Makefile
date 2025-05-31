.PHONY: clean setup_dev setup lint fix format mypy start

clean:
	rm -rf .venv .ruff_cache .mypy_cache

setup_dev:
	uv sync

setup:
	uv sync --no-dev

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix .

format:
	uv run ruff format .

mypy:
	uv run mypy .

start:
	uv run python bot.py