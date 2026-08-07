"""
Turn a plain Streamlit .py calculator into a self-contained stlite HTML
page that runs entirely in the browser via WebAssembly (no server) - for
embedding in the static mkdocs site through an <iframe>.

Usage:
    Rebuild one calculator by path:
        .venv\\Scripts\\python scripts\\build_calculator.py docs\\Calculators\\Info_magnetiet_FeSi\\Info_magnetiet_FeSi.py

    Rebuild whichever calculators are uncommented in CALCULATORS below:
        .venv\\Scripts\\python scripts\\build_calculator.py

Writes <name>.html next to each source .py file. Re-run this any time a
.py file changes - the .html is generated output, not something to
hand-edit.
"""

import html
import sys
from pathlib import Path

# Pin the stlite version so a new release upstream can't silently change
# how a calculator behaves/looks. Bump deliberately and re-test when
# there's a reason to (e.g. a bug fix or a package you need that a newer
# stlite bundles).
STLITE_VERSION = "1.8.1"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{title}</title>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@stlite/browser@{version}/build/stlite.css"
/>
<style>
  /* This page is only ever loaded inside an <iframe> on a chapter page -
     let the app fill all the space it's given. */
  html, body {{
    margin: 0;
    height: 100%;
  }}
</style>
</head>
<body>
<streamlit-app>
{code}
</streamlit-app>
<script
  type="module"
  src="https://cdn.jsdelivr.net/npm/@stlite/browser@{version}/build/stlite.js"
></script>
</body>
</html>
"""


def build(py_path: Path) -> Path:
    source = py_path.read_text(encoding="utf-8")

    # <streamlit-app> is a normal HTML custom element, not a "raw text"
    # element like <script>/<style> - the browser parses its content as
    # HTML. Without escaping, something like `List[MyClass<T>]` or a
    # stray `&` could be misread as a tag/entity and silently corrupt
    # the Python source before Pyodide ever sees it. html.escape()
    # handles & first, then < and >, in the right order to avoid
    # double-escaping.
    escaped = html.escape(source, quote=False)

    html_out = TEMPLATE.format(
        title=py_path.stem, version=STLITE_VERSION, code=escaped
    )
    out_path = py_path.with_suffix(".html")
    out_path.write_text(html_out, encoding="utf-8")
    return out_path


# Comment/uncomment a line to control which calculator(s) get rebuilt
# when running this script with no arguments (add a new line here for
# every new calculator).
CALCULATORS = [
    Path("docs/Calculators/Info_magnetiet_FeSi/Info_magnetiet_FeSi.py"),
    #Path("docs/Calculators/Weight_calculations_platforms/Weight_calculations_platforms.py"),
]

if __name__ == "__main__":
    targets = [Path(sys.argv[1])] if len(sys.argv) == 2 else CALCULATORS
    for py_path in targets:
        result = build(py_path)
        print(f"Wrote {result}")