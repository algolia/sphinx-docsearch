"""Test the DOM."""

from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .utils import read_as_html


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinx_docsearch"],
        "docsearch_container": "docsearch-test",
    },
)
def test_no_builtin_search(app: Sphinx) -> None:
    """It adds the docsearch container to the DOM."""
    app.build()

    test_file = read_as_html(Path(app.outdir) / "index.html")
    search = test_file.select("#docsearch-test")
    assert len(search) == 1
