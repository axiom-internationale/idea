# Organization

## Factory Structure

```
Founding Partner (You)          The only human in the system
        |
General Secretary (GS)          Orchestrator and manager of the entire AWF
        |
Think Tank (TT)                 C-Suite officers (shared across all businesses)
        |
        +-- CV1 (CPO1 + Team)
        +-- CV2 (CPO2 + Team)
        +-- CVn (CPOn + Team)
```

**Agentic Workforce (AWF)** = Think Tank + Company Verticals

### Structural Rules

- **CVs are under TT, not parallel to TT.** The Think Tank is the parent management layer.
- **Everything below the Founding Partner is an AI agent.**
- **The hierarchy is strictly linear at the top:** Founder > GS > TT > CVs. Parallel branches begin only at the CV level.

---

## Founding Partner

The sole human user of the entire system.

**Does:**
- Sit at the top of the organizational chain
- Monitor the autonomous company and its performance
- Provide rough ideas and inputs about existing or new businesses
- Communicate primarily through 1-on-1 discussions with GS
- Review refined proposals from GS and the Think Tank
- Approve red-gated actions (money, legal, irreversible — see [operations.md](operations.md))
- Provide strategic feedback and direction

**Does not:**
- Perform day-to-day operations
- Manually manage every agent or business
- Configure every new agent — the org spawns agents on its own

> The human gives direction; the agentic organization performs the work.

---

## General Secretary (GS)

Top-most officer of the Agentic Workforce. The single point of contact between the Founding Partner and the rest of the organization.

### Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Aggregate rough ideas** | Takes raw inputs from the Founder and turns them into discussion-ready material for the Think Tank |
| **Orchestrate Think Tank** | Leads group discussions with C-Suite officers to research, brainstorm, and refine ideas |
| **Return refined proposals** | Presents polished business plans and follow-ups to the Founding Partner |
| **Manage all agents** | Oversees every agent — Think Tank members and CV teams alike |
| **Auto-suggest improvements** | Independently identifies refinements to existing businesses and proposes new opportunities |
| **Enforce stability** | Collects feedback from all agents, enforces standards, maintains business health |
| **Create agents** | Spawns new agents to accomplish specific tasks as needed |
| **Maintain Decision Queue** | Manages the centralized queue for all red-gated actions awaiting Founder approval |

### Position

- Directly below the Founding Partner
- Above the Think Tank (leads it) while also being a member of it
- Bridge between the Founder and the entire organization

### Fallback Chain

GS is the critical routing node. If GS is fully down, the fallback chain ensures continuity:

```
GS (primary)
 |
 v  if GS is down
Think Tank collectively (handles org-level duties as a group)
 |
 v  if a single decision-maker is needed
Respective department C-Suite officer
 |
 v
CPOs (Company Vertical heads)
 |
 v
Founding Partner (last resort)
```

**Rules:** The fallback is temporary — GS should be restored as the primary orchestrator as soon as possible. The fallback chain is documented so every agent knows the succession order without asking.

---

## Think Tank (TT)

A group of C-Suite officers, each an AI agent, responsible for their domain across all parallel businesses.

> There is exactly one agent per C-Suite role. That single CFO, single CMO, etc. manages their domain for every business the factory runs — whether 1 or 100.

### C-Suite Roster

| Role | Abbr. | Domain |
|------|-------|--------|
| Chief Executive Officer | CEO | Overall business leadership, vision execution, cross-vertical synergy |
| Chief Strategy Officer | CSO | Competitive analysis, M&A, market positioning, OKRs |
| Chief Financial Officer | CFO | Financial modeling, unit economics, cash flow; owns per-CV ledger and monthly close |
| Chief Human Resource Officer | CHRO | Agent hiring, performance, compensation, culture |
| Chief Law Officer | CLO | Contracts, IP, compliance; countersigns all legal gate cards |
| Chief Marketing Officer | CMO | GTM strategy, brand, communications, PR |
| Chief Operating Officer | COO | Process design, vendor management, operational scaling |
| Chief Communications Officer | CCO | Board decks, investor relations, governance |
| Chief Technology Officer | CTO | Tech architecture, infrastructure, engineering standards |
| Chief Designer Officer | CDO | Design systems, UX/UI, brand visuals |
| Chief Research Officer | CRO | Market research, trend analysis, R&D |

