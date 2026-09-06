"""Route handlers for the Axiom Intelligence website."""

from fasthtml.common import A, Div, Main, Script
from starlette.responses import PlainTextResponse, Response

from website.sections.brief_dialog import brief_dialog
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
from website.sections.footer import footer_section
from website.sections.founder import founder_section
from website.sections.hero import hero_section
from website.sections.machine import machine_section
from website.sections.nav import nav_section
from website.sections.pillars import pillars_section
from website.sections.portfolio import portfolio_section
from website.sections.stack import stack_section
from website.sections.think_tank import think_tank_section
from website.seo import SITE_URL, jsonld_organization, jsonld_service, page_meta

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
  <url>
    <loc>{SITE_URL}/dfy</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>
"""


def setup_home_routes(app):
    @app.get("/")
    def homepage():
        return (
            *page_meta(
                title="Axiom Intelligence — Autonomous Agentic Factory",
                description=(
                    "Axiom Intelligence is an autonomous agentic factory that turns ideas "
                    "into enduring, profitable companies — with one human at the helm."
                ),
            ),
            jsonld_organization(),
            Div(cls="ambient ambient--one", aria_hidden="true"),
            Div(cls="ambient ambient--two", aria_hidden="true"),
            Main(
                nav_section(active="home"),
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
            Script(src="/static/script.js", defer=True),
        )

    @app.route("/robots.txt")
    async def robots_txt(request):
        return PlainTextResponse(ROBOTS_TXT)

    @app.route("/sitemap.xml")
    async def sitemap_xml(request):
        return Response(SITEMAP_XML.strip(), media_type="application/xml")

    @app.get("/dfy")
    def dfy_page():
        return (
            *page_meta(
                title="Done For You — Full-Stack AI Services for Local Business",
                description=(
                    "Website, SEO, ads, automations, dashboards, and AI agents — "
                    "everything your main street business needs, delivered and managed "
                    "by Axiom Intelligence's agentic workforce."
                ),
                path="/dfy",
            ),
            jsonld_service(),
            Div(cls="ambient ambient--one", aria_hidden="true"),
            Div(cls="ambient ambient--two", aria_hidden="true"),
            Main(
                nav_section(active="dfy"),
                dfy_hero_section(),
                dfy_mission_section(),
                dfy_services_section(),
                dfy_domains_section(),
                dfy_process_section(),
                dfy_evolve_section(),
                dfy_cta_section(),
                footer_section(),
                cls="shell",
            ),
            Script(src="/static/script.js", defer=True),
        )

    @app.get("/{path:path}")
    def not_found(path: str):
        return (
            Main(
                nav_section(active="none"),
                Div("404 — nothing here.", cls="intro"),
                A("Back home", href="/", cls="text-link"),
                cls="shell",
            ),
            Script(src="/static/script.js", defer=True),
        ), 404
