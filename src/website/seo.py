"""SEO utilities — JSON-LD structured data."""

from fasthtml.common import NotStr, Script


def jsonld_organization() -> Script:
    return Script(NotStr("""{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Axiom Intelligence",
  "legalName": "Axiom Intelligence Inc.",
  "url": "https://www.axiomintelligence.xyz",
  "logo": "https://www.axiomintelligence.xyz/media/sun.png",
  "description": "An autonomous agentic factory that turns ideas into enduring, profitable companies — with one human at the helm.",
  "foundingDate": "2026",
  "founder": {
    "@type": "Person",
    "name": "Priyanshu Sharma"
  },
  "address": [
    {
      "@type": "PostalAddress",
      "addressLocality": "Bhiwadi",
      "addressCountry": "IN"
    },
    {
      "@type": "PostalAddress",
      "addressLocality": "Los Angeles",
      "addressRegion": "CA",
      "addressCountry": "US"
    },
    {
      "@type": "PostalAddress",
      "addressLocality": "New York",
      "addressRegion": "NY",
      "addressCountry": "US"
    },
    {
      "@type": "PostalAddress",
      "addressLocality": "San Diego",
      "addressRegion": "CA",
      "addressCountry": "US"
    }
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hello@axiomintelligence.xyz",
    "contactType": "customer service"
  },
  "sameAs": []
}"""), type="application/ld+json")
