"""Test rendering of the Ask AI (askAi) config, both string and object forms."""

from pathlib import Path

import pytest
from sphinx.application import Sphinx


def read_config_js(app: Sphinx) -> str:
    """Read the rendered docsearch_config.js from the build output."""
    return (Path(app.outdir) / "_static" / "docsearch_config.js").read_text()


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinx_docsearch"],
        "docsearch_askai": "test_assistant_id",
    },
)
def test_askai_string_form(app: Sphinx) -> None:
    """It renders the string form as a quoted string with a trailing comma."""
    app.build()
    config_js = read_config_js(app)
    assert 'askAi: "test_assistant_id",' in config_js


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinx_docsearch"],
        "docsearch_askai": {
            "assistantId": "test_assistant_id",
            "agentStudio": True,
            "searchParameters": {
                "test_index": {"filters": "type:content"},
            },
        },
    },
)
def test_askai_object_form(app: Sphinx) -> None:
    """It renders the Agent Studio object form as serialized JSON."""
    app.build()
    config_js = read_config_js(app)
    assert '"assistantId": "test_assistant_id"' in config_js
    assert '"agentStudio": true' in config_js
    # searchParameters keyed by index name for Agent Studio's multi-index support.
    assert '"searchParameters": {"test_index":' in config_js


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinx_docsearch"],
        "docsearch_askai": "test_assistant_id",
        "docsearch_initial_query": "test_query",
    },
)
def test_askai_followed_by_key_has_comma(app: Sphinx) -> None:
    """It keeps a comma after askAi when a later key is set (valid JS)."""
    app.build()
    config_js = read_config_js(app)
    assert 'askAi: "test_assistant_id",' in config_js
    # Guards against the missing-comma regression producing invalid JS.
    assert 'askAi: "test_assistant_id"\n' not in config_js
