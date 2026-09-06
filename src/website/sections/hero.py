"""Hero bento grid section."""

from fasthtml.common import (
    H1,
    H2,
    A,
    Article,
    B,
    Br,
    Button,
    Div,
    Em,
    I,
    P,
    Section,
    Span,
    Strong,
)

from data_service import get_section
from website.components.agent_row import agent_row
from website.components.eyebrow import eyebrow
from website.components.icons import ARROW_SVG
from website.components.topline import card_topline

HERO = get_section("hero")
CARDS = {card["key"]: card for card in HERO["cards"]}


def _topline(left, right):
    return card_topline(left, Span("Live", cls="status") if right == "Live" else right)


def _label_pair(label, inverse=False):
    cls = "card-label card-label--inverse" if inverse else "card-label"
    return Div(Strong(label[0]), Span(label[1]), cls=cls)


def _manifesto():
    d = HERO["manifesto"]
    return Article(
        eyebrow(d["eyebrow"]),
        H1(d["title"][0], Br(), Em(d["title"][1]), id="hero-title"),
        P(
            d["intro"],
            cls="intro",
        ),
        Div(
            Button(
                d["primary_button"]["label"],
                ARROW_SVG,
                cls="button button--primary",
                type="button",
                data_open_brief="",
            ),
            *[A(f"{link['label']} ", Span(link["glyph"]), cls="text-link", href=link["href"]) for link in d["links"]],
            cls="hero-actions",
        ),
        cls="card card--manifesto",
        data_depth="3",
    )


def _status():
    d = CARDS["status"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Span(cls="pulse", aria_hidden="true"),
            Span(d["note"][0], B(d["note"][1])),
            cls="hero-note",
        ),
        P(d["copy"][0], Br(), Strong(d["copy"][1]), cls="status-copy"),
        cls="card card--status-card",
        data_depth="6",
    )


def _sun():
    d = CARDS["sun"]
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
        _label_pair(d["label"], inverse=True),
        cls="card card--sun card--large",
        data_depth="14",
    )


def _orchestrator():
    d = CARDS["orchestrator"]
    return Article(
        _topline(*d["topline"]),
        agent_row(*d["agent"]),
        Div(I(), I(), I(), I(), cls="signal-lines", aria_hidden="true"),
        cls="card card--glass card--orchestrator",
        data_depth="8",
    )


def _think():
    d = CARDS["think"]
    return Article(
        _topline(*d["topline"]),
        Div(H2(d["heading"][0], Br(), d["heading"][1]), P(d["text"])),
        Div(*[Span(initial) for initial in d["initials"]], cls="stacked-initials", aria_hidden="true"),
        cls="card card--lime card--think",
        data_depth="6",
    )


def _verticals():
    d = CARDS["verticals"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), I(), cls="vertical-icon", aria_hidden="true"),
        _label_pair(d["label"], inverse=True),
        cls="card card--violet card--verticals",
        data_depth="10",
    )


def _metrics():
    d = CARDS["metrics"]
    return Article(
        card_topline(d["topline"][0], Span(d["topline"][1], cls="metric-glyph")),
        Strong(d["heading"][0], Br(), d["heading"][1]),
        Div(I(), cls="metric-line", aria_hidden="true"),
        Span(d["caption"][0], Br(), d["caption"][1], cls="metric-caption"),
        cls="card card--dark card--metrics",
        data_depth="4",
    )


def _gates():
    d = CARDS["gates"]
    return Article(
        _topline(*d["topline"]),
        Div(Span(), Span(), Span(), cls="gate-grid", aria_hidden="true"),
        _label_pair(d["label"]),
        cls="card card--pearl card--gates",
        data_depth="7",
    )


def _async():
    d = CARDS["async"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="async-mark", aria_hidden="true"),
        _label_pair(d["label"]),
        cls="card card--async",
        data_depth="5",
    )


def _command():
    d = CARDS["command"]
    return Article(
        _topline(*d["topline"]),
        P(d["text"][0], Br(), Strong(d["text"][1])),
        Span(d["note"], cls="command-note"),
        cls="card card--command",
        data_depth="4",
    )


def _memory():
    d = CARDS["memory"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        _label_pair(d["label"]),
        cls="card card--memory",
        data_depth="7",
    )


def _parallel():
    d = CARDS["parallel"]
    return Article(
        _topline(*d["topline"]),
        P(Strong(d["text"][0]), Br(), d["text"][1]),
        Div(I(), I(), I(), I(), I(), cls="parallel-bars", aria_hidden="true"),
        Span(d["note"]),
        cls="card card--parallel",
        data_depth="5",
    )


def hero_section():
    return Section(
        Div(
            _manifesto(),
            _status(),
            _sun(),
            _orchestrator(),
            _think(),
            _verticals(),
            _metrics(),
            _gates(),
            _async(),
            _command(),
            _memory(),
            _parallel(),
            cls="bento bento--hero",
            data_bento="",
        ),
        cls="hero",
        id="top",
        aria_labelledby="hero-title",
    )
