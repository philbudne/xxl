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

All objects _should_ have a const.CLASS property
        which points to an Instance of the Class Class (or subclass)

Classes may have one or more superclasses (const.SUPERS property)

Only "Object" class has no supers.

By default language Classes are instances of the "Class" metaclass,
        (the source of the default "new" method).

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

sys_types = {}

# all language objects are represented by the interpreter
# as instances of the Python Instance class:

class Instance(object):
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
            return "untitled"
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
        if c == Class:          # XXX handle subclassing of Class?!!!
            name = 'Class: %s' % self.getprop(const.NAME).value
        else:
            name = self.classname()
        return '<%s at %#x>' % (name, id(self))

class VInstance(Instance):
    """
    Instance w/ a value property which is a Python type
    XXX Need to have special VObjectClass metaclass (w/ custom 'new')
    to ensure that ALL newly created instances come here?!
    """
    def __init__(self, klass, value):
        assert klass is not None
        super().__init__(klass)
        self.value = value      # XXX invoke INIT method????

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '<%s: %s at %#x>' % \
            (self.classname(), repr(self.value), id(self))

################

# Calling Python functions (ie; primative class methods) was orignally
# implemented as Closure with two VM instructions (pycall, return).
# The invoke method avoids those two instructions when calling
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
        # XXX method must be callable (CInstance)
        super().__init__(BoundMethod)
        # NOTE: opaque -- need repr!
        self.obj = obj
        self.method = method

    def __repr__(self):
        return "<BoundMethod: %s %s>" % (self.obj, self.method)
        
    def invoke(self, vm):
        vm.args.insert(0, self.obj) # prepend saved "this" to arguments
        self.method.invoke(vm)      # return value in AC

class CPyFunc(Instance):
    """
    A Callable instance backed by a Python function
    """
    def __init__(self, func):
        super().__init__(PyFunc)
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

def pyfunc(func):
    """
    Return an Instance with (Python) invoke method that runs Python code.
    Used for Python methods on base types.
    """
    return CPyFunc(func)

################
# EXP: NOT YET USED... may replace PyFunc!

class CPyFuncVM(CPyFunc):
    """
    A Callable instance backed by a Python function, passed VM
    as first argument
    """
    # XXX NOTE no __init__ method: looks just like PyFunc
    def invoke(self, vm):
        vm.args.insert(0, vm)
        super().invoke(vm)

def pyfuncvm(func):
    """
    Return an Instance with (Python) invoke method that runs Python code.
    Used for Python methods on base types.
    """
    return CPyFuncVM(func)

################################################################

def new_vinst(this_class, arg):
    """
    for internal use only!
    creates an interpreter object wrapped around a Python Value
    XXX use INIT method???
    """
    return VInstance(this_class, arg)

