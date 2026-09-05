"""Route handlers for the Axiom Intelligence website."""

from starlette.responses import PlainTextResponse, Response

from fasthtml.common import Div, Main, Script

from website.seo import jsonld_organization
from website.sections.brief_dialog import brief_dialog
from website.sections.connect import connect_section
from website.sections.dna import dna_section
from website.sections.footer import footer_section
from website.sections.founder import founder_section
from website.sections.hero import hero_section
from website.sections.machine import machine_section
from website.sections.nav import nav_section
from website.sections.pillars import pillars_section
from website.sections.portfolio import portfolio_section
from website.sections.stack import stack_section
from website.sections.think_tank import think_tank_section

SITE_URL = "https://www.axiomintelligence.xyz"

ROBOTS_TXT = f"""User-agent: *
Allow: /
Disallow: /api/

Sitemap: {SITE_URL}/sitemap.xml
"""

SITEMAP_XML = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""


def setup_routes(app):
    @app.get("/")
    def homepage():
        return (
            jsonld_organization(),
            Div(cls="ambient ambient--one", aria_hidden="true"),
            Div(cls="ambient ambient--two", aria_hidden="true"),
            Main(
                nav_section(),
                hero_section(),
                machine_section(),
                pillars_section(),
                think_tank_section(),
                portfolio_section(),
                dna_section(),
                stack_section(),
                founder_section(),
                connect_section(),
                footer_section(),
                cls="shell",
            ),
            brief_dialog(),
            Script(src="/static/script.js"),
        )

    @app.route("/robots.txt")
    async def robots_txt(request):
        return PlainTextResponse(ROBOTS_TXT)

    @app.route("/sitemap.xml")
    async def sitemap_xml(request):
        return Response(SITEMAP_XML.strip(), media_type="application/xml")
