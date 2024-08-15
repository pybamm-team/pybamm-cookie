"""
Copyright (c) 2024 The PyBaMM Team. All rights reserved.

pybamm-cookie: A template for creating battery modeling projects based on PyBaMM
"""
from __future__ import annotations

from pybamm_cookie.cli import pybamm_cookie_cli
from pybamm_cookie._version import __version__

__all__ : list[str] = [
    "__version__",
    "pybamm_cookie_cli",
]
