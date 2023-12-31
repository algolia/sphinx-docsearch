"""Sphinx configuration."""
import os

from dotenv import load_dotenv
from sphinxawesome_theme.postprocess import Icons

# Load environment variables
load_dotenv()

# Project information
project = "Algolia DocSearch Sphinx extension"
author = "Algolia"
copyright = f"{author}."
html_title = "Algolia DocSearch for Sphinx"

# General configuration
extensions = ["sphinx_docsearch", "myst_parser"]
myst_enable_extensions = ["colon_fence", "deflist"]

# DocSearch Sphinx extension
docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
# docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")
docsearch_index_name = "crawler_sphinx test"

# Support building the docs with different themes
# Add `-t alabaster` or `-t rtd` to the build arguments
if tags.has("rtd"):  # noqa
    html_theme = "sphinx_rtd_theme"
    html_theme_options = {
        "style_external_links": True,
    }
elif tags.has("alabaster"):  # noqa
    html_theme = "alabaster"
elif tags.has("furo"):  # noqa
    html_theme = "furo"
else:
    html_theme = "sphinxawesome_theme"
    html_permalinks_icon = Icons.permalinks_icon
    html_theme_options = {"awesome_external_links": True}
    extensions += ["sphinxawesome_theme.highlighting"]
