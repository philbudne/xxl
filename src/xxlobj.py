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

from typing import Any, List, NoReturn, Optional, Union

# XXL:
import classes
import const
import vmx

################################################################
# functions

STR = (str, bytes)              # Python3

def isstr(x: Any) -> bool:      # XXX TEMP
    """
    return true if `x` is a Python string type
    """
    return isinstance(x, STR)

################ debug:

@classes.pyfunc
def xxl_break(x: Any = None) -> classes.CObject:
    """
    break to python debugger to debug VM
    argument (if any) available as `x`
    """
    breakpoint()
    return classes.null_value

@classes.pyvmfunc
def xxl_backtrace(vm: vmx.VM) -> classes.CObject:
    """
    print VM backtrace to stderr
    """
    vm.backtrace()
    return classes.null_value

################

@classes.pyfunc
def xxl_uerror(msg: classes.CObject) -> NoReturn:
    raise classes.UError(msg)

################

XXL_LIB_PATH = os.getenv('XXL_LIB_PATH', const.XXL_LIB_PATH)\
                 .split(os.path.pathsep)

DEBUG_LIB_PATH = False

if DEBUG_LIB_PATH:
    print('XXL_LIB_PATH', XXL_LIB_PATH)

def find_in_lib_path(fname: str, suffixes: List[str] = []) -> str:
    def trydir(dir: Optional[str]) -> Optional[str]:
        if dir:
            path = os.path.join(dir,fname)
        else:
            path = fname
        if DEBUG_LIB_PATH:
            print('try', path)
        if os.path.exists(path):
            if DEBUG_LIB_PATH:
                print(' found', path)
            return path
        for suffix in suffixes:
            p2 = path + suffix
            if DEBUG_LIB_PATH:
                print('try', p2)
            if os.path.exists(p2):
                if DEBUG_LIB_PATH:
                    print(' found', p2)
                return p2
        return None

    p = trydir(None)
    if p:
        return p
    for dir in XXL_LIB_PATH:
        p = trydir(dir)
        if p:
            return p

    return fname                # fail on open attempt

@classes.pyfunc
def xxl__find_in_lib_path(fname: classes.CObject,
                          suffixes: Optional[classes.CObject] = None) -> classes.CObject:
    """
    return full path of file in current dir, or in XXL_LIB_PATH
    """
    if suffixes:
        suff2 = [x.getvalue() for x in suffixes.getvalue()] # XXX unwrap?
    else:
        suff2 = []
    return classes.mkstr(find_in_lib_path(fname.getvalue(), suff2))

################

DEBUG_IMPORT = False

@classes.pyfunc
def xxl__import(filename: classes.CObject) -> classes.CObject:
    """
    worker function for __xxl.import()
    (defined in bootstrap.xxl)
    """
    fname = filename.getvalue() # XXX getstr???
    if DEBUG_IMPORT:
        print("xxl__import", fname, file=sys.stderr)

    # returns (mod,boot) tuple:
    mod_boot = classes.new_module(fname=fname)
    if DEBUG_IMPORT:
        print("mod_boot", mod_boot, file=sys.stderr)

    return classes.wrap(mod_boot) # turns 2-tuple into List

################

# PLB: wrote a native replacement, but it's slooooow
import jslex

@classes.pyfunc
def xxl__tokenizer(filename: classes.CObject,
                   prefix: classes.CObject,
                   suffix: classes.CObject) -> classes.CObject:
    """
    returns a token generator:
    returns Objects, and then null
    """
    fnstr = filename.getvalue() # getstr()?
    pstr = prefix.getvalue()    # getstr()?
    sstr = suffix.getvalue()    # getstr()?
    if fnstr == '-':
        f = sys.stdin
        print("XXL/0")
        print("type a complete statement, or an expression terminated with ';'")
        interactive = True
    else:
        # encoding= needed for pypy3 7.3.1 (python 3.6)
        f = open(fnstr, encoding="utf8")
        interactive = False
    tokenizer = jslex.Tokenizer(f, pstr, sstr, interactive)
    # XXX wrap in a PyObject (create token as namedtuple, return as list?)

    @classes.pyfunc
    def next() -> classes.CObject:
        t = tokenizer.next()    # jslex.Token object
        if not t:
            return classes.null_value
        where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
        if t.type_ == 'number':
            v = classes.mknumber(t.value)
        else:
            v = classes.mkstr(t.value)
        tok = classes._mkobj({ # XXX create a Token
            'type': classes.mkstr(t.type_),
            'value': v,
            'where': classes.mkstr(where)
        })
        if t.msg:
            tok.setprop('msg', classes.mkstr(t.msg))
        return tok

    @classes.pyfunc
    def pointer(line: classes.CObject, pos: classes.CObject) -> classes.CObject:
        tokenizer.pointer(line.getvalue(), pos.getvalue()) # XXX getint
        return classes.null_value

    @classes.pyfunc
    def reset_prompt() -> classes.CObject:
        tokenizer.reset_prompt()
        return classes.null_value

    @classes.pyfunc
    def reset_tokenizer() -> classes.CObject:
        tokenizer.reset()
        return classes.null_value

    return classes.wrap([next, reset_prompt, pointer,
                         tokenizer.s.interactive, reset_tokenizer])

################

