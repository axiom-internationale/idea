# Decision Log

Historical record of all organizational decisions. Append-only — never delete entries.

| # | Date | Topic | Decision | Source |
|---|------|-------|----------|--------|
| 1 | 2026-08-31 | CPO naming collision | TT's people role renamed to **CHRO** (Chief Human Resource Officer). **CPO = Chief Product Officer only.** No abbreviation collision. | GLM recommendation, Founder approved |
| 2 | 2026-08-31 | GS as single point of contact | Feedback: anyone to Founder directly. Improvements/queries: manager first, then escalate. GS remains the primary routine channel. | GLM recommendation, Founder approved |
| 3 | 2026-08-31 | GS fallback chain | TT collectively, then individual C-Suite officers, then CPOs, then Founder (last resort). | Founder decision |
| 4 | 2026-08-31 | Engine | Grok Bot as Tier 1 engine. Herdr multiplexer for parallel agent sessions (not mandatory). | Founder decision |
| 5 | 2026-08-31 | Human-approval gates | 3-tier system (green/yellow/red). Fail-closed. Gate cards with CFO/CLO countersign. Earned delegation for proven CVs. | GLM recommendation, Founder approved |
| 6 | 2026-08-31 | Profitability enforcement | Per-CV ledger, break-even contract at launch, loss alarm after 2 months, kill criteria, no revenue-free headcount. | GLM recommendation, Founder approved |
| 7 | 2026-08-31 | Communication default | Async by default. Synchronous only when genuinely faster. | GLM recommendation, Founder approved |
| 8 | 2026-08-31 | Business flow | ChatGPT's 10-stage flow + GLM's "Evolve" stage = 11 stages. | Founder decision |
| 9 | 2026-08-31 | Token optimization | Hybrid LLM model: Grok Bot (Tier 1) for orchestration and critical tasks; open-source/free APIs (Tier 2) for routine work. Default to Tier 2, escalate to Tier 1 on justification. | Founder decision |
| 10 | 2026-08-31 | Direct improvement plans | Any agent can submit improvement plans directly to Founder (bypassing manager chain) covering token cost, org profitability, and quality of work. GS tracks in `_org/improvement-plans.md`. | Founder decision |
| 11 | 2026-09-07 | First CV | CV1 = AI Consulting for Multi-location Home Services. Beachhead: HVAC. DFY 4-stage model. | Founder decision |
| 12 | 2026-09-08 | Outreach process | Parameterized cold outreach runs with two-stage filtering funnel, AI Business Health Score rubric, and compliance-first approach. | Founder decision, refined by evaluation |
| 13 | 2026-09-08 | Second CV | CV2 = AI Consulting for Law Firms. Beachhead: personal injury and family law. DFY 4-stage model with legal compliance layer. Slightly higher pricing ($12K+ audit) and longer sales cycle than CV1. | Founder decision |
| 14 | 2026-09-09 | Report standards | Axiom Intelligence Reports must meet McKinsey/BCG/Bain deliverable quality: 8-section structure, insight-led analysis, evidence-backed findings, financial impact quantification, professional tone. Reports are the primary conversion tool. | Founder decision |
| 15 | 2026-09-14 | Law GTM + page ICP | Law acquisition is ZIP/pincode-by-ZIP: enumerate all firms in the ZIP, profile each, McKinsey-style report. Client-facing voice is founding partner (never agentic). Public offer is all practice areas. Firm size follows docs (5–50 attorneys), not an invented 1–10 page filter. First geography: NYC metro. Overlay: `docs/cvs/law_firm_ai/gtm.md`. | Founding Partner |
| 16 | 2026-09-14 | Law page is geo-agnostic | Public `/dfy/law` must not name NYC, a borough, a metro, or a ZIP (11372 stays off the site). Location is outbound/ZIP ops only. Founding-partner voice and all-practices offer stay. | Founding Partner / CPO |
| 17 | 2026-09-15 | Law page has no size lock | Public `/dfy/law` welcomes law firms of any size. Do not hardcode 1–10, 5–50, solo-only, or “small and mid” as who we sell to. Practice names on the page are examples, not a closed set. 5–50 remains docs/outbound ICP only. | Founding Partner |
