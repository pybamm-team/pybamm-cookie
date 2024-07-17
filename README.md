# pybamm-cookiecutter

<!-- TODO: configure badges -->

<!-- [![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussions][github-discussions-badge]][github-discussions-link]

[actions-badge]:            https://github.com/pybamm-team/pybamm-cookiecutter/workflows/CI/badge.svg
[actions-link]:             https://github.com/pybamm-team/pybamm-cookiecutter/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/pybamm-cookiecutter
[conda-link]:               https://github.com/conda-forge/pybamm-cookiecutter-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/pybamm-team/pybamm-cookiecutter/discussions
[pypi-link]:                https://pypi.org/project/pybamm-cookiecutter/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/pybamm-cookiecutter
[pypi-version]:             https://img.shields.io/pypi/v/pybamm-cookiecutter
[rtd-badge]:                https://readthedocs.org/projects/pybamm-cookiecutter/badge/?version=latest
[rtd-link]:                 https://pybamm-cookiecutter.readthedocs.io/en/latest/?badge=latest -->

<!-- SPHINX-START -->
[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](http://numfocus.org)

This repository contains a `cookiecutter` template for battery modeling projects using PyBaMM, released under the [BSD-3-Clause license](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/LICENSE). Currently under active development.

## 📄 Using `pybamm-cookiecutter`

### Generating projects with `pybamm-cookiecutter`

This template is not on PyPI yet, so it cannot be installed through `pip` until the first release. Meanwhile, it can be used by cloning this repository and using `cookiecutter` to generate a project with this template.

To use pybamm-cookiecutter template, first clone this repository on your local machine.
```bash
git clone https://github.com/pybamm-team/pybamm-cookiecutter.git
```
Create a temporary virtual environment inside the reposiory and activate it.
```bash
python3 -m venv venv
source venv/bin/activate
```
Install cookiecutter and generate the project using the pybamm-cookiecutter template by moving outside the parent pybamm-cookiecutter directory.
```bash
pip install cookiecutter
cookiecutter pybamm-cookiecutter/
```

Cookiecutter will prompt you with various configurations and you may choose the ones that suit your use case.

**Note**: If you created a repository using this template within GitHub and cloned it locally, you can skip the next step.

Once the project is generated through cookiecutter, initialise `git` by executing `git init` inside your project directory.


### Installing the `pybamm-cookiecutter` project

This is our version of the project generated using the cookiecutter template. There are two ways to install this project, either through `nox` or `pip`. `nox` uses `uv pip` or `pip` internally, and in this case creates a virtual environment for you to activate.
To install, navigate to the root directory of this repository and execute either of these commands:

`nox -s dev`
or
`pip install -e .[dev]`

To check if the project was successfully installed, import the project inside Python.

```python
import pybamm_cookiecutter

pybamm_cookiecutter._version.version
```

## 🛠️ Contributing to `pybamm-cookiecutter`

If you'd like to help us develop `pybamm-cookiecutter` by improving the template's features, writing documentation, or fixing embarrassing bugs, please have a look at these [guidelines](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/CONTRIBUTING.md).

## 📫 Get in touch

For any questions, comments, suggestions or bug reports, please see the
[contact page](https://www.pybamm.org/community).

## 📃 License

`pybamm-cookiecutter` is fully open source. For more information about its license, see [LICENSE](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/LICENSE).
<!-- SPHINX-END -->
