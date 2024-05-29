"""Test configuration checks."""

import os
from io import StringIO
from pathlib import Path

import pytest
import sphinx_docsearch
from sphinx.application import Sphinx


def test_returns_version() -> None:
    """It returns the correct version."""
    assert sphinx_docsearch.__version__ == "0.0.7"


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_docsearch_config(app: Sphinx) -> None:
    """It tests the addition of DocSearch configuration options."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinx_docsearch" in app.extensions
    assert not app.config.docsearch_app_id
    assert not app.config.docsearch_api_key
    assert not app.config.docsearch_index_name
    assert app.config.docsearch_container == "#docsearch"
    assert not app.config.docsearch_initial_query
    assert not app.config.docsearch_placeholder
    assert not app.config.docsearch_search_parameter
    assert not app.config.docsearch_missing_results_url


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_raises_warnings(app: Sphinx, warning: StringIO) -> None:
    """It raises warnings when the required config options are missing."""
    app.build()
    warnings = warning.getvalue()

    assert (
        "WARNING: You must provide your Algolia application ID for DocSearch to work."
        in warnings
    )
    assert (
        "WARNING: You must provide your Algolia search API key for DocSearch to work."
        in warnings
    )
    assert (
        "WARNING: You must provide your Algolia index name for DocSearch to work."
        in warnings
    )


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinx_docsearch"],
        "docsearch_app_id": "test_app_id",
        "docsearch_api_key": "test_api_key",
        "docsearch_index_name": "test_docsearch_index_name",
        "docsearch_container": "test_docsearch_container",
        "docsearch_placeholder": "test_docsearch_placeholder",
        "docsearch_initial_query": "test_docsearch_initial_query",
        "docsearch_search_parameter": "test_docsearch_parameter",
        "docsearch_missing_results_url": "test_docsearch_url",
    },
)
def test_add_docsearch_config(app: Sphinx, warning: StringIO) -> None:
    """It parses the DocSearch configuration options."""
    app.build()
    warnings = warning.getvalue()
    assert warnings == ""
    assert app.config.docsearch_app_id == "test_app_id"
    assert app.config.docsearch_api_key == "test_api_key"
    assert app.config.docsearch_index_name == "test_docsearch_index_name"
    assert app.config.docsearch_container == "test_docsearch_container"
    assert app.config.docsearch_placeholder == "test_docsearch_placeholder"
    assert app.config.docsearch_initial_query == "test_docsearch_initial_query"
    assert app.config.docsearch_search_parameter == "test_docsearch_parameter"
    assert app.config.docsearch_missing_results_url == "test_docsearch_url"
