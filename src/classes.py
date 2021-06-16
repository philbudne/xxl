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
import system
import const
import vmx

NUM = (int, float)              # Python3

# used to set MODINFO_DEBUG_BOOTSTRAP
XXL_DEBUG_BOOTSTRAP = os.getenv('XXL_DEBUG_BOOTSTRAP', None)

CWD = os.getcwd();              # current working directory
CWD_SEP = CWD + os.sep

classes_scope = scopes.Scope()  # scope for "classes" internal Module

__initialized = False

class UError(Exception):
    """
    Exception class for user errors; show vm backtrace
    """

# All language objects are represented by the interpreter
# as instances of the Python CObject class (or subclasses thereof).
# All such Python classes should start with the letter "C"
#       (the variable ClassName should point to the Class object of that name)

class CObject:
    __slots__ = ['props', 'klass']

    def __init__(self, klass):
        # klass may only be None when creating initial Class (Object)
        self.setclass(klass)
        self.props = {}

    def setclass(self, klass):
        self.klass = klass

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
        if not c or c == null_value:
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
        vm.args.insert(0, self)
        m.invoke(vm)

    def hasprop(self, prop):
        return prop in self.props

    def delprop(self, prop):
        self.props.pop(prop)

    def getprop(self, prop):
        return self.props.get(prop, null_value)

    def setprop(self, prop, value):
        self.props[prop] = value

    def __str__(self):
        return repr(self)       # XXX ???

    def __repr__(self):
        return '<%s at %#x>' % (self.classname(), id(self))

class CPObject(CObject):
    """
    Python backing class for Primative Object Classes
    (has a value property which contains a Python type)
    """
    __slots__ = ['value']

    def __init__(self, this_class):
        ### XXX TEMP
        super().__init__(this_class)
        self.value = None       # set by init method

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
        i = self.fp.cb[self.fp.pc]
        return "<Continuation: %s:%s>" % (i.fn, i.where)
        
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
        return ["value"]

    def defn(self):
        return self.fp.cb[self.fp.pc].fn_where()

class CClosure(CCallable):
    """
    A Callable instance backed by a Closure (VM code + scope)
    NOTE: opaque (no Class methods to expose innards) for now
    """
    def __init__(self, code, scope, doc=None):
        super().__init__(Closure)
        self.code = code
        self.scope = scope
        self.setprop(const.DOC, mkstr(doc or ""))

    def __repr__(self):
        return "<Closure: %s>" % self.code[0].fn_where()
        
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
        return self.code[0].fn_where()

class CBClosure(CClosure):
    """
    create closure for a {} block
    (hidden in backtraces)
    not currently visible to user
    (unless flow control implemented by passing block closure pointers)
    """
    def __repr__(self):
        i = self.code[0]
        return "<CBClosure: %s:%s>" % (i.fn, i.where)
        
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
        # *THIS* is the place "this" is explicitly passed!!!
        vm.args.insert(0, self.obj) # prepend saved "this" to arguments
        self.method.invoke(vm)      # return value in AC

    def args(self):
        return self.method.args()[1:] # omit "this" arg

    def defn(self):
        return self.method.defn()

# Calling Python functions (ie; primative class methods) was orignally
# implemented as a Closure with two VM instructions (pycall, return).
# The CObject.invoke method avoids that.

class CPyFunc(CCallable):
    """
    A Callable instance backed by a Python function
    """
    def __init__(self, func):
        super().__init__(PyFunc)
        # detect pyfunc() calls on a pre-decorated function
        if isinstance(func, CPyFunc):
            # Python programming error, want Python backtrace:
            raise Exception("double wrapping %s" % func.func)
        self.func = func
        # make sure PyFunc.__doc never shows through
        self.setprop(const.DOC, _mkstr(func.__doc__ or ""))

    def __repr__(self):
        return "<PyFunc: %s>" % self.func.__name__
        
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
        import inspect
        fas = inspect.getfullargspec(self.func)
        args = list(fas.args)
        if fas.varargs:
            args.append('...' + fas.varargs)
        return args

    def defn(self):
        co = self.func.__code__
        fname = co.co_filename
        if fname.startswith(CWD_SEP):
            fname = fname[len(CWD_SEP):]
        return "%s:%s" % (fname, co.co_firstlineno)

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
    creates an interpreter Primative Object of Class `this_class`
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
    used to create System object, lexer tokens
    """
    #assert(not __initialized)
    o = CObject(Object)
    o.props.update(props)
    return o

################ use once System.types initialized

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
        for x in s.value:       # XXX check if List
            if x not in visited and check(x):
                return True
        return False
    return check(this_class)

def instance_of(this, classes):
    """
    test if `this` is an instance of any Class in `classes` list
    `this` is CObject
    `classes` is list of Classes (CObjects of class or subclasses of Class)
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

