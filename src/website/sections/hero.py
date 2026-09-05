"""Hero bento grid section."""

from fasthtml.common import (
    A, Article, B, Br, Button, Div, Em, H1, H2, I, P, Section, Small, Span, Strong,
)

from website.components.icons import ARROW_SVG
from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.agent_row import agent_row


def _manifesto():
    return Article(
        eyebrow("A personalized agentic factory"),
        H1("Many businesses.", Br(), Em("One intelligence."), id="hero-title"),
        P(
            "Axiom Intelligence is a self-directed organization that turns ideas into "
            "enduring, profitable companies—with one human at the helm.",
            cls="intro",
        ),
        Div(
            Button(
                "Read the factory brief", ARROW_SVG,
                cls="button button--primary", type="button", data_open_brief="",
            ),
            A("Explore the system ", Span("↓"), cls="text-link", href="#machine"),
            cls="hero-actions",
        ),
        cls="card card--manifesto", data_depth="3",
    )


def _status():
    return Article(
        card_topline("Workforce status", "24 / 7"),
        Div(
            Span(cls="pulse", aria_hidden="true"),
            Span("Agentic workforce ", B("active")),
            cls="hero-note",
        ),
        P("One system.", Br(), Strong("Always in motion."), cls="status-copy"),
        cls="card card--status-card", data_depth="6",
    )


def _sun():
    return Article(
        card_topline("01 / Origin", "⎁"),
        Div(
            Span(cls="orbit orbit--one"), Span(cls="orbit orbit--two"), Span(cls="orbit orbit--three"),
            Span(I(), cls="solar-core"),
            Span(cls="satellite satellite--one"), Span(cls="satellite satellite--two"),
            cls="solar-system", aria_hidden="true",
        ),
        Div(Strong("Founding Partner"), Span("The only human in the system"), cls="card-label card-label--inverse"),
        cls="card card--sun card--large", data_depth="14",
    )


def _orchestrator():
    return Article(
        card_topline("02 / Direction", Span("Live", cls="status")),
        agent_row("GS", "General Secretary", "Orchestrator & manager"),
        Div(I(), I(), I(), I(), cls="signal-lines", aria_hidden="true"),
        cls="card card--glass card--orchestrator", data_depth="8",
    )


def _think():
    return Article(
        card_topline("03 / Intelligence", "11"),
        Div(H2("Think", Br(), "Tank"), P("One shared C-suite, across every company.")),
        Div(Span("CE"), Span("CF"), Span("CT"), Span("CM"), cls="stacked-initials", aria_hidden="true"),
        cls="card card--lime card--think", data_depth="6",
    )


def _verticals():
    return Article(
        card_topline("04 / Expansion", "∞"),
        Div(I(), I(), I(), I(), I(), cls="vertical-icon", aria_hidden="true"),
        Div(Strong("Company Verticals"), Span("Parallel by design"), cls="card-label card-label--inverse"),
        cls="card card--violet card--verticals", data_depth="10",
    )


def _metrics():
    return Article(
        card_topline("Operating principle", Span("↗", cls="metric-glyph")),
        Strong("Profitability", Br(), "first."),
        Div(I(), cls="metric-line", aria_hidden="true"),
        Span("Decisions measured", Br(), "against real revenue.", cls="metric-caption"),
        cls="card card--dark card--metrics", data_depth="4",
    )


def _gates():
    return Article(
        card_topline("Safe to scale", "●"),
        Div(Span(), Span(), Span(), cls="gate-grid", aria_hidden="true"),
        Div(
            Strong("Human approval, when it matters."),
            Span("Clear gates for money, legal & irreversible moves."),
            cls="card-label",
        ),
        cls="card card--pearl card--gates", data_depth="7",
    )


def _async():
    return Article(
        card_topline("Operating rhythm", "↗"),
        Div(I(), I(), I(), cls="async-mark", aria_hidden="true"),
        Div(Strong("Async by default."), Span("Focus compounds when work never waits."), cls="card-label"),
        cls="card card--async", data_depth="5",
    )


def _command():
    return Article(
        card_topline("Control layer", "01"),
        P("The human gives direction.", Br(), Strong("The factory does the work.")),
        Span("Final approval for the moves that matter.", cls="command-note"),
        cls="card card--command", data_depth="4",
    )


def _memory():
    return Article(
        card_topline("Memory", "⎁"),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        Div(Strong("Local-first."), Span("Readable, durable, yours."), cls="card-label"),
        cls="card card--memory", data_depth="7",
    )


def _parallel():
    return Article(
        card_topline("Scale", "n"),
        P(Strong("One C-suite."), Br(), "Every company."),
        Div(I(), I(), I(), I(), I(), cls="parallel-bars", aria_hidden="true"),
        Span("Built to operate in parallel."),
        cls="card card--parallel", data_depth="5",
    )


def hero_section():
    return Section(
        Div(
            _manifesto(), _status(), _sun(), _orchestrator(),
            _think(), _verticals(), _metrics(), _gates(),
            _async(), _command(), _memory(), _parallel(),
            cls="bento bento--hero", data_bento="",
        ),
        cls="hero", id="top", aria_labelledby="hero-title",
    )
