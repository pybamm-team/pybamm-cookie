"""
Copyright (c) {{ cookiecutter.__year }} {{ cookiecutter.full_name }}. All rights reserved.

{{ cookiecutter.project_name }}: {{ cookiecutter.project_short_description }}
"""
{%- if cookiecutter.mypy %}
from __future__ import annotations
{%- endif %}

{%- if cookiecutter.vcs %}
from ._version import version as __version__
{%- else %}
__version__ = "0.1.0"
{%- endif %}
import pybamm
from .entry_point import Model, parameter_sets, models
{# keep this line here for newline #}
{%- if cookiecutter.mypy %}
__all__: list[str] = [
{%- else %}
__all__ = [
{%- endif %}
    "__version__",
    "pybamm",
    "parameter_sets",
    "Model",
    "models",
]
