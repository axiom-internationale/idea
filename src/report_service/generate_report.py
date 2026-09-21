"""
Generate personalized Law Firm AI Health Reports as PDFs.

Reads structured company data (9 fields each), writes a per-company
JSON sidecar, and invokes Typst to compile each report in parallel.

Usage:
    python generate_report.py                 # 4 built-in sample companies
    python generate_report.py companies.json  # from an external JSON array
"""

from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

SERVICE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SERVICE_DIR.parent.parent
TEMPLATE_PATH = SERVICE_DIR / "report_template.typ"
ICLOUD_LAW_DIR = Path.home() / "iCloudDrive" / "Axiom" / "Law"
OUTPUT_DIR = SERVICE_DIR / "output"


def current_report_date() -> str:
    """SEPTEMBER 2026 — derived from runtime, not per-company input."""
    return datetime.now().strftime("%B %Y").upper()


def batch_output_dir() -> Path:
    """iCloudDrive/Axiom/Law/YYYY-MM-DD/HH/ — one folder per bulk run."""
    now = datetime.now()
    return ICLOUD_LAW_DIR / now.strftime("%Y-%m-%d") / now.strftime("%H")


def sanitize_filename(name: str) -> str:
    clean = name.replace("&", "and").replace(" ", "_")
    return "".join(c for c in clean if c.isalnum() or c in ("_", "-"))


def validate_company(company: dict) -> None:
    required = ["firm_name", "practice_area", "city_state", "zip_code", "problems"]
    missing = [k for k in required if k not in company]
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    if len(company["problems"]) != 3:
        raise ValueError(
            f"Expected exactly 3 problems, got {len(company['problems'])} "
            f"for {company['firm_name']}"
        )
    for i, p in enumerate(company["problems"]):
        if "headline" not in p or "evidence" not in p:
            raise ValueError(f"Problem {i+1} missing headline or evidence")


def generate_report(
    company: dict,
    output_dir: Path = OUTPUT_DIR,
    template_path: Path = TEMPLATE_PATH,
) -> Path:
    """Generate a single PDF report for one company."""
    validate_company(company)
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_name = sanitize_filename(company["firm_name"])
    pdf_path = output_dir / f"{safe_name}.pdf"

    # Write JSON sidecar next to the template (not in the output dir)
    # because Typst resolves json() paths relative to the template file.
    data_path = template_path.parent / f"_tmp_{safe_name}.json"

    payload = {**company, "report_date": current_report_date()}
    data_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    try:
        data_rel = data_path.name
        result = subprocess.run(
            [
                "typst",
                "compile",
                "--root", str(PROJECT_ROOT),
                str(template_path),
                str(pdf_path),
                "--input",
                f"data={data_rel}",
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Typst failed for {company['firm_name']}:\n{result.stderr}"
            )
    finally:
        data_path.unlink(missing_ok=True)

    return pdf_path


def generate_all(
    companies: list[dict],
    output_dir: Path = OUTPUT_DIR,
    template_path: Path = TEMPLATE_PATH,
    max_workers: int = 4,
) -> list[Path]:
    """Generate reports for a batch of companies in parallel."""
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[Path] = []
    errors: list[str] = []

    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(generate_report, co, output_dir, template_path): co
            for co in companies
        }
        for future in as_completed(futures):
            co = futures[future]
            try:
                pdf = future.result()
                print(f"  [OK] {pdf.name}")
                results.append(pdf)
            except Exception as exc:
                msg = f"  [FAIL] {co['firm_name']}: {exc}"
                print(msg, file=sys.stderr)
                errors.append(msg)

    if errors:
        print(f"\n{len(errors)} failure(s) out of {len(companies)}", file=sys.stderr)

    return results


# ---------------------------------------------------------------------------
# Sample data — 4 companies (9 fields each)
# ---------------------------------------------------------------------------

SAMPLE_COMPANIES: list[dict] = [
    {
        "firm_name": "Chen & Ortiz LLP",
        "practice_area": "Personal injury",
        "city_state": "Jackson Heights, NY",
        "zip_code": "11372",
        "problems": [
            {
                "headline": "After-hours calls are not answered the same day.",
                "evidence": "GBP hours end early evening; no after-hours line or chat on the site.",
            },
            {
                "headline": "You do not promise a same-day callback; nearby PI firms do.",
                "evidence": "No speed-to-lead claim on site; local competitors advertise faster response.",
            },
            {
                "headline": "Buying ads now would pour leads into the same gap.",
                "evidence": "No clear LSA or ads running — fix intake before spending on demand.",
            },
        ],
    },
    {
        "firm_name": "Goldberg & Associates",
        "practice_area": "Family law",
        "city_state": "Brooklyn, NY",
        "zip_code": "11201",
        "problems": [
            {
                "headline": "No online intake form — every lead requires a phone call.",
                "evidence": "Website has no contact form or chat; only a phone number listed.",
            },
            {
                "headline": "Google Business Profile has no reviews in the last 6 months.",
                "evidence": "Last review is from January; competitors have 10+ recent reviews.",
            },
            {
                "headline": "Practice area pages are thin and don’t target local keywords.",
                "evidence": "Service pages under 200 words; no mention of Brooklyn or surrounding areas.",
            },
        ],
    },
    {
        "firm_name": "Martinez Law Group",
        "practice_area": "Immigration",
        "city_state": "Los Angeles, CA",
        "zip_code": "90012",
        "problems": [
            {
                "headline": "Website is not available in Spanish despite a bilingual market.",
                "evidence": "No language toggle; competitors offer full Spanish-language sites.",
            },
            {
                "headline": "No FAQ or resource section to capture informational search traffic.",
                "evidence": "Zero blog posts or guides; missing common immigration-question keywords.",
            },
            {
                "headline": "Consultation booking requires email back-and-forth, not self-service.",
                "evidence": "No calendar widget; contact page says ‘we will get back to you.’",
            },
        ],
    },
    {
        "firm_name": "Park & Sullivan PLLC",
        "practice_area": "Estate planning",
        "city_state": "Austin, TX",
        "zip_code": "78701",
        "problems": [
            {
                "headline": "No trust or will pricing transparency — visitors leave to compare.",
                "evidence": "Competitors list starting prices; your site says ‘call for a quote.’",
            },
            {
                "headline": "GBP category is ‘Lawyer’ instead of ‘Estate planning attorney.’",
                "evidence": "Generic category hurts ranking for estate-specific searches.",
            },
            {
                "headline": "Site loads in 6+ seconds on mobile — half of visitors bounce.",
                "evidence": "PageSpeed score 38; unoptimized images and render-blocking scripts.",
            },
        ],
    },
]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        companies = json.loads(input_path.read_text(encoding="utf-8"))
    else:
        companies = SAMPLE_COMPANIES

    dest = batch_output_dir()
    dest.mkdir(parents=True, exist_ok=True)

    # Save the input manifest alongside the PDFs
    manifest_path = dest / "companies.json"
    manifest_path.write_text(
        json.dumps(companies, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Saved {manifest_path.name} → {dest}")

    print(f"Generating {len(companies)} report(s) → {dest}")
    paths = generate_all(companies, output_dir=dest, max_workers=min(len(companies), 8))
    print(f"\nDone — {len(paths)} PDF(s) + companies.json in {dest}")
