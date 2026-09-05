"""Think Tank section with C-suite agent cards."""

from fasthtml.common import Article, Br, Div, Em, H2, P, Section, Small, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.agent_row import agent_row
from website.components.stat_grid import stat_grid


def _gs():
    return Article(
        eyebrow("Central command"),
        H2("One brain.", Br(), Em("Many arms."), cls="section-h2", id="think-tank-title"),
        P(
            "The General Secretary orchestrates every agent, every company, every decision. "
            "It delegates, monitors, and ensures the factory stays aligned.",
            cls="intro-sm",
        ),
        agent_row("GS", "General Secretary", "Chief orchestrator"),
        cls="card card--glass card--gs", data_depth="3", data_reveal="",
    )


def _agent_card(label, initials, title, desc, color_cls, depth):
    inverse = "card-label card-label--inverse" if color_cls in ("card--sun", "card--indigo") else "card-label"
    return Article(
        card_topline("Agent", label),
        Div(initials, cls="agent-orb agent-orb--sm", aria_hidden="true"),
        Div(Strong(title), Span(desc), cls=inverse),
        cls=f"card card--{color_cls} card--agent-{label.lower()}", data_depth=str(depth), data_reveal="",
    )


def _agent_count():
    return Article(
        card_topline("Think tank", Span("Live", cls="status")),
        stat_grid([("1", "GS"), ("4+", "Agents"), ("∞", "Scale")]),
        cls="card card--dark card--agent-count", data_depth="3", data_reveal="",
    )


def think_tank_section():
    return Section(
        section_divider("The think tank"),
        Div(
            _gs(),
            _agent_card("CEO", "CE", "Chief Executive", "Strategy, positioning & growth direction.", "sun", 5),
            _agent_card("CFO", "CF", "Chief Financial", "Revenue tracking, budgets & financial modeling.", "amber", 4),
            _agent_card("CTO", "CT", "Chief Technology", "Architecture, development & infrastructure.", "indigo", 5),
            _agent_card("CMO", "CM", "Chief Marketing", "Brand, growth & customer acquisition.", "lime", 4),
            _agent_count(),
            cls="bento bento--tank", data_bento="",
        ),
        cls="section", id="think-tank", aria_labelledby="think-tank-title",
    )
