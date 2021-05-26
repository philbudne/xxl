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
"System" object
"""

import os                       # os.environ
import sys                      # sys.exit
import json

import classes
import scopes
import const
import vmx

SYSTEM = 'System'               # maybe __xxl??
SYS_TYPES = 'types'             # maybe top level __classes?
SYS_PARSER = 'parser'

# should be used ONLY to create items to set up "System" & System.types objects!
# can't use create_sys_type: which needs the System object!!!
# ALSO used for:
#       sys_import (returned module) -- should return Module??
#       tokenizer returns -- should return Token??
def __obj_create(props):        # TEMP??
    return classes._mkobj(props)

################################################################
# functions

try:
    STR = basestring            # Python2: unicode and str
except:
    STR = (str, bytes)          # Python3

def isstr(x):                   # XXX TEMP
    """
    return true if `x` is a Python string type
    """
    return isinstance(x, STR)

################ debug:

@classes.pyfunc
def sys_break(x=None):
    """
    break to python debugger to debug VM
    argument (if any) available as `x`
    """
    breakpoint()

################

# XXX replace with native code
# (need file I/O; use pyimport??)

@classes.pyvmfunc
def sys_tokenizer(vm, filename, prefix, suffix):
    """
    returns a token generator:
    returns Objects, and then null
    """
    import jslex
    # XXX assert(isinstance(filename, classes.CPObject))??
    if isstr(filename): # XXX XXX here from parser.xxl?
        print("XXX TEMP sys_tokenizer got str", filename)
        fnstr = filename
    else:
        fnstr = filename.value # XXX getstr()?
    pstr = prefix.value    # XXX getstr()?
    sstr = suffix.value    # XXX getstr()?
    generator = jslex.tokenize(open(fnstr), pstr, sstr)

    # XXX create general purpose PyIterator wrapper class??
    @classes.pyfunc
    def gen_wrapper(*args):
        """
        generator function, wrapper around jslex.tokenize
        """
        # find_sys_types doesn't like to return "null_value"
        # XXX just uses classes.null_value???
        null = vm.iscope.lookup(SYSTEM).getprop(SYS_TYPES).getprop('null')
        try:
            t = next(generator)
            if not t:
                return null
            where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
            return __obj_create({ # XXX create a Token
                'type': classes.mkstr(t.type_, vm.iscope),
                'value': classes.mkstr(t.value, vm.iscope),
                'where': classes.mkstr(where, vm.iscope)
            })
        except StopIteration:
            return null

    return gen_wrapper          # returns PyFunc

################

@classes.pyfunc
def sys_exit(value=0):
    # XXX check if VCObject?!
    sys.exit(value.value)       # XXX to_int??

################
# XXX should be a string() method!

@classes.pyvmfunc
def sys_tree(vm, t):
    """
    format JSON
    """
    t2 = obj2python_json(t)     # strip down to Python data structures
    return classes.mkstr(json.dumps(t2, indent=1), vm.iscope)

def format_instr(instr, indent=''):
    """
    format one instruction (Python list)
    """
    op = instr[1]
    if op not in ('close', 'bccall'):
        return indent + json.dumps(instr)

    # here to handle "close" and "bccall" (instr[2] is a new code list)
    nindent = indent + " "
    return ('%s["%s", "%s",\n%s%s]' % \
            (indent, instr[0], op,
             nindent, format_code(instr[2], nindent)))

def format_code(code, indent=''):
    """
    takes Python list of instructions (Python lists)
    """
    sep = ",\n" + indent + " "
    return (indent + "[" + format_instr(code[0]) + sep + # first line
            sep.join([format_instr(inst, indent) for inst in code[1:]]) +
            "]")

def trim_where(code, fname):
    """
    trim `fname` from all instruction list where fields
    `code` is Python list of lists: MODIFIED IN PLACE!!!
    """
    if not fname:
        return
    fnamelen = len(fname) + 1   # remove fname:
    def helper(c):
        for instr in c:
            if instr[0].startswith(fname):
                instr[0] = instr[0][fnamelen:]
            if instr[1] in ('close', 'bccall'):
                helper(instr[2])
    helper(code)

@classes.pyvmfunc
def sys_vtree(vm, t, fname=classes.null_value):
    """
    pretty print a VM code tree (returns Str)
    `t`: List of List
    """
    t2 = obj2python_json(t)     # convert to list of list of str

    if fname and fname is not classes.null_value:
        fn = fname.value        # getstr?
        trim_where(t2, fn)

    return classes.mkstr(format_code(t2), vm.iscope)

# used in System.tree (above), parse, parse_and_execute, System.assemble (below)
def obj2python_json(x):
    """
    take AST (tree of Objects) or List of VMCode (Lists)
    return as Python list of lists
    *NOT* a general purpose JSON converter!!!
    """

    # can't remember why;
    # parser ASTs may once have had cycles?
    memo = {}

    def clean1(x):
        """
        worker function
        """
        # XXX paranoia:
        if not isinstance(x, classes.CObject):
            return x

        ix = id(x)
        if ix in memo:
            return memo[ix]
        n = x.classname()       # OOF!
        if n == 'Null':
            return None
        if n in ('Str', 'Number', 'Bool'):
            return x.value
        if n == 'List':
            return [clean1(z) for z in x.value]

        # here to handle AST nodes:
        r = []
        for attr in ['where', 'arity', 'value']:
            r.append(clean1(x.getprop(attr)))
            for attr in ['first', 'second', 'third']:
                if attr not in x.props: # OUCH!!!
                    break
                r.append(clean1(x.getprop(attr)))

            memo[ix] = r
            return r

    return clean1(x)

################

@classes.pyvmfunc
def sys_assemble(vm, tree, srcfile):
    """
    `tree`: List of Lists of VM code
    `srcfile`: source of code
    returns Closure using caller's initial scope
        (XXX XXX XXX make this a Module method????)
    """
    # convert List of Lists to Python list of lists
    js = obj2python_json(tree)
    trim_where(js, srcfile.value) # XXX getstr?

    # convert into Python list of Instrs (scope for type name lookup):
    code = vmx.convert_instrs(js, vm.iscope, srcfile)

    # turn into Closure in module initial scope
    #   (any variables created are globals):
    return classes.CClosure(code, vm.iscope)

################ "pyimport" returns a PyObject wrapper around a Python module

@classes.pyvmfunc
def sys_pyimport(vm, module):
    import importlib
    m = importlib.import_module(module.value) # XXX getstr?
    return classes.wrap(m, vm.iscope)         # make PyObject

# XXX create an "auto-import" object? __python.sys == pyimport("sys")???

################

# used only by import_worker XXX inline?
# XXX take filename, save (as __file, or __module.file??)
# XXX keep Dict of modules by (file)name??  in System.modules???
def init_module(argv, main=False):
    """
    create namespace and System object (w/o parser)
    main: bool -- used to set __main__
    """
    scope = scopes.Scope(None)    # create scope for module
    sys = create_sys_object(scope, argv)
    classes.copy_types(scope, sys) # populate scope

    # put in System.main?? __module.main???
    scope.defvar('__main__', classes.mkbool(main))

    return scope                # XXX return Module object??

# called only from import_worker! XXX inline?
# requires initial scope with System.types set up.
def load_parser(scope, parser_vmx, filename=None, trace=False):
    """
    load parser from vmx file into scope's System.parser
    """
    sys_obj = scope.lookup(SYSTEM)
    m = import_worker(vmx_file=parser_vmx, main=False,
                      trace=trace, parser=False)
    # XXX check return

    # point System.parser at parser module
    sys_obj.setprop(SYS_PARSER, m)

    if filename:                # source file name, for bootstrap.vmx
        m.setprop('filename', classes.mkstr(filename, scope))

def breakpoint_if_debugging():
    #breakpoint()
    pass

################

@classes.pyfunc
def sys_import(filename):
    """
    user called System.import function
    `filename` is Str of name of source file to parse
    """
    # XXX check if already imported (or import in progress)
    #   lookup in System.modules[filename]????
    # XXX take filename w/o extension?????
    # XXX search for .vmx file?
    # XXX propogate trace from caller??
    mod = import_worker(src_file=filename.value) # XXX getstr???
    if mod is None:
        Exception("import failed")

    # XXX run __extensions__ on caller's initial scope? System object?
    # XXX take arg to bypass __extensions__
    return mod

# Worker function to implement "import" (where modules come from)
# used by: vmx.py (running src & vmx files)
#       sys_import (System.import function)
#       load_parser (called from here!)
# XXX returns Object (want Module)
def import_worker(src_file=None,
                  vmx_file=None,
                  main=False,
                  argv=[],
                  parser=True,
                  parser_vmx=None,
                  stats=False,
                  trace=False):
    """
    NOTE!!!! ALWAYS PASS ARGS BY NAME!!!
    Takes either `src_file` or `vmx_file` [XXX autodetect by filename?]
        XXX take bare name and try both .xxl and .vmx??
    `argv`: list of str for command line args
    bool `main` True when loading from command line
    bool `parser` to create System.parser (False to load parser.vmx)
    str `parser_vmx` name of file with parser VM code
    bool `stats` enable VM stats
    bool `trace` enable VM trace of user code
    """
    scope = init_module(argv, main=main) # XXX pass fname(s)?

    if parser:
        # NOTE!!! Calls this routine recursively, w/ parser=False & vmx_file
        # passes source file name in to set System.parser.filename
        load_parser(scope,
                    parser_vmx or os.environ.get('XXL_PARSER', 'parser.vmx'),
                    filename=src_file
        )

    vmx_files = ['bootstrap.vmx']
    if vmx_file:
        vmx_files.append(vmx_file)

    vm = vmx.VM(scope, stats=stats, trace=trace)
    try:
        for vf in vmx_files:
            # XXX handle Exception from load_vm_json?
            code = vmx.load_vm_json(vf, scope)
            vm.start(code, scope)
    except SystemExit:          # from os.exit
        raise
    except vmx.VMError as e:    # an internal error
        # NOTE: displays VM Instr
        sys.stderr.write("VM Error @ {}: {}\n".format(vm.ir, e))
        # XXX dump VM registers?
        vm.backtrace()
        breakpoint_if_debugging()
        sys.exit(1)
    except classes.UError as e:
        # NOTE: user error: just displays "where" and VM backtrace
        if vm.ir:
            sys.stderr.write("Error @ {}:{}: {}\n".format(
                vm.ir.fn, vm.ir.where, e))
        else:
            sys.stderr.write("Error @ ???: {}\n".format(e))
        vm.backtrace()
        breakpoint_if_debugging()
        sys.exit(1)
    # NOTE!! copies vars dict; not a live view!
    #   (System.types needs to be a copy)
    return __obj_create(scope.get_vars()) # XXX want Module

################################################################

# called only from init_module: create SYSTEM Object
def create_sys_object(iscope, argv):
    sys_obj = __obj_create({})
    iscope.defvar(SYSTEM, sys_obj)

    # create System.types object from sys_types
    # NOTE!!! copies sys_types dict entries
    #   so that each module has a private namespace!!!
    #   **BUT** the referenced Class Objects are all shared(?)!!!
    tt = __obj_create(classes.sys_types)
    sys_obj.setprop(SYS_TYPES, tt)         # XXX XXX top level __classes?

    # *** now safe to call "create_sys_type" and "wrap" ***

    # debug functions (TEMP?!)
    sys_obj.setprop('break', sys_break) # break to PDB

    # command line args, and exit:
    sys_obj.setprop('argv',  classes.wrap(argv, iscope))
    sys_obj.setprop('exit', sys_exit)

    # for parser:
    sys_obj.setprop('tokenizer', sys_tokenizer) # TEMP creates token generator
    sys_obj.setprop('tree', sys_tree) # TEMP!!!
    sys_obj.setprop('vtree', sys_vtree) # TEMP!!!
    sys_obj.setprop('assemble', sys_assemble) # move to Module?  __module??

    # external modules:
    sys_obj.setprop('import', sys_import) # import source module
    sys_obj.setprop('pyimport', sys_pyimport) # import Python module

    return sys_obj

################################################################

def find_sys_type(name, scope):
    """
    Lookup System.types.`name` in `scope`
    """
    sys = scope.lookup(SYSTEM)
    if sys:
        types = sys.getprop(SYS_TYPES)
        if types and types is not classes.null_value:
            ty = types.getprop(name)
            if ty and ty is not classes.null_value:
                return ty
    # internal error:
    raise Exception("cannot find %s.%s.%s" % (SYSTEM, SYS_TYPES, name))

def create_sys_type(name, scope, value):
    """
    Create an Object of Class `name`
    `name` is Python string for a system type (System.types.name)
    `scope` is used to find System object
    `value` is Python value to wrap
    """
    #import sys
    #print("create_sys_type", name, type(value), value, file=sys.stderr)
    ty = find_sys_type(name, scope)
    # does not call Class 'init' method -- would need an Object as argument!!
    return classes._new_pobj(ty, value)
