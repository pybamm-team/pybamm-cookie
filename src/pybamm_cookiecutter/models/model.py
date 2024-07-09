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
from collections.abc import Mapping
from typing import Callable
import textwrap

class ModelEntryPoints(Mapping):

    def __init__(self):
        self._all_models = dict()
        for entry_point in self.get_entries("model_entry_points"):
            self._all_models[entry_point.name] = entry_point

    @staticmethod
    def get_entries(group_name):
        return importlib.metadata.entry_points(group=group_name)

    def __new__(cls):
        """Ensure only one instance"""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __getitem__(self, key) -> dict:
        return self._load_entry_point(key)()

    def _load_entry_point(self, key) -> Callable:
        """Check that ``key`` is a registered ``model_entry_points``,
        and return the entry point for the model, loading it needed.
        """
        if key not in self._all_models:
            raise KeyError(f"Unknown Model: {key}")
        model = self._all_models[key]
        try:
            model = self._all_models[key] = model.load()
        except AttributeError:
            pass
        return model

    def __iter__(self):
        return self._all_models.__iter__()

    def __len__(self) -> int:
        return len(self._all_models)

    def get_docstring(self, key):
        """Return the docstring for the ``key`` model"""
        return textwrap.dedent(self._load_entry_point(key).__doc__)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError as error:
              raise error

#: Singleton Instance of :class:ModelEntryPoints"""
model_instance = ModelEntryPoints()

def models(model:str):
    """
    Returns the loaded model object

    Parameters
    ----------
    model : str
        The model name or author name of the model mentioned at the model entry point.
    Returns
    -------
    pybamm.model
        Model object of the initialised model.
    """
    return model_instance[model]
