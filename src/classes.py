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

[some of the above probably DOESN'T belong in the docstring!!]
"""

# NOTE!!! For methods/ops use 'xxx' strings (make searching easier)

# XXX split this up (into classes/xxx.py) before it gets much larger??
#       maybe have one file per Class?? named classes/ClassName.py??
#       (lots of stuff is missing, so it's bound to grow....)

import system
import const
import vmx

NUM = (int, float)              # Python3

# used to initialize new System.types objects in new top level (module) scopes.
# for _current_ definitions, need to lookup in iscope (use find_sys_type)
sys_types = {}

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
        # will raise exception if op not found:
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

################

class CContinuation(CObject):
    """
    A Callable instance backed by a native (VM) Continuation
    """
    def __init__(self, fp):
        super().__init__(Continuation)
        # NOTE: opaque for now
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
    """
    def __init__(self, code, scope):
        super().__init__(Closure)
        # NOTE: opaque for now
        self.code = code
        self.scope = scope

    def __repr__(self):
        i = self.code[0]
        return "<Closure: %s:%s>" % (i.fn, i.where)
        
    def invoke(self, vm):
        vm.save_frame(True)     # show=True
        # return or leave label Continuation will be generated from FP
        #       by "args" or "lscope" Instr (first Instr in code)
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
    """
    def __init__(self, obj, method):
        super().__init__(BoundMethod)
        # NOTE: opaque -- need repr!
        self.obj = obj
        self.method = method

    def __repr__(self):
        return "<BoundMethod: %s %s>" % (self.obj, self.method)
        
    def invoke(self, vm):
        # *THIS* is the place "this" is explicitly passed!!!
        vm.args.insert(0, self.obj) # prepend saved "this" to arguments
        self.method.invoke(vm)      # return value in AC

# Calling Python functions (ie; primative class methods) was orignally
# implemented as a Closure with two VM instructions (pycall, return).
# The CObject.invoke method avoids those two instructions when calling
# from VM code, and allows invoke_{function,method} from Python code
# to call Python code directly, without executing VM instructions.

class CPyFunc(CObject):
    """
    A Callable instance backed by a Python function
    """
    def __init__(self, func):
        super().__init__(PyFunc)
        if isinstance(func, CPyFunc):
            raise Exception("double wrapping %s" % func.func)
        self.func = func

    def __repr__(self):
        return "<PyFunc: %s>" % self.func.__name__
        
    def invoke(self, vm):
        # XXX have helper method for this & invoke_function??!!
        args = vm.args
        n = len(args)
        if n == 0:
            ret = self.func()
        elif n == 1:
            ret = self.func(args[0])
        elif n == 2:
            ret = self.func(args[0], args[1])
        elif n == 3:
            ret = self.func(args[0], args[1], args[2])
        elif n == 4:
            ret = self.func(args[0], args[1], args[2], args[3])
        else:
            ret = self.func(*args)

        # XXX wrap result here, so function doesn't need to know about
        # initial scope??  Would need to check if ret is not an instance
        # of CObject, so maybe have different PyFunc flavors
        # that do or do not do wrapping??
        vm.ac = ret

    def __call__(self, *args):
        # to catch mistakenly calling a CPyFunc (eg; from another method)
        raise Exception("Attempt to call %s" % self)

def pyfunc(func):
    """
    (decorator)
    Return a CObject with (Python) invoke method that runs Python code.
    Used for Python methods on base types, system utilities.
    """
    return CPyFunc(func)

################
# A PyFunc that needs access to internals: passed vm as first arg

class CPyVMFunc(CPyFunc):
    """
    A Callable instance backed by a Python function, passed VM as
    first argument.  MOSTLY used for access to "initial scope" for
    lookup of Classes by name.  But could be used for all kinds of
    reflection fun (inspection of current scope, code, traceback,
    etc).

    PLB NOTE!  To avoid bloat and inefficiency, VM internals (Frame,
    Scope, VMInstrs) are NOT backed (fronted?) by language Objects.
    and my current (may 2021) thoughts are to expose particulars with
    Objects created on demand, either with copies of the backing data,
    or, in the case of Scopes, an Object which references the backing
    (Python) dict.
    """
    # XXX NOTE no __init__ method: looks just like PyFunc
    def invoke(self, vm):
        vm.args.insert(0, vm)   # prepend vm to arguments
        super().invoke(vm)

def pyvmfunc(func):
    """
    decorator for Python functions that need pointer to VM
    """
    return CPyVMFunc(func)

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
    return _new_pobj(Dict, vals)

def _mklist(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return _new_pobj(List, vals)

def _mkstr(s):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    see mkstr
    """
    return _new_pobj(Str, s)

def _mkobj(props):
    """
    used to create System, System.types, tokens
    """
    o = CObject(Object)
    o.props.update(props)       # copy, so System.types is module local
    return o

def mkstr(s, scope):
    return system.create_sys_type('Str', scope, s)

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
List = defclass(PClass, 'List', [PObject]) # subclass of Sequence? FrozenList??
Str = defclass(PClass, 'Str', [PObject])   # subclass of Sequence?
Dict  = defclass(PClass, 'Dict', [PObject]) # subclass of Mapping? FrozenDict??
Number = defclass(PClass, 'Number', [PObject])

# XXX own metaclass to return singleton?
Null = defclass(PClass, 'Null', [PObject]) # XXX singleton
# XXX own metaclass to return doubleton values? subclass into two singletons??
Bool = defclass(PClass, 'Bool', [PObject])

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
def new_obj(vm, this_class, *args):
    """
    default "new" method for Object (and therefore Class)
    makes an instance of this_class
    Creates a Python CObject, calls this_class's 'init' method with args
    """
    # XXX stash Python class to use in a Python attr??????
    n = CObject(this_class)

    m = find_in_class(n, const.INIT) # returns BoundMethod
    if m and m is not null_value:
        vmx.invoke_function(m, vm, args) # XXX reuse VM
    return n

@pyfunc
def obj_init(this_obj, *args):
    if len(args) > 0:
        raise UError("%s.%s takes no arguments" %
                        (this_obj.classname(), const.INIT))

@pyvmfunc
def obj_str(vm, l):
    return mkstr(str(l), vm.iscope) # native method that calls this.repr()?

@pyvmfunc
def obj_repr(vm, l):
    return mkstr(repr(l), vm.iscope)

@pyvmfunc
def obj_reprx(vm, l):
    """
    for debug: show Class, and Python value (which may include id?)
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l)), vm.iscope)

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
def find_in_supers(l, rv):
    """
    breadth first search of superclass methods/properties
    """
    c = l.getclass()
    #if c is null_value:
    #    return null_value       # XXX raise Exception?

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

# utility, not method
def find_op(obj, optype, op):
    """
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

    raise Exception("%s %s %s not found" %
                    (obj, optype, op))

@pyfunc
def obj_get_in_supers(l, r):
    return find_in_supers(l, r.value) # XXX check for VInst

@pyfunc
def obj_getclass(this):
    return this.getclass()

@pyfunc
def obj_setclass(this, klass):
    return this.setclass(klass)

@pyfunc
def obj_call(l, *args):
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
        this_class.setprop(const.SUPERS, _mklist([Object]))

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
    const.NEW: new_obj,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member
    "subclass_of": class_subclass_of
}))

