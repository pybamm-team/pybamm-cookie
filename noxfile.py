import nox
from pathlib import Path
import os

# Options to modify nox behaviour
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_existing_virtualenvs = True

VENV_DIR = Path("./venv").resolve()

@nox.session(name="docs")
def build_docs(session: nox.Session) -> None:
    """Build the documentation and load it in a browser tab, rebuilding on changes."""
    envbindir = session.bin
    session.install("-e", ".[docs]")
    session.chdir("docs/")
    # For local development
    if session.interactive:
        session.run(
            "sphinx-autobuild",
            "-j",
            "auto",
            "--open-browser",
            "-qT",
            ".",
            f"{envbindir}/../tmp/html",
        )
    # For CI testing if documentation builds
    else:
        session.run(
            "sphinx-build",
            "-b",
            "html",
            "-W",
            "--keep-going",
            ".",
            f"{envbindir}/../tmp/html",
        )

@nox.session(name="test-generation")
def run_template_generation(session):
    """Run the tests for testing template generation"""
    session.install("setuptools", silent=False)
    session.install("-e", ".[dev]", silent=False)
    session.run("pytest", "tests")

@nox.session(name="coverage")
def run_coverage(session):
    """Run the coverage tests and generate an XML report."""
    session.install("setuptools", silent=False)
    session.install("coverage", silent=False)
    session.install("-e", ".[all,dev,jax]", silent=False)
    session.run("pytest", "--cov=src/pybamm_cookiecutter", "--cov-report=xml", "tests/")

@nox.session(name="dev")
def set_dev(session):
    """Install pybamm-cookiecutter in editable mode"""
    session.install("virtualenv")
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)
    python = os.fsdecode(VENV_DIR.joinpath("bin/python"))
    session.run(python, "-m", "pip", "install", "-e", ".[dev]")
