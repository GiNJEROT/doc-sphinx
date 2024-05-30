import sys
import os
from pathlib import Path

import sphinx_rtd_theme

# PROJECT_BASE = Path("/docs") #Path(__file__).resolve().parents[1]
# DOC_DIR = "source"
PROJECT_BASE = Path(__file__).resolve().parents[1]
DOC_DIR = "docs"

# Add the '_extensions' directory to sys.path, to enable finding Sphinx
# extensions within.
sys.path.insert(0, str(PROJECT_BASE / DOC_DIR / "_extensions"))

# Add the '_scripts' directory to sys.path, to enable finding utility
# modules.
# sys.path.insert(0, str(PROJECT_BASE / "docs" / "_scripts"))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Automatisation Usine SA'
copyright = '2024, BluBlu SA'
author = 'Gregory Jerot'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.drawio",
    "myst_parser",
    "sphinxcontrib.jquery",
    "sphinx_immaterial.task_lists"
]

clickable_checkbox : bool = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}
# -- Options for plantuml output ---------------------------------------------
plantuml_output_format = "svg"

# -- Options for drawio output -----------------------------------------------
drawio_default_transparency = True
drawio_no_sandbox = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "prev_next_buttons_location": None
}
html_title = "Automatisation Usine SA"
html_logo = str(PROJECT_BASE / DOC_DIR / "_static" / "images" / "logo.jpeg")
html_favicon = str(PROJECT_BASE / DOC_DIR / "_static" / "images" / "logo.jpeg")
html_static_path = [str(PROJECT_BASE / DOC_DIR / "_static")]
html_last_updated_fmt = "%d %b %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_search_scorer = str(PROJECT_BASE / DOC_DIR / "_static" / "js" / "scorer.js")

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "papersize": "a4paper",
    "maketitle": open(PROJECT_BASE / DOC_DIR / "_static" / "latex" / "title.tex").read(),
    "preamble": open(PROJECT_BASE / DOC_DIR / "_static" / "latex" / "preamble.tex").read(),
    "fontpkg": r"\usepackage[sfdefault]{roboto}",
    "sphinxsetup": ",".join(
        (
            # NOTE: colors match those found in light.css stylesheet
            "verbatimwithframe=false",
            "VerbatimColor={HTML}{f0f2f4}",
            "InnerLinkColor={HTML}{2980b9}",
            "warningBgColor={HTML}{e9a499}",
            "warningborder=0pt",
            r"HeaderFamily=\rmfamily\bfseries",
        )
    ),
}
latex_logo = str(PROJECT_BASE / DOC_DIR / "_static" / "images" / "logo-latex.pdf")

latex_documents = [
    ("index-tex", "doc.tex", project, author, "manual"),
]

def setup(app):
    # theme customizations
    app.add_css_file("css/custom.css")
    app.add_js_file("js/dark-mode-toggle.min.mjs", type="module")
