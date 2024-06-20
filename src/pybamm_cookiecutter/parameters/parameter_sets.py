from __future__ import annotations

import importlib.metadata
import sys
import textwrap
import warnings
from collections.abc import Mapping
from typing import Callable


class ParameterSets(Mapping):
    """
    Dict-like interface for accessing parameter sets through entry points in cookiecutter template.
    Access via :py:data:`pybamm_cookiecutter.parameter_sets`

    Examples
    --------
    Listing available parameter sets:


        >>> import pybamm_cookiecutter
        >>> list(pybamm_cookiecutter.parameter_sets)
        ['Chen2020', ...]

    Get the docstring for a parameter set:


        >>> print(pybamm_cookiecutter.parameter_sets.get_docstring("Ai2020"))
        <BLANKLINE>
        Parameters for the Enertech cell (Ai2020), from the papers :footcite:t:`Ai2019`,
        :footcite:t:`rieger2016new` and references therein.
        ...

    See also: :ref:`adding-parameter-sets`

    """

    def __init__(self):
        # Dict of entry points for parameter sets, lazily load entry points as
        self.__all_parameter_sets = dict()
        for entry_point in self.get_entries("cookie_parameter_sets"):
            self.__all_parameter_sets[entry_point.name] = entry_point

    @staticmethod
    def get_entries(group_name):
        # Wrapper for the importlib version logic
        if sys.version_info < (3, 10):  # pragma: no cover
            return importlib.metadata.entry_points()[group_name]
        else:
            return importlib.metadata.entry_points(group=group_name)

    def __new__(cls):
        """Ensure only one instance of ParameterSets exists"""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __getitem__(self, key) -> dict:
        return self.__load_entry_point__(key)()

    def __load_entry_point__(self, key) -> Callable:
        """Check that ``key`` is a registered ``cookie_parameter_sets``,
        and return the entry point for the parameter set, loading it needed.
        """
        if key not in self.__all_parameter_sets:
            raise KeyError(f"Unknown parameter set: {key}")
        ps = self.__all_parameter_sets[key]
        try:
            ps = self.__all_parameter_sets[key] = ps.load()
        except AttributeError:
            pass
        return ps

    def __iter__(self):
        return self.__all_parameter_sets.__iter__()

    def __len__(self) -> int:
        return len(self.__all_parameter_sets)

    def get_docstring(self, key):
        """Return the docstring for the ``key`` parameter set"""
        return textwrap.dedent(self.__load_entry_point__(key).__doc__)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError as error:
            # For backwards compatibility, parameter sets that used to be defined in
            # this file now return the name as a string, which will load the same
            # parameter set as before when passed to `ParameterValues`
            if name in self:
                msg = (
                    f"Parameter sets should be called directly by their name ({name}), "
                    f"instead of via pybamm_cookiecutter.parameter_sets (pybamm_cookiecutter.parameter_sets.{name})."
                )
                warnings.warn(msg, DeprecationWarning, stacklevel=2)
                return name
            raise error

#: Singleton Instance of :class:ParameterSets """
parameter_sets = ParameterSets()
