# Roadmap — factory.md vision vs code

Source of truth for the org design: `factory.md` (v1.0, 2026-08-31).
This file tracks what is implemented in code and what is still docs-only.

## Implemented

- Marketing site (`src/website/`): nav, hero, machine, pillars, think-tank,
  portfolio, dna, stack, founder, connect, footer, brief dialog
- SEO: canonical, OG/Twitter, JSON-LD Organization, `/robots.txt`, `/sitemap.xml`, 404
- Backend probes: `/api/health`, `/api/liveness`, `/api/readiness` (file-based, multi-worker safe)
- Deploy: gunicorn+uvicorn (`server_config/`), nginx dev/prod with CSP + rate-limit, Dockerfile, CI (ruff + pytest)
- Tests: `tests/test_backend.py`, `tests/test_sections.py` (bento classname snapshot)

## Still docs-only (from factory.md)

- [ ] `_org/decisions.md` gate queue + gate cards (Section 16)
- [ ] `_org/kpis.md` per-CV ledger + monthly close (Section 17)
- [ ] `gs/` digests, `tt/` C-suite folders, `cvs/<name>/brief.md|ledger.md|agents.md|work/` (Section 21)
- [ ] Break-even contracts + loss alarms + kill criteria (Section 17)
- [ ] Async digest pipeline to replace sync meetings (Section 20)
- [ ] Grok-only engine + Herdr multiplexer wiring (Section 21)

## Next suggested slice

1. `cvs/demo/` with `brief.md` + `ledger.md` backed by `/api/cvs` read-only endpoints
2. `_org/decisions.md` append-only log + `POST /api/decisions` gated to Founder
3. Weekly digest generator (script, not agent yet) → `gs/digest-YYYY-Www.md`