def _mkdict(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return new_vinst(Dict, vals)

def _mklist(vals):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return new_vinst(List, vals)

def _mkstr(s):
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    return new_vinst(Str, s)

def mkstr(s):
    # XXX use wrap (lookup types by System.types.NAME)?????
    # XXX need initial scope
    return new_vinst(Str, s)

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

Object = defclass(Class, 'Object', [])

# wrappers, with .value
# make children of VObject (XXX private 'new' using new_vinst?)
List = defclass(Class, 'List', [Object]) # interhit from "Sequence"? "FrozenList"?
Str = defclass(Class, 'Str', [Object])
Dict  = defclass(Class, 'Dict', [Object]) # inherit from "Mapping"? FrozenDict?
Number = defclass(Class, 'Number', [Object])
# XXX own metaclass to return singleton?
Null = defclass(Class, 'Null', [Object])         # XXX singleton
# XXX own metaclass to return doubleton values?
Bool = defclass(Class, 'Bool', [Object])

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
Callable = defclass(Class, 'Callable', [Object]) # virtual XXX FLUSH?
# all backed by Python CXyZzy classes with invoke methods:
Closure = defclass(Class, 'Closure', [Callable])
BoundMethod = defclass(Class, 'BoundMethod', [Callable])
PyFunc = defclass(Class, 'PyFunc', [Callable])
Continuation = defclass(Class, 'Continuation', [Callable])

################

null_value = new_vinst(Null, None)

# create (only) instances of true/false (a doubleton)!
true_val = new_vinst(Bool, True)
false_val = new_vinst(Bool, False)

################ helper methods

def mtrue(o):
    return true_val

def mfalse(o):
    return false_val


################ Object -- the base type for all instances and classes

def new_inst(this_class, *args):
    """
    default "new" method for Object (and therefore Class)
    makes an instance of this_class
    Creates a Python Instance, calls this_class's 'init' method with args
    """
    n = Instance(this_class)

    m = find_in_class(n, const.INIT) # returns BoundMethod
    if m and m is not null_value:
        vmx.invoke_function(m, None, args)
    return n

def obj_init(this_obj, *args):
    if len(args) > 0:
        raise Exception("need to override %s to pass arguments" % const.INIT)

def obj_str(l):
    return mkstr(str(l))

def obj_repr(l):
    return mkstr(repr(l))

def is_true(obj):
    """
    return Python True/False for an object
    non-premature optimization:
    only "null" and "false" objects, and zero are false
    """
    if obj is false_val or obj is null_value:
        return False
    if hasattr(obj, 'value') and obj.value == 0:
        return False
    return True

def obj_eq(x, y):
    return mkbool(x == y)    # XXX use "is" ???

def obj_ne(x, y):
    return mkbool(x != y)    # XXX use "is not" ???

def obj_not(x):
    """Object unary ! operator"""
    return mkbool(not is_true(x))

def obj_put(l, r, value):
    # XXX check for VInstance?
    l.setprop(r.value, value)
    return value                # lhsop MUST return value

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

def obj_get(l, r):
    rv = r.value              # XXX must be Str
    if l.hasprop(rv):
        return l.getprop(rv)
    return find_in_class(l, rv) # may return BoundMethod

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
                    (obj.classname(), optype, op))

def obj_get_in_supers(l, r):
    return find_in_supers(l, r.value) # XXX check for VInst

def obj_class(this):
    return this.getclass()

def obj_call(l, r):
    raise Exception("%s not callable" % l.classname())

Object.setprop(const.METHODS, _mkdict({
    const.INIT: pyfunc(obj_init),
    'class': pyfunc(obj_class), # clutter!? might as well be a normal property?!
    'putprop': pyfunc(obj_put),
    'getprop': pyfunc(obj_get),
    'str': pyfunc(obj_str),
    'repr': pyfunc(obj_repr),
}))
Object.setprop(const.BINOPS, _mkdict({
    '.': pyfunc(obj_get),       # same as getprop!!
    '..': pyfunc(obj_get_in_supers),
    '==': pyfunc(obj_eq),
    '!=': pyfunc(obj_ne),
    '(': pyfunc(obj_call),
}))
Object.setprop(const.UNOPS, _mkdict({
    '!': pyfunc(obj_not),
}))
Object.setprop(const.LHSOPS, _mkdict({
    '.': pyfunc(obj_put)        # same as putprop!!
}))

################ Class -- base type for Classes (a MetaClass)

def class_init(this_class, props):
    """
    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    """
    # XXX check props is a Dict!
    metaclass = this_class.classname()
    for key, val in props.value.items():
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

    if const.SUPERS not in this_class.props:
        # XXX complain??
        this_class.setprop(const.SUPERS, _mklist([Object]))
    if const.NAME not in this_class.props:
        # display metaclass name (typ Class)
        for key, value in const.CLASS_PROPS.items():
            if value == const.NAME:
                break
        else:
            key = 'name?'
        raise Exception("%s.new requires '%s'"  % (metaclass, key))

def class_name(this_class):
    return this_class.getprop(const.NAME)

def class_call(this_class, args):
    """
    "(" binop for Class
    """
    # PLB: I keep on doing this (Python fingers)
    raise Exception("call %s.new!" % class_name(this_class).value)

