"""Four pillars section."""

from fasthtml.common import H2, Article, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.topline import card_topline

PILLARS = get_section("pillars")
PILLAR_CARDS = {card["key"]: card for card in PILLARS["cards"]}


def _titled(lines, cls):
    parts = []
    for i, line in enumerate(lines):
        if i:
            parts.append(Br())
        parts.append(line)
    return Strong(*parts, cls=cls)


def _main():
    d = PILLARS["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="pillars-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--dark card--pillar-main",
        data_depth="3",
        data_reveal="",
    )


def _pillar(key, color, depth, inverse=False):
    d = PILLAR_CARDS[key]
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    slug = {"self": "self", "profit": "profit", "stable": "stable", "autonomous": "auton"}[key]
    return Article(
        card_topline(*d["topline"]),
        _titled(d["title"], "pillar-title"),
        Div(Span(d["text"]), cls=label_cls),
        cls=f"card card--{color} card--pillar-{slug}",
        data_depth=str(depth),
        data_reveal="",
    )


def pillars_section():
    return Section(
        section_divider(PILLARS["divider"]),
        Div(
            _main(),
            _pillar("self", "mint", 5),
            _pillar("profit", "amber", 4),
            _pillar("stable", "indigo", 5, inverse=True),
            _pillar("autonomous", "glass", 4),
            cls="bento bento--pillars",
            data_bento="",
        ),
        cls="section",
        id="pillars",
        aria_labelledby="pillars-title",
    )
