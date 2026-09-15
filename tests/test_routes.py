"""HTTP smoke tests for marketing routes."""

from starlette.testclient import TestClient

from website.app import create_app
from website.seo import SITE_URL


def _client() -> TestClient:
    return TestClient(create_app())


def test_home_dfy_and_law_routes_ok():
    client = _client()
    home = client.get("/")
    dfy = client.get("/dfy")
    law = client.get("/dfy/law")
    assert home.status_code == 200
    assert dfy.status_code == 200
    assert law.status_code == 200
    for response in (home, dfy, law):
        assert 'href="/dfy/law"' in response.text
        assert "Law" in response.text
        assert 'name="theme-color"' in response.text


def test_law_page_seo_and_jsonld():
    response = _client().get("/dfy/law")
    html = response.text
    assert "Done For You Law Firms" in html
    assert f'href="{SITE_URL}/dfy/law"' in html
    assert '"@type": "Service"' in html
    assert '"name": "US"' in html
    assert "NYC" not in html
    assert "11372" not in html
    assert "Queens" not in html
    assert "metropolitan" not in html
    assert "One founding partner" in html
    assert "Founder-led delivery" in html
    assert "Priyanshu ·" not in html
    assert "mailto:priyanshu.sharma@axiomintelligence.xyz" in html
    assert "axiom.intelligence.inc@gmail.com" not in html
    assert "data-law-intake" in html
    assert "Your firm" in html
    assert "The company" in html
    assert "The agentic factory" not in html
    assert "Intelligence" in html
    assert "firm knowledge" in html.lower()
    assert "any size" in html.lower()
    assert "5–50" not in html
    assert "1–10" not in html
    assert "small and mid" not in html.lower()
    assert "Family and criminal come later" not in html
    assert "Employment" in html
    assert "Corporate" in html
    for phrase in (
        "agentic",
        "factory",
        "Think Tank",
        "General Secretary",
        "AI workforce",
        "multi-agent",
        "zero employees",
        "autonomous organization",
    ):
        assert phrase.lower() not in html.lower()


def test_public_pages_use_current_contact_email():
    client = _client()
    for path in ("/", "/dfy", "/dfy/law"):
        html = client.get(path).text
        assert "mailto:priyanshu.sharma@axiomintelligence.xyz" in html
        assert "axiom.intelligence.inc@gmail.com" not in html
        assert "hello@axiomintelligence.xyz" not in html


def test_sitemap_includes_law():
    response = _client().get("/sitemap.xml")
    assert response.status_code == 200
    assert f"{SITE_URL}/dfy/law" in response.text
