# Copyright © 2021 Philip L. Budne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
*runtime* scope management
(the remains of terp.py)
"""

from typing import Dict, Optional

import classes                  # CContinuation, UError
import frame

VarsDict = Dict[str, classes.CObject]

class Scope:
    """
    runtime scope.
    currently invisible (or at least opaque)
    """
    def __init__(self, parent: Optional["Scope"] = None) -> None:
        self.parent = parent
        self.vars: VarsDict = {}

    def new_scope(self) -> "Scope":
        """
        create a scope using current scope as parent
        """
        return Scope(self)

    def func_scope(self, fp: frame.Frame) -> "Scope":
        s = Scope(self)
        s.defvar('return', classes.CContinuation(fp))
        return s

    def labeled_scope(self, fp: frame.Frame, name: str) -> "Scope": # Closure with leave label
        s = Scope(self)
        s.defvar(name, classes.CContinuation(fp))
        return s

    def defvar(self, var: str, value: classes.CObject) -> None:
        """
        `var` is Python string
        `value` is CObject
        """
        # duplicate var is fatal in compiler
        self.vars[var] = value

    # XXX the compiler could tell us how far up the ("static") scope chain
    # the variable lives (and could assign numeric slot ids for variable
    # lookup to avoid dict)
    def lookup(self, name: str) -> classes.CObject:
        s: Optional[Scope] = self
        while s:
            if name in s.vars:
                return s.vars[name]
            s = s.parent
        raise classes.UError("Unknown variable %s" % name) # SNH

    # see note above "lookup" (compiler could tell us stuff)
    def store(self, name: str, val: classes.CObject) -> classes.CObject:
        """
        name: Python string
        val: CObject
        """
        s: Optional[Scope] = self
        while s:
            if name in s.vars:
                s.vars[name] = val
                return val
            s = s.parent
        raise classes.UError("Unknown variable %s" % name)

    def get_vars(self) -> VarsDict:  # UGH! used by new_module
        return self.vars
