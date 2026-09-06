"""SEO utilities — per-page meta tags and JSON-LD structured data."""

import json

from fasthtml.common import Link, Meta, NotStr, Script, Title

SITE_URL = "https://www.axiomintelligence.xyz"
SITE_NAME = "Axiom Intelligence"


def page_meta(
    *,
    title: str,
    description: str,
    path: str = "/",
    og_type: str = "website",
) -> tuple:
    canonical = f"{SITE_URL}{path}" if path != "/" else SITE_URL
    full_title = f"{title} | {SITE_NAME}" if path != "/" else title
    image = f"{SITE_URL}/media/sun.png"

    return (
        Title(full_title),
        Meta(name="description", content=description),
        Meta(name="robots", content="index, follow"),
        Link(rel="canonical", href=canonical),
        Meta(property="og:title", content=full_title),
        Meta(property="og:description", content=description),
        Meta(property="og:type", content=og_type),
        Meta(property="og:url", content=canonical),
        Meta(property="og:site_name", content=SITE_NAME),
        Meta(property="og:locale", content="en_US"),
        Meta(property="og:image", content=image),
        Meta(property="og:image:width", content="1200"),
        Meta(property="og:image:height", content="1200"),
        Meta(property="og:image:alt", content="Axiom Intelligence logo"),
        # Square logo suits the compact card, not the large-image variant.
        Meta(name="twitter:card", content="summary"),
        Meta(name="twitter:title", content=full_title),
        Meta(name="twitter:description", content=description),
        Meta(name="twitter:image", content=image),
    )


def jsonld_organization() -> Script:
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Axiom Intelligence",
        "legalName": "Axiom Intelligence Inc.",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/media/sun.png",
        "description": (
            "An autonomous agentic factory that turns ideas into enduring, "
            "profitable companies — with one human at the helm."
        ),
        "foundingDate": "2026",
        "founder": {"@type": "Person", "name": "Priyanshu Sharma"},
        "address": [
            {"@type": "PostalAddress", "addressLocality": "Bhiwadi", "addressCountry": "IN"},
            {
                "@type": "PostalAddress",
                "addressLocality": "Los Angeles",
                "addressRegion": "CA",
                "addressCountry": "US",
            },
            {
                "@type": "PostalAddress",
                "addressLocality": "New York",
                "addressRegion": "NY",
                "addressCountry": "US",
            },
            {
                "@type": "PostalAddress",
                "addressLocality": "San Diego",
                "addressRegion": "CA",
                "addressCountry": "US",
            },
        ],
        "contactPoint": {
            "@type": "ContactPoint",
            "email": "hello@axiomintelligence.xyz",
            "contactType": "customer service",
        },
        "sameAs": [],
    }
    return Script(NotStr(json.dumps(data, indent=2)), type="application/ld+json")


def jsonld_service() -> Script:
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Done For You (DFY) — AI Services for Local Business",
        "provider": {
            "@type": "Organization",
            "name": "Axiom Intelligence",
            "url": SITE_URL,
        },
        "description": (
            "Full-stack AI-powered services for main street businesses — websites, "
            "SEO, ads, automations, dashboards, and AI agents, delivered and managed "
            "by an intelligent agentic workforce."
        ),
        "serviceType": "AI-Powered Business Services",
        "areaServed": {"@type": "Country", "name": "US"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "DFY Service Categories",
            "itemListElement": [
                {
                    "@type": "OfferCatalog",
                    "name": "Web & Marketing",
                    "description": "Website, hosting, SEO, paid ads, social media, reputation.",
                },
                {
                    "@type": "OfferCatalog",
                    "name": "AI Agents",
                    "description": "Receptionist, chatbot, scheduler, follow-up & screening.",
                },
                {
                    "@type": "OfferCatalog",
                    "name": "Automation & Ops",
                    "description": "CRM, invoicing, onboarding workflows, staff scheduling.",
                },
                {
                    "@type": "OfferCatalog",
                    "name": "Intelligence & Growth",
                    "description": "Dashboards, analytics, competitor intel, loyalty, strategy.",
                },
            ],
        },
    }
    return Script(NotStr(json.dumps(data, indent=2)), type="application/ld+json")
