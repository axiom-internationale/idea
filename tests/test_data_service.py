"""data_service — homepage content index stays valid and complete."""

from data_service import DFY_PATH, INDEX_PATH, get_section, load_index

EXPECTED_SECTIONS = (
    "nav",
    "hero",
    "machine",
    "pillars",
    "think_tank",
    "portfolio",
    "dna",
    "stack",
    "founder",
    "connect",
    "footer",
    "brief_dialog",
)


def test_index_loads_with_all_homepage_sections():
    index = load_index()
    assert index["_meta"]["page"] == "/"
    for name in EXPECTED_SECTIONS:
        assert isinstance(index[name], dict), f"missing section {name}"


def test_hero_manifesto_copy():
    hero = get_section("hero")
    assert hero["id"] == "top"
    assert hero["manifesto"]["title"] == ["Many businesses.", "One intelligence."]
    assert len(hero["cards"]) == 11
    hrefs = [link["href"] for link in hero["manifesto"]["links"]]
    assert hrefs == ["#machine", "/dfy"]


def test_key_copy_spot_checks():
    assert get_section("contact")["email"] == "axiom.intelligence.inc@gmail.com"
    assert get_section("machine")["pipeline"]["flow"] == ["Idea", "Research", "Build", "Launch", "Revenue"]
    assert len(get_section("think_tank")["agents"]) == 4
    assert len(get_section("stack")["layers"]) == 4
    assert get_section("footer")["tagline"] == "Built to build what's next."
    assert get_section("connect")["cta"]["button"]["href"].startswith("mailto:")
    assert "Understood" in get_section("brief_dialog")["confirm_button"]


def test_no_banned_glyphs_in_index():
    raw = INDEX_PATH.read_text(encoding="utf-8")
    assert "⎁" not in raw  # U+2381 renders as tofu on Windows


def test_unknown_section_raises_helpful_error():
    try:
        get_section("dfy")
    except KeyError as exc:
        assert "dfy" in str(exc)
    else:
        raise AssertionError("expected KeyError for unknown section")


def test_dfy_page_loads_with_all_sections():
    dfy = load_index("dfy")
    assert dfy["_meta"]["page"] == "/dfy"
    for name in ("nav", "hero", "mission", "services", "domains", "process", "evolve", "cta", "footer"):
        assert isinstance(dfy[name], dict), f"missing dfy section {name}"


def test_dfy_copy_spot_checks():
    hero = get_section("hero", page="dfy")
    assert hero["manifesto"]["title"] == ["Your business.", "Done for you."]
    assert len(hero["cards"]) == 8
    assert len(get_section("services", page="dfy")["cards"]) == 4
    assert len(get_section("domains", page="dfy")["cards"]) == 4
    assert len(get_section("process", page="dfy")["steps"]) == 5
    cta = get_section("cta", page="dfy")
    assert cta["main"]["button"]["href"].startswith("mailto:")
    assert "DFY" in cta["cards"][1]["label"][1]


def test_no_banned_glyphs_in_dfy():
    raw = DFY_PATH.read_text(encoding="utf-8")
    assert "⎁" not in raw  # U+2381 renders as tofu on Windows


def test_unknown_page_raises_helpful_error():
    try:
        load_index("pricing")
    except KeyError as exc:
        assert "pricing" in str(exc)
    else:
        raise AssertionError("expected KeyError for unknown page")


def test_nav_menu_in_both_pages():
    for page in ("index", "dfy"):
        menu = get_section("nav", page=page)["menu"]
        assert [item["href"] for item in menu] == ["/", "/dfy"]
        assert [item["label"] for item in menu] == ["Home", "DFY"]
