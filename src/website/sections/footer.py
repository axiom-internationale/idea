"""Site footer."""

from fasthtml.common import A, Div, Footer, Img, Span

from data_service import get_section

FOOTER = get_section("footer")


def footer_section():
    return Footer(
        Div(
            Img(
                cls="footer-logo",
                src="/media/mini_sun.png",
                alt=FOOTER["logo_alt"],
                width="32",
                height="32",
                loading="lazy",
            ),
            Span(FOOTER["brand"], cls="footer-name"),
            cls="footer-brand",
        ),
        Span(
            Span(FOOTER["locations_full"], cls="footer-locations--full"),
            Span(FOOTER["locations_short"], cls="footer-locations--short"),
            cls="footer-locations",
        ),
        Span(FOOTER["tagline"], cls="footer-tagline"),
        Div(
            Span(FOOTER["copyright"]),
            A(
                f"{FOOTER['site_link']['label']} ",
                Span(FOOTER["site_link"]["glyph"]),
                href=FOOTER["site_link"]["href"],
                target="_blank",
                rel="noreferrer",
            ),
            cls="footer-meta",
        ),
        cls="footer",
    )
