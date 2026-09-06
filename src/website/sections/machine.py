"""How-it-works section with pipeline bento grid."""

from fasthtml.common import H2, Article, Br, Div, Em, I, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.stat_grid import stat_grid
from website.components.topline import card_topline

MACHINE = get_section("machine")
MACHINE_CARDS = {card["key"]: card for card in MACHINE["cards"]}


def _topline(left, right):
    return card_topline(left, Span("Live", cls="status") if right == "Live" else right)


def _label_pair(label, inverse=False):
    cls = "card-label card-label--inverse" if inverse else "card-label"
    return Div(Strong(label[0]), Span(label[1]), cls=cls)


def _titled(lines, cls):
    parts = []
    for i, line in enumerate(lines):
        if i:
            parts.append(Br())
        parts.append(line)
    return Strong(*parts, cls=cls)


def _pipeline():
    d = MACHINE["pipeline"]
    flow = []
    for i, label in enumerate(d["flow"]):
        dot = "pip-dot pip-dot--active" if i < 3 else "pip-dot"
        flow.append(Span(cls=dot))
        flow.append(Span(label, cls="pip-label"))
        if i < len(d["flow"]) - 1:
            flow.append(Span(cls="pip-line"))
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="machine-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        Div(
            *flow,
            cls="pipeline-flow",
            aria_hidden="true",
        ),
        cls="card card--glass card--pipeline",
        data_depth="3",
        data_reveal="",
    )


def _research():
    d = MACHINE_CARDS["research"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), I(), I(), cls="step-dots", aria_hidden="true"),
        _label_pair(d["label"]),
        cls="card card--teal card--research",
        data_depth="5",
        data_reveal="",
    )


def _build():
    d = MACHINE_CARDS["build"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="step-blocks", aria_hidden="true"),
        _label_pair(d["label"]),
        cls="card card--rose card--build",
        data_depth="5",
        data_reveal="",
    )


def _launch():
    d = MACHINE_CARDS["launch"]
    return Article(
        _topline(*d["topline"]),
        Div(d["glyph"], cls="launch-arrow", aria_hidden="true"),
        _label_pair(d["label"], inverse=True),
        cls="card card--indigo card--launch",
        data_depth="5",
        data_reveal="",
    )


def _optimize():
    d = MACHINE_CARDS["optimize"]
    return Article(
        _topline(*d["topline"]),
        _titled(d["heading"], "opt-title"),
        Div(I(), cls="metric-line", aria_hidden="true"),
        Span(d["note"], cls="command-note"),
        cls="card card--dark card--opt",
        data_depth="4",
        data_reveal="",
    )


def _always_on():
    d = MACHINE_CARDS["always"]
    return Article(
        _topline(*d["topline"]),
        Div(Span(cls="pulse", aria_hidden="true"), Strong(d["headline"]), cls="always-pulse"),
        _label_pair(d["label"]),
        cls="card card--pearl card--always",
        data_depth="4",
        data_reveal="",
    )


def _stats():
    d = MACHINE_CARDS["stats"]
    return Article(
        _topline(*d["topline"]),
        stat_grid([tuple(stat) for stat in d["stats"]]),
        cls="card card--glass card--stats",
        data_depth="3",
        data_reveal="",
    )


def _loop():
    d = MACHINE_CARDS["loop"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="loop-ring", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--amber card--loop",
        data_depth="4",
        data_reveal="",
    )


def _speed():
    d = MACHINE_CARDS["speed"]
    return Article(
        _topline(*d["topline"]),
        _titled(d["heading"], "speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--mint card--speed",
        data_depth="4",
        data_reveal="",
    )


def machine_section():
    return Section(
        section_divider(MACHINE["divider"]),
        Div(
            _pipeline(),
            _research(),
            _build(),
            _launch(),
            _optimize(),
            _always_on(),
            _stats(),
            _loop(),
            _speed(),
            cls="bento bento--machine",
            data_bento="",
        ),
        cls="section",
        id="machine",
        aria_labelledby="machine-title",
    )
