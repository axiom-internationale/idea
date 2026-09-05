"""DNA / origin section."""

from fasthtml.common import Article, Br, Div, Em, H2, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _story():
    return Article(
        eyebrow("The origin"),
        H2("Born from", Br(), Em("a question."), cls="section-h2", id="dna-title"),
        P(
            "What if one person could build and run many profitable companies—not by hiring "
            "hundreds, but by directing an intelligent system that does the work?",
            cls="intro-sm",
        ),
        P(
            "That question became Axiom Intelligence: a factory where AI agents operate as "
            "a unified workforce under human direction.",
            cls="intro-sm",
        ),
        cls="card card--pearl card--story", data_depth="3", data_reveal="",
    )


def _year():
    return Article(
        card_topline("Founded", "⎁"),
        Strong("2026", cls="year-num"),
        Span("Axiom Intelligence Inc.", cls="command-note"),
        cls="card card--dark card--year", data_depth="4", data_reveal="",
    )


def _different():
    return Article(
        card_topline("No overhead", "⎁"),
        Div(Strong("Zero employees.", Br(), "Pure execution."), cls="card-label"),
        cls="card card--rose card--different", data_depth="5", data_reveal="",
    )


def _values():
    return Article(
        card_topline("Core values", "03"),
        Div(Span("Speed"), Span("Focus"), Span("Compounding"), cls="vals-list", aria_hidden="true"),
        Div(Strong("Move fast, stay sharp, stack gains."), cls="card-label"),
        cls="card card--lime card--vals", data_depth="4", data_reveal="",
    )


def _principle():
    return Article(
        card_topline("Axiom", "01"),
        Strong("Revenue", Br(), "is truth.", cls="principle-text"),
        Div(Span("The only metric that matters."), cls="card-label"),
        cls="card card--amber card--principle", data_depth="5", data_reveal="",
    )


def dna_section():
    return Section(
        section_divider("The DNA"),
        Div(
            _story(), _year(), _different(), _values(), _principle(),
            cls="bento bento--dna", data_bento="",
        ),
        cls="section", id="dna", aria_labelledby="dna-title",
    )