# metaclass for PObjects (creates Python CPObject)
PClass = defclass(Class, 'PClass', [Class],
                  doc="Metaclass for Primitive/Python value Classes")

# Primative Object Base Class
# superclass (with .value) of Classes that are wrappers around Python classes
PObject = defclass(PClass, 'PObject', [Object],
                   doc="Base class for Primitive/Python value Classes")

# wrappers, with .value

# XXX own metaclass to return singleton?
Null = defclass(PClass, 'Null', [PObject],
                doc="Built-on Class of `null` value") # XXX singleton
# XXX own metaclass to return doubleton values? subclass into two singletons??
Bool = defclass(PClass, 'Bool', [PObject],
                doc="Built-in Class for `true` and `false` values")

# pure virtual base:
Iterable = defclass(PClass, 'Iterable', [PObject],
                    doc="Virtual base Class classes that can be iterated over")

List = defclass(PClass, 'List', [Iterable],
                doc="Built-in mutable sequence Class")
Str = defclass(PClass, 'Str', [Iterable],
               doc="Built-in immutable Unicode string Class")
Dict  = defclass(PClass, 'Dict', [Iterable],
                 doc="Built-in dictionary mapping Class")

# non-iterable:
Number = defclass(PClass, 'Number', [PObject],
                  doc="Built-in int/float wrapper Class")

PyIterable = defclass(PClass, 'PyIterable', [Iterable],
                      doc="""
    Wrapper for Python 'iterable' Objects
    (classes which can generate iterators)
    returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), PyIterable.range(),
    """)

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

# internal object w/ direct invoke methods
#       (avoids binop lookup and List construction on each call)

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
PyIterator = defclass(Class, 'PyIterator', [Object],
                      doc="Built-in Class for a wrapper around a Python iterator")

################

null_value = _new_pobj(Null, None)

# create (only) instances of true/false (a doubleton)!
# subclass Bool into True and False singleton Classes??
true_val = _new_pobj(Bool, True)
false_val = _new_pobj(Bool, False)

################

# utility called by VM jumpn/jumpe: NOT a method/pyfunc
# (had originally planned to have all Classes have an is_true method)
def is_true(obj):
    """
    return Python True/False for an object
    non-premature optimization:
    only "null" and "false" objects, and zero are false
    """
    if obj is false_val or obj is null_value:
        return False
    if hasattr(obj, 'value') and obj.value == 0: # faster than isinstance?
        return False
    return True

################ Object -- the base type for all instances and classes

@pyfunc
def obj_create(this_class, *args):
    """
    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    """
    return CObject(this_class)

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
    return mkiterable(iter(this.props))

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
    this.props.pop(name)
    return null_value

@pyfunc
def obj_putprop(l, r, value):
    """
    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    """
    # XXX check r is Str!!!
    # implement access via descriptors??
    l.setprop(r.value, value)
    return value                # lhsop MUST return value

# NOTE! utility, not method
# XXX return (obj, value) to avoid generating BoundMethod?
def find_in_supers(l, rv):
    """
    breadth first search of superclass methods/properties
    """
    c = l.getclass()

    supers = c.getprop(const.SUPERS)
    q = []                      # queue
    seen = set()

    while True:
        if not supers or supers is null_value:
            break

        for s in supers.value:  # XXX check
            q.append(s)
            seen.add(s)

        if not q:
            break

        c = q.pop(0)            # front of queue
        if c.hasprop(rv):
            return c.getprop(rv)

        methods = c.getprop(const.METHODS)
        if methods and methods is not null_value:
            m = methods.value.get(rv) # Dict
            if m and m is not null_value:
                return CBoundMethod(l, m)

        supers = c.getprop(const.SUPERS)

    return null_value

# NOTE! utility, not method
# XXX return (obj, value) to avoid generating BoundMethod?
def find_in_class(l, rv):
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
    if methods and methods is not null_value:
        m = methods.value.get(rv) # Dict
        if m and m is not null_value:
            return CBoundMethod(l, m)

    return find_in_supers(l, rv)

