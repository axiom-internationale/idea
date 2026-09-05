.PHONY: dev dev-gunicorn prod format lint check fix clean

SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command

# ── Development ──────────────────────────────────────────────
dev:
	uv run uvicorn axiom.app:app --reload --port 8000

dev-gunicorn:
	uv run gunicorn axiom.app:app -c server_config/multiprocessing.py --reload

# ── Production ───────────────────────────────────────────────
prod:
	$$env:AXIOM_ENV='production'; uv run gunicorn axiom.app:app -c server_config/multiprocessing.py

# ── Code quality ─────────────────────────────────────────────
format:
	uv run ruff format src/

lint:
	uv run ruff check src/

check: lint
	uv run ruff format --check src/

fix:
	uv run ruff check --fix src/
	uv run ruff format src/

# ── Cleanup ──────────────────────────────────────────────────
clean:
	Get-ChildItem -Path . -Recurse -Directory -Filter __pycache__ -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
	Get-ChildItem -Path . -Recurse -Directory -Filter *.egg-info -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
	Get-ChildItem -Path . -Recurse -Directory -Filter .ruff_cache -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
	Get-ChildItem -Path . -Recurse -Directory -Filter .mypy_cache -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
	if (Test-Path dist) { Remove-Item -Recurse -Force dist }
	if (Test-Path build) { Remove-Item -Recurse -Force build }
