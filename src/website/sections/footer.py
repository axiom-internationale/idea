"""Site footer."""

from fasthtml.common import A, Div, Footer, Img, Span


def footer_section():
    return Footer(
        Div(
            Img(cls="footer-logo", src="/media/mini_sun.png", alt="Axiom Intelligence logo", width="32", height="32"),
            Span("Axiom Intelligence", cls="footer-name"),
            cls="footer-brand",
        ),
        Span(
            Span("Bhiwadi — Los Angeles — New York — San Diego", cls="footer-locations--full"),
            Span("BH — LA — NY — SD", cls="footer-locations--short"),
            cls="footer-locations",
        ),
        Span("Built to build what's next.", cls="footer-tagline"),
        Div(
            Span("© 2026 Axiom Intelligence Inc."),
            A("axiomintelligence.xyz ", Span("↗"), href="https://www.axiomintelligence.xyz", target="_blank", rel="noreferrer"),
            cls="footer-meta",
        ),
        cls="footer",
    )
