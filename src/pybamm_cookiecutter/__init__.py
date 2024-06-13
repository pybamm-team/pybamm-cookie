"""
Copyright (c) 2023 The PyBaMM Team. All rights reserved.

pybamm-cookiecutter: A template for creating battery modeling projects based on PyBaMM
"""
from __future__ import annotations

import pybamm

from ._version import version as __version__

__all__ : list[str] = [
    "__version__",
    "pybamm",
]
