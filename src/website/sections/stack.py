"""Tech stack section."""

from fasthtml.common import H2, Article, Br, Div, Em, I, P, Section, Span, Strong

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.section_divider import section_divider
from website.components.topline import card_topline

STACK = get_section("stack")

# (num, color, depth, slug, inverse) — copy comes from the JSON layers.
LAYER_SPECS = [
    (1, "violet", 5, "models", True),
    (2, "memory", 4, "mem", False),
    (3, "amber", 5, "orch", False),
    (4, "mint", 4, "infra", False),
]


def _main():
    d = STACK["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="stack-title"),
        P(
            d["body"],
            cls="intro-sm",
        ),
        cls="card card--dark card--stack-main",
        data_depth="3",
        data_reveal="",
    )


def _layer(layer, num, color, depth, slug, inverse=False):
    label_cls = "card-label card-label--inverse" if inverse else "card-label"
    content = [card_topline(f"Layer 0{num}", layer["glyph"])]
    if layer["title"] == "Persistent Memory":
        content.append(Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"))
    content.append(Div(Strong(layer["title"]), Span(layer["desc"]), cls=label_cls))
    return Article(*content, cls=f"card card--{color} card--stack-{slug}", data_depth=str(depth), data_reveal="")


def stack_section():
    layers = {layer["num"]: layer for layer in STACK["layers"]}
    return Section(
        section_divider(STACK["divider"]),
        Div(
            _main(),
            *[
                _layer(layers[num], num, color, depth, slug, inverse)
                for num, color, depth, slug, inverse in LAYER_SPECS
            ],
            cls="bento bento--stack",
            data_bento="",
        ),
        cls="section",
        id="stack",
        aria_labelledby="stack-title",
    )
