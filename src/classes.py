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

`Instance` to mean a language object instance
        (implemented as an instance of the Python Instance class
        or subclass thereof).

and

`Class` to mean an Instance of language class "Class" --
        the base metaclass, or a subclass thereof.

`class` can mean a Python class/type.

And avoiding the word "type"!

The root language Class is Object.

Only "Object" class has no super classes; all others have one or more.

All objects _should_ have a const.CLASS property
        which points to an Instance of the Class (meta)Class (or a subclass off)

By default language Classes are instances of the "Class" metaclass,
        (the source of the default "new" method); if you need to
        override the default "new" behavior, subclass "Class"
        (and end the new (meta)class name in Class)

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

# All language objects are represented by the interpreter
# as instances of the Python Instance class (or subclasses thereof).
# All such Python classes should start with the letter "C"

class Instance(object):         # XXX CObject??
    def __init__(self, klass):
        # klass may only be None for Object??
        self.props = {const.CLASS: klass}

    def getclass(self):
        """
        return Instance for object Class
        """
        return self.getprop(const.CLASS)

    def classname(self):
        """
        return Python string for object class
        """
        c = self.getclass()
        if not c or c == null_value:
            return "Unknown!"
        return c.getprop(const.NAME).value # XXX guard?

    def invoke(self, vm):
        # will raise exception if op not found:
        # NOTE!! find_op does not return BoundMethod
        #       (called 99.999% of time from XxxOpInstrs)
        m = find_op(self, const.BINOPS, "(")

        # XXX _mklist meant to be used only at startup
        vm.args = [self, _mklist(vm.args)]
        m.invoke(vm)

    def hasprop(self, prop):    # internal use only?
        return prop in self.props

    def getprop(self, prop):
        return self.props.get(prop, null_value)

    def setprop(self, prop, value):
        self.props[prop] = value

    def __str__(self):
        return repr(self)       # XXX ???

    def __repr__(self):
        # XXX call object method??? (could cause debugging pain)
        c = self.getclass()
        if c is Class:
            name = 'Class: %s' % self.getprop(const.NAME).value
        elif subclass_of(c, Class):
            name = '%s: %s' % (c.getprop(const.NAME).value,
                               self.getprop(const.NAME).value)
        else:
            name = self.classname()
        return '<%s at %#x>' % (name, id(self))

class VInstance(Instance):      # XXX CVObject??
    """
    Instance w/ a value property which is a Python type
    (rename this PObject (Primative Object)?)
    """
    def __init__(self, klass, value):
        assert klass is not None
        super().__init__(klass)
        self.value = value      # XXX invoke INIT method????

    def __str__(self):
        if self.value is None:
            return "null"
        if isinstance(self.value, bool):
            return str(self.value).lower()
        return str(self.value)

    # someday allow Dict to be indexed by any Instance...
    def __hash__(self):
        return self.value.__hash__()

    def __repr__(self):
        """show wrapped value"""
        return '<%s: %s at %#x>' % \
            (self.classname(), repr(self.value), id(self))

################

# Calling Python functions (ie; primative class methods) was orignally
# implemented as Closure with two VM instructions (pycall, return).
# The Instance.invoke method avoids those two instructions when calling
# from VM code, and allows invoke_{function,method} from Python code
# to call Python code directly, without executing VM instructions.

class CContinuation(Instance):
    """
    A Callable instance backed by a native (VM) Continuation
    """
    def __init__(self, fp):
        super().__init__(Continuation)
        # NOTE: opaque for now
        self.fp = fp

    def __repr__(self):
        return "<Continuation: %s>" % self.fp.cb[self.fp.pc].where
        
    def invoke(self, vm):
        vm.restore_frame(self.fp) # just like ReturnInstr
        l = len(vm.args)
        if l == 1:
            vm.ac = vm.args[0]  # return value
        elif l == 0:
            vm.ac = null_value
        else:
            raise Exception("Too many Continuation args %s" % len(vm.args))

class CClosure(Instance):
    """
    A Callable instance backed by a Closure (VM code + scope)
    """
    def __init__(self, code, scope):
        super().__init__(Closure)
        # NOTE: opaque for now
        self.code = code
        self.scope = scope

    def __repr__(self):
        return "<Closure: %s>" % self.code[0].where
        
    def invoke(self, vm):
        vm.save_frame()
        # contin = CContinuation(vm.fp)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope
        # NOTE! vm.args picked up by "args" opcode!

