import importlib.metadata

project = "pybamm-cookie"
copyright = "2018-2023, The PyBaMM Team"
author = "Agriya Khetarpal"
version = release = importlib.metadata.version("pybamm_cookie")

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "pydata_sphinx_theme",
    "nbsphinx",
]

source_suffix = [".rst", ".md"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

html_theme = "pydata_sphinx_theme"

myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pybamm": ("https://docs.pybamm.org/en/latest/", None),
}

always_document_param_types = True
