"""Top navigation bar."""

from fasthtml.common import A, Button, Div, Img, Nav, Span

from website.components.icons import MOON_SVG, SUN_SVG


def nav_section():
    return Nav(
        A(
            Img(cls="brand-logo", src="/media/mini_sun.png", alt="Axiom Intelligence logo", width="32", height="32"),
            cls="brand-symbol",
            href="#top",
            aria_label="Back to top",
        ),
        A(
            Span("Axiom", Span("/", cls="wordmark-muted"), "Intelligence"),
            Span(
                Span("Bhiwadi — Los Angeles — New York — San Diego", cls="nav-locations--full"),
                Span("BH — LA — NY — SD", cls="nav-locations--short"),
                cls="nav-locations",
            ),
            cls="wordmark",
            href="#top",
            aria_label="Axiom Intelligence home",
        ),
        Div(
            Span(Span(cls="pulse"), Span("Live"), cls="nav-status", aria_hidden="true"),
            Button(
                Span(SUN_SVG, cls="theme-icon theme-icon--sun", aria_hidden="true"),
                Span(MOON_SVG, cls="theme-icon theme-icon--moon", aria_hidden="true"),
                cls="theme-toggle",
                type="button",
                aria_label="Switch to dark mode",
                aria_pressed="false",
            ),
            cls="nav-right",
        ),
        cls="nav",
        aria_label="Main navigation",
    )
