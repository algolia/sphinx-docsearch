"""Automate everything everywhere all at once.

Requires [Nox](https://nox.thea.codes/).

- Run `nox -ls` to list all sessions.
- Run `nox -s <NAME>` to run the session _`<NAME>`_.
- Run `nox -s docs -p 3.14 -- --live` to build the docs with live-reloading.
"""

from __future__ import annotations

import nox
import nox_uv

nox.options.stop_on_first_error = True
nox.options.default_venv_backend = "uv"
nox.options.sessions = ["tests", "typecheck", "docs"]

project = nox.project.load_toml("pyproject.toml")
supported_python_versions = nox.project.python_versions(project)
python_versions = [supported_python_versions[0], supported_python_versions[-1]]


@nox_uv.session(python=python_versions, uv_groups=["docs"])
def docs(s: nox.Session) -> None:
    """Build the docs."""
    args = ["-aWTE", "docs", "docs/_dist"]
    sphinx_build = "sphinx-build"

    if "--live" in s.posargs:
        sphinx_build = "sphinx-autobuild"
        s.posargs.remove("--live")

    if s.posargs:
        args = s.posargs + args

    s.run(sphinx_build, *args)


@nox_uv.session(uv_groups=["docs"])
def check_links(s: nox.Session) -> None:
    """Check links in docs."""
    args = ["-b", "linkcheck", "docs", "docs/_dist/_links"]

    if s.posargs:
        args = s.posargs + args

    s.run("sphinx-build", *args)


@nox_uv.session(uv_groups=["lint"])
def fmt(s: nox.Session) -> None:
    """Format the code with ruff."""
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("ruff", "format", ".")


@nox_uv.session(uv_groups=["lint"])
def lint(s: nox.Session) -> None:
    """Lint the code with ruff."""
    s.run("ruff", "check", ".")


@nox_uv.session(python=python_versions, uv_groups=["test"])
def tests(s: nox.Session) -> None:
    """Run unit tests."""
    args = s.posargs or ["--cov"]
    s.run("pytest", *args)


@nox_uv.session(python=python_versions, uv_groups=["typecheck"])
def typecheck(s: nox.Session) -> None:
    """Typecheck."""
    s.run("pyright")


@nox.session(python=False)
def build(s: nox.Session) -> None:
    """Build the packages."""
    s.run("uv", "build", external=True)
