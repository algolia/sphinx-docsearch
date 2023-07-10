"""Sphinx configuration."""
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project information
project = "Algolia DocSearch Sphinx extension"
author = "Algolia"
copyright = f"{author}."

# General configuration
extensions = ["sphinx_docsearch", "myst_parser"]

docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")

# DocSearch custom CSS examples for multiple Sphinx themes
multi_theme = {
    "furo": "furo-docsearch-custom.css"
}

html_static_path = ["static"]

for theme in multi_theme:
    if tags.has(theme):
        html_theme = theme
        html_css_files = [multi_theme[theme]]
else:
    html_css_files = ["alabaster-docsearch-custom.css"]
