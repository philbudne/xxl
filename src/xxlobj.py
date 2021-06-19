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
"__xxl" object
(was once named "System")
"""

import os                       # os.environ
import sys                      # sys.exit
import json
import importlib                # for pyimport

# XXL:
import classes
import scopes
import const
import vmx

XXLOBJ = '__xxl'               # maybe __xxl??

DEBUG_IMPORT = False

# should be used ONLY to create items to set up "__xxl" object
# ALSO used for:
#       tokenizer returns -- should return Token??
def __obj_create(props):        # TEMP??
    return classes._mkobj(props)

################################################################
# functions

STR = (str, bytes)              # Python3

def isstr(x):                   # XXX TEMP
    """
    return true if `x` is a Python string type
    """
    return isinstance(x, STR)

################ debug:

@classes.pyfunc
def xxl_break(x=None):
    """
    break to python debugger to debug VM
    argument (if any) available as `x`
    """
    breakpoint()
    return classes.null_value

@classes.pyvmfunc
def xxl_backtrace(vm):
    """
    print VM backtrace to stderr
    """
    vm.backtrace()
    return classes.null_value

################

@classes.pyfunc
def xxl_uerror(msg):
    raise classes.UError(msg)

################

# XXX replace with native code
# (need file I/O; use pyimport??)

@classes.pyfunc
def xxl_tokenizer(filename, prefix, suffix):
    """
    returns a token generator:
    returns Objects, and then null
    """
    import jslex
    # XXX assert(isinstance(filename, classes.CPObject))??
    if isstr(filename): # XXX XXX here from parser.xxl?
        print("XXX TEMP xxl_tokenizer got str", filename)
        fnstr = filename
    else:
        fnstr = filename.value # XXX getstr()?
    pstr = prefix.value    # XXX getstr()?
    sstr = suffix.value    # XXX getstr()?
    generator = jslex.tokenize(open(fnstr), pstr, sstr)

    # XXX use PyIterator???
    @classes.pyfunc
    def gen_wrapper(*args):
        """
        generator function, wrapper around jslex.tokenize
        """
        try:
            t = next(generator)
            if not t:
                return classes.null_value
            where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
            if t.type_ == 'number':
                v = classes.mknumber(t.value)
            else:
                v = classes.mkstr(t.value)
            return __obj_create({ # XXX create a Token
                'type': classes.mkstr(t.type_),
                'value': v,
                'where': classes.mkstr(where)
            })
        except StopIteration:
            return null

    return gen_wrapper          # returns PyFunc

################

@classes.pyfunc
def xxl_exit(value=0):
    # XXX check if VCObject?!
    sys.exit(value.value)       # XXX to_int??

################

@classes.pyfunc
def xxl_tree(t):
    """
    format JSON (returns Str) from AST of Symbols
    """
    t2 = obj2python_json(t)     # strip down to Python data structures
    return classes.mkstr(json.dumps(t2, indent=1))

################

def format_instr(instr, indent=''):
    """
    helper for xxl_vtree
    format one instruction (Python list)
    """
    op = instr[1]
    if op not in vmx.INST2CODE:
        return indent + json.dumps(instr)

    # here to handle "close" and "bccall" (instr[2] is a code list)
    nindent = indent + " "
    if op == "close" and len(instr) >= 4 and instr[3]: # now with doc string!!
        return ('%s["%s", "%s",\n%s%s,\n%s%s]' %
                (indent, instr[0], op,
                 nindent, format_code(instr[2], nindent),
                 nindent, json.dumps(instr[3])))
    else:
        return ('%s["%s", "%s",\n%s%s]' % \
                (indent, instr[0], op,
                 nindent, format_code(instr[2], nindent)))

def format_code(code, indent=''):
    """
    helper for xxl_vtree
    takes Python list of instructions (Python lists)
    """
    sep = ",\n" + indent + " "
    return (indent + "[" + format_instr(code[0]) + sep + # first line
            sep.join([format_instr(inst, indent) for inst in code[1:]]) +
            "]")

def trim_where(code, fname):
    """
    helper for xxl_vtree, assemble
    `code` is Python list of lists: MODIFIED IN PLACE!!!
    trim `fname` from all Python instruction list "where" fields
    """
    if not fname:
        return
    fnamelen = len(fname) + 1   # remove "fname:"
    def helper(c):
        for instr in c:
            if instr[0].startswith(fname):
                instr[0] = instr[0][fnamelen:]
            if instr[1] in vmx.INST2CODE:
                helper(instr[2])
    helper(code)

@classes.pyfunc
def xxl_vtree(t, fname=classes.null_value):
    """
    pretty print a VM code tree (List of List) `t`; returns Str
    """
    t2 = obj2python_json(t)     # convert to list of list of str

    if fname and fname is not classes.null_value:
        fn = fname.value        # getstr?
        trim_where(t2, fn)

    return classes.mkstr(format_code(t2))

# used in:
# __xxl.tree (above) XXX replace with a Symbol.json method??
# __xxl.vtree (above)
# ModInfo.assemble (via vmx.assemble)
def obj2python_json(x):
    """
    take AST (tree of parser Symbols) or List of VMCode (Lists)
    return as Python list of lists
    *NOT* a general purpose JSON converter!!!
    """

    value_classes = [classes.Number, classes.Str, classes.Bool, classes.Null]
    iterable_classes = [classes.List]
    def clean1(x):
        """
        worker function
        """
        if classes.instance_of(x, value_classes):
            return x.value

        if classes.instance_of(x, iterable_classes):
            return [clean1(z) for z in x.value]

        # NOTE!! Does not handle Dict!!!

        # assume here with AST "Symbol" node; turn into JSON list
        r = []
        print(x)
        for attr in ['where', 'arity', 'value']:
            r.append(clean1(x.getprop(attr)))
        for attr in ['first', 'second', 'third']:
            if attr not in x.props:
                break
            r.append(clean1(x.getprop(attr)))
        return r

    return clean1(x)

################ "pyimport" returns a PyObject wrapper around a Python module

@classes.pyfunc
def xxl_pyimport(module):
    m = importlib.import_module(module.value) # XXX getstr?
    return classes.wrap(m)         # make PyObject

################

DEBUG_IMPORT = False

@classes.pyfunc
def xxl__import(filename):
    """
    worker function for __xxl.import()
    (defined in bootstrap.xxl)
    """
    fname = filename.value      # XXX getstr???
    if DEBUG_IMPORT:
        print("xxl__import", fname, file=sys.stderr)

    # returns (mod,boot) tuple:
    mod_boot = classes.new_module(fname=fname)
    if DEBUG_IMPORT:
        print("mod_boot", mod_boot, file=sys.stderr)

    return classes.wrap(mod_boot) # turns into List

################################################################

# called only from classes.new_module: create XXLOBJ Object
# XXX move to internal "xxl" module??
def create_xxl_object(iscope, argv):
    xxl_obj = __obj_create({})
    iscope.defvar(XXLOBJ, xxl_obj)

    xxl_obj.setprop('uerror', xxl_uerror) # fatal error w/ backtrace

    # debug functions (TEMP?!)
    xxl_obj.setprop('break', xxl_break) # break to PDB
    xxl_obj.setprop('backtrace', xxl_backtrace) # output backtrace to stderr

    # command line args, and exit:
    xxl_obj.setprop('argv',  classes.wrap(argv)) # move to ModInfo??
    xxl_obj.setprop('exit', xxl_exit)            # move to ModInfo??

    # functions for parser & bootstrap:
    xxl_obj.setprop('tokenizer', xxl_tokenizer) # TEMP creates token generator
    xxl_obj.setprop('tree', xxl_tree) # TEMP!!!
    xxl_obj.setprop('vtree', xxl_vtree) # TEMP!!!

    # external modules:
    xxl_obj.setprop('_import', xxl__import) # import source module
    xxl_obj.setprop('pyimport', xxl_pyimport) # import Python module

    return xxl_obj