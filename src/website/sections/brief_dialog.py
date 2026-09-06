"""Factory brief modal dialog."""

from fasthtml.common import H2, Button, Dialog, Div, I, P, Span

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.icons import CLOSE_SVG

BRIEF = get_section("brief_dialog")


def brief_dialog():
    return Dialog(
        Button(CLOSE_SVG, cls="dialog-close", type="button", aria_label=BRIEF["close_label"]),
        Div(I(), cls="dialog-mark", aria_hidden="true"),
        eyebrow(BRIEF["eyebrow"]),
        H2(
            BRIEF["title"],
            id="brief-title",
        ),
        P(BRIEF["body"]),
        Button(f"{BRIEF['confirm_button']} ", Span("→"), cls="button button--primary dialog-button", type="button"),
        cls="brief-dialog",
        aria_labelledby="brief-title",
    )
