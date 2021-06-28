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
type system.

Trying to be consistent, and in comments/docstrings use:

`Object` to mean a **language** object instance
        (implemented as an instance of the Python CObject class
        or subclass thereof).

and

`Class` to mean a CObject of language class "Class" --
        the base metaclass, or a subclass thereof.

`class` can mean a Python class/type.

And avoiding the word "type"!

All Objects have a Class.

The root language Class is Object.

Only "Object" class has no super classes; all others have one or more.

By default language Classes are instances of the "Class" metaclass,
        (the source of the default "new" method); if you need to
        override the default "new" behavior, subclass "Class"
        (and end the new (meta)class name in Class)

If a language Class "ClassName" needs a Python class of it's own,
        the python class should be named CClassName

"this" is used in pyfunc (Class methods) to show that the argument
is a language CObject, and not just any Python object.

[some of the above probably DOESN'T belong in the docstring!!]
"""

# NOTE!!! For methods/ops use 'xxx' strings (make searching easier)

# XXX split this up (into classes/xxx.py) before it gets much larger??
#       maybe have one file per Class?? named classes/ClassName.py??
#       (lots of stuff is missing, so it's bound to grow....)

# Python
import os

# XXL:
import scopes
import xxlobj
import const
import vmx

NUM = (int, float)              # Python3

# used to set MODINFO_DEBUG_BOOTSTRAP
XXL_DEBUG_BOOTSTRAP = os.getenv('XXL_DEBUG_BOOTSTRAP', None)

CWD = os.getcwd()               # current working directory
CWD_SEP = CWD + os.sep

root_scope = scopes.Scope()

classes_scope = scopes.Scope(root_scope) # scope for "classes" internal Module

__initialized = False

class UError(Exception):
    """
    Exception class for user errors; show vm backtrace
    """

# All language objects are represented by the interpreter
# as instances of the Python CObject class (or subclasses thereof).
# All such Python classes should start with the letter "C"
#       (the variable ClassName should point to the Class object of that name)

GETPROP_NONE = None

class CObject:
    __slots__ = ['props', 'klass']

    def __init__(self, klass):
        # klass may only be None when creating initial Class (Object)
        self.setclass(klass)
        self.props = {}

    def setclass(self, klass):
        self.klass = klass
        return klass

    def getclass(self):
        """
        return CObject for object Class
        """
        return self.klass

    def classname(self):
        """
        return Python string for object class name
        """
        c = self.getclass()
        if not getprop_ok(c):
            return "Unknown!"

        n = c.getprop(const.NAME).value # XXX getstr
        if subclass_of(c, [Class]):
            return '%s: %s' % (n, self.getprop(const.NAME).value)

        return n

    def invoke(self, vm):
        # will raise UError if op not found:
        # NOTE!! find_op does not return BoundMethod
        #       (called 99.999% of time from XxxOpInstrs)
        m = find_op(self, const.BINOPS, '(')
        vm.args.insert(0, self) # OK, another place where THIS is passed
        m.invoke(vm)

    def hasprop(self, prop):
        return prop in self.props

    def delprop(self, prop):
        self.props.pop(prop)

    def getprop(self, prop):
        return self.props.get(prop, GETPROP_NONE)

    def setprop(self, prop, value):
        self.props[prop] = value

    def getvalue(self):
        raise UError("not a Python valued Object")

    def __str__(self):
        return repr(self)       # XXX ???

    def __repr__(self):
        return '<%s at %#x>' % (self.classname(), id(self))

class CPObject(CObject):
    """
    Python backing class for Primitive Object Classes
    (has a value property which contains a Python type)
    """
    __slots__ = ['value']

    def __init__(self, this_class):
        ### XXX TEMP
        super().__init__(this_class)
        self.value = None       # set by init method

    def getvalue(self):
        return self.value

    def __str__(self):
        if self.value is None:
            return "null"
        if isinstance(self.value, bool):
            return str(self.value).lower()
        return str(self.value)

    # someday allow Dict to be indexed by any CObject?
    #   (except List!)
    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        return (isinstance(other, CPObject) and self.value == other.value)

    def __lt__(self, other):
        return (isinstance(other, CPObject) and self.value < other.value)

    def __repr__(self):
        """show wrapped value"""
        return '<%s: %s at %#x>' % \
            (self.classname(), repr(self.value), id(self))

################

class CCallable(CObject):
    """
    Base class for directly callable CObjects.
    """
    def invoke(self, vm):
        raise Exception("invoke not overridden")

    def args(self):
        return ["<FIXME1>"]     # XXX

    def defn(self):
        return "<FIXME2>"

class CContinuation(CCallable):
    """
    A Callable instance backed by a native (VM) Continuation
    NOTE: opaque (no Class methods to expose innards) for now
    """
    def __init__(self, fp):
        super().__init__(Continuation)
        self.fp = fp

    def __repr__(self):
        return "<Continuation: %s>" % self.defn()

    def invoke(self, vm):
        vm.restore_frame(self.fp) # just like ReturnInstr
        l = len(vm.args)
        if l == 1:
            vm.ac = vm.args[0]  # return value
        elif l == 0:
            vm.ac = null_value
        else:
            raise UError("Too many Continuation args %s" % len(vm.args))

    def args(self):
        """
        for __args method: return Python list of str argument names
        """
        return ["value"]

    def defn(self):
        """
        Return Python str for "definition" location.

        (in this case, it's where it will return to,
         which may be the statement after, if return value not used)
        """
        return vmx.fp_where(self.fp)

    def backtrace(self):
        """
        Return Python list of str
        """
        return vmx.fp_backtrace_list(self.fp)

class CClosure(CCallable):
    """
    A Callable instance backed by a Closure (VM code + scope)
    NOTE: opaque (no Class methods to expose innards) for now
    """
    def __init__(self, code, scope, doc=None):
        super().__init__(Closure)
        self.code = code
        self.scope = scope
        # PLB: I _HATE_ the Python ternary
        self.setprop(const.DOC, doc and mkstr(doc) or null_value)

    def __repr__(self):
        return "<Closure: %s>" % self.defn()

    def invoke(self, vm):
        vm.save_frame(True)     # show=True
        # 'return' Continuation will be generated from FP
        #       by "args" Instr (first Instr in code)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope
        # NOTE! vm.args picked up by "args" opcode!

    def args(self):
        return self.code[0].args() # ask first VM Instr about args!!

    def defn(self):
        return self.code[0].fn_where() # ask first VM Instr about location!

class CBClosure(CClosure):
    """
    create closure for a {} block
    (hidden in backtraces)
    not currently visible to user
    (unless flow control implemented by passing block closure pointers)
    """
    def __repr__(self):
        return "<BClosure: %s>" % self.defn()

    def invoke(self, vm):
        vm.save_frame(False)    # show=False
        # leave label Continuation will be generated from FP
        #       by ""[lu]scope" Instr (first Instr in code)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope

    def args(self):
        return [""]

    # inherit defn() from CClosure

class CBoundMethod(CCallable):
    """
    A method bound to an object
    created when Object.methodname dereferenced
    XXX bring back use of "method" opcode (or binop_lit_call?)
        as optimization which fetches method and calls invoke
        without creating a BoundMethod Object!!!???
    NOTE: opaque (no Class methods to expose innards) for now
    """
    def __init__(self, obj, method):
        super().__init__(BoundMethod)
        self.obj = obj
        self.method = method

    def __repr__(self):
        return "<BoundMethod: %s %s>" % (repr(self.obj), self.method)

    def invoke(self, vm):
        # *this* is the main place "THIS" is explicitly passed!!!
        vm.args.insert(0, self.obj) # prepend saved "this" to arguments
        self.method.invoke(vm)      # returns value in AC

    def args(self):
        return self.method.args()[1:] # omit "this" arg

    def defn(self):
        return self.method.defn()

# Calling Python functions (ie; primitive class methods) was orignally
# implemented as a Closure with two VM instructions (pycall, return).
# The CObject.invoke method avoids that.
class CPyFunc(CCallable):
    """
    A Callable instance backed by a Python function
    """
    __slots__ = ['func']
    def __init__(self, func, argfunc=None):
        super().__init__(PyFunc)
        # detect pyfunc() calls on a pre-decorated function
        if isinstance(func, CPyFunc):
            # Python programming error, want Python backtrace:
            raise Exception("double wrapping %s" % func.func)
        self.func = func
        self.argfunc = argfunc or func
        # make sure PyFunc.__doc never shows through
        self.setprop(const.DOC, _mkstr(func.__doc__ or ""))

    def __repr__(self):
        # was self.func.__name___
        return "<PyFunc: %s>" % self.defn()

    def invoke(self, vm):
        vm.ac = self.func(*vm.args)
        assert(isinstance(vm.ac, CObject))

    def __call__(self, *args):
        """
        catch mistakenly calling a CPyFunc (decorated Python function)
        from another Python function.
        """
        # Python programming error, want Python backtrace:
        raise Exception("Attempt to call %s" % self)

    def args(self):
        """
        For documentation: return Python list of str of arg names
        """
        try:
            import inspect
            fas = inspect.getfullargspec(self.argfunc)
        except:
            return ['...args']  # str.find, str.format, str.rfind
        args = list(fas.args)
        if fas.varargs:
            args.append('...' + fas.varargs)
        return args

    def defn(self):
        """
        For documentation: NOT in "usual" format (includes name)
        (have separate "name" method??)
        """
        co = self.func.__code__
        fname = co.co_filename
        if fname.startswith(CWD_SEP): # trim CWD/ from file name
            fname = fname[len(CWD_SEP):]
        return "%s:%s (%s)" % (fname, co.co_firstlineno, self.func.__name__)

def pyfunc(func):
    """
    (decorator)
    Return a Python CObject with (Python) invoke method that runs Python code.
    Used for Python methods on base types, system utilities.
    """
    return CPyFunc(func)

################
# A PyFunc that needs access to internals: passed vm as first arg

class CPyVMFunc(CPyFunc):
    """
    A Callable instance backed by a Python function, passed VM as
    first argument.  MOSTLY used for access to scope for
    lookup of Classes by name.  But could be used for all kinds of
    reflection fun (inspection of current scope, code, traceback,
    etc).

    PLB NOTE!  To avoid bloat and inefficiency, VM internals (Frame,
    Scope, VMInstrs) are NOT backed (fronted?) by language Objects.
    and my current (may 2021) thoughts are to expose particulars with
    Objects created on demand, either with copies of the backing data,
    or, in the case of Scopes, an Object which references the backing
    (Python) dict, or (late may) perhaps with methods to alter live data.
    """
    # __init__ method from PyFunc

    def invoke(self, vm):
        vm.args.insert(0, vm)   # prepend vm to arguments
        super().invoke(vm)

    def args(self):
        return super().args()[1:] # trim "vm" arg

def pyvmfunc(func):
    """
    decorator for Python functions that need pointer to VM
    """
    return CPyVMFunc(func)

################

class CPyIterator(CPObject):
    """
    wrapper around a Python iterator
    """
    def __init__(self, iterator):
        super().__init__(PyIterator)
        self.value = iterator

    def __str__(self):
        return repr(self)

def pyiterator(iterator):
    """
    Make a PyIterator from a Python iterator (has a __next__ method)
    """
    assert hasattr(iterator, '__next__')
    return CPyIterator(iterator)

################################################################

def _new_pobj(this_class, arg):
    """
    FOR INTERNAL USE ONLY!!
    creates an interpreter Primitive Object of Class `this_class`
    wrapped around Python value `arg`
    does not run this_class 'init' method (which would want an Object)
    """
    o = CPObject(this_class)
    o.value = arg
    return o

def _mkdict(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    assert(not __initialized)
    return _new_pobj(Dict, vals)

def _mklist(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    assert(not __initialized)
    return _new_pobj(List, vals)

def _mkstr(s):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    see mkstr
    """
    if __initialized:           # doc strings
        return mkstr(s)
    return _new_pobj(Str, s)

def _mkobj(props):
    """
    used to create __xxl object, lexer tokens
    """
    #assert(not __initialized)
    o = CObject(Object)
    o.props.update(props)
    return o

################ use once __xxl.types initialized

def class_by_name(name):
    """
    look for class `name` in classes Module scope
    """
    assert(__initialized)
    return classes_scope.lookup(name)

def new_by_name(name, value):
    """
    create a new CPObject of class `name` w/ value `value`
    """
    ty = class_by_name(name)
    return _new_pobj(ty, value)

def mkstr(s):
    """
    used to create Str from Python str, once up and running
    """
    return new_by_name('Str', s)

def mknumber(n):
    """
    used to create Number from Python int/float, once up and running
    """
    assert(__initialized)
    return new_by_name('Number', n)

def mkiterable(i):
    assert(__initialized)
    return new_by_name('PyIterable', i)

################
null_value = None               # forward

def subclass_of(this_class, bases):
    """
    test if Class `this_class` is a subclass of any Class in bases
    `this_class` is CObject for a Class
    `bases` is Python list of CObjects (of class or subclass Class)
    """
    visited = set()
    def check(c):
        visited.add(c)
        if c in bases:
            return True
        s = c.getprop(const.SUPERS)
        if s is None or s is null_value:
            return False
        for x in s.getvalue():       # XXX check if List
            if x not in visited and check(x):
                return True
        return False
    return check(this_class)

def instance_of(this, classes):
    """
    test if `this` is an instance of any Class in `classes` list
    `this` is CObject
    `classes` is list of Classes (CObject instances of (subclasses of) Class)
    """
    return subclass_of(this.getclass(), classes)

################################################################

# backpatch Classes when Str/List available:
_saved_supers = {}
_saved_names = {}
_saved_docs = {}
Str = None
List = None

def defclass(metaclass, name, supers=None, publish=True, doc=None):
    """
    define a system Class
    `name` is Python string
    `metaclass` of this class (typ. Class)
      (the class that the returned object is an instance of
       ie; supplies "new" method)
    `supers` is Python list of superclass Class objects
    """
    class_obj = CObject(metaclass)
    if Str:                     # Str class available?
        class_obj.setprop(const.NAME, _mkstr(name))
        class_obj.setprop(const.DOC, _mkstr(doc or ""))
    else:
        _saved_names[class_obj] = name
        _saved_docs[class_obj] = doc or ""

    if supers:
        if List:                # List class available?
            class_obj.setprop(const.SUPERS, _mklist(supers))
        else:
            _saved_supers[class_obj] = supers

    if publish:
        classes_scope.defvar(name, class_obj)

    return class_obj

# base metaclass
Class = defclass(None, 'Class',
                 doc="Base Metaclass, home of the default 'new' method")

Class.setclass(Class)             # circular! Class.new creates a new Class!
# supers set to [Object] below

# root Class; circular with "Class" metaclass, so defined second.
Object = defclass(Class, 'Object', [],
                  doc="Base Class") # root Class

Nullish = defclass(Class, 'Nullish', [],
                   doc="Mixin for nullish classes.")

Undefined = defclass(Class, 'Undefined', [Nullish, Object],
                     doc="Class for undefined value.")

####
# wrappers, with .value

# metaclass for PObjects (creates Python CPObject)
PClass = defclass(Class, 'PClass', [Class],
                  doc="Metaclass for Primitive/Python value Classes")

# Primitive Object Base Class
# superclass (with .value) of Classes that are wrappers around Python classes
PObject = defclass(PClass, 'PObject', [Object],
                   doc="Base class for Primitive/Python value Classes")

# bootstrap.xxl defines static 'new' method
Null = defclass(Class, 'Null', [Nullish, PObject],
                doc="Built-in Class of `null` value")

# bootstrap.xxl defines static 'new' method
Bool = defclass(PClass, 'Bool', [PObject],
                doc="Built-in Class for `true` and `false` values")

# Pure Mixin
Iterable = defclass(Class, 'Iterable', [],
                    doc="Mixin for Classes that can be iterated over")

# created by mkiterable
PyIterable = defclass(PClass, 'PyIterable', [PObject, Iterable],
                      doc="""
    Wrapper for Python 'iterable' Objects (Dict, List, Str);
    Also returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), static method PyIterable.range().
    """)

List = defclass(PClass, 'List', [PyIterable],
                doc="Built-in mutable sequence Class")
Str = defclass(PClass, 'Str', [PyIterable],
               doc="Built-in immutable Unicode string Class")
Dict  = defclass(PClass, 'Dict', [PyIterable],
                 doc="Built-in dictionary mapping Class")

# non-iterable:
Number = defclass(PClass, 'Number', [PObject],
                  doc="Built-in int/float wrapper Class")

################
# Str, List now exist:
# set Class metaclass super list
Class.setprop(const.SUPERS, _mklist([Object]))

# do fixups for Strs and Lists in primitive Classes
for klass, name in _saved_names.items():
    klass.setprop(const.NAME, _mkstr(name))
for klass, supers in _saved_supers.items():
    klass.setprop(const.SUPERS, _mklist(supers))
for klass, doc in _saved_docs.items():
    klass.setprop(const.DOC, _mkstr(doc))

# wrapper around CCallable: internal object w/ direct invoke methods
#       (avoids binop lookup and List construction on each call)
#       w/ __args and __defn methods
Callable = defclass(Class, 'Callable', [Object],
                    doc="""
    Virtual base Class for built-in callable classes
    (BoundMethod, Continuation, PyFunc, PyVMFunc)
    """)

# all backed by Python CXyZzy classes with invoke methods:
# XXX use metaclass (CClass?) that prohibits user call of 'new' method?
BoundMethod = defclass(Class, 'BoundMethod', [Callable],
                       doc="Built-in Class for a method bound to an Object")
Closure = defclass(Class, 'Closure', [Callable],
                   doc="Built-in Class for a native function bound to a scope")
Continuation = defclass(Class, 'Continuation', [Callable],
                        doc="Built-in Class for a Continuation")
PyFunc = defclass(Class, 'PyFunc', [Callable],
                  doc="Built-in Class for function implemented in Python")
PyVMFunc = defclass(Class, 'PyVMFunc', [Callable],
                    doc="""
   Built-in Class for function implemented in Python
   with access to VM internals
   """)


# wrapper around a Python iterator (w/ next method)
PyIterator = defclass(Class, 'PyIterator', [Object, Iterable],
                      doc="Built-in Class for a wrapper around a Python iterator")

################

null_value = _new_pobj(Null, None)

undef_value = CObject(Undefined)

# create (only) instances of true/false (a doubleton)!
# subclass Bool into True and False singleton Classes??
true_value = _new_pobj(Bool, True)
false_value = _new_pobj(Bool, False)

GETPROP_NONE = null_value
def getprop_ok(x):
    """
    check a getprop return value
    """
    assert(x is not None)
    return x is not GETPROP_NONE  # see CObject.getprop

################

# utility called by VM jumpn/jumpe: NOT a method/pyfunc
# (had originally planned to have all Classes have an is_true method)
def is_true(obj):
    """
    return Python True/False for an object
    non-premature optimization:
    only "null", "false", "undefined" objects, and zero are false.
    """
    if obj is false_value or obj is null_value or obj is undef_value:
        return False
    if hasattr(obj, 'value') and obj.value == 0: # faster than isinstance?
        return False
    return True

################ Object -- the base type for all instances and classes

@pyfunc
def obj_init(this_obj, *args):
    """
    default init method for Object class
    a fatal error if any arguments given
    """
    if len(args) > 0:
        raise UError("%s.%s takes no arguments" %
                        (this_obj.classname(), const.INIT))
    return null_value

@pyfunc
def obj_str(this):
    """
    default to_str method: should return a human-friendly string
    """
    return mkstr(str(l))

@pyfunc
def obj_props(this):
    """
    returns an Iterable for (String) property names
    of `this` Object
    """
    return mkiterable(this.props.keys())

@pyfunc
def obj_repr(this):
    """
    Default Object string representation method
    (calls Python repr(this))
    """
    return mkstr(repr(this))

@pyfunc
def obj_reprx(l):
    """
    for debug: show Class, and Python value (which may include id?)
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l)))

@pyfunc
def obj_ident(l, r):            # SNOBOL4 IDENT
    """
    Test if `l` and `r` refer to the same Object
    """
    return mkbool(l is r)

@pyfunc
def obj_differ(l, r):           # SNOBOL4 DIFFER
    """
    Test if `l` and `r` refer to different Objects
    """
    return mkbool(l is not r)

def _not(x):
    """
    not a pyfunc (may call at any time)
    takes CObject, returns CObject
    """
    return mkbool(not is_true(x))

# XXX do this in pobj_not? all other objects always true????
@pyfunc
def obj_not(x):
    """
    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    """
    return _not(x)

@pyfunc
def obj_delprop(this, name):
    """
    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    """
    this.props.pop(name.getvalue())
    return null_value

@pyfunc
def obj_setprop(l, r, value):
    """
    Object setprop method/operator
    store `value` as `r` (String) property of object `l`
    """
    # XXX check r is Str!!!
    # implement access via descriptors??
    l.setprop(r.getvalue(), value)
    return value                # lhsop MUST return value

# NOTE! utility, not method
# XXX return (obj, value) to avoid generating BoundMethod?
def find_in_supers(l, rv, default):
    """
    Breadth first search of superclass methods/properties;
    `l` is CObject, `rv` is Python string for method/property name.
    """
    c = l.getclass()

    supers = c.getprop(const.SUPERS)
    q = []                      # queue
    seen = set()

    while True:
        if getprop_ok(supers):
            for s in supers.getvalue():  # XXX check
                q.append(s)
                seen.add(s)

        if not q:
            break

        c = q.pop(0)            # front of queue

        # NOTE!! doc.xxl also know that properties take precedence
        # over methods (would be moot w/ descriptors); search for MRO.
        if c.hasprop(rv):
            return c.getprop(rv) # never BoundMethod

        methods = c.getprop(const.METHODS)
        if getprop_ok(methods):
            m = methods.getvalue().get(rv, GETPROP_NONE) # Dict
            if getprop_ok(m):
                return CBoundMethod(l, m)

        supers = c.getprop(const.SUPERS)

    return default

# NOTE! utility, not method
# XXX return (obj, value) to avoid generating BoundMethod?
def find_in_class(l, rv, default):
    """
    `rv` is Python string
    may return BoundMethod
    """
    # XXX XXX XXX use descriptors (objects w/ get/set methods) for methods
    #           class methods, members, (read-only members)???
    #           all kept in "props"?!!!!!!
    c = l.getclass()

    # check for class property
    if c.hasprop(rv):
        return c.getprop(rv)

    methods = c.getprop(const.METHODS)
    if getprop_ok(methods):
        m = methods.getvalue().get(rv, GETPROP_NONE) # Dict
        if getprop_ok(m):
            return CBoundMethod(l, m)

    return find_in_supers(l, rv, default)

@pyfunc
def obj_getprop(l, r):
    """
    Object getprop method/operator
    return `r` (String) property of object `l`
    """
    rv = r.getvalue()              # XXX must be Str
    if l.hasprop(rv):
        return l.getprop(rv)
    return find_in_class(l, rv, undef_value) # may return BoundMethod

@pyfunc
def obj_hasprop(l, r):
    """
    Return `true` if object `l` has own (Str) property `r` (not interited).
    """
    return mkbool(l.hasprop(r.getvalue())) # XXX getstr

def find_op(obj, optype, op):
    """
    Utility (not method)
    `obj` is CObject
    `optype` is Python string: UNOPS, BINOPS, or LHSOPS
    `op` is Python string for operator
    NOTE!! Does *NOT* return BoundMethod!!
        called from XxxOpInstrs 99.999% of time
        (only exception is CObject.invoke)
    """
    #print("find_op", obj, optype, op)
    c = c0 = obj.getclass()
    q = []
    seen = set()
    seen.add(c)
    while True:
        ops = c.getprop(optype)
        if ops and ops != null_value:
            if op in ops.getvalue():
                return ops.getvalue()[op]

        supers = c.getprop(const.SUPERS)
        if supers and supers != null_value:
            # XXX check if List
            for s in supers.getvalue():
                if s not in seen:
                    q.append(s)
                    seen.add(s)

        if not q:
            break
        c = q.pop(0)

    raise UError("%s %s for %s not found" % ( \
        const.OPDICT2ENGLISH.get(optype,optype), op, obj.classname()))

@pyfunc
def obj_get_in_supers(this, prop):
    """
    Object `..` operator; for calling superclass methods
    Looks for `prop` as property or method of superclasses of `this`;
    can be used w/ `this.as_class(MyClass)..method`.
    """
    return find_in_supers(this, prop.getvalue(), undef_value)

# once upon a time class was stored as '__class' property,
# but it was messy when cloning.
@pyfunc
def obj_getclass(this):
    """
    return Class for `this`
    """
    return this.getclass()

@pyfunc
def obj_setclass(this, klass):
    """
    set Class for `this`!!
    """
    return this.setclass(klass)

@pyfunc
def obj_as_class(this, klass):
    """
    return an Object of Class `klass`, sharing properties with `this`.
    Use for calling superclass methods: `this.as_class(MyClass)..method`.
    """
    # XXX Have CObject methods?! Need to copy private (eg CPObject) members!?
    n = type(this)(klass)
    n.props = this.props        # YIKES! Proxy instead??
    return n

@pyfunc
def obj_call(l, *args):
    """
    default Object `(` binop
    (fatal error)
    """
    raise UError("%s does not have '(' binop" % l.classname())

@pyfunc
def obj_instance_of(this, c):
    """
    return `true` if Object `this` is an instance of
    Class (or List of Classes) `c`
    """
    if subclass_of(c.getclass(), [List]):
        c = c.getvalue()             # get Python list
    else:
        c = [c]                 # make Python list
    return mkbool(instance_of(this, c))

Object.setprop(const.METHODS, _mkdict({
    const.INIT: obj_init,
    'getclass': obj_getclass,
    'setclass': obj_setclass,
    'as_class': obj_as_class,
    'instance_of': obj_instance_of,
    'delprop': obj_delprop,
    'setprop': obj_setprop,
    'getprop': obj_getprop,
    'hasprop': obj_hasprop,
    'props': obj_props,
    'repr': obj_repr,
    'reprx': obj_reprx,
    # 'to_str' in bootstrap.xxl -- invokes repr.
}))
Object.setprop(const.BINOPS, _mkdict({
    '.': obj_getprop,           # same as getprop method!!
    '..': obj_get_in_supers,
    '===': obj_ident,           # "is"
    '!==': obj_differ,          # "is not"
    '==': obj_ident,            # allow null where str/num expected?
    '!=': obj_differ,           # ditto
    '(': obj_call,
}))
Object.setprop(const.UNOPS, _mkdict({
    '!': obj_not,
}))
Object.setprop(const.LHSOPS, _mkdict({
    '.': obj_setprop                # same as setprop!!
}))
Object.setprop(const.NULLISH, false_value)

################ Class -- base type for Classes (a MetaClass)

@pyfunc
def class_create(this_class, *args):
    """
    Default create method for `Class` (the base metaclass);
    Creates an empty instance of this_class (called from `Class.new`).
    """
    return CObject(this_class)

@pyfunc
def class_init(this_class, props):
    """
    init method for meta-class "Class" -- used to create new Classes.
    `props` is Dict holding properties (see doc/creating-classes.md and
    src/const.py CLASS_PROPS)
    """
    # XXX check props is a Dict!
    for key, val in props.getvalue().items():
        # XXX depends on key as Python str
        # XXX check val is a Dict!
        if key == 'props':
            # XXX check for overlap with methods?
            # XXX use descriptors for methods/members?!!!
            this_class.props.update(val.getvalue()) # XXX getdict
            continue
        ikey = const.CLASS_PROPS.get(key)
        if not ikey:
            metaclassname = this_class.classname()
            raise UError("Unknown %s property %s" % (metaclassname, key))
        this_class.props[ikey] = val # NOTE! stashes argument Dict value!!!

    if const.NAME not in this_class.props:
        raise UError("Class.new requires '%s'"  % (metaclass, const.NAME))

    # XXX complain if NAME doesn't start with a capitol letter??

    # XXX check if a metaclass: subclass_of(this_class, [Class])
    #   and insist that NAME ends with "Class"??

    if const.SUPERS not in this_class.props:
        # XXX complain??
        this_class.setprop(const.SUPERS, wrap([Object]))

    return null_value

@pyfunc
def class_call(this_class, *args):
    """
    `(` binop for Class -- fatal error
    (but common mistake if you have Python fingers) --
    tells you to use .new method!!
    """
    name = this_class.getprop(const.NAME).getvalue()
    raise UError("Called %s Class! Did you mean %s.new?" % (name, name))

@pyfunc
def class_subclass_of(this, c):
    """
    Return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    """
    if subclass_of(c.getclass(), List):
        c = c.getvalue()             # XXX getlist
    else:
        c = [c]                 # make Python list
    return mkbool(subclass_of(this, c))

# Class: a meta-class: all Classes are instances of a meta-class
# (Class.new creates a new Class)
Class.setprop(const.METHODS, _mkdict({
    # Class.new in bootstrap.vmx
    const.CREATE: class_create,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member, not a method!
    'subclass_of': class_subclass_of
}))

Class.setprop(const.BINOPS, _mkdict({
    '(': class_call
}))

################ PClass -- metaclass for PObjects

@pyfunc
def pclass_create(this_class):
    """
    'create' method for PClass metaclass
    makes an instance of this_class backed by a CPObject
    used to create PClass subclass objects (Number, List, Dict, Bool, Null)
    """
    return CPObject(this_class)

PClass.setprop(const.METHODS, _mkdict({
   const.CREATE: pclass_create
}))

################ generic methods for PObject

@pyfunc
def pobj_len(this):
    """
    returns length (of String, List or Dict)
    """
    return _new_pobj(Number, len(this.getvalue())) # XXX look up by name?

@pyfunc
def pobj_str(this):
    """
    return human-friendly string representation of `this`
    (uses Python str function on value)
    """
    return mkstr(str(this.getvalue()))

@pyfunc
def pobj_repr(this):
    """
    return less human-friendly string representation of `this`
    (use Python repr function on value)
    """
    return mkstr(repr(this.getvalue()))

@pyfunc
def pobj_reprx(this):
    """
    for debug: show Class name, and Python repr
    """
    return mkstr("<%s: %s>" % (this.classname(), repr(this.getvalue())))

@pyfunc
def pobj_init(l, value):
    """
    default PObject init method
    (fatal error)
    """
    raise UError("{} missing init method".format(l.classname()))

@pyfunc
def pobj__init0(this, value):
    """
    default PObject init0 method
    (fatal error)
    """
    raise UError("{} missing init0 method".format(this.classname()))

@pyfunc
def pobj_ident(l, r):
    """
    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    """
    lv = l.value
    rv = r.getvalue()
    return mkbool(lv is rv)

@pyfunc
def pobj_differ(l, r):
    """
    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    """
    lv = l.value
    rv = r.getvalue()
    return mkbool(lv is not rv)

@pyfunc
def pobj__format(this, fmt):
    return mkstr(format(this.getvalue(), fmt.getvalue())) # XXX fmt.getstr()

PObject.setprop(const.METHODS, _mkdict({
    'repr': pobj_repr,
    'reprx': pobj_reprx,
    const.INIT: pobj_init,
    '__init0': pobj__init0,
    '__format': pobj__format
}))

PObject.setprop(const.BINOPS, _mkdict({
    '===': pobj_ident,
    '!==': pobj_differ,
    '==': pobj_ident,
    '!=': pobj_differ
}))

################ Callable base class

@pyfunc
def callable__args(this):
    """
    currently private/hidden (to create docs)
    returns formatted string for args (as if a native function) with parens
    """
    return mkstr("(%s)" % ", ".join(this.args()))

@pyfunc
def callable__defn(this):
    """
    currently private/hidden (to create docs)
    returns location (source file and line) of function definition
    """
    return mkstr(this.defn())

Callable.setprop(const.METHODS, _mkdict({
    '__args': callable__args,
    '__defn': callable__defn
}))

################ Continuation

@pyfunc
def continuation__backtrace_list(this):
    """
    return List of return locations on Continuation stack.
    """
    return wrap(this.backtrace())

Continuation.setprop(const.METHODS, _mkdict({
    '__backtrace_list': continuation__backtrace_list
    # XXX have a visible method to print? replace xxl_backtrace??
}))

################ Iterable

# for_each, each_for, map, map2 in bootstrap.xxl
Iterable.setprop(const.METHODS, _mkdict({
}))

################ List

# init, repr, extend in bootstrap.xxl
List.setprop(const.METHODS, _mkdict({
}))

################ PyIterable

# subclass of Iterable, PObject
# superclass of List, Dict, Str!
# also created by mkiterable, used in:
#       Dict.{item,key,value}s()
#       Object.props()
#       PyIterable.range()

@pyfunc
def pyiterable_iter(this):
    """
    Return forward iterator.
    """
    return pyiterator(iter(this.getvalue()))

@pyfunc
def pyiterable_reversed(this):
    """
    Return reverse iterator.
    """
    # XXX handle TypeError for "not reversible" (dict pre Python 3.8)?
    # XXX XXX make list, and reverse that??
    return pyiterator(reversed(this.getvalue()))

@pyfunc
def pyiterable_sorted(this, reverse=false_value):
    """
    Return sorted List of iterator values.
    `reverse` is Bool to sort in reverse order (defaults to `false`).
    """
    return wrap(sorted(this.getvalue(), reverse=is_true(reverse)))

PyIterable.setprop(const.METHODS, _mkdict({
    'iter': pyiterable_iter,
    'reversed': pyiterable_reversed,
    'sorted': pyiterable_sorted
}))


@pyfunc
def pyiterable_range(*args):
    """
    Static method:
    returns PyIterable for an integer range;
    iter() method generates fresh Iterators.

    range(10): returns Iterable for 0..9;
    range(1,10): returns Iterable for 1..9;
    range(1,10,2): returns Iterable for odd numbers 1..9
    """
    if len(args) == 1:
        r = range(args[0].getvalue()) # XXX getint?
    elif len(args) == 2:
        r = range(args[0].getvalue(), args[1].getvalue()) # XXX getint?
    elif len(args) == 3:
        r = range(args[0].getvalue(), args[1].getvalue(), args[2].getvalue()) # XXX getint?
    else:
        raise UError("range requires one to three arguments")

    return mkiterable(r)

PyIterable.setprop('range', pyiterable_range) # static method

################ Dict

@pyfunc
def dict_put(l, r, value):
    """
    `l[r] = value`
    """
    entry = r.getvalue()             # XXX
    l.value[entry] = value
    return value                # lhsop MUST return value

@pyfunc
def dict_get(l, r):
    """
    `l[r]`
    """
    entry = r.getvalue()             # XXX
    ret = l.value.get(entry, null_value)
    return ret

@pyfunc
def dict__init0(this):
    """
    Called by Dict.init (in bootstrap.xxl).
    Dodges needing private metaclass for Dict.
    """
    this.value = {}
    return null_value

@pyfunc
def dict_pop(obj, key):
    """
    Remove Dict item with specified `key`.
    """
    return obj.getvalue().pop(key.getvalue()) # XXX check arg has value!!!

@pyfunc
def dict_items(this):
    """
    Return PyIterable for [key, value] value pairs.
    """
    return mkiterable(this.getvalue().items())

@pyfunc
def dict_keys(this):
    """
    Return PyIterable for Dict keys.
    """
    return mkiterable(this.getvalue().keys())

@pyfunc
def dict_values(this):
    """
    Return PyIterable for Dict values.
    """
    return mkiterable(this.getvalue().values())

Dict.setprop(const.METHODS, _mkdict({
    '__init0': dict__init0,
    'items': dict_items,
    'keys': dict_keys,
    'len': pobj_len,
    'pop': dict_pop,
    'values': dict_values,
}))
Dict.setprop(const.BINOPS, _mkdict({
    '[': dict_get
}))
Dict.setprop(const.LHSOPS, _mkdict({
    '[': dict_put
}))

################ List

@pyfunc
def list__init0(l):
    """
    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    """
    l.value = []
    return null_value

@pyfunc
def list_append(this, item):
    """
    append `item`.
    """
    this.getvalue().append(item)
    return null_value

@pyfunc
def list_pop(l, index=None):
    """
    Remove and return item at `index` (default last).
    """
    if index is None:
        return l.value.pop()
    return l.value.pop(index.getvalue()) # XXX getnum

@pyfunc
def list_get(l, r):
    """
    `l[r]`
    """
    # XXX check if integer
    return l.value[r.getvalue()]

@pyfunc
def list_insert(l, index, object):
    """
    Insert `object` at `index` (0 is first, -1 is last); Returns `null`.
    """
    l.value.insert(index.getvalue(), object)
    return null_value

@pyfunc
def list_put(l, r, value):
    """
    `l[r] = value`
    """
    # XXX check if integer
    l.value[r.getvalue()] = value
    return value		# lhsop MUST return value

# str, repr, for_each, each_for, map, map2 from Iterable (in bootstrap.xxl)
List.setprop(const.METHODS, _mkdict({
    'append': list_append,
    'insert': list_insert,
    'len': pobj_len,
    'pop': list_pop,
    # XXX slice(start[,end]) (return range of elements)
    '__init0': list__init0,
}))
List.setprop(const.BINOPS, _mkdict({
    '[': list_get
}))
List.setprop(const.LHSOPS, _mkdict({
    '[': list_put
}))

################ Number

# XXX TEMP? replace with Int and Real?
# XXX XXX need to use "to_number" method on LHS (y) values??????!!!!!!

@pyfunc
def neg(x):
    """
    Return negative of `x`
    """
    return _new_pobj(x.getclass(), -x.getvalue())

@pyfunc
def add(l, r):
    """
    add `l` and `r`
    """
    lv = l.value
    rv = r.getvalue()
    if lv == 0:
        return r
    if rv == 0:
        return l
    return _new_pobj(l.getclass(), lv + rv)

@pyfunc
def sub(l, r):
    """
    subtract `r` from `l`
    """
    lv = l.value
    rv = r.getvalue()
    if rv == 0:
        return l
    return _new_pobj(l.getclass(), lv - rv)

@pyfunc
def mul(l, r):
    """
    multiply `l` and `r`
    """
    lv = l.value
    rv = r.getvalue()
    if lv == 1:
        return r
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), l.value * r.getvalue())

@pyfunc
def div(l, r):
    """
    Divide `l` by `r`; always creates float.
    """
    lv = l.value
    rv = r.getvalue()
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), lv / rv)

def _eq(l, r):
    """
    call any time (not a pyfunc)
    takes CPObject, returns CPObject
    """
    return mkbool(l.value == r.getvalue())

@pyfunc
def eq(l, r):
    """
    return `true` if value of `l` is the same as value of `r`
    """
    return _eq(l, r)

@pyfunc
def ne(l, r):
    """
    return `true` if value of `l` is different from the value of `r`
    """
    return _not(_eq(l, r))

def _ge(l, r):
    return mkbool(l.value >= r.getvalue())

@pyfunc
def ge(l, r):
    """
    return `true` if value of `l` is >= the value of `r`
    """
    return _ge(l, r)

@pyfunc
def lt(l, r):
    """
    return `true` if value of `l` is < the value of `r`
    """
    return _not(_ge(l, r))

def _le(l, r):
    return mkbool(l.value <= r.getvalue())

@pyfunc
def le(l, r):
    """
    return `true` if value of `l` is <= the value of `r`
    """
    return _le(l, r)

@pyfunc
def gt(l, r):
    """
    return `true` if value of `l` is > the value of `r`
    """
    return _not(_le(l, r))

@pyfunc
def bitand(l, r):
    """
    return bitwise (binary) "and" (conjunction) of `l` and `r`
    """
    lv = l.value
    rv = r.getvalue()
    if lv == 0:
        return l
    if rv == 0:
        return r
    return _new_pobj(l.getclass(), lv & rv)

@pyfunc
def bitor(l, r):
    """
    return bitwise (binary) "or" (union) of `l` and `r`
    """
    lv = l.value
    rv = r.getvalue()
    if lv == 0:
        return r
    if rv == 0:
        return l
    return _new_pobj(l.getclass(), lv | rv)

@pyfunc
def bitnot(this):
    """
    return bitwise (binary) "not" (complement) of `this`
    """
    return _new_pobj(this.getclass(), ~this.getvalue())

@pyfunc
def num_to_float(this):
    """
    If value is a float, return `this`
    If value is an int, return a new Number object
    """
    if isinstance(this.getvalue(), float):
        return this
    return _new_pobj(this.getclass(), float(this.getvalue()))

@pyfunc
def num_to_int(this):
    """
    If value is an int, return `this`
    If value is a float, return a new Number object
    """
    if isinstance(this.getvalue(), int):
        return this
    return _new_pobj(this.getclass(), int(this.getvalue()))

@pyfunc
def num_to_number(this):
    """
    identity method; returns `this`
    """
    return this

Number.setprop(const.METHODS, _mkdict({
    'to_float': num_to_float,
    'to_int': num_to_int,
    'to_number': num_to_number,
}))

Number.setprop(const.UNOPS, _mkdict({
    '-': neg,
    '~': bitnot,                # Int only!!
}))
Number.setprop(const.BINOPS, _mkdict({
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '&': bitand,                # Int only!
    '|': bitor,                 # Int only!
    # XXX Orderable mixin?
    '==': eq,
    '!=': ne,
    '>=': ge,
    '<=': le,
    '>': gt,
    '<': lt,
}))

################ Str

@pyfunc
def str_concat(x, y):
    """
    String concatenation
    """
    xv = x.getvalue()                # XXX getstr
    yv = y.getvalue()                # XXX getstr
    if xv == "":
        return y
    if yv == "":
        return x
    return _new_pobj(x.getclass(), xv + yv)

@pyfunc
def str_get(l, r):              # [] operator
    """
    Str l[r]
    return `r`'th character of Str `l`
    """
    # XXX check if r is integer
    return _new_pobj(l.getclass(), l.value[r.getvalue()])

@pyfunc
def str_slice(this, start, end=None):
    """
    return a substring (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to rest of string
    """
    startv = start.getvalue()        # XXX check if int
    if end is not None:
        endv = end.getvalue()            # XXX check if int
        ret = this.value[startv:endv]
    else:
        ret = this.value[startv:]
    return _new_pobj(this.getclass(), ret)

@pyfunc
def str_split(this, sep=None, limit=-1):
    """
    Return a List of the words in the string,
    using sep as the delimiter string (default to `null` -- any whitespace).
    Limit to `limit` return values (defaults to -1 -- no limit)
    """
    if sep is not None:
        sep = sep.getvalue()         # XXX getstr
    if limit != -1:
        limit = limit.getvalue()     # XXX getint
    # will use current "Str" defn:
    return wrap(this.value.split(sep, limit))

@pyfunc
def str_ends_with(this, suff):
    """
    Return `true` if `this` ends with the suffix `suff`, `false` otherwise.
    """
    return mkbool(this.value.endswith(suff.getvalue()))

@pyfunc
def str__join(this, arg):
    """
    Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    """
    return _new_pobj(this.getclass(),
                     this.value.join(unwrap(arg)))

@pyfunc
def str_ord(this):
    """
    Return the Unicode code point for a one-character string `this`
    """
    return mknumber(ord(this.value)) # XXX getstr

@pyfunc
def str_starts_with(this, pref):
    """
    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    """
    return mkbool(this.value.startswith(pref.getvalue()))

@pyfunc
def str_str(this):
    """
    Identity method
    """
    return this                 # identity

@pyfunc
def str_strip(this):
    """
    Return a copy of the string with leading and trailing whitespace removed.
    """
    return _new_pobj(this.getclass(), this.value.strip()) # XXX getstr

@pyfunc
def str_to_float(this):
    """
    Convert string to a floating point Number
    """
    return mknumber(float(this.value))

@pyfunc
def str_to_int(this, base=None):
    """
    Convert string to integer Number.
    Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).
    """
    if base is None:
        base = 0
    else:
        base = base.getvalue()       # XXX getint
    return mknumber(int(this.value, base))

@pyfunc
def str_to_number(this):
    """
    Convert string to a Number
    """
    try:
        return mknumber(int(this.value))
    except ValueError:
        return mknumber(float(this.value))

# static methods (plain function)
@pyfunc
def str_chr(i):
    """
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff
    """
    return mkstr(chr(i.getvalue())) # XXX getint

Str.setprop(const.METHODS, _mkdict({
    'ends_with': str_ends_with,
    '__join': str__join,
    'len': pobj_len,
    'ord': str_ord,
    'slice': str_slice,
    'split': str_split,
    'starts_with': str_starts_with,
    'strip': str_strip,
    'to_float': str_to_float,
    'to_int': str_to_int,
    'to_number': str_to_number,
    'to_str': str_str,
    const.INIT: pobj_init
}))
Str.setprop(const.BINOPS, _mkdict({
    '+': str_concat,
    '[': str_get,
    # XXX Orderable mixin?
    '==': eq,
    '!=': ne,
    '>=': ge,
    '<=': le,
    '>': gt,
    '<': lt,
}))
Str.setprop('chr', str_chr)

################ Null

@pyfunc
def null_str(this):
    """
    to_string/repr method for Null Class: returns "null"
    """
    return mkstr("null")

@pyfunc
def null_call(this, *args):
    """
    `(` method for `null` value (fatal error)
    """
    raise UError("'null' called")

Null.setprop(const.METHODS, _mkdict({
    'repr': null_str
}))
Null.setprop(const.BINOPS, _mkdict({
    '(': null_call
}))
Null.setprop(const.NULLISH, true_value)

################ Nullish

@pyfunc
def nullish_getprop(l, r):
    """
    `.` method for Nullish (null, undefined) values.
    Fatal error if unknown property.

    Allows all Object methods (JavaScript is stricter, Python is not).
    """
    rv = r.getvalue()              # XXX must be Str
    if l.hasprop(rv):
        return l.getprop(rv)

    ILLEGAL_VALUE = nullish_getprop           # can NEVER be seen
    val = find_in_class(l, rv, ILLEGAL_VALUE) # may return BoundMethod
    if val is ILLEGAL_VALUE:
        raise UError("unknown property '%s' of %s" % (rv, l.classname()))
    return val

@pyfunc
def nullish_setprop(l, r, value):
    """
    Nullish Object setprop method/operator
    """
    rv = r.getvalue()              # XXX must be Str
    raise UError("Cannot set property '%s' of %s" % (rv, l.classname()))

Nullish.setprop(const.METHODS, _mkdict({
    'getprop': nullish_getprop,
    'setprop': nullish_setprop
}))
Nullish.setprop(const.BINOPS, _mkdict({
    '.': nullish_getprop
}))
Nullish.setprop(const.LHSOPS, _mkdict({
    '.': nullish_setprop
}))

################ Bool

@pyfunc
def bool_str(this):
    """
    return Str representation: "true" or "false"
    """
    if this.value:
        return mkstr("true")
    else:
        return mkstr("false")

# XXX have own MetaClass "new" to return one of the doubleton values?
# XXX subclass into True and False singleton classes????
Bool.setprop(const.METHODS, _mkdict({
    'repr': bool_str
}))

def mkbool(val):
    """
    convert Python truthiness
    to language true or false Object
    """
    if val:
        return true_value
    else:
        return false_value

################ PyObject

# PyObjects are created by __xxl.pyimport("python_module")
# and are proxy wrappers around generic/naive Python objects

PyObject = defclass(PClass, const.PYOBJECT, [Object],
                    doc="""
    Built-in Class for a wrapper around an arbitrary Python Object
    (returned by pyimport, or operations on PyObjects)
    """)

def unwrap(x):
    """
    recursively unwrap an Object, to pass to PyObject on call
    """
    if hasattr(x, 'value'):     # faster than isinstance(x, PObject)??
        x = x.value
        if isinstance(x, list): # XXX handle any iterable?
            return [unwrap(y) for y in x]
        elif isinstance(x, dict): # XXX handle any mapping?
            return {key: unwrap(val) for key, val in x.items()} # keys Python
        return x
    if x is undef_value:
        return None
    return x

@pyfunc
def pyobj_getprop(l, r):
    """
    PyObject `.` binop -- proxies to Python object getattr
    """
    # XXX r must be Str
    #   for access to Object properties?
    rv = r.getvalue()                # XXX getstr
    if hasattr(l.value, rv):
        v = getattr(l.value, rv) # get Python object attribute
    elif l.hasprop(rv):  # check Object properties (most likely empty)
        v = l.getprop(rv)
    else:
        # allow 'to_str' method so Object can be printed!!
        v = find_in_class(l, rv, undef_value) # may return BoundMethod
    return wrap(v)

@pyfunc
def pyobj_props(this):
    """
    return dir() of wrapped Python object
    """
    return wrap(dir(this.value))

@pyfunc
def pyobj_getitem(l, r):
    """
    PyObject `[` binop
    """
    v = l.value[r.getvalue()]        # XXX unwrap(r)??
    return wrap(v)

@pyfunc
def pyobj_call(this, *args):
    a2 = [unwrap(x) for x in args]
    ret = this.value(*a2)
    return wrap(ret) # may create another PyObject!

# searched AFTER wrapped Python object attrs
PyObject.setprop(const.METHODS, _mkdict({
    const.INIT: pobj_init,
    'props': pyobj_props
}))

PyObject.setprop(const.BINOPS, _mkdict({
    '.': pyobj_getprop,         # gets Python object attr!
    '[': pyobj_getitem,
    '(': pyobj_call,
}))

# XXX TODO LHSOPS for '.' and '[' ?!!! need to unwrap values!

################ PyIterator

@pyfunc
def pyiterator_iter(this):
    """
    Returns `this.`

    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method.
    """
    return this

@pyvmfunc
def pyiterator_next(vm, this, finished_continuation):
    """
    Returns next value; calls `finished_continuation`
    (eg; block leave label or `return`) to call when iterator exhausted.
    """
    try:
        return wrap(next(this.value))
    except StopIteration:
        # here to avoid check on each iteration:
        if not isinstance(finished_continuation, CContinuation):
            raise UError("iterator .next takes Continuation")
        vm.args = []            # will be defaulted to null
        finished_continuation.invoke(vm) # alters VM state; RETURN IMMEDIATELY!
    return null_value

PyIterator.setprop(const.METHODS, _mkdict({
    'iter': pyiterator_iter,    # see above
    'next': pyiterator_next
}))

################ Undefined

@pyfunc
def undef_str(this):
    """
    to_string/repr method for Undefined Class: returns `"undefined"`
    """
    return mkstr("undefined")

@pyfunc
def undef_call(this, *args):
    """
    `(` method for `undefined` value (fatal error).
    commonly happens when a bad method name is used,
    so output a "helpful" message.
    """
    raise UError("'undefined' called; bad method name?")

Undefined.setprop(const.METHODS, _mkdict({
    'repr': undef_str
}))
Undefined.setprop(const.BINOPS, _mkdict({
    '(': undef_call
}))
Undefined.setprop(const.NULLISH, true_value)

################################################################

# Module is what "import" function returns
#       properties are the namespace of the target Module

# XXX need ModuleClass metaclass (unless/until Scope objects visible!!)
#       in order to allow .new
Module = defclass(Class, 'Module', [Object],
        doc="Built-in class for a Module (from import function)")
Module.setprop('modules', _mkdict({})) # Class variable

class CModule(CObject):
    __slots__ = ['scope', 'modinfo']
    def __init__(self, scope):
        super().__init__(Module)
        self.scope = scope      # HIDDEN!
        self.modinfo = None     # convenience; '__modinfo' should suffice
        self.props = scope.get_vars() # XXX THWACK (stealing Scope dict)!!

# ModInfo is the Class of the '__modinfo' variable inside each Module
#       (meta-info about the module-- Module properties are the
#        the contents of the Module namespace/Scope)
ModInfo = defclass(Class, 'ModInfo', [Object],
                   doc="Built-in Class for __modinfo Objects (inside Modules)")

# called from new_module -- should be modinfo_init (ModInfo.init method)?
def new_modinfo(main, module, fname, parser_vmx=None):
    """
    bool `main`
    CModule `module`
    str `fname`
    str `parser_vmx`
    """
    mi = CObject(ModInfo)
    mi.setprop(const.MODINFO_MAIN, mkbool(main)) # is main program
    mi.setprop(const.MODINFO_MODULE, module)     # pointer to Module
    if XXL_DEBUG_BOOTSTRAP:
        mi.setprop(const.MODINFO_DEBUG_BOOTSTRAP, true_value)

    scope = module.scope

    if fname is not None:
        mi.setprop(const.MODINFO_FILE, mkstr(fname))

    if parser_vmx:              # bootstrap defaults to __xxl.parser_vmx
        mi.setprop(const.MODINFO_PARSER_VMX, mkstr(parser_vmx))

    return mi

# "where Modules come from"
# called by:
#       xxl.py (startup)
#       xxlobj.py xxl__import (__xxl._import function)
# XXX should be moduleclass_new?!!
# XXX take optional bootstrap_vmx arg??
def new_module(fname, main=False, parser_vmx=None):
    """
    `fname` is Python str (or None for internal Module)
    `main` is Python True for main program (from command line)
    `argv` is Python list of str (if main is True)
    `parser_vmx` is Python str for parser VMX file to use
    returns (CModule, CClosure) if newly loaded module
        the Closure is the (bootstrap) code to populate the Module
    returns (CModule, None) if previously loaded (or internal Module)
    """

    md = Module.getprop('modules') # Module Dict/directory (Class variable)

    # XXX Dict indexed by Python str
    if fname and fname in md.getvalue(): # previously loaded?
        # XXX Dict indexed by Python str
        return md.getvalue()[fname], None # yes; return it, no bootstrap needed

    scope = scopes.Scope(root_scope) # create base scope for module
    mod = CModule(scope)

    scope.defvar(const.DOC, null_value)

    if fname:
        # XXX Dict indexed by Python str
        md.getvalue()[fname] = mod   # save as previously loaded

    mi = new_modinfo(main=main, module=mod, fname=fname, parser_vmx=parser_vmx)
    mod.modinfo = mi
    scope.defvar(const.MODINFO, mi) # make ModInfo visible in module namespace

    if fname is None:           # internal module?
        return mod, None

    bootstrap_vmx = xxlobj.find_in_lib_path(os.environ.get('XXL_BOOTSTRAP',
                                                           'bootstrap.vmx'))

    # XXX handle Exceptions for I/O, bad JSON, bad instructions
    code = vmx.load_vm_json(bootstrap_vmx, mod.scope)

    boot = CClosure(code, mod.scope) # CClosure with bootstrap_vmx code

    return mod, boot

# called by bootstrap.vmx to load __modinfo.vmxfile (if set)
# NOTE! This _could_ be replaced by native code in bootstrap.xxl
# (reading JSON and calling modinfo_assemble)
# *BUT* load_vm_json has to exist to load the bootstrap anyway!
@pyfunc
def modinfo_load_vmx(this, fname):
    """
    Load compiled `.vmx` file;
    Returns Closure in __modinfo.module top level scope.
    """
    mod = this.getprop(const.MODINFO_MODULE) # XXX check return
    code = vmx.load_vm_json(fname.getvalue(), mod.scope) # XXX getstr
    return CClosure(code, mod.scope)

@pyfunc
def modinfo_assemble(this, tree, srcfile):
    """
    Assemble List of Lists representing VM code.
    `tree`: List of Lists.
    `srcfile`: source of code (for output only).
    Returns Closure in __modinfo.module top level scope.
    """
    mod = this.getprop(const.MODINFO_MODULE) # XXX check
    code = vmx.assemble(mod.scope, tree, srcfile)

    # turn into Closure in scope
    #   (any variables created are globals):
    return CClosure(code, mod.scope)

ModInfo.setprop(const.METHODS, _mkdict({
    'load_vmx': modinfo_load_vmx, # create Closure from .vmx file
    'assemble': modinfo_assemble  # create Closure from List of instruction Lists
}))

################################################################

PyIteratorObject = defclass(PClass, const.PYITERATOROBJECT, [PyObject,PyIterator],
                    doc="""
    Built-in Class for a wrapper around an arbitrary Python Object that is an iterator
    (has a __next__ method -- should also have __iter__ method).
    """)

PyIterableObject = defclass(PClass, const.PYITERABLEOBJECT, [PyObject,PyIterable],
                    doc="""
    Built-in Class for a wrapper around an arbitrary Python Object that is an iterable
    (has an __iter__ method -- an iterator factory).
    """)

# XXX maybe take second arg PObject orig, and return if "value is orig.value"??
def wrap(value):
    """
    wrap a Python `value` in a language CObject

    used by vm `lit`, `push_list` opcodes; type `PyObject`; `PyIterator.next`
    """
    assert(__initialized)

    if isinstance(value, CObject):
        return value

    if isinstance(value, bool):
        return mkbool(value)

    if isinstance(value, NUM):
        return mknumber(value)

    if isinstance(value, str):
        return mkstr(value)

    # XXX handle bytes??

    # tuple added for dict_items iterator
    # but exclude tuple-like things (os.stat results, namedtuples)
    if isinstance(value, list) or type(value) is tuple:
        return new_by_name('List', [wrap(x) for x in value])

    if value is None:
        return null_value

    if isinstance(value, dict):
        return new_by_name('Dict', value)

    if hasattr(value, '__next__'): # Python I/O objects!
        return new_by_name(const.PYITERATOROBJECT, value)

    if hasattr(value, '__iter__'):
        return new_by_name(const.PYITERABLEOBJECT, value)

    return new_by_name(const.PYOBJECT, value)

################################################################

def defmodule(name, mod):
    """
    declare an internal Module by name
    `name` is Python str
    `mod` is CModule
    """
    assert(isinstance(mod, CModule))
    md = Module.getprop('modules') # module Dict
    # XXX indexed by Python str:
    md.getvalue()[name] = mod

classes_module = None           # XXX TEMP?

def classes_init(argv, parser_vmx):
    """
    call once on startup; initializae "root" scope, including __xxl object
    """

    # init root_scope
    root_scope.defvar('true', true_value)
    root_scope.defvar('false', false_value)
    root_scope.defvar('null', null_value)
    root_scope.defvar('undefined', undef_value)
    root_scope.defvar('Class', Class)

    # create __xxl object
    xxlobj.create_xxl_object(root_scope, argv=argv, parser_vmx=parser_vmx)


    # UTTERLY VILE: either hide in a "make_internal_module"
    #   or do it more cleanly!!!!
    #   declare classes_module up top???????????
    global classes_module       # XXX TEMP?
    classes_module, _ = new_module(None)
    classes_module.scope = classes_scope # XXX YUK
    # NOTE: below crushes __modinfo!!!??? (do we care???)
    classes_module.props = classes_scope.vars # XXX XXX DOUBLY SO
    defmodule('classes', classes_module)      # XXX __classes?

################################################################

def def_wrappers(cname, ptype, methods):
    """
    str `cname` is XXL Class name.
    Python type `ptype` is a Python class/type.
    str `pmname` is Python method name
    list `methods` is list of str and/or 2-tuple of str (pymeth, xxlmeth)
    """
    # find Class with cname, find or create methods Dict
    c = classes_scope.lookup(cname)
    if not c.hasprop(const.METHODS):
        mdict = _mkdict({})
        c.setprop(const.METHODS, mdict)
    else:
        mdict = c.getprop(const.METHODS)

    for pmname in methods:
        if isinstance(pmname, (list, tuple)):
            pmname, mname = pmname # (Python_name, XXL_NAME)
        else:
            mname = pmname

        try:
            getattr(ptype, pmname)
        except AttributeError:
            continue            # not in this version of Python

        def def_wrapper(_pmname, _mname):
            # closure with private names, pmethod (not loop variables!)
            pmethod = getattr(ptype, _pmname)
            def wrapper(*args):
                return wrap(pmethod(*[unwrap(x) for x in args]))
            wrapper.__name__ = _mname # crock for CPyFunc.defn()
            pf = CPyFunc(wrapper, pmethod) # second arg crock for CPyFunc.args()
            pf.setprop(const.DOC, _mkstr(pmethod.__doc__ or ""))
            mdict.value[mname] = pf # XXX NOTE Python str key
        def_wrapper(pmname, mname)

################
# XXX need Bytes for "encode" output
def_wrappers('Str', str, ['capitalize',
                          ('casefold', 'case_fold'),
                          'center', 'count',
                          ('expandtabs', 'expand_tabs'),
                          'find',
                          'format', # !!??
                          'index',
                          ('isalnum', 'is_alnum'),
                          ('isalpha', 'is_alpha'),
                          ('isascii', 'is_ascii'),
                          ('isdecimal', 'is_decimal'),
                          ('isdigit', 'is_digit'),
                          ('isidentifier', 'is_identifier'),
                          ('islower', 'is_lower'),
                          ('isnumeric', 'is_numeric'),
                          ('isprintable', 'is_printable'),
                          ('isspace', 'is_space'),
                          ('istitle', 'is_title'),
                          ('isupper', 'is_upper'),
                          'ljust',
                          ('lower', 'to_lower'),
                          'replace', 'rfind', 'rsplit', 'rstrip',
                          ('splitlines', 'split_lines'),
                          ('swapcase', 'swap_case'),
                          # XXX translate??
                         ('upper', 'to_upper'),
                          'zfill'])

# XXX def more classes mere
################################################################

# earlier?!!!!!
__initialized = True        # don't allow _mkXXX any more

classes_scope.defvar(const.DOC, mkstr("Built-in Classes for XXL"))