@pyfunc
def obj_getprop(l, r):
    """
    Object getprop method/operator
    return `r` (String) property of object `l`
    """
    rv = r.value              # XXX must be Str
    if l.hasprop(rv):
        return l.getprop(rv)
    return find_in_class(l, rv) # may return BoundMethod

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
            if op in ops.value:
                return ops.value[op]

        supers = c.getprop(const.SUPERS)
        if supers and supers != null_value:
            # XXX check if List
            for s in supers.value:
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
    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    """
    return find_in_supers(this, prop.value) # XXX check for CPObject

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
def obj_call(l, *args):
    """
    default Object '(' binop
    (fatal error)
    """
    raise UError("%s does not have '(' binop" % l.classname())

@pyfunc
def obj_instance_of(this, c):
    """
    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    """
    if subclass_of(c.getclass(), [List]):
        c = c.value             # get Python list
    else:
        c = [c]                 # make Python list
    return mkbool(instance_of(this, c))

Object.setprop(const.METHODS, _mkdict({
    const.INIT: obj_init,
    'getclass': obj_getclass,
    'setclass': obj_setclass,
    'instance_of': obj_instance_of,
    'delprop': obj_delprop,
    'putprop': obj_putprop,
    'getprop': obj_getprop,
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
    '.': obj_putprop                # same as putprop!!
}))

################ Class -- base type for Classes (a MetaClass)

@pyfunc
def class_init(this_class, props):
    """
    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    """
    # XXX check props is a Dict!
    for key, val in props.value.items():
        # XXX depends on key as Python str
        # XXX check val is a Dict!
        if key == 'props':
            # XXX check for overlap with methods?
            # XXX use descriptors for methods/members?!!!
            this_class.props.update(val.value)
            continue
        ikey = const.CLASS_PROPS.get(key)
        if not ikey:
            metaclass = this_class.classname()
            raise UError("Unknown %s property %s" % (metaclass, key))
        this_class.props[ikey] = val

    if const.NAME not in this_class.props:
        raise UError("Class.new requires '%s'"  % (metaclass, const.NAME))

    # XXX complain if NAME doesn't start with a capitol letter??

    if const.SUPERS not in this_class.props:
        # XXX complain??
        this_class.setprop(const.SUPERS, wrap([Object]))
    return null_value

@pyfunc
def class_call(this_class, *args):
    """
    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    """
    raise UError("call %s.new!" % this_class.getprop(const.NAME).value)

@pyfunc
def class_subclass_of(this, c):
    """
    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    """
    if subclass_of(c.getclass(), List):
        c = c.value             # get Python list
    else:
        c = [c]                 # make Python list
    return mkbool(subclass_of(this, c))

# Class: a meta-class: all Classes are instances of a meta-class
# (Class.new creates a new Class)
Class.setprop(const.METHODS, _mkdict({
    const.CREATE: obj_create,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member
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
    return _new_pobj(Number, len(this.value)) # XXX look up by name?

@pyfunc
def pobj_str(this):
    """
    return human-friendly string representation of `this`
    (uses Python str function on value)
    """
    return mkstr(str(this.value))

@pyfunc
def pobj_repr(this):
    """
    return less human-friendly string representation of `this`
    (use Python repr function on value)
    """
    return mkstr(repr(this.value))

@pyfunc
def pobj_reprx(this):
    """
    for debug: show Class name, and Python repr
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l.value)))

@pyfunc
def pobj_init(l, value):
    """
    default PObject init method
    (fatal error)
    """
    raise UError("{} missing init method".format(l.classname()))

@pyfunc
def pobj_init0(l, value):
    """
    default PObject init0 method
    (fatal error)
    """
    raise UError("{} missing init0 method".format(l.classname()))

@pyfunc
def pobj_ident(l, r):
    """
    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    """
    lv = l.value
    rv = r.value
    return mkbool(lv is rv)

@pyfunc
def pobj_differ(l, r):
    """
    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    """
    lv = l.value
    rv = r.value
    return mkbool(lv is not rv)

