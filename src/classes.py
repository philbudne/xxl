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

# used to initialize new System.types objects in new top level (module) scopes.
# for _current_ definitions, need to lookup in iscope (use find_sys_type)
sys_types = {}

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

        n = c.getprop(const.NAME).value # XXX guard!!
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

    def __repr__(self):
        """show wrapped value"""
        return '<%s: %s at %#x>' % \
            (self.classname(), repr(self.value), id(self))

#    def str(self):              # XXX EXP for PyObject
#        return str(self)

#    def repr(self):             # XXX EXP for PyObject
#        return repr(self)


################

class CContinuation(CObject):
    """
    A Callable instance backed by a native (VM) Continuation
    NOTE: opaque (no Class methods to expose innerds) for now
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

class CClosure(CObject):
    """
    A Callable instance backed by a Closure (VM code + scope)
    NOTE: opaque (no Class methods to expose innerds) for now
    """
    def __init__(self, code, scope):
        super().__init__(Closure)
        self.code = code
        self.scope = scope

    def __repr__(self):
        i = self.code[0]
        return "<Closure: %s:%s>" % (i.fn, i.where)
        
    def invoke(self, vm):
        vm.save_frame(True)     # show=True
        # return or leave label Continuation will be generated from FP
        #       by "args" or "[lu]scope" Instr (first Instr in code)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope
        # NOTE! vm.args picked up by "args" opcode!

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
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope

class CBoundMethod(CObject):
    """
    A method bound to an object
    created when Object.methodname dereferenced
    XXX bring back use of "method" opcode as optimization
        which fetches method and calls invoke without creating
        a BoundMethod Object!!!???
    NOTE: opaque (no Class methods to expose innerds) for now
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

# Calling Python functions (ie; primative class methods) was orignally
# implemented as a Closure with two VM instructions (pycall, return).
# The CObject.invoke method avoids that.

class CPyFunc(CObject):
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
    assert(not __initialized)
    return _new_pobj(Str, s)

def _mkobj(props):
    """
    used to create System, System.types, tokens
    """
    #assert(not __initialized)
    o = CObject(Object)
    o.props.update(props)       # copy, so System.types is module local
    return o

################ use once System.types initialized

def mkstr(s, scope):
    """
    used to create Str from Python str, once up and running
    """
    assert(__initialized)
    return system.create_sys_type('Str', scope, s)

def mknumber(n, scope):
    """
    used to create Number from Python int/float, once up and running
    """
    assert(__initialized)
    return system.create_sys_type('Number', scope, n)

def mkiterable(i, scope):
    assert(__initialized)
    return system.create_sys_type('PyIterable', scope, i)

################
null_value = None               # forward

