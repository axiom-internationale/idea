"""FastHTML application factory for the Axiom Intelligence website."""

import logging

from fasthtml.common import FastHTML, Link, Meta, Script

from website.routes import setup_routes

log = logging.getLogger("axiom.website")

SITE_URL = "https://www.axiomintelligence.xyz"
SITE_TITLE = "Axiom Intelligence — Autonomous Agentic Factory"
SITE_DESCRIPTION = (
    "Axiom Intelligence is an autonomous agentic factory that turns ideas into "
    "enduring, profitable companies — with one human at the helm."
)


def create_app() -> FastHTML:
    theme_init_script = Script(
        "(()=>{"
        "const s=localStorage.getItem('axiom-theme');"
        "const d=window.matchMedia('(prefers-color-scheme:dark)').matches;"
        "document.documentElement.dataset.theme=s||(d?'dark':'light');"
        "})()"
    )

    app = FastHTML(
        title="Axiom Intelligence",
        htmlkw={"lang": "en"},
        pico=False,
        surreal=False,
        htmx=False,
        hdrs=[
            Meta(name="description", content=SITE_DESCRIPTION),
            Meta(name="author", content="Axiom Intelligence Inc."),
            Meta(name="robots", content="index, follow"),
            Meta(name="theme-color", content="#0a0a0a"),
            Link(rel="canonical", href=SITE_URL),
            Meta(property="og:title", content=SITE_TITLE),
            Meta(property="og:description", content=SITE_DESCRIPTION),
            Meta(property="og:type", content="website"),
            Meta(property="og:url", content=SITE_URL),
            Meta(property="og:site_name", content="Axiom Intelligence"),
            Meta(property="og:locale", content="en_US"),
            Meta(property="og:image", content=f"{SITE_URL}/media/sun.png"),
            Meta(property="og:image:alt", content="Axiom Intelligence logo"),
            Meta(name="twitter:card", content="summary_large_image"),
            Meta(name="twitter:title", content=SITE_TITLE),
            Meta(name="twitter:description", content="Many businesses. One intelligence."),
            Meta(name="twitter:image", content=f"{SITE_URL}/media/sun.png"),
            Link(rel="icon", type="image/png", href="/media/mini_sun.png"),
            Link(rel="apple-touch-icon", href="/media/sun.png"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            Link(
                href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap",
                rel="stylesheet",
            ),
            Link(rel="stylesheet", href="/static/styles.css"),
            theme_init_script,
        ],
    )

    app.state.name = "axiom-website"
    app.state.version = "0.1.0"

    setup_routes(app)
    return app
