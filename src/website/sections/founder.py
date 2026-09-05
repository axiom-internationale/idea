"""Founder section."""

from fasthtml.common import Article, Br, Div, Em, H2, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _bio():
    return Article(
        eyebrow("The human at the helm"),
        H2("One founder.", Br(), Em("Infinite leverage."), cls="section-h2", id="founder-title"),
        P(
            "Axiom Intelligence was built on a conviction: one person with the right system "
            "can outperform entire organizations. Not by working harder—by directing smarter.",
            cls="intro-sm",
        ),
        P(
            "The founder sets the vision, approves the high-stakes decisions, and lets the "
            "factory handle everything else.",
            cls="intro-sm",
        ),
        cls="card card--pearl card--founder-bio", data_depth="3", data_reveal="",
    )


def _role():
    return Article(
        card_topline("Role", "01"),
        Strong("Vision &", Br(), "direction.", cls="opt-title"),
        Span("Strategy, final approvals, and the decisions that shape everything.", cls="command-note"),
        cls="card card--dark card--founder-role", data_depth="4", data_reveal="",
    )


def _philosophy():
    return Article(
        card_topline("Philosophy", "⎁"),
        Div(
            Strong("Build systems, not teams."),
            Span("The right architecture beats the right hire every time."),
            cls="card-label card-label--inverse",
        ),
        cls="card card--sun card--founder-phil", data_depth="5", data_reveal="",
    )


def founder_section():
    return Section(
        section_divider("The founder"),
        Div(_bio(), _role(), _philosophy(), cls="bento bento--founder", data_bento=""),
        cls="section", id="founder", aria_labelledby="founder-title",
    )
