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
    assert '"name": "New York"' in html
    assert "data-law-intake" in html
    assert "Your firm" in html
    assert "The company" in html
    assert "The agentic factory" not in html
    assert "All practice areas" in html
    assert "Family and criminal come later" not in html


def test_sitemap_includes_law():
    response = _client().get("/sitemap.xml")
    assert response.status_code == 200
    assert f"{SITE_URL}/dfy/law" in response.text
