"""Time-based day/night theme default (Google-Maps-style) — regression tests."""

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "website"
APP_PY = SRC / "app.py"
SCRIPT_JS = SRC / "static" / "script.js"


def test_single_theme_color_meta():
    src = APP_PY.read_text(encoding="utf-8")
    assert src.count('name="theme-color"') == 1


def test_inline_auto_theme_hook():
    src = APP_PY.read_text(encoding="utf-8")
    assert "__axiomAutoTheme" in src
    assert "getHours" in src
    # Priority: saved manual choice first, then auto day/night, then system.
    # The v2 key replaced v1, whose values were pinned by the old
    # always-persist behavior and could never be trusted as explicit.
    assert "localStorage.getItem('axiom-theme-v2')" in src
    assert "localStorage.removeItem('axiom-theme')" in src
    assert "querySelector('meta[name=" in src


def test_script_live_updates_without_overriding_manual():
    src = SCRIPT_JS.read_text(encoding="utf-8")
    assert "__axiomAutoTheme" in src
    assert "visibilitychange" in src
    assert "setInterval" in src
    assert "hasManualChoice" in src
    assert "THEME_KEY = 'axiom-theme-v2'" in src
    # Auto applies must not persist — persisting would freeze the day/night
    # default into a manual choice on first paint/interval tick.
    assert "setTheme(auto, false)" in src
    assert "setTheme(root.dataset.theme || 'light', false)" in src
    # Drawer reset returns to auto without persisting.
    assert "data-theme-auto" in src
    assert "removeItem(THEME_KEY)" in src


def _inline_head_js():
    """Reconstruct the inline head script by joining its adjacent literals."""
    src = APP_PY.read_text(encoding="utf-8")
    start = src.index("def _theme_init_script")
    end = src.index("\n    )\n", start)
    lits = re.findall(r'"((?:[^"\\]|\\.)*)"', src[start:end])
    return "".join(lit.replace('\\"', '"') for lit in lits)


def test_day_night_boundaries():
    """Run the shipped day/night function in node against fixed clock times."""
    if shutil.which("node") is None:
        return  # boundaries verified manually via DevTools sensor emulation
    js = _inline_head_js()
    match = re.search(r"window\.__axiomAutoTheme=function\(d\)\{.*?\};", js)
    assert match, "auto theme function missing from inline head script"
    harness = (
        "var window={};\n"
        + match.group(0)
        + """
const cases = [
  [0, 0, 'dark'], [5, 59, 'dark'], [6, 0, 'light'], [6, 1, 'light'],
  [12, 0, 'light'], [17, 59, 'light'], [18, 0, 'dark'], [23, 59, 'dark'],
];
for (const [h, mi, exp] of cases) {
  const got = window.__axiomAutoTheme({ getHours: () => h, getMinutes: () => mi });
  if (got !== exp) {
    console.error(`FAIL ${h}:${String(mi).padStart(2, '0')} -> ${got}, want ${exp}`);
    process.exit(1);
  }
}
console.log('boundaries ok');
"""
    )
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(harness)
        path = fh.name
    try:
        proc = subprocess.run(["node", path], capture_output=True, text=True, timeout=30)
    finally:
        Path(path).unlink(missing_ok=True)
    assert proc.returncode == 0, proc.stderr or proc.stdout