def subclass_of(klass, bases):
    """
    `klass` is CObject for a Class
    `bases` is Python list of CObjects
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
    return check(klass)

def instance_of(obj, classes):
    """
    `obj` is CObject
    `classes` is Class or Python list of Classes
    """
    return subclass_of(obj.getclass(), classes)

################################################################

# backpatch Classes when Str/List available:
_saved_supers = {}
_saved_names = {}
Str = None
List = None

def defclass(metaclass, name, supers=None, publish=True):
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
    else:
        _saved_names[class_obj] = name

    if supers:
        if List:                # List class available?
            class_obj.setprop(const.SUPERS, _mklist(supers))
        else:
            _saved_supers[class_obj] = supers

    if publish:
        sys_types[name] = class_obj
    return class_obj

# base metaclass
Class = defclass(None, 'Class')
Class.setclass(Class)             # circular! Class.new creates a new Class!
# supers set to [Object] below

# root Class; circular with "Class" metaclass, so defined second.
Object = defclass(Class, 'Object', []) # root Class

# metaclass for PObjects (creates Python CPObject)
PClass = defclass(Class, 'PClass', [Class])

# Primative Object Base Class
# superclass (with .value) of Classes that are wrappers around Python classes
PObject = defclass(PClass, 'PObject', [Object])

# wrappers, with .value

# XXX own metaclass to return singleton?
Null = defclass(PClass, 'Null', [PObject]) # XXX singleton
# XXX own metaclass to return doubleton values? subclass into two singletons??
Bool = defclass(PClass, 'Bool', [PObject])

# pure virtual base:
Iterable = defclass(PClass, 'Iterable', [PObject])

List = defclass(PClass, 'List', [Iterable])
Str = defclass(PClass, 'Str', [Iterable])
Dict  = defclass(PClass, 'Dict', [Iterable])

# non-iterable:
Number = defclass(PClass, 'Number', [PObject])

PyIterable = defclass(PClass, 'PyIterable', [Iterable])

################
# Str, List now exist:
# set Class metaclass super list
Class.setprop(const.SUPERS, _mklist([Object]))

# do fixups for Strs and Lists in primative Classes
for klass, name in _saved_names.items():
    klass.setprop(const.NAME, _mkstr(name))
for klass, supers in _saved_supers.items():
    klass.setprop(const.SUPERS, _mklist(supers))

# internal object w/ direct invoke methods
#       (avoids binop lookup and List construction on each call)
# all backed by Python CXyZzy classes with invoke methods:
# XXX use metaclass (CClass?) that prohibits user call of 'new' method?
BoundMethod = defclass(Class, 'BoundMethod', [Object])
Closure = defclass(Class, 'Closure', [Object])
Continuation = defclass(Class, 'Continuation', [Object])
PyFunc = defclass(Class, 'PyFunc', [Object])
PyVMFunc = defclass(Class, 'PyVMFunc', [Object])

# wrapper around a Python iterator (w/ next method)
PyIterator = defclass(Class, 'PyIterator', [Object])

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

@pyvmfunc
def obj_create(vm, this_class, *args):
    """
    default "new" method for Object (and therefore Class)
    makes an instance of this_class
    Creates a Python CObject, calls this_class's 'init' method with args
    """
    return CObject(this_class)

@pyfunc
def obj_init(this_obj, *args):
    if len(args) > 0:
        raise UError("%s.%s takes no arguments" %
                        (this_obj.classname(), const.INIT))
    return null_value

@pyvmfunc
def obj_str(vm, l):
    return mkstr(str(l), vm.scope) # native method that calls this.repr()?

@pyvmfunc
def obj_repr(vm, l):
    return mkstr(repr(l), vm.scope)

@pyvmfunc
def obj_reprx(vm, l):
    """
    for debug: show Class, and Python value (which may include id?)
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l)), vm.scope)

@pyfunc
def obj_ident(x, y):            # SNOBOL4 IDENT
    return mkbool(x is y)

@pyfunc
def obj_differ(x, y):           # SNOBOL4 DIFFER
    return mkbool(x is not y)

def _not(x):
    """
    not a pyfunc (may call at any time)
    takes CObject, returns CObject
    """
    return mkbool(not is_true(x))

# XXX do this in pobj_not? all other objects always true????
@pyfunc
def obj_not(x):
    """Object unary ! operator"""
    return _not(x)

@pyfunc
def obj_putprop(l, r, value):
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

    raise UError("%s %s %s not found" % (obj, optype, op))

@pyfunc
def obj_get_in_supers(l, r):
    """
    Object ".." operator; for calling superclass methods
    """
    return find_in_supers(l, r.value) # XXX check for CPObject

# once upon a time class was stored as '__class' property,
# but it was messy when cloning.
@pyfunc
def obj_getclass(this):
    return this.getclass()

@pyfunc
def obj_setclass(this, klass):
    return this.setclass(klass)

@pyfunc
def obj_call(l, *args):
    """
    default '(' binop
    """
    raise UError("%s not callable" % l.classname())

@pyfunc
def obj_instance_of(l, c):
    """
    `l` is Object
    `c` is Class or List of Classes
    """
    if subclass_of(c.getclass(), [List]):
        c = c.value             # get Python list
    else:
        c = [c]                 # make Python list
    return mkbool(instance_of(l, c))

