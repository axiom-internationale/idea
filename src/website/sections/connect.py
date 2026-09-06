"""Connect / contact section."""

from fasthtml.common import H2, A, Article, B, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.icons import ARROW_SVG
from website.components.section_divider import section_divider
from website.components.topline import card_topline

CONNECT = get_section("connect")
CONNECT_CARDS = {card["key"]: card for card in CONNECT["cards"]}


def _cta():
    d = CONNECT["cta"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="connect-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        A(f"{d['button']['label']} ", ARROW_SVG, cls="button button--primary", href=d["button"]["href"]),
        cls="card card--dark card--cta",
        data_depth="3",
        data_reveal="",
    )


def _website():
    d = CONNECT_CARDS["web"]
    return Article(
        card_topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="web-link"),
        A(
            cls="card-overlay-link",
            href=d["href"],
            target="_blank",
            rel="noreferrer",
            aria_label=f"Visit {d['label'][0]}",
        ),
        cls="card card--glass card--web",
        data_depth="4",
        data_reveal="",
    )


def _email():
    d = CONNECT_CARDS["contact"]
    return Article(
        card_topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        A(
            cls="card-overlay-link",
            href=d["href"],
            aria_label=f"Email {d['label'][1]}",
        ),
        cls="card card--sun card--contact",
        data_depth="5",
        data_reveal="",
    )


def _social():
    d = CONNECT_CARDS["social"]
    return Article(
        card_topline(*d["topline"]),
        Div(
            # TODO: wire real profile URLs — placeholders are non-interactive
            # spans until then so keyboard users don't hit dead links.
            *[
                Span(pill + " ", Span("↗"), cls="social-pill", aria_disabled="true", title=d["note"])
                for pill in d["pills"]
            ],
            cls="social-links",
        ),
        cls="card card--violet card--social",
        data_depth="4",
        data_reveal="",
    )


def _office(office):
    text = f" {office['city']} " if "tag" in office else f" {office['city']}"
    children = [B(office["code"]), text]
    if "tag" in office:
        children.append(Em(office["tag"]))
    return Span(*children, cls="loc-office")


def _location():
    d = CONNECT_CARDS["location"]
    return Article(
        card_topline(*d["topline"]),
        Strong(d["headline"], cls="loc-headline"),
        Div(
            *[_office(office) for office in d["offices"]],
            cls="loc-offices",
        ),
        cls="card card--teal card--loc",
        data_depth="5",
        data_reveal="",
    )


def connect_section():
    return Section(
        section_divider(CONNECT["divider"]),
        Div(
            _cta(),
            _website(),
            _email(),
            _social(),
            _location(),
            cls="bento bento--connect",
            data_bento="",
        ),
        cls="section",
        id="connect",
        aria_labelledby="connect-title",
    )
