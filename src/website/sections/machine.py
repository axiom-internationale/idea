"""How-it-works section with pipeline bento grid."""

from fasthtml.common import Article, Br, Div, Em, H2, I, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.stat_grid import stat_grid


def _pipeline():
    return Article(
        eyebrow("The process"),
        H2("From spark", Br(), Em("to scale."), cls="section-h2", id="machine-title"),
        P(
            "Every idea enters the same machine: research, build, launch, optimize. "
            "The factory handles each stage autonomously—from market analysis to revenue.",
            cls="intro-sm",
        ),
        Div(
            Span(cls="pip-dot pip-dot--active"), Span("Idea", cls="pip-label"), Span(cls="pip-line"),
            Span(cls="pip-dot pip-dot--active"), Span("Research", cls="pip-label"), Span(cls="pip-line"),
            Span(cls="pip-dot pip-dot--active"), Span("Build", cls="pip-label"), Span(cls="pip-line"),
            Span(cls="pip-dot"), Span("Launch", cls="pip-label"), Span(cls="pip-line"),
            Span(cls="pip-dot"), Span("Revenue", cls="pip-label"),
            cls="pipeline-flow", aria_hidden="true",
        ),
        cls="card card--glass card--pipeline", data_depth="3", data_reveal="",
    )


def _research():
    return Article(
        card_topline("Step 01", "⎁"),
        Div(I(), I(), I(), I(), I(), I(), cls="step-dots", aria_hidden="true"),
        Div(Strong("Research"), Span("Deep market analysis before market entry."), cls="card-label"),
        cls="card card--teal card--research", data_depth="5", data_reveal="",
    )


def _build():
    return Article(
        card_topline("Step 02", "⎁"),
        Div(I(), I(), I(), cls="step-blocks", aria_hidden="true"),
        Div(Strong("Build"), Span("Ship products, not pitch decks."), cls="card-label"),
        cls="card card--rose card--build", data_depth="5", data_reveal="",
    )


def _launch():
    return Article(
        card_topline("Step 03", "⎁"),
        Div("↗", cls="launch-arrow", aria_hidden="true"),
        Div(Strong("Launch"), Span("Go-to-market at machine speed."), cls="card-label card-label--inverse"),
        cls="card card--indigo card--launch", data_depth="5", data_reveal="",
    )


def _optimize():
    return Article(
        card_topline("Step 04", "↻"),
        Strong("Optimize.", Br(), "Compound.", cls="opt-title"),
        Div(I(), cls="metric-line", aria_hidden="true"),
        Span("Every cycle, the system gets sharper.", cls="command-note"),
        cls="card card--dark card--opt", data_depth="4", data_reveal="",
    )


def _always_on():
    return Article(
        card_topline("Uptime", "∞"),
        Div(Span(cls="pulse", aria_hidden="true"), Strong("Always on."), cls="always-pulse"),
        Div(Strong("No weekends. No holidays."), Span("The factory never sleeps."), cls="card-label"),
        cls="card card--pearl card--always", data_depth="4", data_reveal="",
    )


def _stats():
    return Article(
        card_topline("Factory output", Span("Live", cls="status")),
        stat_grid([("24/7", "Active"), ("∞", "Potential"), ("1", "Human")]),
        cls="card card--glass card--stats", data_depth="3", data_reveal="",
    )


def _loop():
    return Article(
        card_topline("The flywheel", "↻"),
        Div(I(), I(), I(), cls="loop-ring", aria_hidden="true"),
        Div(Strong("Learn. Improve. Repeat."), Span("Compounding intelligence across every company."), cls="card-label"),
        cls="card card--amber card--loop", data_depth="4", data_reveal="",
    )


def _speed():
    return Article(
        card_topline("Velocity", "↗"),
        Strong("10x speed.", Br(), "1/10th cost.", cls="speed-title"),
        Span("When agents work, capital stays lean.", cls="speed-note"),
        cls="card card--mint card--speed", data_depth="4", data_reveal="",
    )


def machine_section():
    return Section(
        section_divider("How it works"),
        Div(
            _pipeline(), _research(), _build(), _launch(),
            _optimize(), _always_on(), _stats(), _loop(), _speed(),
            cls="bento bento--machine", data_bento="",
        ),
        cls="section", id="machine", aria_labelledby="machine-title",
    )
