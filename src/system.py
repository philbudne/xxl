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

SYSTEM = 'System'
TYPES = 'types'

# should be used ONLY to create items to set up "System" & System.types objects!
# can't use create_sys_type: which needs the System object!!!
# ALSO used for:
#       sys_import (returned module)
#       tokenizer returns
def __obj_create(props):          # TEMP??
    return classes._mkobj(props)

def __list_create(l):             # for sys.argv[]
    o = classes._new_vinst(classes.sys_types['List'], l)
    return o

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

def getstr(x):                  # XXX move elsewhere?
    """
    return Python string for an interpreter Instance for sys_print
    """
    if isstr(x):                # XXX odd (tree function?)
        return x

    if isinstance(x, classes.Instance):
        s = vmx.invoke_method(x, 'str', get_initial_scope())

        if isstr(s):            # XXX is Python string???
            return "pstr:" + s  # XXX COMPLAIN?? WRAP???

        # XXX check if is String!!
        return str(s.value)

    # this shouldn't happen either!!!
    return str(x)

@classes.pyfunc
def sys_print(*args):
    print(" ".join([getstr(arg) for arg in args]))

@classes.pyfunc
def sys_error(*args):
    sys.stderr.write("{}\n".format(" ".join([getstr(arg) for arg in args])))

####

def getrepr(x):                 # XXX move elsewhere
    """
    return Python string for an interpreter Instance "repr"
    """
    if isinstance(x, classes.Instance):
        s = vmx.invoke_method(x, 'repr', get_initial_scope())
        if isstr(s):            # XXX TEMP: COMPLAIN
            return "<XXX %s repr returned str: %s>" % (x.classname(), s)

        return str(s.value)

    # this shouldn't happen either!!!
    return str(x)               # XXX repr?

@classes.pyfunc
def sys_print_repr(*args):
    print(" ".join([getrepr(arg) for arg in args]))

################

# XXX replace with native code
# (need file I/O; use pyimport??)

@classes.pyvmfunc
def sys_tokenizer(vm, filename, prefix, suffix):
    """
    returns a token generator:
    returns JSObjects, and then null
    """
    import jslex
    if isstr(filename): # XXX XXX here from parser.xxl?
        fnstr = filename
    else:
        fnstr = filename.value # XXX getstr()?
    pstr = prefix.value    # XXX getstr()?
    sstr = suffix.value    # XXX getstr()?
    generator = jslex.tokenize(open(fnstr), pstr, sstr)

    # find_sys_types doesn't like "null_value"
    null = vm.scope.lookup(SYSTEM).getprop(TYPES).getprop('null')

    # XXX create general purpose PyIterator wrapper class??
    @classes.pyfunc
    def gen_wrapper(*args):
        """
        generator function, wrapper around jslex.tokenize
        """
        try:
            t = next(generator)
            if not t:
                return null
            where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
            # XXX create a Token class???
            return __obj_create({
                'type': classes.mkstr(t.type_),
                'value': classes.mkstr(t.value),
                'where': classes.mkstr(where)
            })
        except StopIteration:
            return null

    return gen_wrapper          # returns PyFunc

################

@classes.pyfunc
def sys_exit(value=0):
    # XXX check if VInstance?!
    sys.exit(value.value)       # XXX to_int??

################
# XXX should be a string() method!

@classes.pyfunc
def sys_tree(t):
    """
    format JSON
    """
    t2 = obj2python_json(t)
    return classes.mkstr(json.dumps(t2, indent=1))

@classes.pyfunc
def sys_vtree(t, fname=classes.null_value):
    """
    pretty print a VM code tree
    """
    t2 = obj2python_json(t)

    if not fname or fname is classes.null_value:
        fnc = ""
        fnclen = 0
    else:
        if isinstance(fname, str):
            # XXX SHOULD NOT HAPPEN!
            fnc = fname + ":"
        else:
            fnc = fname.value + ":" # XXX check Str

        fnclen = len(fnc)

    def format_instr(instr, indent=''):
        """
        format one instruction (Python list)
        """
        if fnclen and instr[0].startswith(fnc):
            instr[0] = instr[0][fnclen:]
        if instr[1] != "close":
            return indent + json.dumps(instr)
        # here to handle "close" (instr[3] is a new code list)
        closure = format_code(instr[2], indent + " ")
        return ('%s["%s", "%s",\n%s%s]' % (indent, instr[0], instr[1],
                                           indent + " ", closure))

    def format_code(code, indent=''):
        """
        takes Python list of instructions (Python lists)
        """
        sep = ",\n" + indent + " "
        return (indent + "[" + format_instr(code[0]) + sep +
                sep.join([format_instr(inst, indent) for inst in code[1:]]) + "]")

    return classes.mkstr(format_code(t2))

