"""Test builder."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_no_builtin_search(app: Sphinx) -> None:
    """It doesn't add the builtin search assets to the HTML output."""
    app.build()
    assert app.builder.search is False  # type: ignore
    assert not os.path.exists(Path(app.outdir) / "search.html")
    assert not os.path.exists(Path(app.outdir) / "searchindex.js")


@pytest.mark.sphinx("xml", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_xml_docs(app: Sphinx) -> None:
    """It builds docs other than HTML."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.xml")