# Class: a meta-class: all Classes are instances of a meta-class
# Class.new creates a new Class
Class.setprop(const.METHODS, _mkdict({
    const.NEW: pyfunc(new_inst),
    const.INIT: pyfunc(class_init), # Class.new creates new Classes
}))
Class.setprop(const.CLASS, Class) # circular!

Class.setprop(const.BINOPS, _mkdict({
    '(': pyfunc(class_call)
}))

################ (JavaScript style) Object
# a class with both "." and "[]" access to properties
# XXX flush??

def jsobj_init(obj, props=None): # XXX take Object
    if props is not None:
        if isinstance(props, dict):
            # TEMP: here from __obj_create
            obj.props.update(props)
        else:
            obj.props.update(props.props) # XXX direct access

JSObject.setprop(const.METHODS, _mkdict({
    const.INIT: pyfunc(jsobj_init),
    'str': pyfunc(obj_str),
}))
JSObject.setprop(const.BINOPS, _mkdict({
    '[': pyfunc(obj_get),
}))
JSObject.setprop(const.LHSOPS, _mkdict({
    '[': pyfunc(obj_put)
}))

################ generic methods for classes with wrapped Python values

def val_len(l):
    return new_vinst(Number, len(l.value)) # XXX look up by name? use l.CLASS?

def val_str(l):
    """
    use Python str function on value
    """
    return mkstr(str(l.value))

def val_repr(l):
    return mkstr("<%s: %s>" % (l.classname(), repr(l.value)))

def val_init(l, value):
    l.value = value             # XXX unwrap?

def val_ge(l, r):
    lv = l.value
    rv = r.value
    # XXX not right!!
    if isinstance(lv, float) or isinstance(rv, float):
        return mkbool(float(lv) >= float(rv))
    if isinstance(lv, int) or isinstance(rv, int):
        return mkbool(int(lv) >= int(rv))
    return mkbool(str(lv) >= str(rv))

def val_eq(l, r):
    lv = l.value
    rv = r.value
    return mkbool(lv == rv)

################ Dict

def dict_put(l, r, value):
    entry = r.value             # XXX need hash method!
#    print "dict_put", l, entry, value
    l.value[entry] = value
    return value                # lhsop MUST return value

def dict_get(l, r):
    entry = r.value             # XXX need hash method!
    ret = l.value.get(entry, null_value)
    return ret

def dict_init(obj, arg=None):
    if arg:
        obj.value = dict(arg.value) # XXX check if Dict!!!
    else:
        obj.value = {}

def dict_pop(obj, arg):
    return obj.value.pop(arg.value) # XXX check arg has value!!!

Dict.setprop(const.METHODS, _mkdict({
    'len': pyfunc(val_len),
    'str': pyfunc(val_str),
    'repr': pyfunc(val_repr),
    'str': pyfunc(val_str),
    'pop': pyfunc(dict_pop),
    const.INIT: pyfunc(dict_init),
}))
Dict.setprop(const.BINOPS, _mkdict({
    '[': pyfunc(dict_get)
}))
Dict.setprop(const.LHSOPS, _mkdict({
    '[': pyfunc(dict_put)
}))

################ List

def list_init(l, value=None):   # XXX take List
    if value is None:
        value = []
    l.value = value

def list_append(l, item):
    l.value.append(item)

def list_pop(l,item=None):
    if item is None:
        return l.value.pop()
    return l.value.pop(item.value) # XXX check if Number

# XXX supply native version for scope issues
#       or pass scope to pyfuncs???
def list_for_each(l, func):
    for item in l.value:
        vmx.invoke_function(func, None, [item]) # XXX need scope?

# XXX supply native version for scope issues
#       or pass scope to pyfuncs???
def list_each_for(l, func): # XXX TEMP until reversed?
    # XXX use backwards counting index (avoid copying list)??
    for item in reversed(l.value):
        vmx.invoke_function(func, None, [item]) # XXX need scope?

def list_get(l, r):
    # XXX check if integer
    return l.value[r.value]

def list_put(l, r, value):
    l.value[r.value] = value
    return value

