"""Section divider component."""

from fasthtml.common import Div

from website.components.eyebrow import eyebrow


def section_divider(text):
    """Horizontal divider with an eyebrow label."""
    return Div(eyebrow(text), cls="section-divider")
