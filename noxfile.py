"""Automate everything everywhere all at once."""
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
    deps = ["sphinx", "python-dotenv", "furo", "myst-parser"]
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
