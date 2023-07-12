"""Test configuration checks."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .utils import read_as_html


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"]})
def test_docsearch_assets(app: Sphinx) -> None:
    """It adds all the DocSearch assets to the HTML output."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "_static" / "docsearch.css")
    assert os.path.exists(Path(app.outdir) / "_static" / "docsearch.js")
    assert os.path.exists(Path(app.outdir) / "_static" / "docsearch_config.js")
    test_file = read_as_html(Path(app.outdir) / "index.html")

    css = test_file.select("link[rel='stylesheet']")
    css = [x["href"] for x in css]  # type: ignore[assignment]
    assert "_static/docsearch.css" in css
    assert "_static/alabaster-docsearch-custom.css" in css

    scripts = test_file.select("script")
    scripts = [x["src"] for x in scripts]  # type: ignore[assignment]
    assert "_static/docsearch.js" in scripts
    assert "_static/docsearch_config.js" in scripts

@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"], "html_theme": "furo"})
def test_custom_furo_assets(app: Sphinx) -> None:
    """It adds the custom CSS for the furo theme."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "_static" / "furo-docsearch-custom.css")
    test_file = read_as_html(Path(app.outdir) / "index.html")

    css = test_file.select("link[rel='stylesheet']")
    css = [x["href"] for x in css]  # type: ignore[assignment]
    assert "_static/furo-docsearch-custom.css" in css


@pytest.mark.sphinx("html", confoverrides={"extensions": ["sphinx_docsearch"], "html_theme": "sphinx_rtd_theme"})
def test_custom_rtd_assets(app: Sphinx) -> None:
    """It adds the custom CSS for the read the docs theme."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "_static" / "rtd-docsearch-custom.css")
    test_file = read_as_html(Path(app.outdir) / "index.html")

    css = test_file.select("link[rel='stylesheet']")
    css = [x["href"] for x in css]  # type: ignore[assignment]
    assert "_static/rtd-docsearch-custom.css" in css
