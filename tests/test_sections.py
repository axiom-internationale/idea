"""Bento-grid classname snapshot — guards against silent CSS misses."""

import re
from pathlib import Path

from fasthtml.common import to_xml

from website.sections.connect import connect_section
from website.sections.dfy import (
    dfy_cta_section,
    dfy_domains_section,
    dfy_evolve_section,
    dfy_hero_section,
    dfy_mission_section,
    dfy_process_section,
    dfy_services_section,
)
from website.sections.dna import dna_section
from website.sections.founder import founder_section
from website.sections.hero import hero_section
from website.sections.machine import machine_section
from website.sections.nav import nav_section
from website.sections.pillars import pillars_section
from website.sections.portfolio import portfolio_section
from website.sections.stack import stack_section
from website.sections.think_tank import think_tank_section


def test_stack_cards():
    html = to_xml(stack_section())
    for cls in ("card--stack-main", "card--stack-models", "card--stack-mem", "card--stack-orch", "card--stack-infra"):
        assert cls in html, f"missing {cls}"
    assert "card--stack-ai" not in html
    assert "card--stack-orchestration" not in html
    assert "card--stack-infrastructure" not in html


def test_think_tank_cards():
    html = to_xml(think_tank_section())
    for cls in ("card--agent-ceo", "card--agent-cfo", "card--agent-cto", "card--agent-cmo", "card--agent-count"):
        assert cls in html, f"missing {cls}"
    # CEO/CTO are on dark backgrounds and need inverse labels
    assert html.count("card-label--inverse") >= 2


def test_portfolio_cards():
    html = to_xml(portfolio_section())
    for cls in ("card--ventures", "card--vent-1", "card--vent-2", "card--vent-3", "card--vent-stats"):
        assert cls in html, f"missing {cls}"


CSS_PATH = Path(__file__).resolve().parent.parent / "src" / "website" / "static" / "styles.css"

ALL_SECTIONS = (
    hero_section,
    machine_section,
    pillars_section,
    think_tank_section,
    portfolio_section,
    dna_section,
    stack_section,
    founder_section,
    connect_section,
    dfy_hero_section,
    dfy_mission_section,
    dfy_services_section,
    dfy_domains_section,
    dfy_process_section,
    dfy_evolve_section,
    dfy_cta_section,
)

# Glyphs known to render as tofu in common fonts (U+2381 broke toplines on Windows).
BANNED_GLYPHS = ("⎁",)


def test_no_tofu_glyphs():
    for section in ALL_SECTIONS:
        html = to_xml(section())
        for glyph in BANNED_GLYPHS:
            assert glyph not in html, f"{glyph!r} tofu glyph rendered by {section.__name__}"


def test_hero_manifesto():
    html = to_xml(hero_section())
    assert "card--manifesto" in html
    assert 'id="hero-title"' in html
    assert 'href="/dfy"' in html
    assert "DFY" in html


def test_card_classes_have_css():
    css = CSS_PATH.read_text(encoding="utf-8")
    for section in ALL_SECTIONS:
        html = to_xml(section())
        for cls in set(re.findall(r"card--[\w-]+", html)):
            assert f".{cls}" in css, f".{cls} used by {section.__name__} has no CSS rule"


def test_no_dead_placeholder_links():
    for section in ALL_SECTIONS:
        html = to_xml(section())
        assert 'href="#"' not in html, f'dead href="#" link in {section.__name__}'


def test_nav_menu_marks_active_page():
    home = to_xml(nav_section(active="home"))
    dfy = to_xml(nav_section(active="dfy"))
    for html in (home, dfy):
        assert "menu-toggle" in html and "menu-drawer" in html
        assert 'href="/"' in html and 'href="/dfy"' in html
        assert html.count('aria-current="page"') == 1
    assert home.index('aria-current="page"') < home.index('href="/dfy"')
    assert dfy.index('aria-current="page"') > dfy.index('href="/"')
    default = to_xml(nav_section())
    assert default.count('aria-current="page"') == 1
    assert "data-theme-auto" in home
