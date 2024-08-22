# Contributing to `pybamm-cookie`

If you'd like to contribute to this project, please have a look at the [guidelines below](#workflow).

If you're already familiar with our workflow, maybe have a quick look at the [pre-commit checks](#pre-commit-checks) directly below.

## `pre-commit` checks

Before you commit any code, please perform the following checks:

- [All tests pass](#testing): `$ nox -s test-generation`
- [The documentation builds](#building-the-documentation): `$ nox -s docs`

### Installing and using pre-commit

`pybamm-cookie` uses a set of `pre-commit` hooks and the `pre-commit` bot to format and prettify the codebase. The hooks can be installed locally using -

```bash
pip install pre-commit
pre-commit install
```

This would run the checks every time a commit is created locally. The checks will only run on the files modified by that commit, but the checks can be triggered for all the files using -

```bash
pre-commit run --all-files
```

If you would like to skip the failing checks and push the code for further discussion, use the `--no-verify` option with `git commit`.

## Workflow

We use [Git](https://en.wikipedia.org/wiki/Git) and [GitHub](https://en.wikipedia.org/wiki/GitHub) to coordinate our work. When making any kind of update, we try to follow the procedure below.

### A. Before you begin

1. Create an [issue](https://guides.github.com/features/issues/) where new proposals can be discussed before any coding is done.
2. Create a [branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) of this repo (ideally on your own [fork](https://help.github.com/articles/fork-a-repo/)), where all changes will be made.
3. Download the source code onto your local system, by [cloning](https://help.github.com/articles/cloning-a-repository/) the repository (or your fork of the repository).
4. Use `nox -s dev` or `pip install -e .[dev]` to install `pybamm-cookie` in editable/development mode.
5. [Test](#testing) if your installation worked, using the test script: `nox -s test-generation` or `pytest`.

You now have everything you need to start making changes!

### B. Writing your code

6. This project is developed in [Python](https://www.python.org)), and uses the [copier](https://copier.readthedocs.io/) templating tool. For testing, we use [`pytest`](https://docs.pytest.org/en/).
7. Make sure to follow our [coding style guidelines](#coding-style-guidelines).
8. Commit your changes to your branch with [useful, descriptive commit messages](https://chris.beams.io/posts/git-commit/): Remember these are
   publicly visible and should still make sense a few months ahead in time.
   While developing, you can keep using the GitHub issue you're working on
   as a place for discussion.

### C. Merging your changes with `pybamm-cookie`

9. [Test your code!](#testing)
10. When you feel your code is finished, or at least warrants serious discussion, run the [pre-commit checks](#pre-commit-checks) and then create a [pull request](https://help.github.com/articles/about-pull-requests/) (PR) on [`pybamm-cookie`'s GitHub page](https://github.com/pybamm-team/pybamm-cookie).
11. Once a PR has been created, it will be reviewed by any member of the community. Changes might be suggested which you can make by simply adding new commits to the branch. When everything's finished, someone with the right GitHub permissions will merge your changes into pybamm-cookie main repository.


## Coding style guidelines

This project follows the [PEP8 recommendations](https://www.python.org/dev/peps/pep-0008/) for coding style. These are very common guidelines, and community tools have been developed to check how well projects implement them. We recommend using pre-commit hooks to check your code before committing it. See [installing and using pre-commit](#installing-and-using-pre-commit) section for more details.

### Ruff

We use [ruff](https://github.com/astral-sh/ruff) to check our PEP8 adherence. To try this on your system, navigate to the parent pybamm-cookie directory in a console and type

```bash
python -m pip install pre-commit
pre-commit run ruff
```

Ruff is configured inside the file `pre-commit-config.yaml`, allowing us to ignore some errors. If you think some rules should be added or removed, please submit an [issue](https://github.com/pybamm-team/pybamm-cookie/issues).

If you performed the `pre-commit install` step above, your code changes will be checked against Ruff automatically when you try to commit them (see [Pre-commit checks](#pre-commit-checks)).


## Testing

All code requires testing. We use the [Pytest](https://docs.pytest.org/en/) package for our tests. (These tests typically just check that the code runs without error, and so, are more _debugging_ than _testing_ in a strict sense. Nevertheless, they are very useful to have!).

If you have `nox` installed, to run tests for the template, type

```bash
nox -s template-tests
```

else, type

```bash
pytest tests/
```

To test a generated project, meaning a project generated out of `pybamm-cookie`, you can simply run
```bash
nox -s generated-project-tests
```

### Writing tests

Every new feature should have its own test. To create ones, have a look at the `test` directory and see if there's a test for a similar method. Copy-pasting this is a good way to start.

Next, add some simple (and speedy!) tests of your main features. If these run without exceptions, that's a good start! Next, check the output of your methods using any of these [assert methods](https://docs.pytest.org/en/stable/how-to/assert.html).


## Documentation

First and foremost, every method and every class should have a [docstring](https://www.python.org/dev/peps/pep-0257/) that describes in plain terms what it does, and what the expected input and output is.

These docstrings can be fairly simple, but can also make use of [reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html), a markup language designed specifically for writing [technical documentation](https://en.wikipedia.org/wiki/ReStructuredText).

Using [Sphinx](http://www.sphinx-doc.org/en/stable/) the documentation in `docs` can be converted to HTML, PDF, and other formats. In particular, we use it to generate the documentation on http://docs.pybamm.org/

### Building the documentation

To test and debug the documentation, it's best to build it locally. To do this, navigate to your pybamm-cookie directory in a console, and then type:

```
nox -s docs
```

And then visit the webpage served at `http://127.0.0.1:8000`. Each time a change to the documentation source is detected, the HTML is rebuilt and the browser automatically reloaded. In CI, the docs are built and tested using the `docs` session in the `noxfile.py` file with warnings turned into errors, to fail the build. The warnings can be removed or ignored by adding the appropriate warning identifier to the `suppress_warnings` list in `docs/conf.py`.

### Continuous Integration using GitHub Actions

Each change pushed to the `pybamm-cookie` GitHub repository will trigger the tests to be run, using [GitHub Actions](https://github.com/features/actions).

Tests are run for different operating systems, and for all Python versions officially supported by the `pybamm-cookie` template. If you open a pull request (PR), feedback is directly available on the corresponding page. If all tests pass, a green tick will be displayed next to the corresponding test run. If one or more test(s) fail, a red cross will be displayed instead.

More details can be obtained by clicking on a specific run.

Configuration files for various GitHub Actions workflows can be found in `.github/workflows/`.

### GitHub

GitHub does some magic with particular filenames. In particular:

- The first page people see when they go to [our GitHub page](https://github.com/pybamm-team/pybamm-cookie) displays the contents of [README.md](https://github.com/pybamm-team/pybamm-cookie/blob/main/README.md), which is written in the [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format. Some guidelines can be found [here](https://help.github.com/articles/about-readmes/).
- The license for using pybamm-cookie is stored in [LICENSE](https://github.com/pybamm-team/pybamm-cookie/blob/main/LICENSE.txt), and [automatically](https://help.github.com/articles/adding-a-license-to-a-repository/) linked to by GitHub.
- This file, [CONTRIBUTING.md](https://github.com/pybamm-team/pybamm-cookie/blob/main/CONTRIBUTING.md) is recognised as the document that lists the contribution guidelines and a link is [automatically](https://github.com/blog/1184-contributing-guidelines) displayed when new issues or pull requests are created.
