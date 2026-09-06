"""SVG icon constants used across the site."""

from fasthtml.common import NotStr

ARROW_SVG = NotStr(
    '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true">'
    '<path d="M3.8 10h12.4M11 5.2l4.8 4.8-4.8 4.8" '
    'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
    "</svg>"
)

SUN_SVG = NotStr(
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true">'
    '<circle cx="12" cy="12" r="3.7"/>'
    '<path d="M12 2.2v2.1M12 19.7v2.1M2.2 12h2.1M19.7 12h2.1'
    'M5.1 5.1l1.5 1.5M17.4 17.4l1.5 1.5M18.9 5.1l-1.5 1.5M6.6 17.4l-1.5 1.5"/>'
    "</svg>"
)

MOON_SVG = NotStr(
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true">'
    '<path d="M20.5 15.3A8.5 8.5 0 0 1 8.7 3.5 8.5 8.5 0 1 0 20.5 15.3Z"/>'
    "</svg>"
)

CLOSE_SVG = NotStr(
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.8" aria-hidden="true">'
    '<path d="M18 6 6 18M6 6l12 12" stroke-linecap="round"/>'
    "</svg>"
)

MENU_SVG = NotStr(
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.8" aria-hidden="true">'
    '<path d="M4 7.5h16M4 12h16M4 16.5h16" stroke-linecap="round"/>'
    "</svg>"
)
