"""Add Algolia DocSearch to Sphinx.

Replace Sphinx built-in search with Algolia DocSearch.

:copyright: Kai Welke.
:license: MIT, see LICENSE for details
"""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

from sphinx.application import Config, Sphinx
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.display import progress_message

logger = logging.getLogger(__name__)

try:
    __version__ = version(__name__.replace(".", "-"))
except PackageNotFoundError:  # pragma: nocover
    __version__ = "unknown"


def check_config(app: Sphinx, config: Config) -> None:
    """Set up Algolia DocSearch.

    The parameters: `docsearch_app_id`, `docsearch_api_key`, and `docsearch_index_name` are required.
    Log warnings if any of these aren't included.
    """
    if not config.docsearch_app_id:
        logger.warning(
            __("You must provide your Algolia application ID for DocSearch to work.")
        )
    if not config.docsearch_api_key:
        logger.warning(
            __("You must provide your Algolia search API key for DocSearch to work.")
        )
    if not config.docsearch_index_name:
        logger.warning(
            __("You must provide your Algolia index name for DocSearch to work.")
        )


@progress_message("DocSearch: set up")
def add_docsearch_assets(app: Sphinx, config: Config) -> None:
    """Add the CSS and JS files for DocSearch.

    Load the CSS with priority 800 to make sure it's loaded after default CSS.
    This prevents global CSS (often used in Sphinx themes) from overriding DocSearch CSS.
    """
    app.add_css_file("docsearch.css", priority=800)
    app.add_js_file("docsearch.js", loading_method="defer")
    app.add_js_file("docsearch_config.js", loading_method="defer")

    static_path = Path(__file__).parent.joinpath("static").absolute()
    templates_path = Path(__file__).parent.joinpath("templates").absolute()
    config.html_static_path.append(str(static_path))
    config.templates_path.append(str(templates_path))

    # Provide custom CSS to support different themes
    if config.html_theme == "furo":
        app.add_css_file("furo-docsearch-custom.css", priority=810)
    elif config.html_theme == "sphinx_rtd_theme":
        app.add_css_file("rtd-docsearch-custom.css", priority=820)
    elif config.html_theme == "alabaster":
        app.add_css_file("alabaster-docsearch-custom.css", priority=820)

    # Update global context
    config.html_context.update(
        {
            "docsearch_app_id": config.docsearch_app_id,
            "docsearch_api_key": app.config.docsearch_api_key,
            "docsearch_index_name": app.config.docsearch_index_name,
            "docsearch_container": app.config.docsearch_container,
            "docsearch_initial_query": app.config.docsearch_initial_query,
            "docsearch_placeholder": app.config.docsearch_placeholder,
            "docsearch_search_parameter": app.config.docsearch_search_parameter,
            "docsearch_missing_results_url": app.config.docsearch_missing_results_url,
        }
    )


def setup(app: Sphinx) -> dict[str, Any]:
    """Register this extension with Sphinx."""
    app.add_config_value("docsearch_app_id", default="", rebuild="html", types=[str])
    app.add_config_value("docsearch_api_key", default="", rebuild="html", types=[str])
    app.add_config_value(
        "docsearch_index_name", default="", rebuild="html", types=[str]
    )
    app.add_config_value(
        "docsearch_container", default="#docsearch", rebuild="html", types=[str]
    )
    app.add_config_value(
        "docsearch_initial_query", default="", rebuild="html", types=[str]
    )
    app.add_config_value(
        "docsearch_placeholder", default="", rebuild="html", types=[str]
    )
    app.add_config_value(
        "docsearch_search_parameter", default="", rebuild="html", types=[str]
    )
    app.add_config_value(
        "docsearch_missing_results_url", default="", rebuild="html", types=[str]
    )

    app.connect("config-inited", check_config)
    app.connect("config-inited", add_docsearch_assets)

    # Disable built-in search
    StandaloneHTMLBuilder.search = False
    DirectoryHTMLBuilder.search = False

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
