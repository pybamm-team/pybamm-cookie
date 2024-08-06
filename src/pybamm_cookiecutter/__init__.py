"""
Copyright (c) 2023 The PyBaMM Team. All rights reserved.

pybamm-cookiecutter: A template for creating battery modeling projects based on PyBaMM
"""
from __future__ import annotations

from pybamm_cookiecutter._version import version as __version__
from pybamm_cookiecutter.cli import pybamm_cookiecutter_cli

__all__ : list[str] = [
    "__version__",
    "pybamm_cookiecutter_cli",
]
