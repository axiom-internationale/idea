"""Portfolio section with venture vertical cards."""

from fasthtml.common import H2, Article, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.topline import card_topline

PORTFOLIO = get_section("portfolio")
VENTURES = {card["key"]: card for card in PORTFOLIO["cards"]}


def _ventures():
    d = PORTFOLIO["ventures"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="portfolio-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--pearl card--ventures",
        data_depth="3",
        data_reveal="",
    )


def _vertical(key, num, color, depth, inverse=False):
    d = VENTURES[key]
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    glyph = d["topline"][1]
    right = Span("Live", cls="status") if glyph == "Live" else glyph
    return Article(
        card_topline(d["topline"][0], right),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls=label_cls),
        cls=f"card card--{color} card--vent-{num}",
        data_depth=str(depth),
        data_reveal="",
    )


def _vent_stats():
    d = PORTFOLIO["stats"]
    return Article(
        card_topline(d["topline"][0], Span(d["topline"][1], cls="metric-glyph")),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="opt-title"),
        Span(d["note"], cls="command-note"),
        cls="card card--dark card--vent-stats",
        data_depth="3",
        data_reveal="",
    )


def portfolio_section():
    return Section(
        section_divider(PORTFOLIO["divider"]),
        Div(
            _ventures(),
            _vertical("ventures_1", 1, "teal", 5),
            _vertical("ventures_2", 2, "violet", 4, inverse=True),
            _vertical("ventures_3", 3, "rose", 5),
            _vent_stats(),
            cls="bento bento--portfolio",
            data_bento="",
        ),
        cls="section",
        id="portfolio",
        aria_labelledby="portfolio-title",
    )
