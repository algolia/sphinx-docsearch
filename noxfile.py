"""Automate everything everywhere all at once.

Requires [Nox](https://nox.thea.codes/).

- Run `nox -ls` to list all sessions.
- Run `nox -s <NAME>` to run the session _`<NAME>`_.
- Run `nox -s docs -p 3.11 -- --live` to build the docs with live-reloading.
"""
import tempfile

from nox import Session, options, session

options.stop_on_first_error = True

python_versions = ["3.11", "3.10", "3.9", "3.8"]


def install_with_requirements(s: Session, group: str = "dev", *args: str) -> None:
    """Export from Poetry for a group."""
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            group,
            "--output",
            requirements.name,
            external=True,
        )
        s.install(*args)


@session(python=python_versions)
def docs(s: Session) -> None:
    """Build the docs."""
    args = ["-aWTE", "docs", "docs/public"]
    deps = [
        "sphinx",
        "python-dotenv",
        "furo",
        "myst-parser",
        "sphinx_rtd_theme",
        "sphinx_book_theme",
    ]
    sphinx_build = "sphinx-build"

    if "--live" in s.posargs:
        deps.append("sphinx-autobuild")
        sphinx_build = "sphinx-autobuild"
        s.posargs.remove("--live")

    if s.posargs:
        args = s.posargs + args

    install_with_requirements(s, "docs", ".", *deps)
    s.run(sphinx_build, *args)


@session
def fmt(s: Session) -> None:
    """Format the code with black and ruff."""
    deps = ["black", "ruff"]
    install_with_requirements(s, "lint", ".", *deps)
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("black", ".")


@session
def lint(s: Session) -> None:
    """Lint the code with ruff."""
    install_with_requirements(s, "lint", ".", "ruff")
    s.run("ruff", "check", ".")


@session(python=python_versions)
def tests(s: Session) -> None:
    """Run unit tests."""
    args = s.posargs or ["--cov"]
    deps = ["pytest", "pytest-cov", "beautifulsoup4"]
    install_with_requirements(s, "dev", ".", *deps)
    s.run("pytest", *args)


@session(python=["3.8", "3.11"])
def typecheck(s: Session) -> None:
    """Typecheck."""
    deps = ["mypy", "pytest", "nox", "bs4", "types-beautifulsoup4"]
    install_with_requirements(s, "dev", ".", *deps)
    s.run("mypy", ".", "--exclude", "docs")


@session(python=False)
def build(s: Session) -> None:
    """Build the packages using Poetry.

    Since Poetry is installed globally,
    skip the virtual environment creation.
    """
    s.run("poetry", "build", external=True)


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
    s.run("poetry", "publish", "--dry-run", external=True)


@session(python=False)
def clean(s: Session) -> None:
    """Delete artifacts."""
    s.run("rm", "-rv", "dist", "docs/public")
