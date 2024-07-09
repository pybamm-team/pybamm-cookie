"""
This code is adopted from the PyBaMM project under the BSD-3-Clause

Copyright (c) 2018-2024, the PyBaMM team.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import importlib.metadata
import sys
import textwrap
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
        """Dict of entry points for parameter sets, lazily load entry points as"""
        self.__all_parameter_sets = dict()
        for entry_point in self.get_entries("cookie_parameter_sets"):
            self.__all_parameter_sets[entry_point.name] = entry_point

    @staticmethod
    def get_entries(group_name):
        """Wrapper for the importlib version logic"""
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
        return self._load_entry_point(key)()

    def _load_entry_point(self, key) -> Callable:
        """Check that ``key`` is a registered ``cookie_parameter_sets``,
        and return the entry point for the parameter set, loading it needed."""
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
        return textwrap.dedent(self._load_entry_point(key).__doc__)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError as error:
              raise error

#: Singleton Instance of :class:ParameterSets """
parameter_sets = ParameterSets()
