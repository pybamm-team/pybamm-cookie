"""
Copyright (c) {{ cookiecutter.__year }} {{ cookiecutter.full_name }}. All rights reserved.

{{ cookiecutter.project_name }}: {{ cookiecutter.project_short_description }}
"""
{%- if cookiecutter.mypy %}
from __future__ import annotations
{%- endif %}

from ._version import version as __version__
{# keep this line here for newline #}
{%- if cookiecutter.mypy %}
__all__: tuple[str] = ("__version__",)
{%- else %}
__all__ = ("__version__",)
{%- endif %}
