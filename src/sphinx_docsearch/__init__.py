"""Add Algolia DocSearch to Sphinx.

Replace Sphinx built-in search with Algolia DocSearch.

:copyright: Kai Welke.
:license: MIT, see LICENSE for details
"""
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Dict

from docutils.nodes import Node
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
    Log warnings, if any of these aren't included.
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
    """Add the CSS and JS files for DocSearch."""
    app.add_css_file("docsearch.css")
    app.add_js_file("docsearch.js", loading_method="defer")
    app.add_js_file("docsearch_config.js", loading_method="defer")

    static_path = Path(__file__).parent.joinpath("static").absolute()
    templates_path = Path(__file__).parent.joinpath("templates").absolute()
    config.html_static_path.append(str(static_path))
    config.templates_path.append(str(templates_path))


@progress_message("DocSearch: update global context")
def update_global_context(app: Sphinx, doctree: Node, docname: str) -> None:
    """Update global context with DocSearch configuration."""
    if app.builder.format != "html":
        return

    app.builder.globalcontext["docsearch_app_id"] = app.config.docsearch_app_id
    app.builder.globalcontext["docsearch_api_key"] = app.config.docsearch_api_key
    app.builder.globalcontext["docsearch_index_name"] = app.config.docsearch_index_name
    app.builder.globalcontext["docsearch_container"] = app.config.docsearch_container
    app.builder.globalcontext[
        "docsearch_initial_query"
    ] = app.config.docsearch_initial_query
    app.builder.globalcontext[
        "docsearch_placeholder"
    ] = app.config.docsearch_placeholder
    app.builder.globalcontext[
        "docsearch_search_parameter"
    ] = app.config.docsearch_search_parameter
    app.builder.globalcontext[
        "docsearch_missing_results_url"
    ] = app.config.docsearch_missing_results_url


def setup(app: Sphinx) -> Dict[str, Any]:
    """Register this extension with Sphinx."""
    app.add_config_value("docsearch_app_id", default="", rebuild="html", types=(str))
    app.add_config_value("docsearch_api_key", default="", rebuild="html", types=(str))
    app.add_config_value(
        "docsearch_index_name", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_container", default="#docsearch", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_initial_query", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_placeholder", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_search_parameter", default="", rebuild="html", types=(str)
    )
    app.add_config_value(
        "docsearch_missing_results_url", default="", rebuild="html", types=(str)
    )

    app.connect("config-inited", check_config)
    app.connect("config-inited", add_docsearch_assets)
    app.connect("doctree-resolved", update_global_context)

    # Disable built-in search
    StandaloneHTMLBuilder.search = False
    DirectoryHTMLBuilder.search = False

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