The roster is extensible — new roles can be added based on organizational needs.

### Structure

```
GS (Leader + Member)
 |
 +-- CEO    +-- CSO    +-- CFO    +-- CHRO
 +-- CLO    +-- CMO    +-- COO    +-- CCO
 +-- CTO    +-- CDO    +-- CRO    +-- ...
```

### How the Think Tank Operates

1. **Group discussions** — GS brings refined inputs to TT for brainstorming and research.
2. **Independent proposals** — Any TT member can propose refinements or entirely new business ideas.
3. **Cross-vertical oversight** — Each officer oversees their domain across all CVs. The CFO manages finances for every business, the CMO handles marketing for every business, etc.
4. **Collaboration with CVs** — TT members sync with any CPO or agent in any CV.
5. **Agent creation** — Any TT member can create new agents to accomplish specific tasks.
6. **Communication path** — Most TT communication goes through GS, but members can reach the Founder directly when necessary.

### The n-Business Rule

If the factory runs **n** businesses, each TT member is responsible for their domain across all n businesses. One centralized executive layer — not a duplicated C-Suite per business.

```
1 CFO
 |
 +-- Business A (finances)
 +-- Business B (finances)
 +-- Business N (finances)
```

---

## Company Verticals (CVs)

The actual businesses, products, and services the factory runs in parallel. They sit under the Think Tank in the hierarchy.

### Structure of a Single Vertical

```
Think Tank (shared C-Suite oversight)
        |
Chief Product Officer (CPO)     Head of this specific vertical
        |
        +-- Agent: Engineering
        +-- Agent: Design
        +-- Agent: Content
        +-- Agent: Sales
        +-- Agent: Support
        +-- ... (as many as needed)
```

### How CVs Work

| Aspect | Detail |
|--------|--------|
| **Leadership** | Each vertical is headed by a CPO — a specialized agent |
| **Team** | CPO manages a team of agents dedicated to that product/service/business |
| **Employment** | CPO and team are full-time employees of the AWF — they work 24/7 |
| **Daily operations** | Attend meetings, scrum calls, build products, improve constantly |
| **Continuous improvement** | Must constantly improve the products/services they are responsible for |
| **Agent reuse** | Agents can be shared across verticals (e.g., a PPT agent serving multiple teams) |
| **Agent spawning** | CPOs can create new agents for their respective verticals when needed |
| **Feedback loop** | Agents receive feedback from their CPO and from the Think Tank |

### Parallel Verticals

```
Think Tank (TT)
    |
    +-- CV1 — Business A (CPO1 + Team)
    +-- CV2 — Business B (CPO2 + Team)
    +-- CV3 — Business C (CPO3 + Team)
    +-- CVn — Service N  (CPOn + Team)
```

Each vertical operates independently with its own CPO and team, while sharing the same C-Suite oversight from the Think Tank.

---

## Access and Escalation Policy

### Lane 1 — Feedback (open to everyone)

Any agent can reach the Founding Partner directly, at any time, for feedback. No permission needed, no chain required.

### Lane 2 — Decisions (manager first)

For improvements, queries, escalations, and proposals:

```
CV team agent -> their CPO
CPO / TT member -> GS
GS -> Founding Partner
```

The manager resolves it, or escalates upward only when needed.

### Lane 3 — Improvement Plans (direct to Founder)

Any agent can submit a structured improvement plan directly to the Founding Partner, bypassing the manager chain. Plans must focus on at least one of: token cost optimization, organizational profitability, or quality of work.

```
Any agent -> Founding Partner (direct, structured plan)
```

GS tracks all submitted plans in `_org/improvement-plans.md` for visibility.

### Summary

| Channel | Flow |
|---------|------|
| Feedback | Anyone to Founder — always allowed, direct |
| Improvement plans | Anyone to Founder — structured, direct |
| Decisions / proposals | CV agent > CPO > GS > Founder — manager first |
| Routine | Founder and GS (primary channel) |
| TT coordination | GS orchestrates |
| Cross-org sync | Anyone to anyone — allowed freely |
