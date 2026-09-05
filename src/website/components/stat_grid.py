"""Stat grid component."""

from fasthtml.common import Div, Span


def stat_grid(stats):
    """Grid of stat value/label pairs.

    *stats* is a list of ``(value, label)`` tuples.
    """
    return Div(
        *[Div(Span(value, cls="stat-val"), Span(label, cls="stat-label"), cls="stat") for value, label in stats],
        cls="stat-grid",
    )