Class.setprop(const.BINOPS, _mkdict({
    '(': class_call
}))

################ PClass -- metaclass for PObjects

@pyvmfunc
def pclass_new(vm, this_class, arg):
    """
    'new' method for PClass metaclass (ie; Number.new, Dict.new)
    makes an instance of this_class backed by a CPObject
    """
    o = CPObject(this_class)

    m = find_in_class(o, const.INIT) # returns BoundMethod
    if not m or m is null_value:
        # should not happen: should call back to pobj_init
        raise Exception("SNH: {} has no init method".format(this_class))
    vmx.invoke_function(m, vm, [arg])
    return o

PClass.setprop(const.METHODS, _mkdict({
   const.NEW: pclass_new
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
    return mkstr(str(l.value), vm.iscope)

@pyvmfunc
def pobj_repr(vm, l):
    """
    use Python repr function on value
    """
    return mkstr(repr(l.value), vm.iscope)

@pyvmfunc
def pobj_reprx(vm, l):
    """
    for debug: show Class, and Python value
    XXX show id()? of value???
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l.value)),
                 vm.iscope)

@pyfunc
def pobj_init(l, value):
    raise Exception("{} missing init method".format(l.classname()))

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

# XXX unused?
@pyfunc
def pobj_eq(l, r):
    lv = l.value
    rv = r.value
    return mkbool(lv == rv)

PObject.setprop(const.METHODS, _mkdict({
    'repr': pobj_repr,
    'reprx': pobj_reprx,
    const.INIT: pobj_init
}))

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
def dict_init(obj, arg=None):
    if arg:
        obj.value = dict(arg.value) # XXX check if Dict!!!
    else:
        obj.value = {}

@pyfunc
def dict_pop(obj, arg):
    return obj.value.pop(arg.value) # XXX check arg has value!!!

Dict.setprop(const.METHODS, _mkdict({
    'len': pobj_len,
    'pop': dict_pop,
    const.INIT: dict_init,
}))
Dict.setprop(const.BINOPS, _mkdict({
    '[': dict_get
}))
Dict.setprop(const.LHSOPS, _mkdict({
    '[': dict_put
}))

################ List

@pyfunc
def list_init(l, value=None):   # XXX take List
    if value is None:
        value = []
    l.value = value

@pyfunc
def list_append(l, item):
    l.value.append(item)

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
    return value

# str, repr, for_each, each_for, map, map2 in bootstrap.xxl
List.setprop(const.METHODS, _mkdict({
    'append': list_append,
    'len': pobj_len,
    'pop': list_pop,
    # XXX slice(start[,end]) (return range of elements)
    const.INIT: list_init,
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

Number.setprop(const.METHODS, _mkdict({
#    const.INIT: num_init       # XXX invoke arg.number()?
}))
Number.setprop(const.UNOPS, _mkdict({
    '-': neg,
}))
Number.setprop(const.BINOPS, _mkdict({
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
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
    xv = x.value
    yv = y.value
    if xv == "":
        return yv
    if yv == "":
        return xv
    return _new_pobj(x.getclass(), xv + yv)

@pyfunc
def str_strip(this):
    return _new_pobj(this.getclass(), this.value.strip())

@pyfunc
def str_get(l, r):
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

@pyfunc
def str_str(this):
    return this                 # identity

def _str_eq(l, r):
    l = l.value
    if hasattr(r, 'value'):     # faster than isinstance?
        r = r.value
    return l == r

@pyfunc
def str_eq(l, r):
    return mkbool(_str_eq(l, r))

@pyfunc
def str_ne(l, r):
    return mkbool(not _str_eq(l, r))

@pyfunc
def str_join(this, arg):
    # XXX check arg is List (or Dict) of Str!
    return _new_pobj(this.getclass(),
                     this.value.join([x.value for x in arg.value]))

Str.setprop(const.METHODS, _mkdict({
    'join': str_join,
    'len': pobj_len,
    'slice': str_slice,
    'str': str_str,
    'strip': str_strip,
    const.INIT: pobj_init,
}))
Str.setprop(const.BINOPS, _mkdict({
    '+': str_concat,
    '==': str_eq,
    '!=': str_ne,
    '!=': ne,
    '>=': ge,
    '<=': le,
    '>': gt,
    '<': lt,
    '[': str_get,
}))

################ Null

@pyvmfunc
def null_str(vm, this):
    return mkstr("null", vm.iscope)

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
        return mkstr("true", vm.iscope)
    else:
        return mkstr("false", vm.iscope)

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
        if isinstance(x, list):
            return [unwrap(y) for y in x]
        elif isinstance(x, dict):
            return {key: unwrap(val) for key, val in x.items()}
    # XXX complain??!!!
    return x

@pyvmfunc
def pyobj_getprop(vm, l, r):
    """
    installed as "." binop
    """
    # XXX r must be Str
    # XXX check if exists first? obscures all Class members/methods!!
    # XXX '..' should allow access to parent class methods (getprop/setprop)?
    v = getattr(l.value, r.value) # get Python object attribute
    return wrap(v, vm.iscope)

@pyvmfunc
def pyobj_getitem(vm, l, r):
    v = l.value[r.value]        # XXX unwrap(r)??
    return wrap(v, vm.iscope)

@pyvmfunc
def pyobj_call(vm, this, *args):
    a2 = [unwrap(x) for x in args]
    ret = this.value(*a2)
    return wrap(ret, vm.iscope) # may create another PyObject!
    
PyObject.setprop(const.METHODS, _mkdict({
    const.INIT: pobj_init,
    # NOTE!! pyobj_getprop doesn't search here!!!
    #   XXX see if pyobj..getprop() works!!
}))

PyObject.setprop(const.BINOPS, _mkdict({
    '.': pyobj_getprop,         # gets Python object attr!
    '[': pyobj_getitem,
    '(': pyobj_call,
}))

# XXX TODO LHSOPS for '.' and '[' ?!!! need to unwrap values!

################################################################

def wrap(value, iscope):
    """
    wrap a Python `value` in a language CObject
    `scope` used to find System types by name

    used by vm `lit`, `push_list`; `pyfunc`; type `PyObject`
    """
    if isinstance(value, bool):
        return mkbool(value) # XXX lookup local true/false???

    if isinstance(value, NUM):
        return system.create_sys_type('Number', iscope, value)

    if isinstance(value, str):
        return mkstr(value, iscope)

    # XXX handle bytes??

    if isinstance(value, list): # for System.argv creation!
        return system.create_sys_type('List', iscope,
                                      [wrap(x, iscope) for x in value])

    # XXX handle dict???

    if value is None:
        return null_value

    # XXX complain??
    return system.create_sys_type(const.PYOBJECT, iscope, value)

################################################################

# NOT types!
sys_types['true'] =  true_val
sys_types['false'] = false_val
sys_types['null'] = null_value

def copy_types(to, sys_obj):
    """
    copy a limited set of types/values from
    dict "sys_types" to (top level) Scope "to"
    NOTE: they all end up writable!!!
    """
    sys_types = sys_obj.getprop('types')
    for x in ['true', 'false', 'null', 'Class']:
        to.defvar(x, sys_types.getprop(x))
