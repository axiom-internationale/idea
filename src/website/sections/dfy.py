"""DFY (Done For You) landing page sections."""

from fasthtml.common import (
    H1,
    H2,
    A,
    Article,
    Br,
    Div,
    Em,
    I,
    P,
    Section,
    Span,
    Strong,
)

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.icons import ARROW_SVG
from website.components.section_divider import section_divider
from website.components.stat_grid import stat_grid
from website.components.topline import card_topline

DFY_HERO = get_section("hero", page="dfy")
DFY_HERO_CARDS = {card["key"]: card for card in DFY_HERO["cards"]}
DFY_MISSION = get_section("mission", page="dfy")
DFY_MIS = {card["key"]: card for card in DFY_MISSION["cards"]}
DFY_SERVICES = get_section("services", page="dfy")
DFY_SVC = {card["key"]: card for card in DFY_SERVICES["cards"]}
DFY_DOMAINS = get_section("domains", page="dfy")
DFY_DOM = {card["key"]: card for card in DFY_DOMAINS["cards"]}
DFY_PROCESS = get_section("process", page="dfy")
DFY_STEPS = {step["key"]: step for step in DFY_PROCESS["steps"]}
DFY_EVOLVE = get_section("evolve", page="dfy")
DFY_EVO = {card["key"]: card for card in DFY_EVOLVE["cards"]}
DFY_CTA = get_section("cta", page="dfy")
DFY_CTA_CARDS = {card["key"]: card for card in DFY_CTA["cards"]}


def _topline(left, right):
    return card_topline(left, Span("Live", cls="status") if right == "Live" else right)


def _label_pair(label, inverse=False):
    cls = "card-label card-label--inverse" if inverse else "card-label"
    return Div(Strong(label[0]), Span(label[1]), cls=cls)


# ── Hero ──────────────────────────────────────────────────────────


def _manifesto():
    d = DFY_HERO["manifesto"]
    link = d["links"][0]
    return Article(
        eyebrow(d["eyebrow"]),
        H1(d["title"][0], Br(), Em(d["title"][1]), id="dfy-hero-title"),
        P(
            d["intro"],
            cls="intro",
        ),
        Div(
            A(
                f"{d['primary_button']['label']} ",
                ARROW_SVG,
                cls="button button--primary",
                href=d["primary_button"]["href"],
            ),
            A(f"{link['label']} ", Span(link["glyph"]), cls="text-link", href=link["href"]),
            cls="hero-actions",
        ),
        cls="card card--dfy-manifesto",
        data_depth="3",
    )


def _ai_badge():
    d = DFY_HERO_CARDS["ai"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Span(cls="orbit orbit--one"),
            Span(cls="orbit orbit--two"),
            Span(cls="orbit orbit--three"),
            Span(I(), cls="solar-core"),
            Span(cls="satellite satellite--one"),
            Span(cls="satellite satellite--two"),
            cls="solar-system",
            aria_hidden="true",
        ),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--sun card--dfy-ai",
        data_depth="14",
    )


def _services_count():
    return Article(
        _topline(*DFY_HERO_CARDS["scount"]["topline"]),
        stat_grid([tuple(stat) for stat in DFY_HERO_CARDS["scount"]["stats"]]),
        cls="card card--glass card--dfy-scount",
        data_depth="4",
    )


