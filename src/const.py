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

# object properties
CLASS = '__class'               # Class instance

# Class properties
NAME = 'name'                   # String
METHODS = '__methods'           # Dict
BINOPS = '__binops'             # Dict
UNOPS = '__unops'               # Dict
LHSOPS = '__lhsops'             # Dict
SUPERS = '__supers'             # List of Class instances

# map Class.new argument dict keys to internal property names
CLASS_PROPS = {
    'name': NAME,
    'methods': METHODS,
    'binops': BINOPS,
    'unops': UNOPS,
    'lhsops': LHSOPS,
    'supers': SUPERS
}

# Class methods
NEW = 'new'
INIT = 'init'

# XXX Object methods (str/len/repr)?

# Class names
# XXX more here??
PYOBJECT = 'PyObject'
