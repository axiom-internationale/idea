"""Portfolio section with venture vertical cards."""

from fasthtml.common import Article, Br, Div, Em, H2, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _ventures():
    return Article(
        eyebrow("The ventures"),
        H2("Building in", Br(), Em("parallel."), cls="section-h2", id="portfolio-title"),
        P(
            "The factory doesn't build one company at a time. It runs multiple verticals "
            "simultaneously—each with its own strategy, each sharing the same intelligence.",
            cls="intro-sm",
        ),
        cls="card card--pearl card--ventures", data_depth="3", data_reveal="",
    )


def _vertical(num, status_or_glyph, title, desc, color, depth, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    right = Span("Live", cls="status") if status_or_glyph == "Live" else status_or_glyph
    return Article(
        card_topline(f"Vertical 0{num}", right),
        Div(Strong(title), Span(desc), cls=label_cls),
        cls=f"card card--{color} card--vent-{num}", data_depth=str(depth), data_reveal="",
    )


def _vent_stats():
    return Article(
        card_topline("Pipeline", Span("↗", cls="metric-glyph")),
        Strong("More", Br(), "coming.", cls="opt-title"),
        Span("The factory identifies opportunities continuously.", cls="command-note"),
        cls="card card--dark card--vent-stats", data_depth="3", data_reveal="",
    )


def portfolio_section():
    return Section(
        section_divider("Portfolio"),
        Div(
            _ventures(),
            _vertical(1, "Live", "SaaS Tooling", "Software products that solve real workflow problems.", "teal", 5),
            _vertical(2, "⎁", "AI Services", "Intelligent automation for businesses that need it.", "violet", 4, inverse=True),
            _vertical(3, "⎁", "Digital Commerce", "Revenue-generating storefronts and marketplaces.", "rose", 5),
            _vent_stats(),
            cls="bento bento--portfolio", data_bento="",
        ),
        cls="section", id="portfolio", aria_labelledby="portfolio-title",
    )
