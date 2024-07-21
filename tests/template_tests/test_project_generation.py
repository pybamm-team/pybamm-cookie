import pybamm_cookiecutter as m
import pytest
from pytest_cookies.plugin import Cookies

def test_version() -> None:
    assert m.__version__

def test_bake_project(cookies: Cookies):
    """
    Testing the template generation with default values
    """
    result = cookies.bake()
    assert result.exit_code == 0, f"Exited with code {result.exit_code}, expected 0"
    assert result.exception is None, result.exception
    assert result.project_path.name == "pybamm_example_project"
    assert result.project_path.is_dir(), f"Project directory {result.project_path} not found"


def test_bake_custom_project(cookies: Cookies):
    """
    Testing the template generation with custom template and checking if the projects exists in the tmp_path
    """
    result = cookies.bake(extra_context={
        "author_full_name": "pybamm_user",
        "author_email": "pybamm@pybamm.org",
        "project_name": "pybamm_cookie",
        "project_slug": "example",
        "project_short_description": "This is an example pybamm cookiecutter template",
        "project_url": "pybamm.org",
        "project_version": "0.1.0",
        "documentation_engine": "sphinx(rst)",
    })

    assert result.exit_code == 0, f"Exited with code {result.exit_code}, expected 0"
    assert result.exception is None, result.exception
    assert result.project_path.name == "pybamm_cookie"
    assert result.project_path.is_dir(), f"Project directory {result.project_path} not found"
