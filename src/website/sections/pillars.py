"""Four pillars section."""

from fasthtml.common import Article, Br, Div, Em, H2, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _main():
    return Article(
        eyebrow("Operating principles"),
        H2("Four pillars.", Br(), Em("One system."), cls="section-h2", id="pillars-title"),
        P(
            "Every decision, every process, every agent in the factory "
            "operates under four non-negotiable principles.",
            cls="intro-sm",
        ),
        cls="card card--dark card--pillar-main", data_depth="3", data_reveal="",
    )


def _self_improving():
    return Article(
        card_topline("Pillar 01", "↻"),
        Strong("Self-", Br(), "improving.", cls="pillar-title"),
        Div(Span("Every cycle makes the system smarter. Intelligence compounds."), cls="card-label"),
        cls="card card--mint card--pillar-self", data_depth="5", data_reveal="",
    )


def _profitable():
    return Article(
        card_topline("Pillar 02", "↗"),
        Strong("Profitable.", cls="pillar-title"),
        Div(Span("Revenue is truth. Every decision measured against real returns."), cls="card-label"),
        cls="card card--amber card--pillar-profit", data_depth="4", data_reveal="",
    )


def _stable():
    return Article(
        card_topline("Pillar 03", "∞"),
        Strong("Stable.", cls="pillar-title"),
        Div(Span("24/7 uptime. No burnout, no turnover. Mechanical reliability."), cls="card-label card-label--inverse"),
        cls="card card--indigo card--pillar-stable", data_depth="5", data_reveal="",
    )


def _autonomous():
    return Article(
        card_topline("Pillar 04", "⎁"),
        Strong("Autonomous.", cls="pillar-title"),
        Div(Span("The factory runs itself. Agents decide, execute, and coordinate."), cls="card-label"),
        cls="card card--glass card--pillar-auton", data_depth="4", data_reveal="",
    )


def pillars_section():
    return Section(
        section_divider("The pillars"),
        Div(
            _main(), _self_improving(), _profitable(), _stable(), _autonomous(),
            cls="bento bento--pillars", data_bento="",
        ),
        cls="section", id="pillars", aria_labelledby="pillars-title",
    )