Object.setprop(const.METHODS, _mkdict({
    const.INIT: obj_init,
    'class': obj_getclass,
    'getclass': obj_getclass,
    'setclass': obj_setclass,
    'instance_of': obj_instance_of,
    'putprop': obj_putprop,
    'getprop': obj_getprop,
    # 'str' in bootstrap.xxl -- invokes repr.
    'repr': obj_repr,
    'reprx': obj_reprx,
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

@pyvmfunc
def class_init(vm, this_class, props):
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
        this_class.setprop(const.SUPERS, wrap([Object], vm.scope))
    return null_value

@pyfunc
def class_call(this_class, *args):
    """
    "(" binop for Class
    """
    # PLB: I keep on doing this (Python fingers)
    raise UError("call %s.new!" % this_class.getprop(const.NAME).value)

@pyfunc
def class_subclass_of(l, c):
    """
    `l` is Class
    `c` is Class or List of Classes
    """
    if subclass_of(c.getclass(), List):
        c = c.value             # get Python list
    else:
        c = [c]                 # make Python list
    return mkbool(subclass_of(l, c))

# Class: a meta-class: all Classes are instances of a meta-class
# (Class.new creates a new Class)
Class.setprop(const.METHODS, _mkdict({
    const.CREATE: obj_create,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member
    "subclass_of": class_subclass_of
}))

Class.setprop(const.BINOPS, _mkdict({
    '(': class_call
}))

################ PClass -- metaclass for PObjects

@pyvmfunc
def pclass_create(vm, this_class):
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
def pobj_len(l):
    return _new_pobj(Number, len(l.value)) # XXX look up by name?

@pyvmfunc
def pobj_str(vm, l):
    """
    use Python str function on value
    """
    return mkstr(str(l.value), vm.scope)

@pyvmfunc
def pobj_repr(vm, l):
    """
    use Python repr function on value
    """
    return mkstr(repr(l.value), vm.scope)

@pyvmfunc
def pobj_reprx(vm, l):
    """
    for debug: show Class, and Python value
    XXX show id()? of value???
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l.value)),
                 vm.scope)

@pyfunc
def pobj_init(l, value):
    raise UError("{} missing init method".format(l.classname()))

@pyfunc
def pobj_init0(l, value):
    raise UError("{} missing init0 method".format(l.classname()))

# XXX unused?
@pyfunc
def pobj_ge(l, r):
    lv = l.value
    rv = r.value
    # XXX not right!!
    if isinstance(lv, float) or isinstance(rv, float):
        return mkbool(float(lv) >= float(rv))
    if isinstance(lv, int) or isinstance(rv, int):
        return mkbool(int(lv) >= int(rv))
    return mkbool(str(lv) >= str(rv))

@pyfunc
def pobj_ident(l, r):
    lv = l.value
    rv = r.value
    return mkbool(lv is rv)

@pyfunc
def pobj_differ(l, r):
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
    '!==': pobj_differ
}))

################ Iterable base class

@pyfunc
def iterable_iter(this):
    return pyiterator(iter(this.value))

@pyfunc
def iterable_reversed(this):
    # XXX handle TypeError for "not reversible"
    return pyiterator(reversed(this.value))

# for_each, each_for, map, map2 in bootstrap.xxl
Iterable.setprop(const.METHODS, _mkdict({
    'iter': iterable_iter,
    'reversed': iterable_reversed,
}))

################ PyIterable

# subclass of Iterable for mkiterable callers: Dict.{key,value,item}s()
PyIterable.setprop(const.METHODS, _mkdict({
    'str': pobj_reprx 
}))

@pyvmfunc
def pyiterable_range(vm, *args):
    if len(args) == 1:
        r = range(args[0].value) # XXX getint?
    elif len(args) == 2:
        r = range(args[0].value, args[1].value) # XXX getint?
    elif len(args) == 3:
        r = range(args[0].value, args[1].value, args[2].value) # XXX getint?
    else:
        raise UError("range requires one to three arguments")

    return mkiterable(r, vm.scope)

PyIterable.setprop('range', pyiterable_range) # static method

################ Dict

@pyfunc
def dict_put(l, r, value):
    entry = r.value             # XXX
    l.value[entry] = value
    return value                # lhsop MUST return value

@pyfunc
def dict_get(l, r):
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
    return obj.value.pop(arg.value) # XXX check arg has value!!!

@pyvmfunc
def dict_items(vm, this):
    return mkiterable(this.value.items(), vm.scope)

@pyvmfunc
def dict_keys(vm, this):
    return mkiterable(this.value.keys(), vm.scope)

@pyvmfunc
def dict_values(vm, this):
    return mkiterable(this.value.values(), vm.scope)

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
def list_append(l, item):
    l.value.append(item)
    return null_value

@pyfunc
def list_pop(l,item=None):
    if item is None:
        return l.value.pop()
    return l.value.pop(item.value) # XXX check if Number

@pyfunc
def list_get(l, r):
    # XXX check if integer
    return l.value[r.value]

@pyfunc
def list_put(l, r, value):
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
    return _new_pobj(x.getclass(), -x.value)

@pyfunc
def add(x, y):
    # XXX check if one zero?
    return _new_pobj(x.getclass(), x.value + y.value)

@pyfunc
def sub(x, y):
    # XXX check if y zero?
    return _new_pobj(x.getclass(), x.value - y.value)

@pyfunc
def mul(x, y):
    # XXX check if one is one?
    return _new_pobj(x.getclass(), x.value * y.value)

@pyfunc
def div(x, y):
    # XXX check if y is one? zero??!!
    return _new_pobj(x.getclass(), x.value / y.value)

def _eq(l, r):
    """
    call any time (not a pyfunc)
    takes CPObject, returns CPObject
    """
    return mkbool(l.value == r.value)

@pyfunc
def eq(l, r):
    return _eq(l, r)

@pyfunc
def ne(l, r):
    return _not(_eq(l, r))

def _ge(l, r):
    return mkbool(l.value >= r.value)

@pyfunc
def ge(l, r):
    return _ge(l, r)

@pyfunc
def lt(l, r):
    return _not(_ge(l, r))

def _le(l, r):
    return mkbool(l.value <= r.value)

@pyfunc
def le(l, r):
    return _le(l, r)

@pyfunc
def gt(l, r):
    return _not(_le(l, r))

@pyfunc
def num_init(obj, value):
    if instance_of(value, [Str]):
        # (move this to Str.to_number()???)
        v = value.value
        try:
            obj.value = int(v)
        except:
            obj.value = float(v)
    elif instance_of(value, [Number]):
        # XXX intercept in metaclass 'new' and return "this"?
        obj.value = value.value
    else:
        raise UError("{}.new needs Str or Number".format(obj.getclass().name))
    return null_value

@pyfunc
def bitand(l, r):
    return _new_pobj(l.getclass(), l.value & r.value)

@pyfunc
def bitor(l, r):
    return _new_pobj(l.getclass(), l.value | r.value)

Number.setprop(const.METHODS, _mkdict({
    const.INIT: num_init
}))

Number.setprop(const.UNOPS, _mkdict({
    '-': neg,
}))
Number.setprop(const.BINOPS, _mkdict({
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    # XXX Orderable mixin?
    '==': eq,
    '!=': ne,
    '>=': ge,
    '<=': le,
    '>': gt,
    '<': lt,
    # Int only!
    '&': bitand,
    '|': bitor,
}))

################ Str

@pyfunc
def str_concat(x, y):
    xv = x.value                # XXX getstr
    yv = y.value                # XXX getstr
    if xv == "":
        return y
    if yv == "":
        return x
    return _new_pobj(x.getclass(), xv + yv)

@pyfunc
def str_get(l, r):              # [] operator
    # XXX check if r is integer
    return _new_pobj(l.getclass(), l.value[r.value])

@pyfunc
def str_slice(l, a, b=None):
    av = a.value                # XXX check if int
    if b is not None:
        bv = b.value            # XXX check if int
        ret = l.value[av:bv]
    else:
        ret = l.value[av:]
    return _new_pobj(l.getclass(), ret)

@pyvmfunc
def str_split(vm, this, sep=None, limit=-1):
    if sep is not None:
        sep = sep.value         # XXX getstr
    if limit != -1:
        limit = limit.value     # XXX getint
    # will use current "Str" defn:
    return wrap(this.value.split(sep, limit), vm.scope)

@pyfunc
def str_ends_with(this, arg):
    return mkbool(this.value.endswith(arg.value))

@pyfunc
def str_join(this, arg):
    # XXX check arg is List (or Dict) of Str!
    return _new_pobj(this.getclass(),
                     this.value.join([x.value for x in arg.value]))

@pyvmfunc
def str_ord(vm, this):
    s = this.value              # XXX getstr
    if len(s) != 1:
        raise UError("Str.ord length != 1")
    return mknumber(ord(s), vm.scope)

@pyfunc
def str_starts_with(this, arg):
    return mkbool(this.value.startswith(arg.value))

@pyfunc
def str_str(this):
    return this                 # identity

@pyfunc
def str_strip(this):
    return _new_pobj(this.getclass(), this.value.strip()) # XXX getstr

Str.setprop(const.METHODS, _mkdict({
    'ends_with': str_ends_with,
    'join': str_join,
    'len': pobj_len,
    'ord': str_ord,
    'slice': str_slice,
    'split': str_split,
    'starts_with': str_starts_with,
    'str': str_str,
    'strip': str_strip,
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

################ Null

@pyvmfunc
def null_str(vm, this):
    return mkstr("null", vm.scope)

@pyfunc
def null_call(this, *args):
    raise UError("'null' called; bad method name?")

Null.setprop(const.METHODS, _mkdict({
    'repr': null_str
}))

Null.setprop(const.BINOPS, _mkdict({
    '(': null_call
}))

################ Bool

@pyvmfunc
def bool_str(vm, this):
    if this.value:
        return mkstr("true", vm.scope)
    else:
        return mkstr("false", vm.scope)

# XXX have own MetaClass "new" to return one of the doubleton values?
# XXX subclass into True and False singleton classes????
Bool.setprop(const.METHODS, _mkdict({
    'repr': bool_str
}))

def mkbool(val):
    """
    convert Python truthiness
    to language true or false Object
    XXX use find_sys_type(NAME)?
    """
    if val:
        return true_val
    else:
        return false_val

################ PyObject

# PyObjects are created by System.pyimport("python_module")
# and are proxy wrappers around generic/naive Python objects

PyObject = defclass(PClass, const.PYOBJECT, [Object])

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

@pyvmfunc
def pyobj_getprop(vm, l, r):
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
        # allow 'str' method so Object can be printed!!
        v = find_in_class(l, rv) # may return BoundMethod
    return wrap(v, vm.scope)

@pyvmfunc
def pyobj_getitem(vm, l, r):
    """
    PyObject "[" binop
    """
    v = l.value[r.value]        # XXX unwrap(r)??
    return wrap(v, vm.scope)

@pyvmfunc
def pyobj_call(vm, this, *args):
    a2 = [unwrap(x) for x in args]
    ret = this.value(*a2)
    return wrap(ret, vm.scope) # may create another PyObject!

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
def pyiterator_next(vm, this, finished):
    """
    `finished` should be a Continuation
    (eg; block leave label or "return")
    to call when iterator exhausted
    """
    try:
        return wrap(next(this.value), vm.scope)
    except StopIteration:
        # here to avoid check on each iteration:
        if not isinstance(finished, CContinuation):
            raise UError("iterator .next takes Continuation")
        vm.args = []            # default to null
        finished.invoke(vm)     # alters VM state; return immediately!
    return null_value

PyIterator.setprop(const.METHODS, _mkdict({
    'iter': pyiterator_iter,    # see above
    'next': pyiterator_next
}))

################################################################

# Module is what "import" function returns
#       properties are the namespace of the target Module

# XXX need ModuleClass metaclass (unless/until Scope objects visible!!)
Module = defclass(Class, 'Module', [Object])
Module.setprop('modules', _mkdict({}))

class CModule(CObject):
    __slots__ = ['scope', 'modinfo']
    def __init__(self, scope):
        super().__init__(Module)
        self.scope = scope      # HIDDEN!
        self.modinfo = None     # convenience; __modinfo should suffice

# ModInfo is the __modinfo Object inside each Module
#       (for use inside the module)
ModInfo = defclass(Class, 'ModInfo', [Object])

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

    mi.setprop(const.MODINFO_FILE, mkstr(fname, scope))

    if not parser_vmx:
        # XXX _COULD_ choose parser based on source file name!!!
        #  (could have a file with SUFFIX => VMXFILE mappings)
        parser_vmx = os.environ.get('XXL_PARSER', 'parser.vmx')

    mi.setprop(const.MODINFO_PARSER_VMX, mkstr(parser_vmx, scope))

    return mi

# "where Modules come from"
# called by:
#       xxl.py (startup)
#       sys_import (System.import function)
# XXX should be moduleclass_new?!!
# XXX take optional bootstrap_vmx arg??
def new_module(fname, main=False, argv=[], parser_vmx=None):
    """
    returns (CModule, CClosure) if newly loaded module
        the Closure is the (bootstrap) code to populate the Module
    returns (CModule, None) if previously loaded
    """

    md = Module.getprop('modules') # Module Dict/directory
    if fname in md.value:          # previously loaded?
        return md.value[fname], None # yes; return it, no bootstrap needed

    scope = scopes.Scope(None)  # create root scope for module
    sys = system.create_sys_object(scope, argv) # new System object

    mod = CModule(scope)
    mod.props = scope.get_vars() # XXX THWACK (stealing Scope dict)!!
    md.value[fname] = mod        # save as previously loaded

    mi = new_modinfo(main=main, module=mod, fname=fname, parser_vmx=parser_vmx)
    mod.modinfo = mi
    scope.defvar(const.MODINFO, mi) # make ModInfo visible in module namespace

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

def wrap(value, iscope):
    """
    wrap a Python `value` in a language CObject
    `scope` used to find System types by name

    used by vm `lit`, `push_list` opcodes; type `PyObject`; `PyIterator.next`
    """
    assert(__initialized)

    if isinstance(value, CObject):
        return value

    if isinstance(value, bool):
        return mkbool(value) # XXX lookup local true/false???

    if isinstance(value, NUM):
        return system.create_sys_type('Number', iscope, value)

    if isinstance(value, str):
        return mkstr(value, iscope)

    # XXX handle bytes??

    # tuple added for dict_items iterator
    # but exclude tuple-like things (os.stat results, namedtuples)
    if isinstance(value, list) or type(value) is tuple:
        return system.create_sys_type('List', iscope,
                                      [wrap(x, iscope) for x in value])

    if value is None:
        return null_value

    # XXX handle dict?!!!

    #if hasattr(value, '__next__'): return pyiterator(value)???
    # Add next/iter/reversed methods to PyObject??????

    return system.create_sys_type(const.PYOBJECT, iscope, value)

################################################################

# NOT types!
sys_types['true'] =  true_val
sys_types['false'] = false_val
sys_types['null'] = null_value

def init_scope(iscope):
    """
    copy a limited set of types/values to initial Scope `iscope`
    NOTE: they all end up writable!!!
    """
    global __initialized
    __initialized = True        # don't allow _mkXXX any more

    for x in ['true', 'false', 'null', 'Class']:
        iscope.defvar(x, sys_types[x])
