"""Card topline row component."""

from fasthtml.common import Div, Span


def card_topline(left, right):
    """Standard topline row for bento cards: left label, right glyph."""
    return Div(Span(left), Span(right) if isinstance(right, str) else right, cls="card-topline")
