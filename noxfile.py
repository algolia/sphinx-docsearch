"""Automate everything everywhere all at once.

Requires [Nox](https://nox.thea.codes/).

- Run `nox -ls` to list all sessions.
- Run `nox -s <NAME>` to run the session _`<NAME>`_.
- Run `nox -s docs -p 3.12 -- --live` to build the docs with live-reloading.
"""

import tempfile

from nox import Session, options, session

options.stop_on_first_error = True

python_versions = ["3.12", "3.11", "3.10", "3.9", "3.8"]


def install_with_group(s: Session, group: str = "dev") -> None:
    """Install group dependencies from Poetry."""
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--without-hashes",
            "--with",
            group,
            "--output",
            requirements.name,
            external=True,
        )
        s.install("-r", requirements.name)
        s.install(".")


@session(python=python_versions)
def docs(s: Session) -> None:
    """Build the docs."""
    args = ["-aWTE", "docs", "docs/_dist"]
    sphinx_build = "sphinx-build"

    if "--live" in s.posargs:
        sphinx_build = "sphinx-autobuild"
        s.posargs.remove("--live")

    if s.posargs:
        args = s.posargs + args

    install_with_group(s, "docs")
    s.run(sphinx_build, *args)


@session
def check_links(s: Session) -> None:
    """Check links in docs."""
    args = ["-b", "linkcheck", "docs", "docs/_dist/_links"]

    if s.posargs:
        args = s.posargs + args

    install_with_group(s, "docs")
    s.run("sphinx-build", *args)


@session
def fmt(s: Session) -> None:
    """Format the code with black and ruff."""
    install_with_group(s, "lint")
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("ruff", "format", ".")


@session
def lint(s: Session) -> None:
    """Lint the code with ruff."""
    install_with_group(s, "lint")
    s.run("ruff", "check", ".")


@session(python=python_versions)
def tests(s: Session) -> None:
    """Run unit tests."""
    args = s.posargs or ["--cov"]
    install_with_group(s, "dev,docs")
    s.run("pytest", *args)


@session(python=["3.8", "3.12"])
def typecheck(s: Session) -> None:
    """Typecheck."""
    install_with_group(s, "dev")
    s.run("mypy", ".", "--exclude", "docs")


@session(python=False)
def build(s: Session) -> None:
    """Build the packages using Poetry.

    Since Poetry is installed globally,
    skip the virtual environment creation.
    """
    s.run("poetry", "build", external=True)


@session(python=False)
def export(s: Session) -> None:
    """Export Poetry dependencies for ReadTheDocs.

    Since Poetry is installed globally,
    skip the virtual environment creation.
    """
    s.run(
        "poetry",
        "export",
        "--with",
        "docs",
        "--without-hashes",
        "--output",
        "docs/requirements.txt",
        external=True,
    )


@session(python=False)
def publish(s: Session) -> None:
    """Publish this package to the Python package index (PyPI).

    Since Poetry is installed globally,
    skip the virtual environment creation.

    Always build the package before publishing.

    Requires the environment variable `POETRY_PYPI_TOKEN_PYPI`
    with the token for publishing the package to PyPI.
    """
    build(s)
    s.run("poetry", "publish", external=True)


@session(python=False)
def clean(s: Session) -> None:
    """Delete artifacts."""
    s.run("rm", "-rv", "dist", "docs/_dist")