@classes.pyfunc
def xxl_exit(status: Optional[classes.CObject] = None) -> NoReturn:
    """
    Exit the interpreter.
    `status` defaults to zero.
    """
    xstatus: Union[str, int]
    if status is None:
        xstatus = 0
    else:
        try:
            xstatus = status.getvalue()
        except:
            xstatus = repr(status)
    sys.exit(xstatus)

################

@classes.pyfunc
def xxl__tree(t: classes.CObject) -> classes.CObject:
    """
    format JSON (returns Str) from AST of Symbols
    """
    t2 = obj2python_json(t)     # strip down to Python data structures
    return classes.mkstr(json.dumps(t2, indent=1))

################

# NOTE: used to do string concatenation rather than list building.
#       not clear that on average this is any better

def format_instr(instr: List[Any], indent: str = '') -> List[str]:
    """
    helper for xxl_vtree
    format one instruction (Python list)
    returns list of strings to concatenate
    """
    op = instr[1]
    if op not in vmx.INST2CODE:
        return [indent, json.dumps(instr)]

    # here to handle "close" and "bccall" (instr[2] is a code list)
    nindent = indent + " "
    ret = [indent, '["', instr[0], '", "', op, '",\n', nindent]
    ret.extend(format_code(instr[2], nindent))
    if op == "close" and len(instr) >= 4 and instr[3]: # now with doc string!!
        ret.append(',\n')
        ret.append(nindent)
        ret.append(json.dumps(instr[3])) # doc string
    ret.append(']')
    return ret

def format_code(code: List[Any], indent: str = '') -> List[str]:
    """
    helper for xxl_vtree
    takes Python list of instructions (Python lists)
    returns list of strings to concatenate
    """
    ret = [indent, "["]
    sep = ',\n' + indent + ' '
    ret.extend(format_instr(code[0]))
    for inst in code[1:]:
        ret.append(sep)
        ret.extend(format_instr(inst, indent))
    ret.append("]")
    return ret

JCode = List[str]
def trim_where(code: JCode, fname: str) -> None:
    """
    helper for xxl_vtree, assemble
    `code` is Python list of lists: ***MODIFIED IN PLACE!!!***
    trim `fname` from all Python instruction list "where" fields
    """
    if not fname:
        return
    fnamelen = len(fname) + 1   # remove "fname:"
    def helper(c: JCode) -> None:
        for instr in c:
            if instr[0].startswith(fname):
                instr[0] = instr[0][fnamelen:]
            if instr[1] in vmx.INST2CODE:
                helper(instr[2])
    helper(code)

################

@classes.pyfunc
def xxl__vtree(t: classes.CObject, fname: classes.CObject = classes.null_value) -> classes.CObject:
    """
    pretty print a VM code tree (List of List) `t`; returns Str
    """
    t2 = obj2python_json(t)     # convert to list of list of str

    if fname and fname is not classes.null_value:
        fn = fname.getvalue()
        trim_where(t2, fn)

    return classes.mkstr(''.join(format_code(t2)))

# used in:
# __xxl.tree (above) XXX replace with a Symbol.json method??
# __xxl.vtree (above)
# ModInfo.assemble (via vmx.assemble)
def obj2python_json(x: classes.CObject) -> Any:
    """
    take AST (tree of parser Symbols) or List of VMCode (Lists)
    return as Python list of lists
    *NOT* a general purpose JSON converter!!!
    """

    value_classes = [classes.Number, classes.Str, classes.Bool, classes.Null]
    iterable_classes = [classes.List]
    def clean1(x: classes.CObject) -> Any:
        """
        worker function
        """
        if classes.instance_of(x, value_classes):
            return x.getvalue()

        if classes.instance_of(x, iterable_classes):
            return [clean1(z) for z in x.getvalue()]

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
def xxl_pyimport(module: classes.CObject) -> classes.CObject:
    m = importlib.import_module(module.getvalue()) # XXX getstr?
    return classes.wrap(m)         # make PyObject

################################################################

def create_xxl_class(argv: List[str], parser_vmx: str) -> None:
    XXLObject = classes.defclass(classes.Class, 'XXLObject', [classes.Object],
                                 doc="Class for __xxl object")

    # NOTE! Everything a static method (evolved from simple object)
    # (unlikely that anything NEEDS access to the module local __xxl object)

    XXLObject.setprop('uerror', xxl_uerror) # fatal error w/ backtrace

    # debug functions (TEMP?!)
    XXLObject.setprop('break', xxl_break) # break to PDB
    XXLObject.setprop('backtrace', xxl_backtrace) # output backtrace to stderr

    # command line args, and exit:
    XXLObject.setprop('argv', classes.wrap(argv)) # move to ModInfo??
    XXLObject.setprop('exit', xxl_exit)            # move to ModInfo??

    # for parser & bootstrap:
    XXLObject.setprop('parser_vmx', classes.mkstr(parser_vmx))
    # private, subject to change:
    XXLObject.setprop('_tokenizer', xxl__tokenizer) # creates token generator
    XXLObject.setprop('_tree', xxl__tree)
    XXLObject.setprop('_vtree', xxl__vtree)
    XXLObject.setprop('_find_in_lib_path', xxl__find_in_lib_path)

    # external modules:
    XXLObject.setprop('_import', xxl__import) # import source module (helper)
    XXLObject.setprop('pyimport', xxl_pyimport) # import Python module
