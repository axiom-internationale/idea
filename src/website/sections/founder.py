"""Founder section."""

from fasthtml.common import H2, Article, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.topline import card_topline

FOUNDER = get_section("founder")
FOUNDER_CARDS = {card["key"]: card for card in FOUNDER["cards"]}


def _bio():
    d = FOUNDER["bio"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="founder-title"),
        *[P(paragraph, cls="intro-sm") for paragraph in d["body"]],
        cls="card card--pearl card--founder-bio",
        data_depth="3",
        data_reveal="",
    )


def _role():
    d = FOUNDER_CARDS["role"]
    return Article(
        card_topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="opt-title"),
        Span(d["note"], cls="command-note"),
        cls="card card--dark card--founder-role",
        data_depth="4",
        data_reveal="",
    )


def _philosophy():
    d = FOUNDER_CARDS["philosophy"]
    return Article(
        card_topline(*d["topline"]),
        Div(
            Strong(d["label"][0]),
            Span(d["label"][1]),
            cls="card-label card-label--inverse",
        ),
        cls="card card--sun card--founder-phil",
        data_depth="5",
        data_reveal="",
    )


def founder_section():
    return Section(
        section_divider(FOUNDER["divider"]),
        Div(_bio(), _role(), _philosophy(), cls="bento bento--founder", data_bento=""),
        cls="section",
        id="founder",
        aria_labelledby="founder-title",
    )