def _industries_count():
    return Article(
        _topline(*DFY_HERO_CARDS["ind"]["topline"]),
        Div(
            Strong(DFY_HERO_CARDS["ind"]["label"][0]),
            Span(DFY_HERO_CARDS["ind"]["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--violet card--dfy-ind",
        data_depth="5",
    )


def _always_on():
    d = DFY_HERO_CARDS["always"]
    return Article(
        _topline(*d["topline"]),
        Div(Span(cls="pulse", aria_hidden="true"), Strong(d["headline"]), cls="always-pulse"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--pearl card--dfy-always",
        data_depth="4",
    )


def _speed():
    d = DFY_HERO_CARDS["speed"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--mint card--dfy-speed",
        data_depth="4",
    )


def _web_preview():
    d = DFY_HERO_CARDS["web"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="step-blocks", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--teal card--dfy-web",
        data_depth="5",
    )


def _seo_preview():
    d = DFY_HERO_CARDS["seo"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="async-mark", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--amber card--dfy-seo",
        data_depth="5",
    )


def _auto_preview():
    d = DFY_HERO_CARDS["auto"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--rose card--dfy-auto",
        data_depth="4",
    )


def dfy_hero_section():
    return Section(
        Div(
            _manifesto(),
            _ai_badge(),
            _services_count(),
            _industries_count(),
            _always_on(),
            _speed(),
            _web_preview(),
            _seo_preview(),
            _auto_preview(),
            cls="bento bento--dfy-hero",
            data_bento="",
        ),
        cls="hero",
        id="top",
        aria_labelledby="dfy-hero-title",
    )


# ── Mission ──────────────────────────────────────────────────────


def _mission_main():
    d = DFY_MISSION["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-mission-title"),
        P(
            d["body"][0],
            cls="intro-sm",
        ),
        P(
            d["body"][1],
            cls="intro-sm",
        ),
        cls="card card--pearl card--dfy-mis-main",
        data_depth="3",
        data_reveal="",
    )


def _mission_consulting():
    d = DFY_MIS["consult"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Span(cls="orbit orbit--one"),
            Span(cls="orbit orbit--two"),
            Span(I(), cls="solar-core"),
            cls="solar-system solar-system--sm",
            aria_hidden="true",
        ),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--dark card--dfy-mis-consult",
        data_depth="5",
        data_reveal="",
    )


def _mission_access():
    d = DFY_MIS["access"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"], cls="pillar-title"),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--sun card--dfy-mis-access",
        data_depth="4",
        data_reveal="",
    )


def _mission_playbook():
    d = DFY_MIS["playbook"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--indigo card--dfy-mis-playbook",
        data_depth="5",
        data_reveal="",
    )


def _mission_scale():
    d = DFY_MIS["scale"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--mint card--dfy-mis-scale",
        data_depth="4",
        data_reveal="",
    )


def dfy_mission_section():
    return Section(
        section_divider(DFY_MISSION["divider"]),
        Div(
            _mission_main(),
            _mission_consulting(),
            _mission_access(),
            _mission_playbook(),
            _mission_scale(),
            cls="bento bento--dfy-mission",
            data_bento="",
        ),
        cls="section",
        id="dfy-mission",
        aria_labelledby="dfy-mission-title",
    )


# ── Services ─────────────────────────────────────────────────────


def _svc_main():
    d = DFY_SERVICES["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-services-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--dark card--dfy-svc-main",
        data_depth="3",
        data_reveal="",
    )


def _svc_card(card, color, depth, slug, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    return Article(
        card_topline(f"Category 0{card['num']}", card["glyph"]),
        Div(Strong(card["title"]), Span(card["desc"]), cls=label_cls),
        cls=f"card card--{color} card--dfy-svc-{slug}",
        data_depth=str(depth),
        data_reveal="",
    )


def dfy_services_section():
    return Section(
        section_divider(DFY_SERVICES["divider"]),
        Div(
            _svc_main(),
            _svc_card(DFY_SVC["web"], "teal", 5, "web"),
            _svc_card(DFY_SVC["agents"], "violet", 4, "agents", inverse=True),
            _svc_card(DFY_SVC["ops"], "amber", 5, "ops"),
            _svc_card(DFY_SVC["growth"], "mint", 4, "growth"),
            cls="bento bento--dfy-services",
            data_bento="",
        ),
        cls="section",
        id="dfy-services",
        aria_labelledby="dfy-services-title",
    )


# ── Domains ──────────────────────────────────────────────────────


def _dom_main():
    d = DFY_DOMAINS["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-domains-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--pearl card--dfy-dom-main",
        data_depth="3",
        data_reveal="",
    )


def _dom_card(card, color, depth, slug, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    return Article(
        card_topline(f"Domain 0{card['num']}", "○"),
        Div(Strong(card["title"]), Span(card["examples"]), cls=label_cls),
        cls=f"card card--{color} card--dfy-dom-{slug}",
        data_depth=str(depth),
        data_reveal="",
    )


def dfy_domains_section():
    return Section(
        section_divider(DFY_DOMAINS["divider"]),
        Div(
            _dom_main(),
            _dom_card(DFY_DOM["legal"], "indigo", 5, "legal", inverse=True),
            _dom_card(DFY_DOM["health"], "teal", 4, "health"),
            _dom_card(DFY_DOM["finance"], "amber", 5, "finance"),
            _dom_card(DFY_DOM["home"], "rose", 4, "home"),
            cls="bento bento--dfy-domains",
            data_bento="",
        ),
        cls="section",
        id="dfy-domains",
        aria_labelledby="dfy-domains-title",
    )


# ── Process ──────────────────────────────────────────────────────


def _proc_main():
    d = DFY_PROCESS["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-process-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--glass card--dfy-proc-main",
        data_depth="3",
        data_reveal="",
    )


def _proc_step(card, color, depth, slug, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    return Article(
        card_topline(f"Step 0{card['num']}", card["glyph"]),
        Div(Strong(card["title"]), Span(card["desc"]), cls=label_cls),
        cls=f"card card--{color} card--dfy-step-{slug}",
        data_depth=str(depth),
        data_reveal="",
    )


def dfy_process_section():
    return Section(
        section_divider(DFY_PROCESS["divider"]),
        Div(
            _proc_main(),
            _proc_step(DFY_STEPS["onboard"], "teal", 5, "onboard"),
            _proc_step(DFY_STEPS["build"], "rose", 5, "build"),
            _proc_step(DFY_STEPS["launch"], "indigo", 5, "launch", inverse=True),
            _proc_step(DFY_STEPS["optimize"], "dark", 4, "optimize"),
            _proc_step(DFY_STEPS["scale"], "mint", 4, "scale"),
            cls="bento bento--dfy-process",
            data_bento="",
        ),
        cls="section",
        id="dfy-process",
        aria_labelledby="dfy-process-title",
    )


# ── Evolve ──────────────────────────────────────────────────────


def _evolve_main():
    d = DFY_EVOLVE["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-evolve-title"),
        P(
            d["body"][0],
            cls="intro-sm",
        ),
        P(
            d["body"][1],
            cls="intro-sm",
        ),
        cls="card card--dark card--dfy-evo-main",
        data_depth="3",
        data_reveal="",
    )


def _evolve_research():
    d = DFY_EVO["research"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="step-dots", aria_hidden="true"),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label",
        ),
        cls="card card--teal card--dfy-evo-research",
        data_depth="5",
        data_reveal="",
    )


def _evolve_learn():
    d = DFY_EVO["learn"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label",
        ),
        cls="card card--amber card--dfy-evo-learn",
        data_depth="4",
        data_reveal="",
    )


def _evolve_adapt():
    d = DFY_EVO["adapt"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="async-mark", aria_hidden="true"),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--indigo card--dfy-evo-adapt",
        data_depth="5",
        data_reveal="",
    )