# used in System.tree (above), parse, parse_and_execute (below)
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
        if not isinstance(x, classes.Instance):
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

################ "pyimport" returns a PyObject wrapper around a Python module

@classes.pyvmfunc
def sys_pyimport(vm, module):
    import importlib
    m = importlib.import_module(module.value) # XXX getstr?
    return classes._new_vinst(classes.sys_types[const.PYOBJECT], m) # XXX wrap!!!?

# XXX create an "auto-import" object? python.sys == pyimport("sys")???

################

# used only by import_worker XXX inline?
# XXX take filename, save (as __file__, or __module__.file??) w/ last modify time??
def init_module(argv, main=False):
    """
    create namespace and System object (w/o parser)
    main: bool -- used to set __main__
    """
    scope = scopes.Scope(None)    # create scope for module
    if main:
        save_initial_scope(scope)
    sys = create_sys_object(scope, argv)
    classes.copy_types(scope, sys) # populate scope

    # put in System.main?? __module__.main???
    scope.defvar('__main__', classes.mkbool(main))

    return scope                # XXX return Module object??

# called only from import_worker! XXX inline?
# requires initial scope with System.types set up.
def load_parser(scope, parser_vmx, trace=False):
    """
    load parser from vmx file into scope's System.parser
    """
    sys_obj = scope.lookup('System')
    m = import_worker(vmx_file=parser_vmx, main=False, trace=trace, parser=False)
    # XXX check return

    # point System.parser at parser module
    sys_obj.setprop('parser', m)

# not currently used.
# expects System.parser.parse to be a function that takes a file name
# and returns an AST of Symbol instances, and System.parser.gen to
# take an AST and return a List of Lists of VM instructions.
def parse(filename, scope, dump): # XXX take trace?
    """
    `filename` is Python string for file to parse
    `scope` is scope to find System object
    `dump` is null to return list of Python VMInstr instances
        "ast" to return Python list of lists for AST
        "vm" to return Python list of lists for VM code
    """
    sys_parser = scope.lookup('System').getprop('parser') # XXX guard
    if not sys_parser or sys_parser is classes.null_value:
        raise Exception("Could not find System.parser")

    parse_function = sys_parser.getprop('parse') # bound method!
    if not parse_function or parse_function is classes.null_value:
        raise Exception("Could not find System.parser.parse")
    ast = vmx.invoke_function(parse_function, scope, [filename]) # XXX trace?
    if dump == "ast":
        return obj2python_json(ast)

    gen_function = sys_parser.getprop('gen')
    if not gen_function or gen_function is classes.null_value:
        raise Exception("Could not find System.parser.gen")
    code = vmx.invoke_function(gen_function, scope, [ast]) # XXX trace?

    j = obj2python_json(code)   # TEMP: get as list of Python lists
    if dump == "vm":
        return j                # return "vm" json

    # convert to list of Python Instrs; scope for wrapping Lits
    return vmx.convert_instrs(j, scope, filename)

