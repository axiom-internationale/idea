"""Top navigation bar."""

from fasthtml.common import A, Button, Div, Img, Nav, Span

from data_service import get_section
from website.components.icons import CLOSE_SVG, MENU_SVG, MOON_SVG, SUN_SVG

NAV = get_section("nav")
CONTACT_EMAIL = get_section("contact")["email"]


def _menu_link(label, sub, href, is_active):
    attrs = {"cls": "menu-link", "href": href}
    if is_active:
        attrs["aria_current"] = "page"
    return A(
        Span(label, cls="menu-link-title"),
        Span(sub, cls="menu-link-sub"),
        **attrs,
    )


def _menu_link_for(item, active):
    key = "home" if item["href"] == "/" else "dfy"
    return _menu_link(item["label"], item["sub"], item["href"], active == key)


def nav_section(active="home"):
    active = active if active in ("home", "dfy") else None
    return Nav(
        A(
            Img(
                cls="brand-logo",
                src="/media/mini_sun.png",
                alt=NAV["logo_alt"],
                width="32",
                height="32",
                loading="eager",
                fetchpriority="high",
            ),
            cls="brand-symbol",
            href="#top",
            aria_label="Back to top",
        ),
        A(
            Span(NAV["wordmark"][0], Span("/", cls="wordmark-muted"), NAV["wordmark"][1]),
            Span(
                Span(NAV["locations_full"], cls="nav-locations--full"),
                Span(NAV["locations_short"], cls="nav-locations--short"),
                cls="nav-locations",
            ),
            cls="wordmark",
            href="#top",
            aria_label=f"{NAV['brand']} home",
        ),
        Div(
            Span(
                Span(cls="pulse"),
                Span(NAV["status"]),
                cls="nav-status",
                aria_hidden="true",
            ),
            Button(
                Span(SUN_SVG, cls="theme-icon theme-icon--sun", aria_hidden="true"),
                Span(MOON_SVG, cls="theme-icon theme-icon--moon", aria_hidden="true"),
                cls="theme-toggle",
                type="button",
                aria_label=NAV["theme_toggle_labels"]["to_dark"],
                aria_pressed="false",
            ),
            Button(
                Span(MENU_SVG, cls="menu-icon", aria_hidden="true"),
                cls="menu-toggle",
                type="button",
                aria_label="Open menu",
                aria_expanded="false",
                aria_controls="site-menu",
            ),
            cls="nav-right",
        ),
        Div(cls="menu-backdrop", aria_hidden="true"),
        Div(
            Div(
                Span("Menu", cls="menu-kicker"),
                Button(
                    CLOSE_SVG,
                    cls="menu-close",
                    type="button",
                    aria_label="Close menu",
                ),
                cls="menu-head",
            ),
            Nav(
                *[_menu_link_for(item, active) for item in NAV["menu"]],
                Button(
                    Span("Follow day & night", cls="menu-link-title"),
                    Span("On — following day & night", cls="menu-link-sub", data_theme_auto_state=""),
                    cls="menu-link menu-link--sm",
                    type="button",
                    data_theme_auto="",
                    aria_pressed="true",
                ),
                cls="menu-links",
                aria_label="Site menu",
            ),
            A(
                CONTACT_EMAIL,
                cls="menu-foot",
                href=f"mailto:{CONTACT_EMAIL}",
            ),
            cls="menu-drawer",
            id="site-menu",
            role="dialog",
            aria_modal="true",
            aria_label="Site menu",
        ),
        cls="nav",
        aria_label="Main navigation",
    )
