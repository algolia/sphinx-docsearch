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
myst_enable_extensions = ["colon_fence"]

# DocSearch Sphinx extension
docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")

# Support building the docs with different themes
# Add `-t furo` or `-t rtd` to the build arguments
if tags.has("furo"):  # noqa
    html_theme = "furo"

if tags.has("rtd"):  # noqa
    html_theme = "sphinx_rtd_theme"
