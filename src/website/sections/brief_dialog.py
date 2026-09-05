"""Factory brief modal dialog."""

from fasthtml.common import Button, Dialog, Div, H2, I, P, Span

from website.components.icons import CLOSE_SVG
from website.components.eyebrow import eyebrow


def brief_dialog():
    return Dialog(
        Button(CLOSE_SVG, cls="dialog-close", type="button", aria_label="Close factory brief"),
        Div(I(), cls="dialog-mark", aria_hidden="true"),
        eyebrow("The factory, in one line"),
        H2(
            "One human founder + one autonomous organization + many parallel businesses.",
            id="brief-title",
        ),
        P(
            "The General Secretary directs a shared Think Tank, which in turn powers "
            "independent Company Verticals. The result: deliberate autonomy, real-world "
            "focus, and a system designed to compound."
        ),
        Button("Understood ", Span("→"), cls="button button--primary dialog-button", type="button"),
        cls="brief-dialog",
        aria_labelledby="brief-title",
    )
