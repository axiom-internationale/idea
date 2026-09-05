"""Tech stack section."""

from fasthtml.common import Article, Br, Div, Em, H2, I, P, Section, Span, Strong

from website.components.topline import card_topline
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider


def _main():
    return Article(
        eyebrow("Infrastructure"),
        H2("Built on", Br(), Em("modern AI."), cls="section-h2", id="stack-title"),
        P(
            "The factory runs on frontier language models, custom orchestration, "
            "and persistent memory—designed for autonomous operation at scale.",
            cls="intro-sm",
        ),
        cls="card card--dark card--stack-main", data_depth="3", data_reveal="",
    )


def _layer(num, glyph, title, desc, color, depth, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    content = [card_topline(f"Layer 0{num}", glyph)]
    if title == "Persistent Memory":
        content.append(Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"))
    content.append(Div(Strong(title), Span(desc), cls=label_cls))
    return Article(*content, cls=f"card card--{color} card--stack-{title.split()[0].lower()}", data_depth=str(depth), data_reveal="")


def stack_section():
    return Section(
        section_divider("The stack"),
        Div(
            _main(),
            _layer(1, "⎁", "AI Models", "Frontier LLMs for reasoning, coding & analysis.", "violet", 5, inverse=True),
            Article(
                card_topline("Layer 02", "⎁"),
                Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
                Div(Strong("Persistent Memory"), Span("Local-first, durable knowledge across sessions."), cls="card-label"),
                cls="card card--memory card--stack-mem", data_depth="4", data_reveal="",
            ),
            _layer(3, "↻", "Orchestration", "Multi-agent coordination and task delegation.", "amber", 5),
            _layer(4, "∞", "Infrastructure", "Cloud-native, auto-scaling, always available.", "mint", 4),
            cls="bento bento--stack", data_bento="",
        ),
        cls="section", id="stack", aria_labelledby="stack-title",
    )
