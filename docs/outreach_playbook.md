# Outreach Playbook

The end-to-end process for finding, qualifying, and reaching prospective clients. Designed for token efficiency, legal compliance, and measurable results.

## Concepts

**Run:** A single parameterized execution of the outreach pipeline targeting one domain in one geography. Runs are the atomic unit of outreach work.

**AI Business Health Score (ABHS):** A standardized score (0–10) measuring how well a business leverages technology and AI. Used to identify high-potential prospects and as a value hook in outreach — the report shows the prospect their score and how to improve it.

---

## Run Inputs

Each run takes exactly four parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Domain** | One business vertical per run | Multi-location HVAC |
| **Country** | One country per run (start with USA) | USA |
| **Region** | ZIP code, city, or metro area | Atlanta, GA / 30301 |
| **ICP description** | Ideal Customer Profile criteria | 8–25 locations, $8M–$40M revenue, owner-operated |

### Country Prioritization

| Priority | Country | Rationale |
|----------|---------|-----------|
| 1 | USA | Primary market, ICP pricing ($10K+ audit) matches, English-language outreach |
| 2 | UK | English-speaking, similar business models, GDPR compliance required |
| 3 | Canada | English-speaking, proximity to USA market dynamics |
| Later | India, China, others | Require different pricing, positioning, language, and regulatory approach — defer until USA playbook is validated |

---

## Run Steps

### Step 1 — Discover Businesses

Agents browse Google Maps like a normal human being. No APIs, no scraping — just open a browser, search, scroll, click, read, and take notes.

**How it works:**

1. Agent opens a browser and navigates to Google Maps.
2. Searches for the domain in the target region (e.g., "HVAC companies near Atlanta, GA").
3. Scrolls through results, clicking into each business listing.
4. For each business, the agent notes:
   - Business name, address, phone, website
   - Google rating and review count
   - Number of locations (visible from the map or website)
   - Photos and general impression
   - Anything interesting — a standout review, a unique service offering, a visible problem

The agent uses human judgment while browsing. If a business looks promising, they note it. If it's clearly a one-person shop or has 2 stars, they skip it and move on.

**Additional browsing sources** (as the agent sees fit):
- Yelp, Facebook, and Instagram — browse like a human, not via API
- Industry directories and association member lists
- LinkedIn company pages
- Local business news

**Target:** Identify 200–300 raw businesses per run.

### Step 2 — Quick Screen

While browsing, the agent applies quick ICP judgment to filter obvious misfits. This is not a separate batch process — it happens naturally during discovery.

**Quick screen signals:**

| Signal | What the Agent Looks For |
|--------|--------------------------|
| Scale | Does this look like a multi-location operation or a solo operator? |
| Reputation | Is the rating above 3.0? Do they have meaningful review volume (50+)? |
| Website | Do they have a functional website? Is it modern or a 2008 template? |
| Maturity | Do they appear to have been in business 3+ years? |
| Decision maker | Can the agent identify an owner, GM, or managing partner? |

Businesses that clearly don't fit the ICP are noted as "screened out" with a one-line reason and the agent moves on. No token spend on deep research for obvious misfits.

**Target:** Reduce to 50–80 qualified candidates.

### Step 3 — Deep Research (McKinsey-Grade)

This is the core value-creation step. For each qualified business, the agent conducts research at the level of a **senior associate at McKinsey, BCG, or Bain** — structured, evidence-backed, and directly actionable for the business.

The research is not data collection. It is analysis that produces insights the business owner can act on immediately, whether or not they hire Axiom.

**Research Framework:**

**1. Business Model Analysis**
- What services do they offer and how do they monetize?
- Pricing strategy — premium positioning or volume play?
- Geographic footprint and expansion pattern (single city, regional, multi-state)
- Customer mix — residential vs. commercial, one-time vs. recurring
- Revenue drivers — what brings in the most money?

**2. Competitive Positioning**
- Who are 3–5 direct competitors in the same geography?
- What differentiates this business (or fails to)?
- Where do they win vs. lose against competitors on reputation, pricing, service range?
- Are competitors doing anything with AI/automation that this business is not?

**3. Customer Voice Analysis**
- Read 30–50 recent Google/Facebook/Yelp reviews in detail
- Identify what customers praise consistently (specific patterns, not just "good service")
- Identify recurring complaints — scheduling, communication, pricing, quality, response time
- Spot sentiment trends over time — is the business improving or declining?
- Pull 3–5 direct quotes that illustrate key strengths and weaknesses

