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

import ast
import base64
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

  /* stlite mounts the actual rendered app as a position:fixed child of
     <streamlit-app> (so it's unaffected by this), but never clears the
     original Python source text that's still sitting inside it as a
     sibling text node - left alone, that text renders in normal
     document flow and inflates this page's real height far beyond the
     visible app, which shows up as a bogus internal scrollbar once
     something outside sizes the iframe to the app's true (smaller)
     height. Collapsing streamlit-app's own box to nothing hides that
     leftover text without touching the fixed-position app itself. */
  streamlit-app {{
    display: block;
    height: 0;
    overflow: hidden;
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


def _images_prelude(py_path: Path) -> str:
    """Python source that recreates a sibling images/ folder inside
    Pyodide's virtual filesystem, so a calculator can just call
    st.image("images/x.png") and have it work identically under a normal
    `streamlit run` (real files on disk) and here (no real disk at all).
    Returns "" if the calculator has no images/ folder to bundle."""
    images_dir = py_path.parent / "images"
    if not images_dir.is_dir():
        return ""

    lines = [
        "import base64 as _b64_calc, pathlib as _pathlib_calc",
        '_pathlib_calc.Path("images").mkdir(exist_ok=True)',
    ]
    for image_path in sorted(images_dir.iterdir()):
        if not image_path.is_file():
            continue
        encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
        lines.append(
            f'_pathlib_calc.Path("images/{image_path.name}").write_bytes('
            f'_b64_calc.b64decode("{encoded}"))'
        )
    return "\n".join(lines) + "\n\n"


def _insert_after_docstring(source: str, prelude: str) -> str:
    """Splice `prelude` in right after the module docstring, if there is
    one, instead of before it. Prepending code demotes a real module
    docstring to just an ordinary bare string expression (no longer the
    file's literal first statement) - and Streamlit's magic commands
    feature auto-renders bare string expressions, so a demoted docstring
    would leak onto the page as visible text. Splicing after it leaves it
    as the true first statement, exempt from that."""
    if not prelude:
        return source
    tree = ast.parse(source)
    has_docstring = (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    )
    if not has_docstring:
        return prelude + source
    end_line = tree.body[0].end_lineno
    lines = source.splitlines(keepends=True)
    return "".join(lines[:end_line]) + "\n" + prelude + "".join(lines[end_line:])


def build(py_path: Path) -> Path:
    source = _insert_after_docstring(
        py_path.read_text(encoding="utf-8"), _images_prelude(py_path)
    )

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