def list_str(l):
    return mkstr("[%s]" %
                 (", ".join([vmx.invoke_method(x, 'str', None).value # XXX scope
                             for x in l.value])))

List.setprop(const.METHODS, _mkdict({
    'append': pyfunc(list_append),
    'len': pyfunc(val_len),
    'str': pyfunc(list_str),
    'pop': pyfunc(list_pop),
    'repr': pyfunc(val_repr),
    # XXX slice(start[,end]) (return range of elements)
    const.INIT: pyfunc(list_init),
    # TEMP: replace with native code:
    'each_for': pyfunc(list_each_for),
    'for_each': pyfunc(list_for_each)
}))
List.setprop(const.BINOPS, _mkdict({
    '[': pyfunc(list_get)
}))
List.setprop(const.LHSOPS, _mkdict({
    '[': pyfunc(list_put),
}))

################ Number

# XXX TEMP? replace with Int and Real?
# XXX XXX need to use "to_number" method on LHS (y) values??????!!!!!!

def neg(x):
    return new_vinst(x.getclass(), -x.value)

def add(x, y):
    return new_vinst(x.getclass(), x.value + y.value)

def sub(x, y):
    return new_vinst(x.getclass(), x.value - y.value)

def mul(x, y):
    return new_vinst(x.getclass(), x.value * y.value)

def div(x, y):
    return new_vinst(x.getclass(), x.value / y.value)

def eq(l, r):
    l = l.value
    r = r.value                 # XXX str()?
#    print "eq", l, r
    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) == float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) == int(r))
    return mkbool(str(l) == str(r))

def ne(l, r):
    return obj_not(eq(l, r))

def ge(l, r):
    l = l.value
    r = r.value

    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) >= float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) >= int(r))
    return mkbool(str(l) >= str(r))

def lt(l, r):
    return obj_not(ge(l, r))

def le(l, r):
    l = l.value
    r = r.value

    if isinstance(l, float) or isinstance(r, float):
        return mkbool(float(l) <= float(r))
    if isinstance(l, int) or isinstance(r, int):
        return mkbool(int(l) <= int(r))
    return mkbool(str(l) <= str(r))

def gt(l, r):
    return obj_not(le(l, r))

Number.setprop(const.METHODS, _mkdict({
    'str': pyfunc(val_str),
    'repr': pyfunc(val_repr),
    const.INIT: pyfunc(val_init),
}))
Number.setprop(const.UNOPS, _mkdict({
    '-': pyfunc(neg),
}))
Number.setprop(const.BINOPS, _mkdict({
    '+': pyfunc(add),
    '-': pyfunc(sub),
    '*': pyfunc(mul),
    '/': pyfunc(div),
    '==': pyfunc(eq),
    '!=': pyfunc(ne),
    '>=': pyfunc(ge),
    '<=': pyfunc(le),
    '>': pyfunc(gt),
    '<': pyfunc(lt),
}))

################ Str

def str_concat(x, y):
    ys = vmx.invoke_method(y, 'str', None) # XXX scope

    # XXX optimization: check if either is empty!!
    return new_vinst(x.getclass(), x.value + y.value)

def str_strip(this):
    return new_vinst(this.getclass(), this.value.strip())

def str_get(l, r):
    # XXX check if r is integer
    return new_vinst(l.getclass(), l.value[r.value])

def str_slice(l, a, b=None):
    av = a.value                # XXX check if int
    if b is not None:
        bv = b.value            # XXX check if int
        ret = l.value[av:bv]
    else:
        ret = l.value[av:]
    return new_vinst(l.getclass(), ret)

def str_str(this):
    return this

def str_repr(this):
    # XXX check if contains '"'
    # no way to handle both kinds of quotes
    # without backslashing or triple quote
    return mkstr('"%s"' % this.value)

def str_eq(l, r):
    l = l.value
    r = r.value                 # XXX str()?

    return mkbool(str(l) == str(r))


