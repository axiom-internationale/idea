# Axiom Intelligence Inc. — Documentation

> Master documentation for the personalized autonomous agentic factory.

---

## Documents

| Document | Purpose | Status |
|----------|---------|--------|
| [vision.md](vision.md) | Original founding vision — the raw idea that started Axiom Intelligence. Historical reference. | Final (origin doc) |
| [factory.md](factory.md) | **Master blueprint** — organizational structure, operating principles, decision-making, safety gates, profitability enforcement, tech stack, and all operational rules. The single source of truth. | Active (v1.0) |
| [domain.md](domain.md) | Target markets (40 domains, tiered), the 4-stage DFY product offering (Audit → Intelligence → Execute → Improve), and worked examples (HVAC, Professional Services). | Active |

## How These Relate

```
vision.md          The spark — why this exists
    │
    ▼
factory.md         The engine — how the org works
    │
    ▼
domain.md          The first business — what we sell and to whom
```

- **vision.md** is the historical origin. It was consolidated into factory.md and is preserved as the founding record.
- **factory.md** is the operating manual. All organizational decisions, policies, and structures live here.
- **domain.md** defines the first Company Vertical — the DFY AI consulting service. When this CV launches, it will get its own folder under `cvs/` in the operational workspace as defined in factory.md Section 21.

## Operational Workspace (Separate from Docs)

The factory's runtime workspace (where agents actually work) follows the layout defined in factory.md:

```
axiom-intelligence/
├── _org/           ← decisions.md, kpis.md, policies, improvement-plans.md
├── gs/             ← GS's notes, meeting digests, follow-ups
├── tt/             ← one folder per C-Suite officer
└── cvs/            ← one folder per company vertical
```

This `docs/` folder is the **design documentation**. The operational workspace above is where the agentic workforce operates day-to-day.
