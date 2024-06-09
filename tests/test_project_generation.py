import pybamm_cookiecutter as m
import pytest
from pytest_cookies.plugin import Cookies

def test_version() -> None:
    assert m.__version__

@pytest.fixture
def custom_template(tmpdir):
    """
    Generating a project using the template into a tempdir
    """
    template = tmpdir.ensure("cookiecutter-template", dir=True)
    template.join("cookiecutter.json").write('{"project_name": "pybamm_cookie"}')

    repo_dir = template.ensure("{{cookiecutter.project_name}}", dir=True)
    repo_dir.join("README.rst").write("{{cookiecutter.project_name}}")

    return template


def test_bake_custom_project(cookies: Cookies, custom_template):
    """
    Testing if the projects exists in the tempdir
    """
    result = cookies.bake(template=str(custom_template))

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "pybamm_cookie"
    assert result.project_path.is_dir()