Str.setprop(const.METHODS, _mkdict({
    'len': pyfunc(val_len),
    'repr': pyfunc(val_repr),
    'slice': pyfunc(str_slice),
    'str': pyfunc(str_str),
    'strip': pyfunc(str_strip),
    const.INIT: pyfunc(val_init),
}))
Str.setprop(const.BINOPS, _mkdict({
    '+': pyfunc(str_concat),
    '==': pyfunc(eq),
    '!=': pyfunc(ne),
    # XXX full relops?
    '[': pyfunc(str_get),      # XXX needs wrap
}))

################ Null

def null_str(this):
    return mkstr("null")

def null_call(*args):
    raise Exception("'null' called; bad method name?")

Null.setprop(const.METHODS, _mkdict({
    'str': pyfunc(null_str)
}))

Null.setprop(const.BINOPS, _mkdict({
    '(': pyfunc(null_call)
}))

################ Bool

def bool_str(this):
    if this.value:
        return mkstr("true")
    else:
        return mkstr("false")

# XXX have own MetaClass "new" to return one of the doubleton values?
# XXX subclass into True and False singleton classes????
Bool.setprop(const.METHODS, _mkdict({
    'str': pyfunc(bool_str)
}))

def mkbool(val):
    """
    convert Python truthiness
    to language true or false Instance
    XXX lookup by name??
    """
    if val:
        return true_val
    else:
        return false_val

################ Callable

def callable_str(o):
    return mkstr(repr(o))

Callable.setprop(const.METHODS, _mkdict({
    'str': pyfunc(callable_str) # fallback
}))

################ PyObjClass meta-class for PyObject
#               (creates PInstance for direct invoke)

# XXX eliminate by having PyObject provide '(' binop???
#       (cleaner, but slower)

def unwrap(x):
    if hasattr(x, 'value'):     # faster than isistance(x, VInstance)??
        return x.value
    else:
        return x

class PInstance(VInstance):
    """
    Python class for PyObjects (Python objects from pyimport)
    .value is the Python object
    .invoke method attempts to call the object directly
    """

    def invoke(self, vm):
        ret = self.value(*[unwrap(x) for x in vm.args])

        if isinstance(ret, Instance):
            return ret
        vm.ac = wrap(ret, vm.iscope) # may create another PyObject!

def pyobj_new(x,y):
    return PInstance(x, y)

PyObjClass = defclass(Class, 'PyObjClass', [Class])
PyObjClass.setprop(const.METHODS, _mkdict({
    const.NEW: pyfunc(pyobj_new),
}))

################ PyObject -- wrapper around a Python Object (PInstance)
# PyObjects are created by pyimport("python_module")

PyObj = defclass(PyObjClass, 'PyObj', [Callable])

def pyobj_get(l, r):
    v = getattr(l.value, r.value) # get Python object attribute
    return wrap(v, system.get_initial_scope()) # XXX needs scope / CPyObject???

PyObj.setprop(const.METHODS, _mkdict({
    const.INIT: pyfunc(val_init)
    # getprop gets language Instance property
    #   XXX have a getattr method to get Python attr?!
}))

# XXX TODO binary '['
PyObj.setprop(const.BINOPS, _mkdict({
    '.': pyfunc(pyobj_get),     # gets Python object attr!
}))

# XXX TODO LHSOPS for '.' and '[' ?!!! need to unwrap values!

################################################################

def wrap(value, scope):
    """
    wrap a Python `value` in a language Instance
    `scope` used to find System types by name

    used by vm `lit` and `pyfunc`; type `PyObject`
    """
    if isinstance(value, bool):
        return mkbool(value) # XXX lookup local true/false??

    if isinstance(value, NUM):
        return system.create_sys_type('Number', scope, value)

    if isinstance(value, str):
        return system.create_sys_type('Str', scope, value)

    # XXX handle bytes??

    if value is None:
        return null_value

    # XXX complain??
    return system.create_sys_type('PyObj', scope, value)

################################################################
# TEMP:

def sys_foo(vm, *args):
    print(vm, args)
    return null_value

sys_types['foo'] = CPyFuncVM(sys_foo)

################################################################
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