def _evolve_compound():
    d = DFY_EVO["compound"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--lime card--dfy-evo-compound",
        data_depth="4",
        data_reveal="",
    )


def dfy_evolve_section():
    return Section(
        section_divider(DFY_EVOLVE["divider"]),
        Div(
            _evolve_main(),
            _evolve_research(),
            _evolve_learn(),
            _evolve_adapt(),
            _evolve_compound(),
            cls="bento bento--dfy-evolve",
            data_bento="",
        ),
        cls="section",
        id="dfy-evolve",
        aria_labelledby="dfy-evolve-title",
    )


# ── CTA ──────────────────────────────────────────────────────────


def _cta():
    d = DFY_CTA["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-connect-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        A(
            f"{d['button']['label']} ",
            ARROW_SVG,
            cls="button button--primary",
            href=d["button"]["href"],
        ),
        cls="card card--dark card--dfy-cta",
        data_depth="3",
        data_reveal="",
    )


def _email():
    d = DFY_CTA_CARDS["email"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        A(
            cls="card-overlay-link",
            href=d["href"],
            aria_label=f"Email {d['label'][1]}",
        ),
        cls="card card--sun card--dfy-email",
        data_depth="5",
        data_reveal="",
    )


def _powered():
    d = DFY_CTA_CARDS["powered"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label",
        ),
        A(cls="card-overlay-link", href=d["href"], aria_label="Learn about Axiom Intelligence"),
        cls="card card--glass card--dfy-powered",
        data_depth="4",
        data_reveal="",
    )


def _stats():
    d = DFY_CTA_CARDS["stat"]
    return Article(
        card_topline(d["topline"][0], Span(d["topline"][1], cls="metric-glyph")),
        stat_grid([tuple(stat) for stat in d["stats"]]),
        cls="card card--glass card--dfy-stat",
        data_depth="4",
        data_reveal="",
    )


def _home_link():
    d = DFY_CTA_CARDS["home"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        A(cls="card-overlay-link", href=d["href"], aria_label="Visit Axiom Intelligence homepage"),
        cls="card card--violet card--dfy-home",
        data_depth="4",
        data_reveal="",
    )


def dfy_cta_section():
    return Section(
        section_divider(DFY_CTA["divider"]),
        Div(
            _cta(),
            _email(),
            _powered(),
            _stats(),
            _home_link(),
            cls="bento bento--dfy-cta",
            data_bento="",
        ),
        cls="section",
        id="dfy-connect",
        aria_labelledby="dfy-connect-title",
    )
