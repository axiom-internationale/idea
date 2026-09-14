"""DFY Law Firms landing page — NYC-first commercial wedge."""

from fasthtml.common import (
    H1,
    H2,
    A,
    Article,
    Br,
    Button,
    Div,
    Em,
    Form,
    I,
    Input,
    Label,
    Li,
    Option,
    P,
    Section,
    Select,
    Span,
    Strong,
    Ul,
)

from data_service import get_section
from website.components.eyebrow import eyebrow
from website.components.icons import ARROW_SVG
from website.components.section_divider import section_divider
from website.components.stat_grid import stat_grid
from website.components.topline import card_topline

LAW_HERO = get_section("hero", page="dfy_law")
LAW_HERO_CARDS = {card["key"]: card for card in LAW_HERO["cards"]}
LAW_WEDGE = get_section("wedge", page="dfy_law")
LAW_WEDGE_CARDS = {card["key"]: card for card in LAW_WEDGE["cards"]}
LAW_PACKAGES = get_section("packages", page="dfy_law")
LAW_PKG = {card["key"]: card for card in LAW_PACKAGES["cards"]}
LAW_TRUST = get_section("trust", page="dfy_law")
LAW_TRUST_CARDS = {card["key"]: card for card in LAW_TRUST["cards"]}
LAW_CTA = get_section("cta", page="dfy_law")
LAW_CTA_CARDS = {card["key"]: card for card in LAW_CTA["cards"]}


def _topline(left, right):
    return card_topline(left, Span("Live", cls="status") if right == "Live" else right)


# ── Hero ──────────────────────────────────────────────────────────


def _manifesto():
    d = LAW_HERO["manifesto"]
    link = d["links"][0]
    return Article(
        eyebrow(d["eyebrow"]),
        H1(d["title"][0], Br(), Em(d["title"][1]), id="dfy-law-hero-title"),
        P(d["intro"], cls="intro"),
        Div(
            A(
                f"{d['primary_button']['label']} ",
                ARROW_SVG,
                cls="button button--primary",
                href=d["primary_button"]["href"],
            ),
            A(f"{link['label']} ", Span(link["glyph"]), cls="text-link", href=link["href"]),
            cls="hero-actions",
        ),
        cls="card card--dfy-law-manifesto",
        data_depth="3",
    )


def _nyc_badge():
    d = LAW_HERO_CARDS["nyc"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Span(cls="orbit orbit--one"),
            Span(cls="orbit orbit--two"),
            Span(cls="orbit orbit--three"),
            Span(I(), cls="solar-core"),
            Span(cls="satellite satellite--one"),
            Span(cls="satellite satellite--two"),
            cls="solar-system",
            aria_hidden="true",
        ),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--sun card--dfy-law-nyc",
        data_depth="14",
    )


def _size_stats():
    return Article(
        _topline(*LAW_HERO_CARDS["size"]["topline"]),
        stat_grid([tuple(stat) for stat in LAW_HERO_CARDS["size"]["stats"]]),
        cls="card card--glass card--dfy-law-size",
        data_depth="4",
    )


def _practices_badge():
    d = LAW_HERO_CARDS["practices"]
    return Article(
        _topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--violet card--dfy-law-practices",
        data_depth="5",
    )


def _audit_pulse():
    d = LAW_HERO_CARDS["audit"]
    return Article(
        _topline(*d["topline"]),
        Div(Span(cls="pulse", aria_hidden="true"), Strong(d["headline"]), cls="always-pulse"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--pearl card--dfy-law-audit",
        data_depth="4",
    )


def _metro_speed():
    d = LAW_HERO_CARDS["metro"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--mint card--dfy-law-metro",
        data_depth="4",
    )


_PKG_PREVIEW_MARK = {
    "web": ("step-blocks", 3),
    "intake": ("async-mark", 3),
    "ads": ("memory-mark", 4),
}


def _pkg_preview(key, color, slug):
    d = LAW_HERO_CARDS[key]
    mark_cls, mark_n = _PKG_PREVIEW_MARK[key]
    return Article(
        _topline(*d["topline"]),
        Div(*[I() for _ in range(mark_n)], cls=mark_cls, aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls=f"card card--{color} card--dfy-law-{slug}",
        data_depth="5" if key != "ads" else "4",
    )


def dfy_law_hero_section():
    return Section(
        Div(
            _manifesto(),
            _nyc_badge(),
            _size_stats(),
            _practices_badge(),
            _audit_pulse(),
            _metro_speed(),
            _pkg_preview("web", "teal", "web"),
            _pkg_preview("intake", "amber", "lead"),
            _pkg_preview("ads", "rose", "ads"),
            cls="bento bento--dfy-law-hero",
            data_bento="",
        ),
        cls="hero",
        id="top",
        aria_labelledby="dfy-law-hero-title",
    )


# ── Wedge ─────────────────────────────────────────────────────────


def _wedge_main():
    d = LAW_WEDGE["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-law-wedge-title"),
        P(d["body"][0], cls="intro-sm"),
        P(d["body"][1], cls="intro-sm"),
        cls="card card--pearl card--dfy-law-wedge-main",
        data_depth="3",
        data_reveal="",
    )


def _wedge_ground():
    d = LAW_WEDGE_CARDS["ground"]
    return Article(
        _topline(*d["topline"]),
        Div(
            Span(cls="orbit orbit--one"),
            Span(cls="orbit orbit--two"),
            Span(I(), cls="solar-core"),
            cls="solar-system solar-system--sm",
            aria_hidden="true",
        ),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--dark card--dfy-law-wedge-ground",
        data_depth="5",
        data_reveal="",
    )


def _wedge_practices():
    d = LAW_WEDGE_CARDS["practices"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"], cls="pillar-title"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--sun card--dfy-law-wedge-practices",
        data_depth="4",
        data_reveal="",
    )


def _wedge_later():
    d = LAW_WEDGE_CARDS["later"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), I(), cls="memory-mark", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--indigo card--dfy-law-wedge-later",
        data_depth="5",
        data_reveal="",
    )


