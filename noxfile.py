"""Automate everything everywhere all at once."""
import tempfile

from nox import Session, options, session

options.stop_on_first_error = True

python_versions = ["3.11", "3.10", "3.9", "3.8"]


@session(python=python_versions)
def docs(s: Session) -> None:
    """Build the docs."""
    args = s.posargs or ["-aWTE", "docs", "docs/public"]

    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            "docs",
            "--output",
            f"{requirements.name}",
            external=True,
        )
        s.install(".", "sphinx", "python-dotenv")
    s.run("sphinx-build", *args)


@session
def fmt(s: Session) -> None:
    """Format the code with black and ruff."""
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            "lint",
            "--output",
            f"{requirements.name}",
            external=True,
        )
        s.install(".", "black", "ruff")
    s.run("ruff", "check", ".", "--select", "I", "--fix")
    s.run("black", ".")


@session
def lint(s: Session) -> None:
    """Lint the code with ruff."""
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            "lint",
            "--output",
            f"{requirements.name}",
            external=True,
        )
        s.install(".", "ruff")
    s.run("ruff", "check", ".")


@session(python=python_versions)
def test(s: Session) -> None:
    """Run unit tests."""
    args = s.posargs or ["--cov"]
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            "dev",
            "--output",
            f"{requirements.name}",
            external=True,
        )
        s.install(".", "pytest", "beautifulsoup4", "pytest-cov")
    s.run("pytest", *args)


@session(python=python_versions)
def typecheck(s: Session) -> None:
    """Typecheck."""
    with tempfile.NamedTemporaryFile() as requirements:
        s.run(
            "poetry",
            "export",
            "--only",
            "dev",
            "--output",
            f"{requirements.name}",
            external=True,
        )
        s.install(".", "mypy", "pytest", "nox", "bs4", "types-beautifulsoup4")
    s.run("mypy", ".", "--exclude", "docs")
