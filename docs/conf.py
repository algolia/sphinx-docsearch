"""Sphinx configuration."""
import os

from dotenv import load_dotenv

# -- Load environment variables ---
load_dotenv()

# -- Project information ---

project = "Awesome DocSearch"
author = "Kai Welke"
copyright = f"{author}."

# -- General configuration ---

extensions = ["sphinxawesome.docsearch", "myst_parser"]

docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")

# -- HTML ---
html_theme = "furo"
html_static_path = ["static"]
html_css_files = ["custom.css"]