def _wedge_addon():
    d = LAW_WEDGE_CARDS["addon"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--mint card--dfy-law-wedge-addon",
        data_depth="4",
        data_reveal="",
    )


def dfy_law_wedge_section():
    return Section(
        section_divider(LAW_WEDGE["divider"]),
        Div(
            _wedge_main(),
            _wedge_ground(),
            _wedge_practices(),
            _wedge_later(),
            _wedge_addon(),
            cls="bento bento--dfy-law-wedge",
            data_bento="",
        ),
        cls="section",
        id="dfy-law-wedge",
        aria_labelledby="dfy-law-wedge-title",
    )


# ── Packages ──────────────────────────────────────────────────────


def _pkg_main():
    d = LAW_PACKAGES["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-law-packages-title"),
        P(d["body"], cls="intro-sm"),
        cls="card card--dark card--dfy-law-pkg-main",
        data_depth="3",
        data_reveal="",
    )


def _pkg_card(card, color, depth, slug):
    return Article(
        card_topline(f"Package 0{card['num']}", card["glyph"]),
        Strong(card["title"], cls="pillar-title"),
        stat_grid([tuple(card["setup"]), tuple(card["monthly"])]),
        Span(card["term"], cls="pkg-term"),
        Ul(*[Li(item) for item in card["includes"]], cls="pkg-list"),
        cls=f"card card--{color} card--dfy-law-pkg-{slug}",
        data_depth=str(depth),
        data_reveal="",
    )


def _pkg_addon(card):
    return Article(
        card_topline(f"Package 0{card['num']}", card["glyph"]),
        Div(Strong(card["title"]), Span(card["desc"]), cls="card-label"),
        cls="card card--rose card--dfy-law-pkg-addon",
        data_depth="4",
        data_reveal="",
    )


def dfy_law_packages_section():
    return Section(
        section_divider(LAW_PACKAGES["divider"]),
        Div(
            _pkg_main(),
            _pkg_card(LAW_PKG["presence"], "teal", 5, "presence"),
            _pkg_card(LAW_PKG["intake"], "violet", 4, "intake"),
            _pkg_card(LAW_PKG["growth"], "mint", 5, "growth"),
            _pkg_addon(LAW_PKG["addon"]),
            cls="bento bento--dfy-law-packages",
            data_bento="",
        ),
        cls="section",
        id="dfy-law-packages",
        aria_labelledby="dfy-law-packages-title",
    )


# ── Trust ─────────────────────────────────────────────────────────


def _trust_main():
    d = LAW_TRUST["main"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-law-trust-title"),
        P(d["body"][0], cls="intro-sm"),
        P(d["body"][1], cls="intro-sm"),
        cls="card card--pearl card--dfy-law-trust-main",
        data_depth="3",
        data_reveal="",
    )


def _trust_own():
    d = LAW_TRUST_CARDS["own"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="step-dots", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--teal card--dfy-law-trust-own",
        data_depth="5",
        data_reveal="",
    )


def _trust_guarantees():
    d = LAW_TRUST_CARDS["guarantees"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"], cls="pillar-title"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        cls="card card--amber card--dfy-law-trust-guarantees",
        data_depth="4",
        data_reveal="",
    )


def _trust_human():
    d = LAW_TRUST_CARDS["human"]
    return Article(
        _topline(*d["topline"]),
        Div(I(), I(), I(), cls="async-mark", aria_hidden="true"),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--indigo card--dfy-law-trust-human",
        data_depth="5",
        data_reveal="",
    )


