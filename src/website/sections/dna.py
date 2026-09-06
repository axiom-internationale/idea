"""DNA / origin section."""

from fasthtml.common import H2, Article, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.topline import card_topline

DNA = get_section("dna")
DNA_CARDS = {card["key"]: card for card in DNA["cards"]}


def _story():
    d = DNA["story"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dna-title"),
        *[P(paragraph, cls="intro-sm") for paragraph in d["body"]],
        cls="card card--pearl card--story",
        data_depth="3",
        data_reveal="",
    )


def _year():
    d = DNA_CARDS["year"]
    return Article(
        card_topline(*d["topline"]),
        Strong(d["value"], cls="year-num"),
        Span(d["note"], cls="command-note"),
        cls="card card--dark card--year",
        data_depth="4",
        data_reveal="",
    )


def _different():
    d = DNA_CARDS["different"]
    return Article(
        card_topline(*d["topline"]),
        Div(Strong(d["label"][0], Br(), d["label"][1]), cls="card-label"),
        cls="card card--rose card--different",
        data_depth="5",
        data_reveal="",
    )


def _values():
    d = DNA_CARDS["values"]
    return Article(
        card_topline(*d["topline"]),
        Div(*[Span(chip) for chip in d["chips"]], cls="vals-list", aria_hidden="true"),
        Div(Strong(d["label"][0]), cls="card-label"),
        cls="card card--lime card--vals",
        data_depth="4",
        data_reveal="",
    )


def _principle():
    d = DNA_CARDS["principle"]
    return Article(
        card_topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="principle-text"),
        Div(Span(d["note"]), cls="card-label"),
        cls="card card--amber card--principle",
        data_depth="5",
        data_reveal="",
    )


def dna_section():
    return Section(
        section_divider(DNA["divider"]),
        Div(
            _story(),
            _year(),
            _different(),
            _values(),
            _principle(),
            cls="bento bento--dna",
            data_bento="",
        ),
        cls="section",
        id="dna",
        aria_labelledby="dna-title",
    )
