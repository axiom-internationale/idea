"""Eyebrow label component."""

from fasthtml.common import P, Span


def eyebrow(text):
    """Small uppercase label with a decorative dot prefix."""
    return P(Span(), f" {text}", cls="eyebrow")