PObject.setprop(const.METHODS, _mkdict({
    'repr': pobj_repr,
    'reprx': pobj_reprx,
    const.INIT: pobj_init,
    'init0': pobj_init0
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
    returns formatted string for args (as if a native function)
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

################ Iterable base class

@pyfunc
def iterable_iter(this):
    """
    return forward iterator
    """
    return pyiterator(iter(this.value))

@pyfunc
def iterable_reversed(this):
    """
    return reverse iterator
    """
    # XXX handle TypeError for "not reversible"
    return pyiterator(reversed(this.value))

@pyfunc
def iterable_sorted(this):
    """
    return sorted list values (or keys)
    """
    return wrap(sorted(this.value))

# for_each, each_for, map, map2 in bootstrap.xxl
Iterable.setprop(const.METHODS, _mkdict({
    'iter': iterable_iter,
    'reversed': iterable_reversed,
    'sorted': iterable_sorted
}))

################ PyIterable

# subclass of Iterable for mkiterable callers: Dict.{key,value,item}s()
PyIterable.setprop(const.METHODS, _mkdict({
    'to_str': pobj_reprx
}))

@pyfunc
def pyiterable_range(*args):
    """
    return an Iterable for an integer range
    (an Iterable can be iterated over any number of times)

    range(10): returns Iterable for 0..9
    range(1,10): returns Iterable for 1..9
    range(1,10,2): returns Iterable for odd numbers 1..9
    """
    if len(args) == 1:
        r = range(args[0].value) # XXX getint?
    elif len(args) == 2:
        r = range(args[0].value, args[1].value) # XXX getint?
    elif len(args) == 3:
        r = range(args[0].value, args[1].value, args[2].value) # XXX getint?
    else:
        raise UError("range requires one to three arguments")

    return mkiterable(r)

PyIterable.setprop('range', pyiterable_range) # static method

################ Dict

@pyfunc
def dict_put(l, r, value):
    """
    put `value` into Dict `l` index `r`
    """
    entry = r.value             # XXX
    l.value[entry] = value
    return value                # lhsop MUST return value

@pyfunc
def dict_get(l, r):
    """
    get entry `r` Dict from dict `l`
    """
    entry = r.value             # XXX
    ret = l.value.get(entry, null_value)
    return ret

@pyfunc
def dict_init0(obj):
    """
    called by Dict.init (in bootstrap.xxl)
    Dodges needing private metaclass for Dict
    """
    obj.value = {}
    return null_value

@pyfunc
def dict_pop(obj, arg):
    """
    remove Dict with specified key
    """
    return obj.value.pop(arg.value) # XXX check arg has value!!!

@pyfunc
def dict_items(this):
    """
    return Iterable for [key, value] value pairs
    """
    return mkiterable(this.value.items())

@pyfunc
def dict_keys(this):
    """
    return Iterable for Dict keys
    """
    return mkiterable(this.value.keys())

@pyfunc
def dict_values(this):
    """
    return Iterable for Dict values
    """
    return mkiterable(this.value.values())

Dict.setprop(const.METHODS, _mkdict({
    'init0': dict_init0,
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
def list_init0(l):
    """
    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    """
    l.value = []
    return null_value

@pyfunc
def list_append(this, item):
    """
    append `item` to `this` List
    """
    this.value.append(item)
    return null_value

@pyfunc
def list_pop(l, index=None):
    """
    Remove and return List item at `index` (default last)
    """
    if index is None:
        return l.value.pop()
    return l.value.pop(index.value) # XXX check if Number

@pyfunc
def list_get(l, r):
    """
    Return List item at index `r`
    """
    # XXX check if integer
    return l.value[r.value]

@pyfunc
def list_put(l, r, value):
    """
    Set List item at index `r` to `value`
    """
    # XXX check if integer
    l.value[r.value] = value
    return value		# lhsop MUST return value

# str, repr, for_each, each_for, map, map2 in bootstrap.xxl
List.setprop(const.METHODS, _mkdict({
    'append': list_append,
    'len': pobj_len,
    'pop': list_pop,
    # XXX slice(start[,end]) (return range of elements)
    'init0': list_init0,
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
    return _new_pobj(x.getclass(), -x.value)

@pyfunc
def add(l, r):
    """
    add `l` and `r`
    """
    lv = l.value
    rv = r.value
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
    rv = r.value
    if rv == 0:
        return l
    return _new_pobj(l.getclass(), lv - rv)

@pyfunc
def mul(l, r):
    """
    multiple `l` and `r`
    """
    lv = l.value
    rv = r.value
    if lv == 1:
        return r
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), l.value * r.value)

@pyfunc
def div(l, r):
    """
    divide `l` by `r`
    """
    lv = l.value
    rv = r.value
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), lv / rv)

def _eq(l, r):
    """
    call any time (not a pyfunc)
    takes CPObject, returns CPObject
    """
    return mkbool(l.value == r.value)

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
    return mkbool(l.value >= r.value)

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
    return mkbool(l.value <= r.value)

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
    rv = r.value
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
    rv = r.value
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
    return _new_pobj(this.getclass(), ~this.value)

@pyfunc
def num_to_float(this):
    """
    If value is a float, return `this`
    If value is an int, return a new Number object
    """
    if isinstance(this.value, float):
        return this
    return _new_pobj(this.getclass(), float(this.value))

@pyfunc
def num_to_int(this):
    """
    If value is an int, return `this`
    If value is a float, return a new Number object
    """
    if isinstance(this.value, int):
        return this
    return _new_pobj(this.getclass(), int(this.value))

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
    xv = x.value                # XXX getstr
    yv = y.value                # XXX getstr
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
    return _new_pobj(l.getclass(), l.value[r.value])

@pyfunc
def str_slice(this, start, end=None):
    """
    return a substring (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to rest of string
    """
    startv = start.value        # XXX check if int
    if end is not None:
        endv = end.value            # XXX check if int
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
        sep = sep.value         # XXX getstr
    if limit != -1:
        limit = limit.value     # XXX getint
    # will use current "Str" defn:
    return wrap(this.value.split(sep, limit))

@pyfunc
def str_ends_with(this, suff):
    """
    Return `true` if `this` ends with the suffix `suff`, `false` otherwise.
    """
    return mkbool(this.value.endswith(suff.value))

@pyfunc
def str_join(this, arg):
    """
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    """
    # XXX check arg is List (or Dict) of Str!
    # XXX XXX should allow an Iterable
    return _new_pobj(this.getclass(),
                     this.value.join([x.value for x in arg.value]))

@pyfunc
def str_ord(this):
    """
    Return the Unicode code point for a one-character string `this`
    """
    s = this.value              # XXX getstr
    if len(s) != 1:
        raise UError("Str.ord length != 1")
    return mknumber(ord(s))

@pyfunc
def str_starts_with(this, pref):
    """
    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    """
    return mkbool(this.value.startswith(pref.value))

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
    Convert string to integer Number
    `base` defaults to zero (accept 0xXXX for base 16)
    """
    if base is None:
        base = 0                # accept 0xXXX
    else:
        base = base.value
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
    return mkstr(chr(i.value)) # XXX getint

Str.setprop(const.METHODS, _mkdict({
    'ends_with': str_ends_with,
    'join': str_join,
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
    "(" method for `null` value (fatal error)
    commonly happens when a bad method name is used
    """
    raise UError("'null' called; bad method name?")

Null.setprop(const.METHODS, _mkdict({
    'repr': null_str
}))

Null.setprop(const.BINOPS, _mkdict({
    '(': null_call
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
        return true_val
    else:
        return false_val

################ PyObject

# PyObjects are created by System.pyimport("python_module")
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
            return {key: unwrap(val) for key, val in x.items()}
        return x
    # XXX complain??!!!
    return x

@pyfunc
def pyobj_getprop(l, r):
    """
    PyObject "." binop -- proxies to Python object getattr
    """
    # XXX r must be Str
    #   for access to Object properties?
    rv = r.value                # XXX getstr
    if hasattr(l.value, rv):
        v = getattr(l.value, rv) # get Python object attribute
    elif l.hasprop(rv):  # check Object properties (most likely empty)
        v = l.getprop(rv)
    else:
        # allow 'to_str' method so Object can be printed!!
        v = find_in_class(l, rv) # may return BoundMethod
    return wrap(v)

@pyfunc
def pyobj_getitem(l, r):
    """
    PyObject "[" binop
    """
    v = l.value[r.value]        # XXX unwrap(r)??
    return wrap(v)

@pyfunc
def pyobj_call(this, *args):
    a2 = [unwrap(x) for x in args]
    ret = this.value(*a2)
    return wrap(ret) # may create another PyObject!

PyObject.setprop(const.METHODS, _mkdict({
    const.INIT: pobj_init
    # NOTE!! pyobj_getprop doesn't search here!!!
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
    Python iterators are also iterables (return self)
    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method:

    Return the iterator object itself. This is required to allow
    both containers and iterators to be used with the for and in
    statements. This method corresponds to the tp_iter slot of the
    type structure for Python objects in the Python/C API.
    """
    return this

@pyvmfunc
def pyiterator_next(vm, this, finished_continuation):
    """
    `finished` should be a CContinuation
    (eg; block leave label or "return")
    to call when iterator exhausted
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
        mi.setprop(const.MODINFO_DEBUG_BOOTSTRAP, true_val)

    scope = module.scope

    if fname is not None:
        mi.setprop(const.MODINFO_FILE, mkstr(fname))

    if not parser_vmx:
        # XXX _COULD_ choose parser based on source file name!!!
        #  (could have a file with SUFFIX => VMXFILE mappings)
        parser_vmx = os.environ.get('XXL_PARSER', 'parser.vmx')

    mi.setprop(const.MODINFO_PARSER_VMX, mkstr(parser_vmx))

    return mi

# "where Modules come from"
# called by:
#       xxl.py (startup)
#       sys__import (System._import function)
# XXX should be moduleclass_new?!!
# XXX take optional bootstrap_vmx arg??
def new_module(fname, main=False, argv=[], parser_vmx=None):
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
    if fname and fname in md.value: # previously loaded?
        return md.value[fname], None # yes; return it, no bootstrap needed

    scope = scopes.Scope(None)  # create root scope for module
    mod = CModule(scope)

    init_scope(scope)           # populate scope w/ true/false/...

    if fname:
        system.create_sys_object(scope, argv) # new System object XXX TEMP

        # XXX Dict indexed by Python str
        md.value[fname] = mod   # save as previously loaded

    mi = new_modinfo(main=main, module=mod, fname=fname, parser_vmx=parser_vmx)
    mod.modinfo = mi
    scope.defvar(const.MODINFO, mi) # make ModInfo visible in module namespace

    if fname is None:           # internal module?
        return mod, None

    # XXX take as optional argument??
    bootstrap_vmx = os.environ.get('XXL_BOOTSTRAP', 'bootstrap.vmx')

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
    mod = this.getprop(const.MODINFO_MODULE) # XXX check return
    code = vmx.load_vm_json(fname.value, mod.scope) # XXX getstr
    return CClosure(code, mod.scope)

@pyfunc
def modinfo_assemble(this, tree, srcfile):
    """
    `tree`: List of Lists of VM code
    `srcfile`: source of code
    returns Closure in __modinfo.module initial scope
    """
    mod = this.getprop(const.MODINFO_MODULE) # XXX check
    code = vmx.assemble(mod.scope, tree, srcfile)

    # turn into Closure in scope
    #   (any variables created are globals):
    return CClosure(code, mod.scope)

    return system.assemble(mod.scope, tree, srcfile)

ModInfo.setprop(const.METHODS, _mkdict({
    'load_vmx': modinfo_load_vmx, # create Closure from .vmx file
    'assemble': modinfo_assemble  # create Closure from List of instruction Lists
}))

################################################################

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
        return new_by_name('Number', value)

    if isinstance(value, str):
        return mkstr(value)

    # XXX handle bytes??

    # tuple added for dict_items iterator
    # but exclude tuple-like things (os.stat results, namedtuples)
    if isinstance(value, list) or type(value) is tuple:
        return new_by_name('List', [wrap(x) for x in value])

    if value is None:
        return null_value

    # XXX handle dict?!!!

    #if hasattr(value, '__next__'): return pyiterator(value)???
    # Add next/iter/reversed methods to PyObject??????

    return new_by_name(const.PYOBJECT, value)

################################################################

def add_to_classes(name, value):
    classes_scope.defvar(name, value)

# NOT classes!
add_to_classes('true', true_val)
add_to_classes('false', false_val)
add_to_classes('null', null_value)

def defmodule(name, mod):
    """
    declare an internal Module by name
    `name` is Python str
    `mod` is CModule
    """
    assert(isinstance(mod, CModule))
    md = Module.getprop('modules') # module Dict
    md.value[name] = mod

classes_module = None           # XXX TEMP?

def classes_init():
    """
    call once on startup
    """
    # UTTERLY VILE: either hide in a "make_internal_module"
    #   or do it more cleanly!!!!
    #   declare classes_module up top???????????
    global classes_module       # XXX TEMP?
    classes_module, _ = new_module(None)
    classes_module.scope = classes_scope # XXX YUK
    # NOTE: below crushes __modinfo!!!??? (do we care???)
    classes_module.props = classes_scope.vars # XXX XXX DOUBLY SO
    defmodule('classes', classes_module)

def init_scope(iscope):
    """
    copy a limited set of types/values to each Module initial Scope `iscope`
    NOTE: they all end up writable!!!
    (if compiler gets "const" stmt, pre-declare them as "const"?)
    """
    for x in ['true', 'false', 'null', 'Class']:
        iscope.defvar(x, classes_scope.lookup(x))

# earlier?!!
__initialized = True        # don't allow _mkXXX any more
