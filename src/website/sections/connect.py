"""Connect / contact section."""

from fasthtml.common import A, Article, B, Br, Div, Em, H2, P, Section, Span, Strong

from website.components.icons import ARROW_SVG
from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _cta():
    return Article(
        eyebrow("Get in touch"),
        H2("Let's", Br(), Em("build."), cls="section-h2", id="connect-title"),
        P(
            "Interested in what Axiom Intelligence is building? Have an idea worth exploring? "
            "We're always looking for the next opportunity.",
            cls="intro-sm",
        ),
        A("Start a conversation ", ARROW_SVG, cls="button button--primary", href="mailto:hello@axiomintelligence.xyz"),
        cls="card card--dark card--cta", data_depth="3", data_reveal="",
    )


def _website():
    return Article(
        card_topline("Website", "↗"),
        Div(Strong("axiomintelligence.xyz"), Span("Visit our main site"), cls="web-link"),
        A(
            cls="card-overlay-link", href="https://www.axiomintelligence.xyz",
            target="_blank", rel="noreferrer", aria_label="Visit axiomintelligence.xyz",
        ),
        cls="card card--glass card--web", data_depth="4", data_reveal="",
    )


def _email():
    return Article(
        card_topline("Email", "✉"),
        Div(Strong("Say hello"), Span("hello@axiomintelligence.xyz"), cls="card-label card-label--inverse"),
        cls="card card--sun card--contact", data_depth="5", data_reveal="",
    )


def _social():
    return Article(
        card_topline("Social", "@"),
        Div(
            A("Twitter / X ", Span("↗"), href="#", cls="social-pill"),
            A("LinkedIn ", Span("↗"), href="#", cls="social-pill"),
            A("GitHub ", Span("↗"), href="#", cls="social-pill"),
            cls="social-links",
        ),
        cls="card card--violet card--social", data_depth="4", data_reveal="",
    )


def _location():
    return Article(
        card_topline("Location", "◉"),
        Strong("Remote-first.", cls="loc-headline"),
        Div(
            Span(B("BH"), " Bhiwadi ", Em("HQ"), cls="loc-office"),
            Span(B("LA"), " Los Angeles", cls="loc-office"),
            Span(B("NY"), " New York", cls="loc-office"),
            Span(B("SD"), " San Diego", cls="loc-office"),
            cls="loc-offices",
        ),
        cls="card card--teal card--loc", data_depth="5", data_reveal="",
    )


def connect_section():
    return Section(
        section_divider("Connect"),
        Div(
            _cta(), _website(), _email(), _social(), _location(),
            cls="bento bento--connect", data_bento="",
        ),
        cls="section", id="connect", aria_labelledby="connect-title",
    )
