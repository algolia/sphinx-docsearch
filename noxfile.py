"""Automate everything everywhere all at once.

Requires [Nox](https://nox.thea.codes/).

- Run `nox -ls` to list all sessions.
- Run `nox -s <NAME>` to run the session _`<NAME>`_.
- Run `nox -s docs -p 3.13 -- --live` to build the docs with live-reloading.
"""

from __future__ import annotations

import nox

nox.options.stop_on_first_error = True
nox.options.default_venv_backend = "uv"
nox.options.sessions = ["tests", "typecheck"]

python_versions = ["3.9", "3.13"]


def get_requirements(groups: list[str] | str | None = None) -> list[str]:
    """Load requirements from a `pyproject.toml` file."""
    pyproject = nox.project.load_toml("pyproject.toml")
    pkgs = pyproject["project"]["dependencies"]

    if groups and "dependency-groups" in pyproject:
        for g in groups if isinstance(groups, list) else [groups]:
            pkgs += pyproject["dependency-groups"].get(g, [])

    return pkgs


def install_requirements(
    session: nox.Session, groups: list[str] | str | None = None
) -> None:
    """Install requirements into the session's environment."""
    requirements = get_requirements(groups)
    session.install(*requirements)
    session.install("-e", ".")


@nox.session(python=python_versions)
def docs(s: nox.Session) -> None:
    """Build the docs."""
    args = ["-aWTE", "docs", "docs/_dist"]
    sphinx_build = "sphinx-build"

    if "--live" in s.posargs:
        sphinx_build = "sphinx-autobuild"
        s.posargs.remove("--live")

    if s.posargs:
        args = s.posargs + args

    install_requirements(s, "docs")
    s.run(sphinx_build, *args)


@nox.session
def check_links(s: nox.Session) -> None:
    """Check links in docs."""
    args = ["-b", "linkcheck", "docs", "docs/_dist/_links"]

    if s.posargs:
        args = s.posargs + args

    install_requirements(s, "docs")
    s.run("sphinx-build", *args)


@nox.session
def fmt(s: nox.Session) -> None:
    """Format the code with ruff."""
    install_requirements(s, "lint")
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("ruff", "format", ".")


@nox.session
def lint(s: nox.Session) -> None:
    """Lint the code with ruff."""
    install_requirements(s, "lint")
    s.run("ruff", "check", ".")


@nox.session(python=python_versions)
def tests(s: nox.Session) -> None:
    """Run unit tests."""
    args = s.posargs or ["--cov"]
    install_requirements(s, "test")
    s.run("pytest", *args)


@nox.session(python=python_versions)
def typecheck(s: nox.Session) -> None:
    """Typecheck."""
    install_requirements(s, "typecheck")
    s.run("pyright")


@nox.session(python=False)
def build(s: nox.Session) -> None:
    """Build the packages."""
    s.run("uv", "build", external=True)


@nox.session(python=False)
def export(s: nox.Session) -> None:
    """Export dependencies for ReadTheDocs."""
    s.run(
        "uv",
        "export",
        "--group=docs",
        "--no-hashes",
        "--output-file=docs/requirements.txt",
        external=True,
    )


@nox.session(python=False)
def clean(s: nox.Session) -> None:
    """Delete artifacts."""
    s.run("rm", "-rv", "dist", "docs/_dist")