# called only from import_worker
def parse_and_execute(src, scope, stats, trace, trace_parser):
    """
    parse `src` file and execute one statement at a time
    (allows parser extensions to take effect immediately)
    """
    # get instance of Parser object visible as System.parser.parser
    sys_obj = scope.lookup('System')
    sys_parser = sys_obj.getprop('parser') # System.parser
    parser_obj = sys_parser.getprop('parser');

    vmx.invoke_method(parser_obj, 'start_parse', scope, [src], trace)

    # top level function, takes parser object, returns List or null
    # XXX call gen inside loop, appending to same code block!?
    p1 = sys_parser.getprop('parse_and_gen_one_stmt')

    # XXX create a VM and reuse it for both parsing and running!
    #   have a System function to take "VM code" (as List of Lists)
    #   and return a Closure that can be called?
    while True:
        # run "parse_and_gen_one_stmt", turn into Python list of lists:
        js = obj2python_json(
            vmx.invoke_function(p1, scope, [parser_obj], trace_parser))

        if not js:              # need to confirm EOF?
            break

        # convert into Python list of Instrs (scope for type name lookup)
        code = vmx.convert_instrs(js, scope, src)
        try:
            # UGH: invoke a new VM to execute code
            vm = vmx.VM(code, scope)
            if trace:
                vm.start_trace()
            else:
                vm.start()
        except SystemExit:
            pass
        except vmx.VMError as e:
            # NOTE: displays VM Instr
            sys.stderr.write("VM Error @ {}: {}\n".format(v.ir, e))
            # XXX dump VM registers?
            vm.backtrace()
            return False
        except Exception as e:
            # NOTE: just displays "where"
            sys.stderr.write("Error @ {}:{}: {}\n".format(
                vm.ir.fn, vm.ir.where, e))
            vm.backtrace()
            raise
            return False
    return True

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
    mod = import_worker(src_file=filename)
    if mod is None:
        Exception("import failed")

    # XXX run __extensions__ on caller's initial scope? System object?
    # XXX take arg to bypass __extensions__
    return mod

# Worker function to implement "import" (where modules come from)
# used by: vmx.py (running src & vmx files)
#       sys_import (System.import function)
#       load_parser (called from here!)
# XXX returns JSObject (want Module)
def import_worker(src_file=None, vmx_file=None, trace=False,
                  parser=True,
                  parser_vmx=None,
                  stats=False, trace_parser=False,
                  main=False, argv=[]):
    """
    Takes either `src_file` or `vmx_file` [XXX autodetect by filename?]
    bool `trace`
    bool `parser` to create System.parser (False to load parser.vmx)
    bool `main` True when loading from command line
    Python list of `argv` strs from command line
    """
    # XXX wrap argv here??
    scope = init_module(argv, main=main) # XXX pass fname(s)?

    if parser:
        load_parser(scope,
                    parser_vmx or os.environ.get('XXL_PARSER', 'parser.vmx'),
                    trace_parser)

    if vmx_file:
        # here (recursively) from load_parser to load parser.vmx!!
        vmx.load_and_run_vmx(vmx_file, scope, stats, trace)
    else:
        # parse source using System.parser.parse() -- loaded above!
        if not parse_and_execute(src_file, scope, stats, trace, trace_parser):
            # all callers need to handle properly
            return None

    return __obj_create(scope.get_vars()) # XXX want Module

################################################################

# called only from init_module: create 'System' Object
def create_sys_object(iscope, argv):
    sys_obj = __obj_create({})
    iscope.defvar('System', sys_obj)

    # create System.types object from sys_types (copies values)
    tt = __obj_create(classes.sys_types) # XXX XXX XXX
    sys_obj.setprop('types', tt)         # XXX XXX top level __classes?
    
    # debug functions (TEMP?!)
    sys_obj.setprop('break', sys_break) # break to PDB
    sys_obj.setprop('print', sys_print) # print to stdout
    sys_obj.setprop('error', sys_error) # print to stderr
    sys_obj.setprop('print_repr', sys_print_repr)

    # command line args, and exit:
    sys_obj.setprop('argv',  __list_create(argv)) # XXX pass in as List?
    sys_obj.setprop('exit', sys_exit)

    # for parser:
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
        types = sys.getprop(TYPES)
        if types and types is not classes.null_value:
            ty = types.getprop(name)
            if ty and ty is not classes.null_value:
                return ty
    raise Exception("cannot find %s.%s.%s" % (SYSTEM, TYPES, name))

# create an instance of a type using System.types.NAME
def create_sys_type(name, scope, value):
    """
    Create an Object by type name
    `name` is Python string for a system type (System.types.name)
    `scope` is used to find System object
    `value` is Python type to wrap
    """
    #import sys
    #print("create_sys_type", name, type(value), value, file=sys.stderr)
    ty = find_sys_type(name, scope)
    # does not call Class 'init' method!
    return classes._new_vinst(ty, value)

################################################################
# TEMP! CROCK!

# called only from vm "main"
def save_initial_scope(scope):
    global _initial_scope
    _initial_scope = scope
    return _initial_scope

# used by getstr (above), LitInstr.__init__ wrap call
def get_initial_scope():
    return _initial_scope
