import pytest
import pybamm_cookiecutter
import importlib.util
import sys
from pathlib import Path

def test_entry_points():
    """Test if the entry points are loaded correctly."""

    entry_points = list(pybamm_cookiecutter.model_instance)
    models = Path("src/pybamm_cookiecutter/models/input/").glob("*.py")
    # Making a list Parameter sets in the parameters/input directory
    models = [x.stem for x in models]

    assert models == entry_points, "Entry points missing either in pyproject.toml or in the input directory"

def test_entry_point_load():
    """Testing if the values get loaded via parameter entry points and are equal when loaded through entry points"""
    # Loading parameter_sets through entry points
    model_instance = pybamm_cookiecutter.models("SPM")
    assert model_instance != None
