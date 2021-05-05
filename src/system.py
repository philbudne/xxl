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

import sys                      # sys.exit
import json

import classes
import scopes
import const
import vmx

# used ONLY to create items to set up "System" object
# can't use create_sys_type: which needs the System object!!!
# XXX switch from JSObject to Object
# used for: sys_import (returned module)
#       System object,
#       System.types object,
#       tokenizer returns
def __obj_create(props):          # TEMP??
    #print("__obj_create", props)
    # invokes init method
    o = classes.new_inst(classes.sys_types['JSObject'], props) # XXX???
    return o

def __list_create(l):             # for sys.argv[]
    o = classes.new_vinst(classes.sys_types['List'], l)
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

def sys_break(x):
    """
    break to python debugger to debug VM
    argument available as `x`
    """
    import pdb; pdb.set_trace() # or breakpoint()?

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

def sys_print(*args):
    print(" ".join([getstr(arg) for arg in args]))

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

def sys_print_repr(*args):
    print(" ".join([getrepr(arg) for arg in args]))

################

# XXX replace with native code
# (need file I/O; use pyimport??)

def sys_tokenizer(filename, prefix, suffix):
    """
    read tokens for parser
    """
    import jslex
    if isstr(filename): # XXXX TEMP for pp.js
        fnstr = filename
    else:
        fnstr = filename.value # XXX str()?
    pstr = prefix.value    # XXX str()?
    sstr = suffix.value    # XXX str()?
    generator = jslex.tokenize(open(fnstr), pstr, sstr)
    null = classes.sys_types['null']    # XXX
    str = classes.sys_types['Str']      # XXX
    
    # XXX use create_sys_type???
    def makestr(s):
        # XXX need scope
        return vmx.invoke_method(str, const.NEW, None, [s])

    def gen_wrapper(*args):
        """
        generator function, wrapper around jslex.tokenize
        """
        try:
            t = next(generator)
            if not t:
                return null
            where = "%s:%s:%s" % (fnstr, t.lineno, t.from_)
            # XXX new_sys_object!!!
            # XXX create a Token class???
            return __obj_create({
                'type': makestr(t.type_),
                'value': makestr(t.value),
                'where': makestr(where)
            })
        except StopIteration:
            return null

    return classes.pyfunc(gen_wrapper)

################

def sys_exit(value=0):
    # XXX check if VInstance?!
    sys.exit(value.value)       # XXX to_int??

################
# XXX should be a string() method!

def sys_tree(t):
    t2 = obj2python_json(t)
    return json.dumps(t2, indent=1)

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

################ "pyimport" returns a PyObject

def sys_pyimport(module):
    import importlib
    m = importlib.import_module(module.value)
    return classes.new_vinst(classes.sys_types['PyObj'], m) # XXX?

# XXX create an "auto-import" object? python.sys == pyimport("sys")???

################

# used only by import_worker XXX inline?
# XXX take filename, save (as __file__, or __module__.file??) w/ last modify time??
def init_module(args, main=False):
    """
    create namespace and System object (w/o parser)
    main: bool -- used to set __main__
    """
    scope = scopes.Scope(None)    # create scope for module
    if main:
        save_initial_scope(scope)
    sys = create_sys_object(scope, args)
    classes.copy_types(scope, sys)

    # put in System.main?? __module__.main???
    scope.defvar('__main__', classes.mkbool(main))

    return scope

# called only from import_worker! XXX inline?
# requires initial scope with System.types set up.
def load_parser(scope, trace=False):
    """
    load parser from vmx file into scope's System.parser
    """
    sys_obj = scope.lookup('System')
    m = import_worker(vmx_file="parser.vmx", main=False, trace=trace, parser=False)
    # point System.parser at parser module
    sys_obj.setprop('parser', __obj_create(m.vars))

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

    # scope for wrapping Lits
    return vmx.convert_instrs(j, scope) # convert to list of Python Instrs

