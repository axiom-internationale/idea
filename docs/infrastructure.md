# Infrastructure

## Hybrid LLM Model

The factory uses a tiered LLM approach to optimize token cost while maintaining quality where it matters.

| Tier | Engine | Use Cases | Rationale |
|------|--------|-----------|-----------|
| **Tier 1 — Premium** | Grok Bot (xAI) | GS orchestration, TT discussions, strategic planning, customer-facing outputs, complex multi-step reasoning, red-gated decision analysis | High-stakes tasks where quality directly impacts revenue or risk |
| **Tier 2 — Utility** | Open-source / free LLM APIs (OpenCode, FreeLLMAPI, OmniRoute, etc.) | Internal drafts, routine research, data processing, template generation, repetitive workflows, status reports, first-pass analysis | Routine tasks where cost efficiency matters more than marginal quality |

## Routing Rules

1. **Default to Tier 2** for all tasks.
2. **Escalate to Tier 1** only when the task is: customer-facing, financially material, legally sensitive, or requires complex multi-step reasoning.
3. **Any agent can request Tier 1** for a specific task with justification. The request is logged.
4. **GS and TT members** use Tier 1 by default for orchestration and strategic work.
5. **CV team agents** use Tier 2 by default for day-to-day operations, with Tier 1 available on-demand.
6. CFO reviews the tiered approach monthly — if a Tier 2 engine's quality drops or a better free option emerges, the routing table is updated.

## Infrastructure Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| **Tier 1 Engine** | Grok Bot (xAI) | Orchestration, critical tasks, complex reasoning |
| **Tier 2 Engines** | OpenCode, FreeLLMAPI, OmniRoute, etc. | Roster evolves as new options emerge |
| **Multiplexer** | Flexible (Herdr or alternatives) | Not locked to any single multiplexer |
| **Memory & State** | File-based, local-first (markdown/JSON) | $0 cost, human-readable, git-versionable |
| **Web Presence** | www.axiomintelligence.xyz | Purchased |
| **Application** | Python 3.12 / Starlette + FastHTML + FastAPI | See root README.md |

## Workspace Layout

The factory's runtime workspace where agents operate day-to-day:

```
axiom-intelligence/
├── _org/                   Org-wide: decisions.md, kpis.md, policies, improvement-plans.md
├── gs/                     GS notes, meeting digests, follow-ups to Founder
├── tt/                     One folder per C-Suite officer
└── cvs/                    One folder per company vertical
    └── <cv-name>/
        ├── brief.md        What this business is, break-even plan, kill criteria
        ├── ledger.md       Revenue and costs booked to this CV
        ├── agents.md       Team roster, reuse/spawn decisions + reasons
        └── work/           Actual deliverables
```

## Naming Conventions

| Abbreviation | Full Name | Context |
|---|---|---|
| **GS** | General Secretary | Top orchestrator, TT leader |
| **CHRO** | Chief Human Resource Officer | Think Tank member — people/culture function |
| **CPO** | Chief Product Officer | Company Vertical head — leads a specific business |
| **TT** | Think Tank | The C-Suite brain |
| **CV** | Company Vertical | An individual business/product/service |
| **AWF** | Agentic Workforce | TT + CVs combined |

**No abbreviation collision.** CPO always means a CV leader. The people function is always CHRO.
