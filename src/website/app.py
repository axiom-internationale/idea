"""FastHTML application factory for the Axiom Intelligence website."""

import logging

from fasthtml.common import FastHTML, Link, Meta, Script

from axiom import __version__
from website.routes import setup_home_routes

log = logging.getLogger("axiom.website")


def _theme_init_script() -> Script:
    return Script(
        "(()=>{"
        "document.documentElement.classList.add('js');"
        # Day/night default from the visitor's local clock — fixed window,
        # no location needed: light 06:00-18:00, dark otherwise.
        "window.__axiomAutoTheme=function(d){"
        "d=d||new Date();"
        "const h=d.getHours()+d.getMinutes()/60;"
        "return (h>=6&&h<18)?'light':'dark';"
        "};"
        "let s=null;"
        "try{s=localStorage.getItem('axiom-theme-v2');}catch(e){}"
        # Drop values pinned by the old always-persist behavior — they were
        # rarely explicit choices and would override the day/night default.
        "try{localStorage.removeItem('axiom-theme');}catch(e){}"
        "const d=window.matchMedia('(prefers-color-scheme:dark)').matches;"
        "const theme=s||window.__axiomAutoTheme()||(d?'dark':'light');"
        "document.documentElement.dataset.theme=theme;"
        "const m=document.querySelector('meta[name=\"theme-color\"]');"
        "if(m)m.setAttribute('content',theme==='dark'?'#101111':'#f4f4f1');"
        "})()"
    )


def create_app() -> FastHTML:
    app = FastHTML(
        htmlkw={"lang": "en"},
        pico=False,
        surreal=False,
        htmx=False,
        # Per-page tags (title, description, canonical, OG/Twitter, JSON-LD)
        # come from seo.page_meta() in each route — never duplicate them here.
        hdrs=[
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Meta(name="theme-color", content="#f4f4f1"),
            Link(rel="icon", type="image/png", href="/media/mini_sun.png"),
            Link(rel="apple-touch-icon", href="/media/sun.png"),
            Link(rel="preload", href="/media/mini_sun.png", as_="image"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            Link(
                href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap",
                rel="stylesheet",
            ),
            Link(rel="stylesheet", href="/static/styles.css"),
            _theme_init_script(),
        ],
    )

    app.state.name = "axiom-website"
    app.state.version = __version__

    setup_home_routes(app)
    return app