# called only from import_worker
def parse_and_execute(src, scope, trace):
    """
    parse `src` file and execute one statement at a time
    (allows parser extensions to take effect immediately)
    """
    # get instance of Parser object visible as System.parser.parser
    sys_obj = scope.lookup('System')
    sys_parser = sys_obj.getprop('parser') # System.parser
    parser_obj = sys_parser.getprop('parser');

    vmx.invoke_method(parser_obj, 'start_parse', scope, [src])

    # top level function, takes parser object, returns List or null
    # XXX call gen inside loop, appending to same code block!?
    p1 = sys_parser.getprop('parse_and_gen_one_stmt')

    # XXX create a VM and reuse it for both parsing and running!
    #   have a System function to take "VM code" (as List of Lists)
    #   and return a Closure that can be called?
    while True:
        # run "parse_and_gen_one_stmt", turn into Python list of lists:
        js = obj2python_json(vmx.invoke_function(p1, scope, [parser_obj]))

        if not js:              # need to confirm EOF?
            break

        # convert into Python list of Instrs (scope for type name lookup)
        code = vmx.convert_instrs(js, scope)

        # UGH: invoke a new VM to execute code
        v = vmx.VM(code, scope)
        try:
            if trace:
                v.start_stats(trace)
            else:
                v.start()
        except SystemExit:
            pass
        except vmx.VMError as e:
            # NOTE: displays VM Instr
            sys.stderr.write("VM Error @ {}: {}\n".format(v.ir, e))
            # XXX dump VM registers? option to call breakpoint()??
            # XXX backtrace!! (capture "ir.where" in Frame??)
        except Exception as e:
            # NOTE: just displays "where"
            sys.stderr.write("Error @ {}: {}\n".format(v.ir.where, e))
            # XXX backtrace!! (capture "ir.where" in Frame??)

def sys_import(filename):
    """
    user called System.import function
    `filename` is Str of name of source file to parse
    returns Scope object for new module
    """
    # XXX search for .vmx file?
    # XXX propogate trace from caller??
    scope = import_worker(src_file=filename)

    # XXX run __extensions__ on caller's initial scope? System object?
    # XXX take arg to bypass __extensions__

    # wrap in JSObject (XXX change to instance of Module class!!!?)
    return __obj_create(scope.get_vars()) # UGH!

# Worker function to implement "import" (where modules come from)
# used by: vmx.py (running src & vmx files)
#       sys_import (System.import function)
#       load_parser (called from here!)
def import_worker(src_file=None, vmx_file=None, trace=False,
                  parser=True, trace_parser=False,
                  main=False, args=[]):
    """
    Takes either `src_file` or `vmx_file`
    bool `trace`
    bool `parser` to create System.parser (False to load parser.vmx)
    bool `main` True when loading from command line
    list of str `args` from command line
    """
    scope = init_module(args, main=main) # XXX pass fname(s)?

    if parser:
        load_parser(scope, trace_parser) # load unadulterated parser

    if vmx_file:
        # here (recursively) from load_parser to load parser.vmx!!
        vmx.load_and_run_vmx(vmx_file, scope, False, trace)
    else:
        # parse source using System.parser.parse() -- loaded above!
        parse_and_execute(src_file, scope, trace)
    return scope                # XXX return as Module class Instance?

################################################################

def create_sys_object(iscope, args):
    sys_obj = __obj_create({})
    iscope.defvar('System', sys_obj)

    # create System.types object from sys_types (copies values)
    tt = __obj_create(classes.sys_types)
    sys_obj.setprop('types', tt)

    # debug functions (TEMP?!)
    sys_obj.setprop('break', classes.pyfunc(sys_break)) # break to PDB
    sys_obj.setprop('print', classes.pyfunc(sys_print)) # print to stdout
    sys_obj.setprop('error', classes.pyfunc(sys_error)) # print to stderr
    sys_obj.setprop('print_repr', classes.pyfunc(sys_print_repr))

    # command line args, and exit:
    sys_obj.setprop('argv',  __list_create(args))
    sys_obj.setprop('exit', classes.pyfunc(sys_exit))

    # for parser:
    sys_obj.setprop('tokenizer', classes.pyfunc(sys_tokenizer))
    sys_obj.setprop('tree', classes.pyfunc(sys_tree)) # TEMP!!!

    # import source files, access to Python modules:
    sys_obj.setprop('import', classes.pyfunc(sys_import))
    sys_obj.setprop('pyimport', classes.pyfunc(sys_pyimport))

    return sys_obj

################################################################

# create an instance of a type using System.types.NAME
# XXX just lookup bare 'NAME' ???????? (rename to type_new?)

def create_sys_type(name, scope, *args):
    """
    Create an Instance using Class "new" method
    `name` is Python string for a system type (System.types.name)
    `scope` is used to find System object
    """
    #print("create_sys_type", name)
    sys = scope.lookup('System')
    if sys:
        types = sys.getprop('types')
        if types:               # check for null_value!
            ty = types.getprop(name)
            if ty:              # check for null_value
                return vmx.invoke_method(ty, const.NEW, scope, args)
    raise Exception("create_sys_type %s" % name)

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
