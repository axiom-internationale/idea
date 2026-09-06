"""Agent row component."""

from fasthtml.common import Div, Small, Span, Strong


def agent_row(initials, title, subtitle, orb_cls="agent-orb--orange"):
    """Row displaying an agent orb with title and subtitle."""
    return Div(
        Span(initials, cls=f"agent-orb {orb_cls}"),
        Span(Strong(title), Small(subtitle)),
        cls="agent-row",
    )
