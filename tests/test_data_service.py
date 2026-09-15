"""data_service — homepage content index stays valid and complete."""

import json

from data_service import DFY_PATH, INDEX_PATH, LAW_PATH, get_section, load_index

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
    expected_hrefs = ["/", "/dfy", "/dfy/law"]
    expected_labels = ["Home", "DFY", "Law"]
    for page in ("index", "dfy", "dfy_law"):
        menu = get_section("nav", page=page)["menu"]
        assert [item["href"] for item in menu] == expected_hrefs
        assert [item["label"] for item in menu] == expected_labels
        home = next(item for item in menu if item["href"] == "/")
        assert home["sub"] == "The company"
        assert "agent" not in home["sub"].lower()
        assert "factory" not in home["sub"].lower()


def test_dfy_law_page_loads_with_all_sections():
    law = load_index("dfy_law")
    assert law["_meta"]["page"] == "/dfy/law"
    for name in ("nav", "hero", "wedge", "packages", "trust", "cta", "footer"):
        assert isinstance(law[name], dict), f"missing law section {name}"


def test_dfy_law_copy_spot_checks():
    hero = get_section("hero", page="dfy_law")
    assert hero["manifesto"]["title"] == ["Your firm.", "Done for you."]
    assert hero["manifesto"]["primary_button"]["href"] == "#dfy-law-connect"
    pkgs = {card["key"]: card for card in get_section("packages", page="dfy_law")["cards"]}
    assert pkgs["presence"]["setup"][0] == "$4,000"
    assert pkgs["presence"]["monthly"][0] == "$2,500"
    assert pkgs["intake"]["setup"][0] == "$7,500"
    assert pkgs["intake"]["monthly"][0] == "$4,500"
    assert pkgs["growth"]["setup"][0] == "$7,500"
    assert "flat" in pkgs["growth"]["term"].lower()
    legal = get_section("domains", page="dfy")["cards"][0]
    assert legal["href"] == "/dfy/law"
    cta = get_section("cta", page="dfy_law")
    assert cta["form"]["action_email"] == "axiom.intelligence.inc@gmail.com"
    assert "firm" in cta["form"]["fields"]
    assert cta["form"]["fields"]["city"]["label"] == "City / ZIP"
    assert [opt["value"] for opt in cta["form"]["fields"]["meeting"]["options"]] == ["In person", "Call or video"]
    hero_cards = {card["key"]: card for card in get_section("hero", page="dfy_law")["cards"]}
    practices = {card["key"]: card for card in get_section("wedge", page="dfy_law")["cards"]}
    assert "Every practice" in hero_cards["practices"]["label"][0]
    assert "employment" in practices["practices"]["label"][0].lower()
    assert "corporate" in practices["practices"]["label"][0].lower()
    assert "family" in practices["practices"]["label"][0].lower()
    assert "criminal" in practices["practices"]["label"][0].lower()
    assert "later" not in practices["later"]["label"][0].lower()
    wedge_body = " ".join(get_section("wedge", page="dfy_law")["main"]["body"]).lower()
    assert "come later" not in wedge_body
    assert "family" in wedge_body and "criminal" in wedge_body
    assert "employment" in wedge_body and "corporate" in wedge_body
    assert "example" in wedge_body
    assert "nyc" not in wedge_body
    assert "metro" not in wedge_body
    assert get_section("cta", page="dfy_law")["form"]["fields"]["practice"]["options"] == [
        "Personal injury",
        "Immigration",
        "Family",
        "Criminal",
        "Employment",
        "Corporate",
        "Other",
    ]


def test_dfy_law_copy_is_founder_led_and_geo_agnostic():
    raw = LAW_PATH.read_text(encoding="utf-8")
    for phrase in (
        "agentic",
        "factory",
        "Think Tank",
        "General Secretary",
        "AI workforce",
        "multi-agent",
        "zero employees",
        "autonomous organization",
        "agentic McKinsey",
        "Family and criminal come later",
        "PI + immigration",
    ):
        assert phrase not in raw, f"banned voice/positioning still in dfy_law.json: {phrase}"
    hero = get_section("hero", page="dfy_law")
    assert "Priyanshu · Axiom Intelligence" in hero["manifesto"]["intro"]
    assert hero["cards"][0]["key"] == "partner"
    assert "Priyanshu" in hero["cards"][0]["label"][0]
    assert "nyc" not in {card["key"] for card in hero["cards"]}
    assert hero["cards"][4]["heading"] == ["Any size.", "Every practice."]
    assert hero["cards"][1]["stats"] == [["Any", "Size"], ["Every", "Practice"]]
    assert "any size" in hero["manifesto"]["intro"].lower()
    page = {k: v for k, v in load_index("dfy_law").items() if k not in ("nav", "footer", "contact", "_meta")}
    blob = json.dumps(page)
    for phrase in (
        "NYC",
        "New York",
        "borough",
        "11372",
        "Queens",
        "Brooklyn",
        "Manhattan",
        "metro",
        "1–10",
        "1-10",
        "5–50",
        "5-50",
        "small and mid",
        "solo",
    ):
        assert phrase not in blob, f"locked ICP/geo phrase still in dfy_law page copy: {phrase}"
    assert get_section("cta", page="dfy_law")["form"]["fields"]["city"]["placeholder"] == "City or ZIP"


def test_no_banned_glyphs_in_dfy_law():
    raw = LAW_PATH.read_text(encoding="utf-8")
    assert "⎁" not in raw  # U+2381 renders as tofu on Windows