**4. Digital and Operational Maturity**
- Website: online booking capability, service descriptions, team pages, content quality, mobile experience
- Social media: posting frequency, engagement, content strategy, review responses
- Technology signals: online scheduling, CRM indicators, mobile app, chat widgets
- Operational signals from reviews: scheduling issues, communication gaps, inconsistent quality across locations, technician knowledge problems

**5. Growth Opportunity Identification**
- Where is the business leaving money on the table? Be specific — "missed calls" is generic; "no after-hours booking option despite 15 reviews mentioning difficulty reaching the office" is actionable
- What operational improvements would have the highest ROI?
- What AI/automation opportunities exist based on observed gaps?
- Rank the top 3–5 opportunities by estimated impact

**6. Financial Impact Estimation**
- Estimate revenue impact of the top 3 improvements (use industry benchmarks and observed signals)
- Estimate cost savings from automation opportunities
- Frame as: "If you fix X, you likely recover $Y per month based on Z"

**Research Quality Bar:**

- Every insight must be backed by evidence — a specific review quote, a website observation, a competitive comparison
- Recommendations must be specific and actionable. "Improve your website" is not acceptable. "Add online booking to your website — you currently require phone calls, and 8 of your last 50 reviews mention difficulty scheduling" is.
- The research output should be valuable enough that the business owner would pay for it as a standalone deliverable
- No filler, no generic advice. If the agent cannot find a specific insight for a dimension, they say so rather than writing boilerplate

**Research sources** (all browsed like a human):
- Google Maps listing and reviews
- Company website (every page, not just the homepage)
- Facebook page and reviews
- Instagram, LinkedIn, Yelp
- Competitor websites and reviews (for positioning context)
- Industry news, local press, Better Business Bureau
- Job postings (reveal tech stack, growth signals, operational pain)

**Output per business:**
- Business profile (name, owner, locations, services, estimated revenue range)
- Contact information (owner name, email, phone, social handles — gathered from website, LinkedIn, etc.)
- Competitive positioning summary (1 paragraph)
- Customer voice summary with direct quotes
- Top 3–5 strengths with evidence
- Top 3–5 improvement opportunities with evidence and estimated financial impact
- AI Business Health Score with per-dimension breakdown (see rubric below)

### Step 4 — ICP Fit Scoring

Based on Stage B research, score each business for ICP fit. Select the top candidates.

