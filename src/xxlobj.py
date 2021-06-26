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

import os                       # os.getenv, os.path
import sys                      # sys.exit
import json
import importlib                # for pyimport

# XXL:
import classes
import scopes
import const
import vmx

XXLOBJ = '__xxl'

DEBUG_IMPORT = False

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

XXL_LIB_PATH = os.getenv('XXL_LIB_PATH',  const.XXL_LIB_PATH)\
                 .split(os.path.pathsep)

DEBUG_LIB_PATH = False

if DEBUG_LIB_PATH:
    print('XXL_LIB_PATH', XXL_LIB_PATH)

def find_in_lib_path(fname, suffixes=[]):
    def trydir(dir):
        if dir:
            path = os.path.join(dir,fname)
        else:
            path = fname
        if DEBUG_LIB_PATH:
            print('try', path)
        if os.path.exists(path):
            if DEBUG_LIB_PATH:
                print('found', path)
            return path
        for suffix in suffixes:
            p2 = path + suffix
            if DEBUG_LIB_PATH:
                print('try', p2)
            if os.path.exits(p2):
                if DEBUG_LIB_PATH:
                    print('found', p2)
                return p2
        return None

    p = trydir(None)
    for dir in XXL_LIB_PATH:
        p = trydir(dir)
        if p:
            return p

    return fname                # fail on open attempt

@classes.pyfunc
def xxl__find_in_lib_path(fname, suffixes=None):
    """
    return full path of file in current dir, or in XXL_LIB_PATH
    """
    if suffixes:
        suff2 = [x.value for x in suffixes.value] # XXX unwrap?
    else:
        suff2 = []
    return classes.mkstr(find_in_lib_path(fname.value, suff2))

################

# PLB: wrote a native replacement, but it's slooooow
import jslex

@classes.pyfunc
def xxl__tokenizer(filename, prefix, suffix):
    """
    returns a token generator:
    returns Objects, and then null
    """
    fnstr = filename.value # XXX getstr()?
    pstr = prefix.value    # XXX getstr()?
    sstr = suffix.value    # XXX getstr()?
    if fnstr == '-':
        f = sys.stdin
        print("XXL/0")
        interactive = True
    else:
        # encoding= needed for pypy3 7.3.1 (python 3.6)
        f = open(fnstr, encoding="utf8")
        interactive = False
    tokenizer = jslex.Tokenizer(f, pstr, sstr, interactive)
    # XXX wrap in a PyObject (create token as namedtuple, return as list?)

    @classes.pyfunc
    def next():
        t = tokenizer.next()
        if not t:
            return classes.null_value
        where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
        if t.type_ == 'number':
            v = classes.mknumber(t.value)
        else:
            v = classes.mkstr(t.value)
        return classes._mkobj({ # XXX create a Token
            'type': classes.mkstr(t.type_),
            'value': v,
            'where': classes.mkstr(where)
        })

    @classes.pyfunc
    def pointer(line, pos):
        tokenizer.pointer(line.value, pos.value) # XXX getint
        return classes.null_value

    @classes.pyfunc
    def reset_prompt():
        tokenizer.reset_prompt()
        return classes.null_value

    return classes.wrap([next, reset_prompt, pointer, tokenizer.s.interactive])

################

@classes.pyfunc
def xxl_exit(value=0):
    # XXX check if VCObject?!
    sys.exit(value.value)       # XXX to_int??

################

@classes.pyfunc
def xxl__tree(t):
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

################

@classes.pyfunc
def xxl__vtree(t, fname=classes.null_value):
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

    return classes.wrap(mod_boot) # turns 2-tuple into List

################################################################

# called only from classes.new_module: create XXLOBJ Object
# XXX move to internal "xxl" module??
def create_xxl_object(iscope, argv, parser_vmx):
    xxl_obj = classes._mkobj({}) # XXX
    iscope.defvar(XXLOBJ, xxl_obj)

    xxl_obj.setprop('uerror', xxl_uerror) # fatal error w/ backtrace

    # debug functions (TEMP?!)
    xxl_obj.setprop('break', xxl_break) # break to PDB
    xxl_obj.setprop('backtrace', xxl_backtrace) # output backtrace to stderr

    # command line args, and exit:
    xxl_obj.setprop('argv',  classes.wrap(argv)) # move to ModInfo??
    xxl_obj.setprop('exit', xxl_exit)            # move to ModInfo??

    # for parser & bootstrap:
    xxl_obj.setprop('parser_vmx', classes.mkstr(parser_vmx))
    # private, subject to change:
    xxl_obj.setprop('_tokenizer', xxl__tokenizer) # creates token generator
    xxl_obj.setprop('_tree', xxl__tree)
    xxl_obj.setprop('_vtree', xxl__vtree)
    xxl_obj.setprop('_find_in_lib_path', xxl__find_in_lib_path)

    # external modules:
    xxl_obj.setprop('_import', xxl__import) # import source module
    xxl_obj.setprop('pyimport', xxl_pyimport) # import Python module

    return xxl_obj