class CBoundMethod(Instance):
    """
    A method bound to an object
    created when Object.methodname dereferenced
    XXX bring back use of "method" opcode as optimization
        which fetches method and calls invoke without creating
        a BoundMethod Instance!!!???
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

class CPyFunc(Instance):
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
        # XXX wrap result here, so function doesn't need to know about
        # initial scope??

        # XXX have helper method for this & invoke_function??!!
        # (helper could be defined in CInstance to create VM?!)
        args = vm.args
        n = len(args)
        if n == 0:
            vm.ac = self.func()
        elif n == 1:
            vm.ac = self.func(args[0])
        elif n == 2:
            vm.ac = self.func(args[0], args[1])
        elif n == 3:
            vm.ac = self.func(args[0], args[1], args[2])
        elif n == 4:
            vm.ac = self.func(args[0], args[1], args[2], args[3])
        else:
            vm.ac = self.func(*args)

    def __call__(self, *args):
        raise Exception("Attempt to call %s" % self)

def pyfunc(func):
    """
    (decorator)
    Return an Instance with (Python) invoke method that runs Python code.
    Used for Python methods on base types.
    """
    return CPyFunc(func)

################
# A PyFunc that needs access to internals: passed vm as first arg

class CPyVMFunc(CPyFunc):
    """
    A Callable instance backed by a Python function, passed VM
    as first argument
    """
    # XXX NOTE no __init__ method: looks just like PyFunc
    def invoke(self, vm):
        vm.args.insert(0, vm)
        super().invoke(vm)

def pyvmfunc(func):
    """
    decorator for Python functions that need pointer to VM
    Return an Instance with (Python) invoke method that runs Python code.
    """
    return CPyVMFunc(func)

################################################################

def _new_vinst(this_class, arg):
    """
    for internal use only!
    creates an interpreter object wrapped around a Python Value
    """
    return VInstance(this_class, arg)

def _mkdict(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return _new_vinst(Dict, vals)

def _mklist(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return _new_vinst(List, vals)

def _mkstr(s):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return _new_vinst(Str, s)

def _mkobj(props):
    """
    used to create System, System.types, tokens
    """
    o = Instance(Object)        # XXX was JSObject
    o.props.update(props)
    return o

def mkstr(s, scope):
    return system.create_sys_type('Str', scope, s)

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
    class_obj = Instance(metaclass)
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

Class = defclass(None, 'Class')   # metaclass of all Classes
Class.setprop(const.CLASS, Class) # circular!
# supers set to [Object] below

Object = defclass(Class, 'Object', []) # root Class

# metaclass for VInstances
VClass = defclass(Class, 'VClass', [Class])

# wrappers, with .value
# make children of VObject (XXX private 'new' using new_vinst?)
List = defclass(VClass, 'List', [Object]) # subclass of Sequence? FrozenList??
Str = defclass(VClass, 'Str', [Object])
Dict  = defclass(VClass, 'Dict', [Object]) # subclass of Mapping? FrozenDict??
Number = defclass(VClass, 'Number', [Object])
# XXX own metaclass to return singleton?
Null = defclass(VClass, 'Null', [Object]) # XXX singleton
# XXX own metaclass to return doubleton values?
Bool = defclass(VClass, 'Bool', [Object])

# JS style Object (TEMP):
JSObject = defclass(Class, 'JSObject', [Object])

# Str, List types now available:
Class.setprop(const.SUPERS, _mklist([Object]))

for klass, name in _saved_names.items():
    klass.setprop(const.NAME, _mkstr(name))
for klass, supers in _saved_supers.items():
    klass.setprop(const.SUPERS, _mklist(supers))

# internal object w/ direct invoke methods
#       (avoids binop lookup)
# XXX use metaclass that prohibits user call of 'new' method?

# all backed by Python CXyZzy classes with invoke methods:
Closure = defclass(Class, 'Closure', [Object])
BoundMethod = defclass(Class, 'BoundMethod', [Object])
PyFunc = defclass(Class, 'PyFunc', [Object])
Continuation = defclass(Class, 'Continuation', [Object])

PyVMFunc = defclass(Class, 'PyVMFunc', [Object])

################

null_value = _new_vinst(Null, None)

# create (only) instances of true/false (a doubleton)!
true_val = _new_vinst(Bool, True)
false_val = _new_vinst(Bool, False)

################

def subclass_of(klass, base):
    visited = set()
    def check(c):
        if c in visited:
            return False
        visited.add(c)
        if c is base:
            return True
        s = c.getprop(const.SUPERS)
        if s is None or s is null_value:
            return False
        for x in s.value:       # XXX check if List
            if check(x):
                return True
        return False
    return check(klass)

################ Object -- the base type for all instances and classes

# utility called by VM jumpn/jumpe: NOT a method/pyfunc
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

@pyvmfunc
def new_inst(vm, this_class, *args):
    """
    default "new" method for Object (and therefore Class)
    makes an instance of this_class
    Creates a Python Instance, calls this_class's 'init' method with args
    """
    # XXX stash Python class to use in a Python attr??????
    n = Instance(this_class)

    m = find_in_class(n, const.INIT) # returns BoundMethod
    if m and m is not null_value:
        vmx.invoke_function(m, vm, args) # XXX reuse VM
    return n

@pyfunc
def obj_init(this_obj, *args):
    if len(args) > 0:
        raise Exception("%s.%s takes no arguments" %
                        (this_obj.classname(), const.INIT))

@pyvmfunc
def obj_str(vm, l):
    return mkstr(str(l), vm.iscope)

@pyvmfunc
def obj_repr(vm, l):
    return mkstr(repr(l), vm.iscope)

@pyfunc
def obj_eq(x, y):
    return mkbool(x is y)

@pyfunc
def obj_ne(x, y):
    return mkbool(x is not y)

def _not(x):
    """
    not a pyfunc (may call at any time)
    takes Instance, returns Instance
    """
    return mkbool(not is_true(x))

@pyfunc
def obj_not(x):
    """Object unary ! operator"""
    return _not(x)

@pyfunc
def obj_putprop(l, r, value):
    # XXX check r is VInstance? Str??
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
        (only exception is Instance.invoke)
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
def obj_class(this):
    return this.getclass()

@pyfunc
def obj_call(l, r):
    raise Exception("%s not callable" % l.classname())

@pyfunc
def obj_instance_of(l, c):
    return mkbool(subclass_of(obj_class(l), c))

Object.setprop(const.METHODS, _mkdict({
    const.INIT: obj_init,
    'class': obj_class, # clutter!? might as well be a normal property?!
    'instance_of': obj_instance_of,
    'putprop': obj_putprop,
    'getprop': obj_getprop,
    'str': obj_str,
    'repr': obj_repr,
}))
Object.setprop(const.BINOPS, _mkdict({
    '.': obj_getprop,               # same as getprop!!
    '..': obj_get_in_supers,
    '===': obj_eq,              # "is"
    '!==': obj_ne,              # "is not"
    '==': obj_eq,               # allow null where str/num expected?
    '!=': obj_ne,               # ditto
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
    metaclass = this_class.classname()
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
            raise Exception("Unknown %s property %s" % (metaclass, key))
        this_class.props[ikey] = val

    if const.NAME not in this_class.props:
        raise Exception("Class.new requires '%s'"  % (metaclass, key))

    # XXX complain if NAME doesn't start with a capitol letter??

    if const.SUPERS not in this_class.props:
        # XXX complain??
        this_class.setprop(const.SUPERS, _mklist([Object]))

@pyfunc
def class_call(this_class, args):
    """
    "(" binop for Class
    """
    # PLB: I keep on doing this (Python fingers)
    raise Exception("call %s.new!" % this_class.getprop(const.NAME).value)

@pyfunc
def class_subclass_of(l, r):
    # complain if l is not a Class -- check using subclass_of(l, Class)?!
    return mkbool(subclass_of(l, r))

# Class: a meta-class: all Classes are instances of a meta-class
# Class.new creates a new Class
Class.setprop(const.METHODS, _mkdict({
    const.NEW: new_inst,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member
    "subclass_of": class_subclass_of
}))
Class.setprop(const.CLASS, Class) # circular!

Class.setprop(const.BINOPS, _mkdict({
    '(': class_call
}))

################ VClass -- metaclass for VInstances
# XXX PClass // PObject

@pyvmfunc
def new_vinst(vm, this_class, arg=None):
    """
    'new' method for VClass metaclass (ie; Number.new, Dict.new)
    makes an instance of this_class
    """
    # XXX need different init method for each class to handle arg/set .value!!!
    raise Exception("new_vinst {} {}".format(this_class, arg))

    # XXX stash Python class to use in this_class.pyclass Python attr
    # XXX stash Python default arg in this_class.defval Python attr???
    n = VInstance(this_class, arg) # XXX unwrap??!!!

    # XXX what to do with arg??
    m = find_in_class(n, const.INIT) # returns BoundMethod
    if m and m is not null_value:
        vmx.invoke_function(m, vm, [arg]) # XXX reuse VM
    return n

VClass.setprop(const.METHODS, _mkdict({
   const.NEW: new_vinst,
#  const.INIT: class_init,     # Class.new creates new Classes
}))

################ (JavaScript style) Object
# a class with both "." and "[]" access to properties
# XXX flush??

@pyfunc
def jsobj_init(obj, proto=None):
    if proto and proto is not null_value:
        obj.props.update(proto.props) # XXX direct access

JSObject.setprop(const.METHODS, _mkdict({
    const.INIT: jsobj_init,
    'str': obj_str,
}))
JSObject.setprop(const.BINOPS, _mkdict({
    '[': obj_getprop
}))
JSObject.setprop(const.LHSOPS, _mkdict({
    '[': obj_putprop
}))

################ generic methods for classes with wrapped Python values

# XXX XXX rename val_xxx to vobj_xxx????

@pyfunc
def val_len(l):
    return _new_vinst(Number, len(l.value)) # XXX look up by name?

@pyvmfunc
def val_str(vm, l):
    """
    use Python str function on value
    """
    return mkstr(str(l.value), vm.iscope)

@pyvmfunc
def val_repr(vm, l):
    return mkstr("<%s: %s>" % (l.classname(), repr(l.value)),
                 vm.iscope)

@pyfunc
def val_init(l, value):
    # XXX create_sys_type calling w/ Python value!!!
    l.value = value             # XXX XXX unwrap?

# XXX unused?
@pyfunc
def val_ge(l, r):
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
def val_eq(l, r):
    lv = l.value
    rv = r.value
    return mkbool(lv == rv)

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
    'len': val_len,
    'str': val_str,
    'repr': val_repr,
    'str': val_str,
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

# XXX supply native version?
@pyvmfunc
def list_for_each(vm, l, func):
    # XXX Continuations generated inside 'func' will be fubar
    for item in l.value:
        vmx.invoke_function(func, vm, [item]) # XXX reuse VM

# XXX supply native version?
@pyvmfunc
def list_each_for(vm, l, func): # XXX TEMP until reversed?
    # XXX XXX use backwards counting index (avoid copying list)??
    # XXX Continuations generated inside 'func' will be fubar
    for item in reversed(l.value):
        vmx.invoke_function(func, vm, [item]) # XXX reuse VM

@pyfunc
def list_get(l, r):
    # XXX check if integer
    return l.value[r.value]

@pyfunc
def list_put(l, r, value):
    l.value[r.value] = value
    return value

# XXX supply native version!?
@pyvmfunc
def list_str(vm, l):
    # XXX Continuations generated inside 'str' will be fubar
    # XXX reuse VM
    return mkstr("[%s]" %
                 (", ".join([vmx.invoke_method(x, 'str', vm).value
                             for x in l.value])),
                 vm.iscope)

List.setprop(const.METHODS, _mkdict({
    'append': list_append,
    'len': val_len,
    'str': list_str,
    'pop': list_pop,
    'repr': val_repr,
    # XXX slice(start[,end]) (return range of elements)
    const.INIT: list_init,
    # TEMP: replace with native code:
    'each_for': list_each_for,
    'for_each': list_for_each
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
    return _new_vinst(x.getclass(), -x.value)

@pyfunc
def add(x, y):
    return _new_vinst(x.getclass(), x.value + y.value)

@pyfunc
def sub(x, y):
    return _new_vinst(x.getclass(), x.value - y.value)

@pyfunc
def mul(x, y):
    return _new_vinst(x.getclass(), x.value * y.value)

@pyfunc
def div(x, y):
    return _new_vinst(x.getclass(), x.value / y.value)

# XXX XXX XXX too liberal!!!
def _eq(l, r):
    """
    call any time (not a pyfunc)
    takes Instance, returns Instance
    """
    l = l.value
    r = r.value                 # XXX str()?
#    print "eq", l, r
    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) == float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) == int(r))
    return mkbool(str(l) == str(r))

@pyfunc
def eq(l, r):
    return _eq(l, r)

@pyfunc
def ne(l, r):
    return _not(_eq(l, r))

def _ge(l, r):
    l = l.value
    r = r.value

    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) >= float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) >= int(r))
    return mkbool(str(l) >= str(r))

@pyfunc
def ge(l, r):
    return _ge(l, r)

@pyfunc
def lt(l, r):
    return _not(_ge(l, r))

def _le(l, r):
    l = l.value
    r = r.value

    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) <= float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) <= int(r))
    return mkbool(str(l) <= str(r))

@pyfunc
def le(l, r):
    return _le(l, r)

@pyfunc
def gt(l, r):
    return _not(_le(l, r))

Number.setprop(const.METHODS, _mkdict({
    'str': val_str,
    'repr': val_repr,
    const.INIT: val_init,
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
    return _new_vinst(x.getclass(), xv + yv)

@pyfunc
def str_strip(this):
    return _new_vinst(this.getclass(), this.value.strip())

@pyfunc
def str_get(l, r):
    # XXX check if r is integer
    return _new_vinst(l.getclass(), l.value[r.value])

@pyfunc
def str_slice(l, a, b=None):
    av = a.value                # XXX check if int
    if b is not None:
        bv = b.value            # XXX check if int
        ret = l.value[av:bv]
    else:
        ret = l.value[av:]
    return _new_vinst(l.getclass(), ret)

@pyfunc
def str_str(this):
    return this                 # identity

@pyvmfunc
def str_repr(vm, this):
    # XXX check if contains '"' and \u escape!!!
    return mkstr('"%s"' % this.value, vm.iscope)

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
    # XXX check arg is List (or Dict)?
    # XXX each List/key element must be a Str!
    return _new_vinst(this.getclass(), this.value.join([x.value for x in arg.value]))

Str.setprop(const.METHODS, _mkdict({
    'join': str_join,
    'len': val_len,
    'repr': val_repr,
    'slice': str_slice,
    'str': str_str,
    'strip': str_strip,
    const.INIT: val_init,
}))
Str.setprop(const.BINOPS, _mkdict({
    '+': str_concat,
    '==': str_eq,
    '!=': str_ne,
    # XXX full relops? (require str lhs!!)
    '[': str_get,
}))

################ Null

@pyvmfunc
def null_str(vm, this):
    return mkstr("null", vm.iscope)

@pyfunc
def null_call(l, r):
    raise Exception("'null' called; bad method name?")

Null.setprop(const.METHODS, _mkdict({
    'str': null_str
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
    'str': bool_str
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

PyObject = defclass(VClass, const.PYOBJECT, [Object])

def unwrap(x):
    """
    recursively unwrap an Object, to pass to PyObject on call
    """
    if hasattr(x, 'value'):     # faster than isistance(x, VInstance)??
        x = x.value
        if isinstance(x, list):
            return [unwrap(y) for y in x]
        elif isinstance(x, dict):
            return {key: unwrap(val) for key, val in x.items()}
    # XXX complain??
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
def pyobj_call(vm, l, r):
    ret = l.value(*[unwrap(x) for x in r.value]) # XXX getlist
    return wrap(ret, vm.iscope) # may create another PyObject!
    
PyObject.setprop(const.METHODS, _mkdict({
    const.INIT: val_init,
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
    wrap a Python `value` in a language Instance
    `scope` used to find System types by name

    used by vm `lit` and `pyfunc`; type `PyObject`
    """
    if isinstance(value, bool):
        return mkbool(value) # XXX lookup local true/false???

    if isinstance(value, NUM):
        return system.create_sys_type('Number', iscope, value)

    if isinstance(value, str):
        return system.create_sys_type('Str', iscope, value)

    # XXX handle bytes??

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