def _trust_flat():
    d = LAW_TRUST_CARDS["flat"]
    return Article(
        _topline(*d["topline"]),
        Strong(d["heading"][0], Br(), d["heading"][1], cls="speed-title"),
        Span(d["note"], cls="speed-note"),
        cls="card card--lime card--dfy-law-trust-flat",
        data_depth="4",
        data_reveal="",
    )


def dfy_law_trust_section():
    return Section(
        section_divider(LAW_TRUST["divider"]),
        Div(
            _trust_main(),
            _trust_own(),
            _trust_guarantees(),
            _trust_human(),
            _trust_flat(),
            cls="bento bento--dfy-law-trust",
            data_bento="",
        ),
        cls="section",
        id="dfy-law-trust",
        aria_labelledby="dfy-law-trust-title",
    )


# ── CTA / intake ──────────────────────────────────────────────────


def _field(name, label, wide=False, **input_kwargs):
    field_id = f"law-{name}"
    return Label(
        Span(label),
        Input(id=field_id, name=name, **input_kwargs),
        cls="law-field law-field--wide" if wide else "law-field",
        fr=field_id,
    )


def _intake_form():
    d = LAW_CTA["main"]
    form = LAW_CTA["form"]
    fields = form["fields"]
    email = form["action_email"]
    practice = fields["practice"]
    meeting = fields["meeting"]
    return Article(
        eyebrow(d["eyebrow"]),
        H2(d["title"][0], Br(), Em(d["title"][1]), cls="section-h2", id="dfy-law-connect-title"),
        P(d["body"], cls="intro-sm"),
        Form(
            _field(
                "firm",
                fields["firm"]["label"],
                type="text",
                required=True,
                autocomplete="organization",
                placeholder=fields["firm"]["placeholder"],
            ),
            Label(
                Span(practice["label"]),
                Select(
                    Option(practice["placeholder"], value="", disabled=True, selected=True),
                    *[Option(opt, value=opt) for opt in practice["options"]],
                    id="law-practice",
                    name="practice",
                    required=True,
                ),
                cls="law-field",
                fr="law-practice",
            ),
            _field(
                "city",
                fields["city"]["label"],
                type="text",
                required=True,
                autocomplete="address-level2",
                placeholder=fields["city"]["placeholder"],
            ),
            _field(
                "website",
                fields["website"]["label"],
                type="text",
                inputmode="url",
                autocomplete="url",
                placeholder=fields["website"]["placeholder"],
            ),
            _field(
                "contact",
                fields["contact"]["label"],
                type="text",
                required=True,
                autocomplete="email",
                placeholder=fields["contact"]["placeholder"],
                wide=True,
            ),
            Div(
                Span(meeting["label"], cls="law-field-label"),
                Div(
                    *[
                        Label(
                            Input(
                                type="radio",
                                name="meeting",
                                value=opt["value"],
                                checked=i == 0,
                                required=True,
                            ),
                            Span(opt["label"]),
                            cls="law-choice",
                        )
                        for i, opt in enumerate(meeting["options"])
                    ],
                    cls="law-choices",
                ),
                cls="law-field law-field--wide",
            ),
            Button(f"{d['button']['label']} ", ARROW_SVG, cls="button button--primary", type="submit"),
            P(d["note"], cls="law-form-note"),
            cls="law-form",
            data_law_intake="",
            action=f"mailto:{email}",
            method="post",
            enctype="text/plain",
        ),
        cls="card card--dark card--dfy-law-form",
        data_depth="3",
        data_reveal="",
    )


def _meet_card():
    d = LAW_CTA_CARDS["meet"]
    return Article(
        _topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        cls="card card--sun card--dfy-law-meet",
        data_depth="5",
        data_reveal="",
    )


def _email_card():
    d = LAW_CTA_CARDS["email"]
    return Article(
        _topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label"),
        A(cls="card-overlay-link", href=d["href"], aria_label=f"Email {d['label'][1]}"),
        cls="card card--glass card--dfy-law-mail",
        data_depth="4",
        data_reveal="",
    )


def _factory_card():
    d = LAW_CTA_CARDS["factory"]
    return Article(
        _topline(*d["topline"]),
        Div(Strong(d["label"][0]), Span(d["label"][1]), cls="card-label card-label--inverse"),
        A(cls="card-overlay-link", href=d["href"], aria_label="Visit the DFY page"),
        cls="card card--violet card--dfy-law-factory",
        data_depth="4",
        data_reveal="",
    )


def dfy_law_cta_section():
    return Section(
        section_divider(LAW_CTA["divider"]),
        Div(
            _intake_form(),
            _meet_card(),
            _email_card(),
            _factory_card(),
            cls="bento bento--dfy-law-cta",
            data_bento="",
        ),
        cls="section",
        id="dfy-law-connect",
        aria_labelledby="dfy-law-connect-title",
    )
