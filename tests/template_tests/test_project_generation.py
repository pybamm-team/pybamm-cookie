import pybamm_cookie as m
import pytest
import os
import subprocess
import shutil

def test_version() -> None:
    assert m.__version__


def test_bake_project(copie): # codespell:ignore copie
    """
    Testing the template generation with default values
    """
    result = copie.copy() # codespell:ignore copie

    assert result.exit_code == 0, f"Exited with code {result.exit_code}, expected 0"
    assert result.exception is None, result.exception
    assert result.project_dir.is_dir(), f"Project directory {result.project_dir} not found"
    with open(result.project_dir / "pybamm-example-project" / "README.md") as f:
       assert f.readline() == "# pybamm-example-project\n", f"{f.readline()} is not the same as # pybamm-example-project\n"


def test_template_with_extra_answers(copie): # codespell:ignore copie
    """
    Testing the template generation with custom template and checking if the projects exists in the tmp_path
    """
    extra_context = {
        "project_name": "test-bake-project",
        "email": "pybamm@pybamm.org",
        "project_slug": "pybamm_cookie",
        "project_short_description": "This is an example pybamm-cookie template",
        "url": "pybamm.org",
    }
    result = copie.copy(extra_answers=extra_context) # codespell:ignore copie

    assert result.exit_code == 0, f"Exited with code {result.exit_code}, expected 0"
    assert result.exception is None, result.exception
    assert result.project_dir.is_dir(), f"Project directory {result.project_dir} not found"
    with open(result.project_dir / extra_context["project_name"] / "README.md") as f:
        assert f.readline() == f"# {extra_context['project_name']}\n", f"{f.readline()} is not the same as {extra_context['project_name']}\n"

def test_cli():
    """
    Testing if the CLI works and returns a successful exit code on execution
    """
    os.mkdir("testcli")
    return_code = subprocess.run(["pybamm-cookie", "--defaults"], cwd = "./testcli")
    shutil.rmtree("testcli")
    assert return_code
