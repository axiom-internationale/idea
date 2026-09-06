"""Think Tank section with C-suite agent cards."""

from fasthtml.common import H2, Article, Br, Div, Em, P, Section, Span, Strong

from data_service import get_section
from website.components.agent_row import agent_row
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.stat_grid import stat_grid
from website.components.topline import card_topline

TANK = get_section("think_tank")


def _gs():
    d = TANK["gs"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="think-tank-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        agent_row(*d["agent"]),
        cls="card card--glass card--gs",
        data_depth="3",
        data_reveal="",
    )


def _agent_card(agent, depth):
    color_cls = agent["color"]
    inverse = "card-label card-label--inverse" if color_cls in ("sun", "indigo") else "card-label"
    return Article(
        card_topline("Agent", agent["label"]),
        Div(agent["initials"], cls="agent-orb agent-orb--sm", aria_hidden="true"),
        Div(Strong(agent["title"]), Span(agent["desc"]), cls=inverse),
        cls=f"card card--{color_cls} card--agent-{agent['label'].lower()}",
        data_depth=str(depth),
        data_reveal="",
    )


def _agent_count():
    d = TANK["count"]
    return Article(
        card_topline(d["topline"][0], Span(d["topline"][1], cls="status")),
        stat_grid([tuple(stat) for stat in d["stats"]]),
        cls="card card--dark card--agent-count",
        data_depth="3",
        data_reveal="",
    )


def think_tank_section():
    return Section(
        section_divider(TANK["divider"]),
        Div(
            _gs(),
            *[_agent_card(agent, depth) for agent, depth in zip(TANK["agents"], (5, 4, 5, 4), strict=True)],
            _agent_count(),
            cls="bento bento--tank",
            data_bento="",
        ),
        cls="section",
        id="think-tank",
        aria_labelledby="think-tank-title",
    )
