"""Test global context."""

import re

import pytest
from sphinx.application import Sphinx


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_global_context(app: Sphinx) -> None:
    """It adds all the DocSearch configuration to global context."""
    app.build()

    pattern = re.compile(r"^docsearch_")
    docsearch_config = filter(pattern.search, app.builder.globalcontext)
    assert len(list(docsearch_config)) == 9

    assert "docsearch_app_id" in app.builder.globalcontext
    assert "docsearch_api_key" in app.builder.globalcontext
    assert "docsearch_index_name" in app.builder.globalcontext
    assert "docsearch_initial_query" in app.builder.globalcontext
    assert "docsearch_container" in app.builder.globalcontext
    assert "docsearch_placeholder" in app.builder.globalcontext
    assert "docsearch_search_parameters" in app.builder.globalcontext
    assert "docsearch_max_results_per_group" in app.builder.globalcontext
    assert "docsearch_missing_results_url" in app.builder.globalcontext
    assert app.builder.globalcontext["docsearch_container"] == "#docsearch"
