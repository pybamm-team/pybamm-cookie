import nox

# Options to modify nox behaviour
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_existing_virtualenvs = True

@nox.session(name="docs")
def build_docs(session: nox.Session) -> None:
    """Build the documentation and load it in a browser tab, rebuilding on changes."""
    envbindir = session.bin
    session.install("-e", ".[docs]")
    with session.chdir("docs/"):
        session.run(
            "sphinx-autobuild",
            "-j",
            "auto",
            "--open-browser",
            "-qT",
            ".",
            f"{envbindir}/../tmp/html",
        )

@nox.session(name="test-generation")
def run_template_generation(session):
    """Run the tests tests for testing template generation"""
    session.install("setuptools", silent=False)
    session.install("pytest", silent=False)
    session.install("pytest-cookies", silent=False)
    session.install("-e", ".", silent=False)
    session.run("pytest", "tests")