**ICP Fit Criteria:**
- Matches target revenue/size range
- Owner is identifiable and reachable
- Clear operational pain points that AI can address
- ABHS in the sweet spot (3.0–6.0 — enough infrastructure to benefit, but haven't adopted AI)
- No signs of active AI consulting engagement

**Target:** Select the top 100 ICP-fit businesses per run.

### Step 5 — Generate Reports

For each selected business, generate a personalized **Axiom Intelligence Report** using the Typst template. The report must meet the presentation and analytical standard of a deliverable from McKinsey, BCG, or Bain — clean, structured, insight-led, and immediately actionable.

**Reports are generated using Tier 1 LLM** (customer-facing content — quality directly impacts conversion).

#### Report Structure (8 sections)

**1. Executive Summary** (1 page)
- One-paragraph overview of the business and its market position
- AI Business Health Score displayed prominently with a visual gauge
- The single most important finding in one sentence
- Three headline opportunities with estimated annual impact in dollars
- Written so the owner gets the full picture in 60 seconds without reading further

**2. Business Profile** (1 page)
- Business name, owner/decision-maker, locations, years in operation
- Services offered and estimated revenue range
- Customer mix (residential/commercial, one-time/recurring)
- Current technology stack (what they use today)
- Presented as a clean fact sheet — no narrative, just structured data

**3. Competitive Landscape** (1–2 pages)
- Positioning map: where this business sits vs. 3–5 direct competitors on key dimensions (reputation, pricing, service breadth, digital maturity)
- What competitors do better — specific, evidence-backed observations
- What this business does better — its genuine competitive advantages
- Competitive blind spots — things competitors are doing (especially with technology/AI) that this business is not
- Framed as strategic context, not a SWOT dump

**4. Customer Voice Analysis** (1–2 pages)
- Sentiment summary: overall trend (improving/stable/declining) based on review analysis
- Top 3 strengths customers consistently praise — each backed by a direct quote
- Top 3 pain points customers consistently report — each backed by a direct quote
- Review response analysis: does the business respond to reviews? How quickly? What tone?
- Net insight: what do customers actually think of this business, and what does that mean for growth?

**5. AI Business Health Score — Detailed Breakdown** (1–2 pages)
- Overall ABHS score with visual breakdown by dimension (see rubric section)
- Per-dimension score with a one-line evidence summary for each
- Comparison to industry average where possible (e.g., "Your digital presence scores 4.2 vs. an industry average of 5.5 for multi-location HVAC")
- The score must feel diagnostic, not judgmental — it's a tool, not a grade

**6. Opportunity Roadmap** (2–3 pages — the core of the report)
- Top 5 improvement opportunities ranked by estimated ROI
- Each opportunity presented as a structured brief:

| Element | What to Include |
|---------|-----------------|
| **Opportunity** | Clear, specific title (not "Improve Scheduling" — "Implement AI-Powered Dynamic Dispatching to Reduce Idle Technician Time") |
| **Evidence** | The specific observations that surfaced this opportunity (review quotes, website gaps, competitive comparison) |
| **Impact** | Estimated financial impact — revenue gained, cost saved, or capacity freed — with the reasoning behind the estimate |
| **Complexity** | Low / Medium / High — how hard is this to implement |
| **Timeline** | Estimated time to implement and time to see results |
| **Quick Win or Strategic** | Is this a 2-week quick win or a 3-month strategic initiative? |

- The roadmap should read like a consulting engagement plan — the owner can see exactly what to do, in what order, and what it's worth
- At least 2 of the 5 opportunities should be quick wins (implementable in under 30 days)

**7. How Axiom Can Help** (1 page)
- Map each opportunity from the roadmap to the relevant Axiom DFY service stage
- Show the 4-stage journey: Diagnose > Install Intelligence > Execute > Continuously Improve
- Include indicative pricing ranges
- This section is the only sales content in the report — it should feel like a natural extension of the roadmap, not a pitch
- Tone: advisory, not salesy. "Based on what we found, here's how we'd approach this" — not "Buy our service"

**8. Next Step** (half page)
- Clear, single CTA: book a 15-minute discovery call with the Founding Partner
- Include calendar link, email, and phone
- One sentence reinforcing the value: "We'll walk you through the findings and discuss which opportunities make sense to pursue first"
- No pressure, no urgency tactics, no "limited time offer"

#### Report Quality Standards

| Standard | What It Means |
|----------|---------------|
| **Insight-led, not data-led** | Every section leads with the "so what" — the insight — then provides supporting evidence. Never present raw data without interpretation. |
| **Evidence-backed** | Every claim is traceable to a specific observation (a review quote, a website screenshot, a competitive data point). No unsubstantiated assertions. |
| **Actionable** | The owner should be able to act on the report without hiring anyone. If they do hire Axiom, the report becomes the engagement brief — but it works standalone. |
| **Visually clean** | Clean typography, consistent layout, ample white space. The Typst template handles this — the LLM focuses on content quality. Charts, gauges, and tables where they add clarity. |
| **Concise** | Total report length: 8–12 pages. No padding. Every page earns its place. If a section has nothing insightful to say, it's shorter — not filled with boilerplate. |
| **Professional tone** | Written like a senior consultant briefing a CEO — direct, respectful, confident. No jargon without explanation. No hedging or filler phrases ("it could be argued that..."). |
| **Personalized** | The report reads like it was written specifically for this business. Generic advice that could apply to any company in the domain is a quality failure. |

**File naming:** `{company_name}_{run_id}.pdf`
**Storage:** Google Drive folder per run, organized by timestamp.

### Step 6 — Outreach

Send personalized messages to each business owner on behalf of the Founding Partner. **This is a red-gated action — requires Founder approval before any messages are sent.**

Outreach is rate-limited and compliance-first (see Compliance section below).

---

## AI Business Health Score (ABHS) Rubric

Standardized scoring methodology. Each dimension is scored 0–10, then weighted to produce the overall score.

| # | Dimension | Weight | What It Measures | Data Sources |
|---|-----------|--------|------------------|--------------|
| 1 | Digital presence | 15% | Website quality, SEO, accuracy of online listings | Website audit, Google listing |
| 2 | Online reputation | 10% | Review volume, average rating, owner response rate to reviews | Google, Facebook, Yelp |
| 3 | Customer communication | 15% | Automated booking, reminders, follow-ups, chatbots, response time | Website, mystery call/inquiry |
| 4 | Operational maturity | 15% | Standardized workflows, scheduling systems, quoting processes | Website, reviews (complaints about scheduling, wait times) |
| 5 | Data infrastructure | 15% | CRM usage, data collection, analytics capabilities | Website tech stack, job postings mentioning tools |
| 6 | Marketing sophistication | 10% | Content strategy, social media activity, lead generation | Social media, blog, ad presence |
| 7 | Technology stack | 10% | Cloud adoption, mobile tools, integration readiness | Website, app store presence, tech mentions |
| 8 | AI readiness | 10% | Existing AI/automation tools, team openness to tech | Website, job postings, social media |

**Overall ABHS** = Weighted average of all dimensions, rounded to 1 decimal.

### Score Interpretation

| Range | Label | Meaning | Axiom Fit |
|-------|-------|---------|-----------|
| 0–2.9 | Critical | Major gaps across the board; may lack basic infrastructure | Low — may not be ready to invest |
| 3.0–4.9 | Below average | Some digital foundation but significant improvement areas | High — strong need, clear ROI story |
| 5.0–6.9 | Average | Decent presence but underutilizing AI opportunities | High — ready to benefit from AI |
| 7.0–8.9 | Above average | Leveraging technology well, some optimization gaps | Medium — optimization focus |
| 9.0–10 | Advanced | Already AI-forward | Low — limited value-add |

**Sweet spot for Axiom: ABHS 3.0–6.9** — businesses with enough infrastructure to benefit from AI but haven't adopted it yet.

---

## Outreach Compliance

### Rate Limits Per Platform

| Platform | Limit | Notes |
|----------|-------|-------|
| Email | 50/day per sending domain | Use dedicated outreach domain (not axiomintelligence.xyz). Warm up the domain for 2 weeks before volume. |
| LinkedIn | 20 connection requests/day, 50 messages/week | Stay well under LinkedIn's limits to avoid account restrictions |
| Instagram | 10–15 DMs/day to non-followers | Highly throttled; use as secondary channel only |
| Facebook | 10–15 messages/day to non-connections | Use business page, not personal profile |

### Legal Requirements

| Regulation | Applies To | Requirements |
|------------|-----------|--------------|
| CAN-SPAM | USA email | Physical address in footer, unsubscribe link, no deceptive subject lines |
| GDPR | UK/EU email | Legitimate interest basis for B2B, opt-out mechanism, data processing transparency |
| CASL | Canada email | Implied consent for B2B (6-month window), identify sender, unsubscribe mechanism |

### Rules

1. **Never send from the primary domain** (axiomintelligence.xyz) — use a dedicated outreach domain.
2. **Always include an unsubscribe mechanism** in email outreach.
3. **Never automate social media DMs** — compose messages, but human-approve the send action.
4. **One platform at a time per prospect** — do not blast the same person across email + LinkedIn + Instagram simultaneously. Start with the platform where contact info is strongest; follow up on a second platform only after no response for 5+ days.
5. **CLO reviews all outreach templates** before first use.
6. **All outreach is a red-gated action** — Founder approves the batch before messages go out.

---

## Run Output

Each completed run produces:

| Output | Description |
|--------|-------------|
| **Run summary** | Domain, region, ICP used, dates, agent hours, token spend |
| **Business list** | All 100 selected businesses with ABHS scores and contact info |
| **Reports folder** | Google Drive link with 100 personalized Axiom Reports (PDF via Typst) |
| **Outreach log** | Per-business: platform used, message sent, date, response status |

---

## Success Metrics

Track these per run and across runs to iterate:

| Metric | Target | How Measured |
|--------|--------|--------------|
| Businesses sourced (Stage A input) | 200–300 | Raw list count |
| Stage A pass rate | 25–40% | Candidates after cheap filter |
| Stage B to ICP-fit rate | 50–70% | Selected / researched |
| Reports generated | 100 | PDFs in Drive folder |
| Outreach sent | 100 | Messages logged |
| Response rate | 5–10% | Replies / messages sent |
| Discovery calls booked | 3–5 per run | Positive responses |
| Cost per run | Track | Tokens (Tier 1 + Tier 2) + browsing time |
| Cost per qualified lead | Track | Total run cost / discovery calls booked |

---

## Data Schema

Use Airtable (or a free alternative like NocoDB) to track run and business data.

### Table: runs

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| domain | Text | Input domain (e.g., "Multi-location HVAC") |
| country | Text | Input country |
| region | Text | Input region/ZIP |
| icp_description | Long text | ICP criteria used |
| status | Select | planned / in_progress / completed / failed |
| businesses_sourced | Number | Raw businesses found |
| businesses_qualified | Number | After Stage A filter |
| businesses_selected | Number | After ICP fit scoring |
| reports_generated | Number | PDFs created |
| outreach_sent | Number | Messages sent |
| responses_received | Number | Replies received |
| calls_booked | Number | Discovery calls |
| tier1_tokens | Number | Tier 1 token spend |
| tier2_tokens | Number | Tier 2 token spend |
| total_cost | Currency | Total run cost (tokens + any tool subscriptions) |
| drive_link | URL | Google Drive folder |
| created_at | DateTime | Run creation timestamp |
| completed_at | DateTime | Run completion timestamp |

### Table: businesses

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| run_id | Link | Foreign key to runs table |
| business_name | Text | Name of the business |
| owner_name | Text | Owner / decision-maker name |
| email | Email | Owner email (if found) |
| phone | Phone | Owner phone (if found) |
| linkedin | URL | Owner LinkedIn (if found) |
| instagram | URL | Business/owner Instagram (if found) |
| facebook | URL | Business Facebook page (if found) |
| website | URL | Business website |
| locations | Number | Number of locations |
| services_summary | Long text | 2-liner on services offered |
| strengths | Long text | Key positive points |
| improvement_areas | Long text | Areas to improve |
| abhs_score | Number (1 decimal) | AI Business Health Score (0–10) |
| abhs_breakdown | Long text | Per-dimension scores (JSON or structured text) |
| icp_fit | Boolean | Selected as ICP fit (yes/no) |
| report_generated | Boolean | PDF report created |
| drive_link | URL | Individual report link (only when icp_fit = true) |
| outreach_platform | Select | email / linkedin / instagram / facebook / none |
| outreach_status | Select | not_started / drafted / sent / replied / call_booked / declined / no_response |
| outreach_date | Date | When message was sent |
| response_date | Date | When reply was received |
| notes | Long text | Free-form notes |
| created_at | DateTime | Record creation timestamp |

---

## Token Optimization

1. **Discovery and quick screen are browsing tasks** — agents use a browser, not LLM calls. Token cost for Steps 1–2 is near zero.
2. **Deep research uses Tier 2** — the analytical framework is structured enough that Tier 2 produces strong synthesis. Escalate to Tier 1 only when the analysis requires complex multi-step reasoning.
3. **Report generation uses Tier 1** — customer-facing quality matters here. This is the one step where premium LLM quality directly impacts conversion.
4. **Batch similar operations** — process all discovery first, then all deep research, then all reports. Avoid context-switching overhead.
5. **Cache reusable context** — ICP description, research framework, report template instructions, and scoring rubric are loaded once per run, not per business.
6. **Template the report structure** — the Typst template handles layout; the LLM fills in business-specific content sections only.
7. **Reuse competitive research** — when multiple businesses are in the same geography, competitor analysis overlaps. Do it once and reference it across businesses in the same run.
8. **Track cost per run** — every run logs Tier 1 tokens, Tier 2 tokens, and browsing time to the CV ledger. If cost per qualified lead exceeds acceptable thresholds, review and optimize the pipeline.

---

## Dependencies

Before the first run:

| Dependency | Owner | Status |
|------------|-------|--------|
| Typst report template | CTO + CDO | Not started |
| ABHS scoring rubric validation (test against 10 real businesses) | CRO + CPO | Not started |
| Deep research framework validation (test 3 businesses end-to-end, verify McKinsey-grade quality bar) | CPO + CRO | Not started |
| Browser access for agents (Grok bots with browsing capability) | CTO | Not started |
| Outreach email domain setup + warmup | CMO + COO | Not started |
| Airtable/NocoDB instance setup | COO | Not started |
| Outreach message templates (email + LinkedIn) | CMO + CPO | Not started |
| CLO review of outreach templates | CLO | Not started |
