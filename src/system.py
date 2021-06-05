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

DEBUG_IMPORT = False

# should be used ONLY to create items to set up "System" & System.types objects!
# can't use create_sys_type: which needs the System object!!!
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
def sys_break(x=None):
    """
    break to python debugger to debug VM
    argument (if any) available as `x`
    """
    breakpoint()

################

@classes.pyfunc
def sys_uerror(msg):
    raise classes.UError(msg)

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

@classes.pyvmfunc
def sys_tree(vm, t):
    """
    format JSON (returns Str) from AST of Symbols
    """
    t2 = obj2python_json(t)     # strip down to Python data structures
    return classes.mkstr(json.dumps(t2, indent=1), vm.iscope)

################

def format_instr(instr, indent=''):
    """
    helper for sys_vtree
    format one instruction (Python list)
    """
    op = instr[1]
    if op not in vmx.INST2CODE:
        return indent + json.dumps(instr)

    # here to handle "close" and "bccall" (instr[2] is a code list)
    nindent = indent + " "
    return ('%s["%s", "%s",\n%s%s]' % \
            (indent, instr[0], op,
             nindent, format_code(instr[2], nindent)))

def format_code(code, indent=''):
    """
    helper for sys_vtree
    takes Python list of instructions (Python lists)
    """
    sep = ",\n" + indent + " "
    return (indent + "[" + format_instr(code[0]) + sep + # first line
            sep.join([format_instr(inst, indent) for inst in code[1:]]) +
            "]")

def trim_where(code, fname):
    """
    helper for sys_vtree, assemble
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

@classes.pyvmfunc
def sys_vtree(vm, t, fname=classes.null_value):
    """
    pretty print a VM code tree (List of List) `t`; returns Str
    """
    t2 = obj2python_json(t)     # convert to list of list of str

    if fname and fname is not classes.null_value:
        fn = fname.value        # getstr?
        trim_where(t2, fn)

    return classes.mkstr(format_code(t2), vm.iscope)

# used in:
# System.tree (above) XXX replace with a Symbol.json method??
# System.vtree (above)
# System.assemble (below)
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

        if not classes.instance_of(x, [classes.Dict]):
            raise classes.UError("obj2python only handles ASTs, code/JSON")

        # here with AST "Symbol" node; turn into JSON list
        r = []
        for attr in ['where', 'arity', 'value']:
            r.append(clean1(x.getprop(attr)))
            for attr in ['first', 'second', 'third']:
                if attr not in x.props:
                    break
                r.append(clean1(x.getprop(attr)))
            return r

    return clean1(x)

################

# helper for ModInfo.assemble
def assemble(scope, tree, srcfile):
    # convert List of Lists to Python list of lists
    js = obj2python_json(tree)
    trim_where(js, srcfile.value) # XXX getstr?

    # convert into Python list of Instrs (scope for type name lookup):
    code = vmx.convert_instrs(js, scope, srcfile)

    # turn into Closure in scope
    #   (any variables created are globals):
    return classes.CClosure(code, scope)

################ "pyimport" returns a PyObject wrapper around a Python module

@classes.pyvmfunc
def sys_pyimport(vm, module):
    import importlib
    m = importlib.import_module(module.value) # XXX getstr?
    return classes.wrap(m, vm.iscope)         # make PyObject

################

@classes.pyvmfunc
def sys_import(vm, filename):
    """
    user called System.import function
    `filename` is Str of name of source file to parse
    """
    # XXX check if already imported (or import in progress)
    #   lookup in System.modules[filename]????
    # XXX take filename w/o extension?????

    fname = filename.value      # XXX getstr???
    args = {}
    if fname.endswith('.vmx'):
        args['vmx_file'] = fname
    else:
        # XXX search for .vmx file?
        args['src_file'] = fname

    mod, bootstrap = import_worker(**args)
    if mod is None:
        Exception("import failed") # XXX UError?

    if DEBUG_IMPORT:
        print("sys_import", mod, bootstrap)

    # XXX run __extensions__ on caller's initial scope? System object?
    # XXX take arg to bypass __extensions__
    vm.save_frame()
    vm.push(mod)                # save Module on stack
    where = "sys_import"
    c2 = [[where, "call0"],     # call bootstrap.vmx Closure
          [where, "pop_temp"],  # UGH: restore Module to TEMP
          [where, "temp"],      # UGH: TEMP to AC
          [where, "return"]]    # return to caller
    vm.cb = vmx.convert_instrs(c2, mod.scope, "")
    vm.pc = 0
    return bootstrap            # CClosure w/ bootstrap.vmx

# Worker function to implement "import" (where modules come from)
# used by: xxl.py (startup)
#       sys_import (System.import function)
# returns `Module`
def import_worker(src_file=None,
                  vmx_file=None,
                  main=False,
                  argv=[],
                  parser_vmx=None):
    """
    Takes either `src_file` or `vmx_file` [XXX autodetect by filename?]
        XXX take bare name and try both .xxl and .vmx??
    `argv`: list of str for command line args
    bool `main` True when loading from command line
    str `parser_vmx` name of file with parser VM code
    """
    if DEBUG_IMPORT:
        print("BEGIN import_worker", src_file, vmx_file, main, argv)

    mod = classes.new_module(main, argv)
    modinfo = mod.modinfo
    scope = mod.scope

    if vmx_file:
        modinfo.setprop(const.MODINFO_VMXFILE, classes.mkstr(vmx_file, scope))

    if src_file:
        modinfo.setprop(const.MODINFO_SRCFILE, classes.mkstr(src_file, scope))

    modinfo.setprop(const.MODINFO_PARSER_VMX,
                    classes.mkstr((parser_vmx or
                                   os.environ.get('XXL_PARSER',
                                                  'parser.vmx')),
                                  scope))

    bootstrap_vmx = os.environ.get('XXL_BOOTSTRAP', 'bootstrap.vmx')

    # XXX handle Exception!
    #sys.stderr.write("calling load_vm_json %s %s\n" % (bootstrap_vmx, main))
    code = vmx.load_vm_json(bootstrap_vmx, scope)

    boot = classes.CClosure(code, mod.scope) # CClosure with bootstrap_vmx code
    if DEBUG_IMPORT:
        print("END import_worker", mod)
    return mod, boot

################

# called by bootstrap.vmx to load __modinfo.vmxfile (if set)
# XXX make a ModInfo method?!!!
@classes.pyvmfunc
def sys_load_vmx(vm, fname):
    code = vmx.load_vm_json(fname.value, vm.iscope) # XXX getstr
    return classes.CClosure(code, vm.iscope)

################################################################

# called only from classes.new_module: create SYSTEM Object
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

    sys_obj.setprop('uerror', sys_uerror) # fatal error w/ backtrace

    # debug functions (TEMP?!)
    sys_obj.setprop('break', sys_break) # break to PDB

    # command line args, and exit:
    sys_obj.setprop('argv',  classes.wrap(argv, iscope)) # move to ModInfo??
    sys_obj.setprop('exit', sys_exit)                    # move to ModInfo??

    # functions for parser & bootstrap:
    sys_obj.setprop('tokenizer', sys_tokenizer) # TEMP creates token generator
    sys_obj.setprop('tree', sys_tree) # TEMP!!!
    sys_obj.setprop('vtree', sys_vtree) # TEMP!!!

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
