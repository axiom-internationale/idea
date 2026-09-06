# Axiom Intelligence

Autonomous agentic factory — one human founder + one agentic organization + many parallel businesses.
Marketing site + stub API. Vision lives in `docs/factory.md`, implementation status in `docs/ROADMAP.md`.

## Stack

- Python 3.12, `uv`
- `Starlette` composition root (`src/axiom/app.py`): `/` → FastHTML site, `/api` → FastAPI, `/static` + `/media` → `StaticFiles`
- `FastHTML` site (`src/website/`): 12 bento sections, SEO + JSON-LD, `robots.txt`/`sitemap.xml`/404
- `FastAPI` (`src/backend_service/`): `GET /api/health`, `/api/liveness`, `/api/readiness` (file-based, multi-worker safe)
- Prod: `gunicorn + uvicorn workers` (`server_config/multiprocessing.py`), `nginx` (`server_config/nginx.*.conf`), `Dockerfile`

## Quickstart

```powershell
cp .env.example .env   # optional
uv sync --extra dev
uv run uvicorn axiom.app:axiom_app --reload --port 4000
# or: make dev
```

Open `http://localhost:4000`, API at `http://localhost:4000/api/health`.

| Command | What |
|---|---|
| `make dev` | uvicorn reload |
| `make dev-gunicorn` | gunicorn reload |
| `make prod` | gunicorn prod config |
| `uv run --with pytest --with httpx pytest -q` | 6 tests: backend probes + bento classname snapshot |
| `uv run --with ruff ruff check src/ tests/` | lint |
| `uv run --with ruff ruff format --check src/ tests/` | format check |

Docker:

```powershell
docker build -t axiom .
docker run -p 4000:4000 axiom
```

## Config

All via env / `.env`, parsed in `server_config/settings.py` with validation + safe prod defaults:

`AXIOM_ENV`, `AXIOM_BIND`, `AXIOM_WORKERS`, `AXIOM_TIMEOUT`, `AXIOM_GRACEFUL_TIMEOUT`,
`AXIOM_KEEPALIVE`, `AXIOM_LOG_LEVEL`, `AXIOM_MAX_REQUESTS`, `AXIOM_MAX_REQUESTS_JITTER`,
`AXIOM_FORWARDED_ALLOW_IPS`, `AXIOM_PROXY_ALLOW_FROM`, `AXIOM_READY_FILE`

Version is single-sourced in `src/axiom/__init__.py:__version__`.

## Layout

```
src/axiom/          Starlette app + lifespan (toggles readiness file)
src/backend_service/ FastAPI: app/health/liveness/readiness/state
src/website/        FastHTML: app/routes/seo + sections/* + components/* + static/* + media/*
server_config/      settings.py + multiprocessing.py (gunicorn) + nginx.dev/prod.conf
tests/              test_backend.py + test_sections.py (bento grid guard)
docs/               factory.md (org spec) + vision.md + ROADMAP.md (spec vs code)
```

Media: canonical images live in `src/website/media/` (`sun.png` 1200px + `sun.webp` 39KB, `mini_sun.png`).
