# Copyright © 2021,2023 Philip L. Budne
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

# LCXyz is a CObject for Language Class Xyz
# CXyz is a Python subclass of CObject
# (since Xyz is reserved for typing names!)

# NOTE!!! For methods/ops use 'xxx' strings (make searching easier)

# XXX split this up (into classes/xxx.py) before it gets much larger??
#       maybe have one file per Class?? named classes/ClassName.py??
#       (lots of stuff is missing, so it's bound to grow....)

# Python
import os
import types
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Tuple, Union, cast

# XXL:
import xxlobj
import const
import vmx

NUM = (int, float)              # Python3

# used to set MODINFO_DEBUG_BOOTSTRAP
XXL_DEBUG_BOOTSTRAP = os.getenv('XXL_DEBUG_BOOTSTRAP', None)

CWD = os.getcwd()               # current working directory
CWD_SEP = CWD + os.sep

root_scope = vmx.Scope()

classes_scope = vmx.Scope(root_scope) # scope for "classes" internal Module

__initialized = False

#PythonValue = Union[int, float, str, Dict, List, None, set, Iterable, Iterator]
PythonValue = Any

class UError(Exception):
    """
    Exception class for user errors; show vm backtrace
    """

# All language objects are represented by the interpreter
# as instances of the Python CObject class (or subclasses thereof).
# All such Python classes should start with the letter "C"
#       (the variable ClassName should point to the Class object of that name)

Cache = Dict[str, "CCallable"]

class CObject:
    """
    Python class representing a language Object
    """

    __slots__ = ['props', 'klass', 'cache']
    hasvalue = False

    def __init__(self, klass: Optional["CObject"]):
        # klass may only be None when creating initial Class (Object)
        self.setclass(klass or self)
        self.props: Dict[str, "CObject"] = {}
        # NOTE! cache only written for Class objects
        # (if per-object caching, including BoundMethods) is desired
        # need to keep a global serial number in each object, and increment it
        # to invalidate all cache entries.
        self.cache: Cache = {}

    def setclass(self, klass: "CObject") -> "CObject":
        self.klass = klass
        return klass

    def getclass(self) -> "CObject":
        """
        return CObject for object Class
        """
        return self.klass

    def classname(self) -> str:
        """
        return Python string for object class name; used in __repr__
        """
        c = self.getclass()
        if c is null_value:
            return "Unknown!"

        assert c is not None
        n = c.getprop(const.NAME).getvalue() # XXX getstr??
        assert isinstance(n, str)
        if subclass_of(c, [LCClass]):
            return '%s: %s' % (n, self.getprop(const.NAME).getvalue())

        return n

    def invoke(self, vm: vmx.VM) -> None:
        # will raise UError if op not found:
        # NOTE!! find_op does not return BoundMethod
        #       (called 99.999% of time from XxxOpInstrs)
        m = find_op(self, const.BINOPS, OPEN_PAREN)
        vm.args.insert(0, self) # OK, another place where THIS is passed
        m.invoke(vm)

    def hasprop(self, prop: str) -> bool:
        return prop in self.props

    def delprop(self, prop: str) -> None:
        self.props.pop(prop)

    def getprop(self, prop: str) -> "CObject":
        return self.props.get(prop, null_value)

    def setprop(self, prop: str, value: "CObject") -> None:
        self.props[prop] = value

    def getvalue(self) -> Any:
        raise UError("not a Python valued Object") # ValueError?!

    def __str__(self) -> str:
        return repr(self)       # XXX ???

    def __repr__(self) -> str:
        return '<%s at %#x>' % (self.classname(), id(self))

class CPObject(CObject):
    """
    Python backing class for Primitive Object Classes
    (has a value property which contains a Python type)
    """
    __slots__ = ['value']
    value: PythonValue
    hasvalue = True

    def __init__(self, this_class: CObject):
        super().__init__(this_class)
        self.value = None       # set by init method and/or _new_pobj

    def getvalue(self) -> PythonValue:
        return self.value

    def getint(self) -> int:
        assert isinstance(self.value, int)
        return self.value

    def __str__(self) -> str:
        if self.value is None:
            return "null"
        if isinstance(self.value, bool):
            return str(self.value).lower()
        return str(self.value)

    def __hash__(self) -> int:
        if not self.value.__hash__: # type: ignore[truthy-function, unused-ignore]
            # avoid error calling None!
            raise UError('%s not hashable' % self.classname())
        return self.value.__hash__() # type: ignore[no-any-return]

    def __eq__(self, other: object) -> bool:
        # XXX raise ValueError?
        return hasattr(other,'value') and self.value == other.value

    def __lt__(self, other: object) -> Any:  # need for sorted iterator
        # XXX raise ValueError?
        assert isinstance(other, CObject)
        return self.value < other.getvalue()

    def __repr__(self) -> str:
        """show wrapped value"""
        return '<%s: %s at %#x>' % \
            (self.classname(), repr(self.value), id(self))

################

Args = List[str]

class CCallable(CObject):
    """
    Base class for directly callable CObjects.
    """
    def invoke(self, vm: vmx.VM) -> None:
        raise Exception("invoke not overridden") # SNH -- Should Not Happen

    def args(self) -> Args:
        raise Exception("args not overridden") # SNH

    def defn(self) -> str:
        raise Exception("defn not overridden") # SNH

class CContinuation(CCallable):
    """
    A Callable instance backed by a native (VM) Continuation
    NOTE: opaque (no Class methods to expose innards) for now
    """
    __slots__ = ['fp']

    def __init__(self, fp: vmx.Frame):
        self.klass = LCContinuation
        self.props = {}
        self.fp = fp

    def __repr__(self) -> str:
        return "<Continuation: %s>" % self.defn()

    def invoke(self, vm: vmx.VM) -> None:
        l = len(vm.args)
        if l == 1:
            vm.ac = vm.args[0]  # return value
        elif l == 0:
            vm.ac = null_value  # XXX undefined??
        else:
            # before restore_frame, to show CALLER!!
            raise UError("Too many args (%d) to %r" % (len(vm.args), self))
        vm.restore_frame(self.fp) # ***JUST*** like ReturnInstr

    def args(self) -> Args:
        """
        for __args method: return Python list of str argument names
        """
        return ["value"]

    def defn(self) -> str:
        """
        Return Python str for "definition" location.

        (in this case, it's where it will return to,
         which may be the statement after, if return value not used)
        """
        return vmx.fp_where(self.fp)

    def backtrace(self) -> List[str]:
        """
        Return Python list of str
        """
        return vmx.fp_backtrace_list(self.fp)

class CClosure(CCallable):
    """
    A Callable instance backed by a Closure (VM code + scope)
    NOTE: opaque (no Class methods to expose innards) for now
    """
    __slots__ = ['code', 'scope'] # XXX extend?

    def __init__(self, code: vmx.VMInstrs, scope: vmx.Scope,
                 doc: Optional[str] = None):
        self.klass = LCClosure
        self.props = {}
        self.code = code
        self.scope = scope
        # PLB: I _HATE_ the Python ternary
        self.setprop(const.DOC, doc and mkstr(doc) or null_value)

    def __repr__(self) -> str:
        return "<Closure: %s>" % self.defn()

    def invoke(self, vm: vmx.VM) -> None:
        vm.save_frame(True)     # show=True
        # 'return' Continuation will be generated from FP
        #       by "args" Instr (first Instr in code)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope
        # NOTE! vm.args picked up by "args" opcode!

    def args(self) -> Args:
        assert isinstance(self.code[0], vmx.ArgsInstr)
        return self.code[0].args() # ask first VM Instr about args!!

    def defn(self) -> str:
        return self.code[0].fn_where() # ask first VM Instr about location!

class CBClosure(CClosure):
    """
    create closure for a {} block
    (hidden in backtraces)
    not currently visible to user
    (unless flow control implemented by passing block closure pointers)
    """
    def __repr__(self) -> str:
        return "<BClosure: %s>" % self.defn()

    def invoke(self, vm: vmx.VM) -> None:
        vm.save_frame(False)    # show=False
        # leave label Continuation will be generated from FP
        #       by ""[lu]scope" Instr (first Instr in code)
        vm.pc = 0
        vm.cb = self.code
        vm.scope = self.scope

    def args(self) -> Args:
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
    __slots__ = ['obj', 'method']

    def __init__(self, obj: CObject, method: CCallable):
        self.klass = LCBoundMethod
        self.props = {}
        self.obj = obj
        self.method = method

    def __repr__(self) -> str:
        return "<BoundMethod: %s %s>" % (repr(self.obj), self.method)

    def invoke(self, vm: vmx.VM) -> None:
        # *this* is the main place "THIS" is explicitly passed!!!
        vm.args.insert(0, self.obj) # prepend saved "this" to arguments
        self.method.invoke(vm)      # returns value in AC

    def args(self) -> Args:
        return self.method.args()[1:] # omit "this" arg

    def defn(self) -> str:
        return self.method.defn()

# Calling Python functions (ie; primitive class methods) was orignally
# implemented as a Closure with two VM instructions (pycall, return).
# The CObject.invoke method avoids that.
class CPyFunc(CCallable):
    """
    A Callable instance backed by a Python function
    """
    __slots__ = ['fun', 'argfunc']

    def __init__(self,
                 f: Callable,                         # PYTHON callable!
                 argfunc: Optional[Callable] = None): # for docstring
        self.klass = LCPyFunc
        self.props = {}
#        # detect pyfunc() calls on a pre-decorated function
#        if isinstance(f, CPyFunc):
#            # Python programming error, want Python backtrace:
#            raise Exception(f"double wrapping {f.fun}")
        self.fun = f
        self.argfunc = argfunc or f
        # make sure PyFunc.__doc never shows through
        self.setprop(const.DOC, _mkstr(f.__doc__ or ""))

    def __repr__(self) -> str:
        # was self.fun.__name___
        return "<PyFunc: %s>" % self.defn()

    def invoke(self, vm: vmx.VM) -> None:
        vm.ac = self.fun(*vm.args)
        #assert(isinstance(vm.ac, CObject))

    def __call__(self, *args: Any) -> Any:
        """
        catch mistakenly calling a CPyFunc (decorated Python function)
        from another Python function.
        """
        # Python programming error, want Python backtrace:
        raise Exception("Attempt to call %s" % self)

    def args(self) -> Args:
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

    def defn(self) -> str:
        """
        For documentation: NOT in "usual" format (includes name)
        (have separate "name" method??)
        """
        co = self.fun.__code__
        fname = co.co_filename
        if fname.startswith(CWD_SEP): # trim CWD/ from file name
            fname = fname[len(CWD_SEP):]
        return "%s:%s (%s)" % (fname, co.co_firstlineno, self.fun.__name__)

def pyfunc(func: Callable) -> "CPyFunc":
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

    def invoke(self, vm: vmx.VM) -> None:
        vm.args.insert(0, cast(CObject,vm))   # prepend vm to arguments
        super().invoke(vm)

    def args(self) -> Args:
        return super().args()[1:] # trim "vm" arg

def pyvmfunc(func: Callable) -> "CPyVMFunc":
    """
    decorator for Python functions that need pointer to VM
    """
    return CPyVMFunc(func)

################

class CPyIterator(CPObject):
    """
    wrapper around a Python iterator
    """
    value: Iterator[Any]

    def __init__(self, iterator: Iterator[Any]):
        self.klass = LCPyIterator
        self.props = {}
        self.value = iterator

    def __str__(self) -> str:
        return repr(self)

def pyiterator(iterator: Iterator) -> CPyIterator:
    """
    Make a PyIterator from a Python iterator (has a __next__ method)
    """
    assert hasattr(iterator, '__next__')
    return CPyIterator(iterator)

################################################################

def _new_pobj(this_class: CObject, arg: PythonValue) -> CPObject:
    """
    FOR INTERNAL USE ONLY!!
    creates an interpreter Primitive Object of Class `this_class`
    wrapped around Python value `arg`
    does not run this_class 'init' method (which would want an Object)
    """
    o = CPObject(this_class)
    o.value = arg
    return o

def _mkdict(vals: Dict[str, CObject]) -> CPObject:
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    nv = {_mkstr(k): v for k, v in vals.items()}
    if __initialized:
        return new_by_name('Dict', nv)
    return _new_pobj(LCDict, nv)

def _mklist(vals: List[Any]) -> CObject:
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    """
    if __initialized:
        return new_by_name('List', vals)
    assert _LCList is not None
    return _new_pobj(_LCList, vals)

def _mkstr(s: str) -> CPObject:
    """
    ONLY USE TO CONSTRUCT BASE TYPES!
    see mkstr
    """
    if __initialized:           # doc strings
        return mkstr(s)
    assert _LCStr
    return _new_pobj(_LCStr, s)

def _mkobj(props: Dict[str, CObject]) -> CObject:
    """
    used to create lexer tokens
    """
    o = CObject(LCObject)
    o.props.update(props)
    return o

################ use once __xxl.types initialized

def class_by_name(name: str) -> CObject:
    """
    look for class `name` in classes Module scope
    """
    assert(__initialized)
    return classes_scope.lookup(name)

def new_by_name(name: str, value: PythonValue) -> CPObject:
    """
    create a new CPObject of class `name` w/ value `value`
    """
    ty = class_by_name(name)
    return _new_pobj(ty, value)

def mkstr(s: str) -> CPObject:
    """
    used to create Str from Python str, once up and running
    """
    return new_by_name('Str', s)

def mknumber(n: Union[int, float]) -> CObject:
    """
    used to create Number from Python int/float, once up and running
    """
    assert(__initialized)
    return new_by_name('Number', n)

def mkiterable(i: Iterable[Any]) -> CObject:
    assert(__initialized)
    return new_by_name('PyIterable', i)

################

def subclass_of(this_class: CObject, bases: List[CObject]) -> bool:
    """
    test if Class `this_class` is a subclass of any Class in bases
    `this_class` is CObject for a Class
    `bases` is Python list of CObjects (of class or subclass Class)
    """
    visited = set()
    def check(c: CObject) -> bool:
        visited.add(c)
        if c in bases:
            return True
        s = c.getprop(const.SUPERS)
        if s is null_value:
            return False
        for x in s.getvalue():       # XXX check if LCList
            if x not in visited and check(x):
                return True
        return False
    return check(this_class)

def instance_of(this: CObject, classes: List[CObject]) -> bool:
    """
    test if `this` is an instance of any Class in `classes` list
    `this` is CObject
    `classes` is list of Classes (CObject instances of (subclasses of) Class)
    """
    klass = this.getclass()
    assert klass
    return subclass_of(klass, classes)

################################################################

# backpatch Classes when Str/CList available:
_saved_supers = {}
_saved_names = {}
_saved_docs = {}
LCStr: CObject
LCList: CObject
_LCStr: Optional[CObject] = None
_LCList: Optional[CObject] = None

def defclass(metaclass: Optional[CObject],
             name: str,
             supers: Optional[List[CObject]] = None,
             publish: bool = True,
             doc: Optional[str] = None) -> CObject:
    """
    define a system Class
    `name` is Python string
    `metaclass` of this class (typ. Class)
      (the class that the returned object is an instance of
       ie; supplies "new" method)
    `supers` is Python list of superclass Class objects
    """
    class_obj = CObject(metaclass)

    if _LCStr:                  # Str class available?
        class_obj.setprop(const.NAME, _mkstr(name))
        class_obj.setprop(const.DOC, _mkstr(doc or ""))
    else:
        _saved_names[class_obj] = name
        _saved_docs[class_obj] = doc or ""

    if supers:
        if _LCList:             # CList class available?
            class_obj.setprop(const.SUPERS, _mklist(supers))
        else:
            _saved_supers[class_obj] = supers

    if publish:
        classes_scope.defvar(name, class_obj)

    return class_obj

# base metaclass
LCClass = defclass(None, 'Class',
                   doc="Base Metaclass, home of the default 'new' method")

LCClass.setclass(LCClass)   # circular! Class.new creates a new Class!
# supers set to [Object] below

# root Class; circular with "Class" metaclass, so defined second.
LCObject = defclass(LCClass, 'Object', [],
                    doc="Base Class") # root Class

LCNullish = defclass(LCClass, 'Nullish', [],
                     doc="Mixin for nullish classes.")

LCUndefined = defclass(LCClass, 'Undefined', [LCNullish, LCObject],
                       doc="Class for undefined value.")

####
# wrappers, with .value

# metaclass for PObjects (creates Python CPObject)
LCPClass = defclass(LCClass, 'PClass', [LCClass],
                  doc="Metaclass for Primitive/Python value Classes")

# Primitive Object Base Class
# superclass (with .value) of Classes that are wrappers around Python classes
LCPObject = defclass(LCPClass, 'PObject', [LCObject],
                   doc="Base class for Primitive/Python value Classes")

# bootstrap.xxl defines static 'new' method
LCNull = defclass(LCClass, 'Null', [LCNullish, LCPObject],
                doc="Built-in Class of `null` value")

# bootstrap.xxl defines static 'new' method
LCBool = defclass(LCPClass, 'Bool', [LCPObject],
                doc="Built-in Class for `true` and `false` values")

# Pure Mixin
LCIterable = defclass(LCClass, 'Iterable', [],
                     doc="Mixin for Classes that can be iterated over")

# created by mkiterable
LCPyIterable = defclass(LCPClass, 'PyIterable', [LCPObject, LCIterable],
                        doc="""
    Wrapper for Python 'iterable' Objects (CDict, CList, Str);
    Also returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), static method PyIterable.range().
    """)

LCList = defclass(LCPClass, 'List', [LCPyIterable],
                 doc="Built-in mutable sequence Class")
_LCList = LCList

LCStr = defclass(LCPClass, 'Str', [LCPyIterable],
                 doc="Built-in immutable Unicode string Class")
_LCStr = LCStr

LCDict = defclass(LCPClass, 'Dict', [LCPyIterable],
                  doc="Built-in dictionary mapping Class")
LCSet  = defclass(LCPClass, 'Set', [LCPyIterable],
                  doc="Built-in unordered collection of unique elements.")

# non-iterable:
LCNumber = defclass(LCPClass, 'Number', [LCPObject],
                    doc="Built-in int/float wrapper Class")

__initialized = True            # new_by_name for Dict, Str, CList now safe

################
# Str, CList now exist:
# set Class metaclass super list
LCClass.setprop(const.SUPERS, _mklist([LCObject]))

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
LCCallable = defclass(LCClass, 'Callable', [LCObject],
                     doc="""
    Virtual base Class for built-in callable classes
    (BoundMethod, Continuation, PyFunc, PyVMFunc)
    """)

# all backed by Python CXyZzy classes with invoke methods:
# XXX use metaclass (CClass?) that prohibits user call of 'new' method?
LCBoundMethod = defclass(LCClass, 'BoundMethod', [LCCallable],
                         doc="Built-in Class for a method bound to an Object")
LCClosure = defclass(LCClass, 'Closure', [LCCallable],
                     doc="Built-in Class for a native function bound to a scope")
LCContinuation = defclass(LCClass, 'Continuation', [LCCallable],
                          doc="Built-in Class for a Continuation")
LCPyFunc = defclass(LCClass, 'PyFunc', [LCCallable],
                    doc="Built-in Class for function implemented in Python")
LCPyVMFunc = defclass(LCClass, 'PyVMFunc', [LCCallable],
                      doc="""
   Built-in Class for function implemented in Python
   with access to VM internals
   """)


# wrapper around a Python iterator (w/ next method)
LCPyIterator = defclass(LCClass, 'PyIterator', [LCObject, LCIterable],
                      doc="Built-in Class for a wrapper around a Python iterator")

################

null_value: CPObject = _new_pobj(LCNull, None)

undef_value = CObject(LCUndefined)

# create (only) instances of true/false (a doubleton)!
# subclass Bool into True and False singleton Classes??
true_value = _new_pobj(LCBool, True)
false_value = _new_pobj(LCBool, False)

################

# utility called by VM jumpn/jumpe: NOT a method/pyfunc
# (had originally planned to have all Classes have an is_true method)
def is_true(obj: CObject) -> bool:
    """
    return Python True/False for an object
    non-premature optimization:
    only "null", "false", "undefined" objects, and zero are false.
    """
    if obj is false_value or obj is null_value or obj is undef_value:
        return False
    if obj.hasvalue and getattr(obj, 'value') == 0:
        return False
    return True                 # not falsey

################ Object -- the base type for all instances and classes

@pyfunc
def obj_init(this_obj: CObject, *args: CObject) -> CObject:
    """
    default init method for Object class
    a fatal error if any arguments given
    """
    if len(args) > 0:
        raise UError("%s.%s takes no arguments" %
                        (this_obj.classname(), const.INIT))
    return null_value

@pyfunc
def obj_str(this: CObject) -> CObject:
    """
    default to_str method: should return a human-friendly string
    """
    return mkstr(str(this))

@pyfunc
def obj_props(this: CObject) -> CObject:
    """
    returns an Iterable for (String) property names
    of `this` Object
    """
    return mkiterable(this.props.keys())

@pyfunc
def obj_repr(this: CObject) -> CObject:
    """
    Default Object string representation method
    (calls Python repr(this))
    """
    return mkstr(repr(this))

@pyfunc
def obj_reprx(l: CObject) -> CObject:
    """
    for debug: show Class, and Python value (which may include id?)
    """
    return mkstr("<%s: %s>" % (l.classname(), repr(l)))

@pyfunc
def obj_ident(l: CObject, r: CObject) -> CObject: # SNOBOL4 IDENT
    """
    Test if `l` and `r` refer to the same Object
    """
    return mkbool(l is r)

@pyfunc
def obj_differ(l: CObject, r: CObject) -> CObject: # SNOBOL4 DIFFER
    """
    Test if `l` and `r` refer to different Objects
    """
    return mkbool(l is not r)

def _not(x: CObject) -> CObject:
    """
    not a pyfunc (may call at any time)
    takes CObject, returns CObject
    """
    return mkbool(not is_true(x))

# XXX do this in pobj_not? all other objects always true????
@pyfunc
def obj_not(x: CObject) -> CObject:
    """
    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, zero, null, or undefined)
    """
    return _not(x)

@pyfunc
def obj_delprop(this: CObject, name: CObject) -> CObject:
    """
    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    """
    this.props.pop(name.getvalue())
    return null_value

@pyfunc
def obj_setprop(l: CObject, r: CObject, value: CObject) -> CObject:
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
def find_in_supers(l: CObject, r: CObject, default: CObject,
                   caching: bool = True) -> CObject:
    """
    Breadth first search of superclass methods/properties;
    `l` is CObject, `r` is Str for method/property name.
    """
    c = c0 = l.getclass()
    assert c is not None
    assert c0 is not None
    rv = r.getvalue()           # XXX getstr?

    supers = c.getprop(const.SUPERS)
    q = []                      # queue
    seen = set()

    while True:
        if supers is not null_value:
            slist = supers.getvalue() # .getvalue, expect List getlist??
            q.extend(slist)
            seen.update(slist)

        if q:
            c = q.pop(0)        # front of queue
        else:
            break

        # NOTE!! doc.xxl also know that properties take precedence
        # over methods (would be moot w/ descriptors); search for MRO.
        assert c is not None
        if c.hasprop(rv):
            return c.getprop(rv) # never BoundMethod

        methods = c.getprop(const.METHODS)
        if methods is not null_value:
            m = methods.getvalue().get(r, null_value) # .getdict?
            if m is not null_value:
                if caching:
                    cache_line = '__method:' + r.getvalue()
                    c0.cache[cache_line] = m
                return CBoundMethod(l, m)

        supers = c.getprop(const.SUPERS)

    return default

# NOTE! utility, not method
# XXX return (obj, value) to avoid generating BoundMethod?
def find_in_class(l: CObject, r: CObject, default: CObject) -> CObject:
    """
    `r` is Str
    may return BoundMethod
    """
    # XXX XXX XXX use descriptors (objects w/ get/set methods) for methods
    #           class methods, members, (read-only members)???
    #           all kept in "props"?!!!!!!
    c = l.getclass()
    assert c is not None

    rv = r.getvalue()
    #print("find_in_class", repr(l), repr(r))

    # check for class property
    if c.hasprop(rv):
        return c.getprop(rv)

    cache_line = '__method:' + rv
    if cache_line in c.cache: # XXX change name?
        m = c.cache[cache_line]
        assert isinstance(m, CCallable)
        return CBoundMethod(l, m)

    methods = c.getprop(const.METHODS)
    if methods is not null_value:
        m = methods.getvalue().get(r, null_value) # .getdict?
        if m is not null_value:
            c.cache[cache_line] = m
            assert isinstance(m, CCallable)
            return CBoundMethod(l, m)

    return find_in_supers(l, r, default)

@pyfunc
def obj_getprop(l: CObject, r: CObject) -> CObject:
    """
    Object getprop method/operator
    return `r` (String) property of object `l`
    """
    rv = r.getvalue()           # XXX check is Str
    if l.hasprop(rv):
        return l.getprop(rv)
    return find_in_class(l, r, undef_value) # may return BoundMethod

@pyfunc
def obj_hasprop(l: CObject, r: CObject) -> CObject:
    """
    Return `true` if object `l` has own (Str) property `r` (not interited).
    """
    # XXX check r is Str
    return mkbool(l.hasprop(r.getvalue()))

def find_op(obj: CObject, optype: str, op: CPObject) -> CObject:
    """
    Utility (not method)
    `obj` is CObject
    `optype` is Python string: UNOPS, BINOPS, or LHSOPS
    `op` is Str for operator
    NOTE!! Does *NOT* return BoundMethod!!
        called from XxxOpInstrs 99.999% of time
        (only exception is CObject.invoke for '(')
    """
    #print("find_op", obj, repr(optype), repr(op))
    c = c0 = obj.getclass()
    assert c is not None
    assert c0 is not None

    assert isinstance(op.value, str)
    cache_line = optype + op.value
    if cache_line in c.cache:
        x = c.cache[cache_line]
        return x

    q = []
    seen = set()
    seen.add(c)
    while True:
        assert c is not None
        ops = c.props.get(optype, null_value) # getprop
        if ops is not null_value:
            v = ops.getvalue()  # .getdict?
            # XXX CCallable or PyObject??
            vd = cast(Dict[CObject, CCallable], v)
            if op in vd:
                val = vd[op]    # get from op dict
                c0.cache[cache_line] = val # save in cache
                return val

        supers = c.props.get(const.SUPERS, null_value) # getprop
        if supers is not null_value:
            for s in supers.getvalue(): # expect Python list
                if s not in seen:
                    q.append(s)
                    seen.add(s)

        try:                    # cheaper than "if not q: break"?
            c = q.pop(0);
        except IndexError:
            break

    raise UError("%s %s for %s not found" % ( \
        const.OPDICT2ENGLISH.get(optype,optype), op, obj.classname()))

@pyfunc
def obj_get_in_supers(this: CObject, prop: CObject) -> CObject:
    """
    Object `..` operator; for calling superclass methods
    Looks for `prop` as property or method of superclasses of `this`;
    can be used as: `this.as_class(MyClass)..method`.
    """
    return find_in_supers(this, prop, undef_value, False)

# once upon a time class was stored as '__class' property,
# but it was messy when cloning.
@pyfunc
def obj_getclass(this: CObject) -> CObject:
    """
    return Class for `this`
    """
    k = this.getclass()
    assert k is not None
    return k

@pyfunc
def obj_setclass(this: CObject, klass: CObject) -> CObject:
    """
    set Class for `this`!!
    """
    k = this.setclass(klass)
    assert k is not None
    return k

@pyfunc
def obj_as_class(this: CObject, klass: CObject) -> CObject:
    """
    return an Object of Class `klass`, sharing properties with `this`.
    Use for calling superclass methods: `this.as_class(MyClass)..method`.
    """
    # XXX Have CObject methods?! Need to copy private (eg CPObject) members!?
    n = type(this)(klass)
    n.props = this.props        # YIKES! Proxy instead??
    return n

@pyfunc
def obj_call(l: CObject, *args: CObject) -> None:
    """
    default Object `(` binop
    (fatal error)
    """
    raise UError("%s does not have '(' binop" % l.classname())

@pyfunc
def obj_instance_of(this: CObject, c: CObject) -> CObject:
    """
    return `true` if Object `this` is an instance of
    Class (or CList of Classes) `c`
    """
    k = c.getclass()
    assert k is not None
    assert LCList is not None
    if subclass_of(k, [LCList]):
        cl = cast(List[CObject], c.getvalue()) # .getlist
    else:
        cl = [c]                # make Python list
    return mkbool(instance_of(this, cl))

LCObject.setprop(const.METHODS, _mkdict({
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
LCObject.setprop(const.BINOPS, _mkdict({
    '.': obj_getprop,           # same as getprop method!!
    '..': obj_get_in_supers,
    '===': obj_ident,           # "is"
    '!==': obj_differ,          # "is not"
    '==': obj_ident,            # allow null where str/num expected?
    '!=': obj_differ,           # ditto
    '(': obj_call,
}))
LCObject.setprop(const.UNOPS, _mkdict({
    '!': obj_not,
}))
LCObject.setprop(const.LHSOPS, _mkdict({
    '.': obj_setprop                # same as setprop!!
}))

################ Class -- base type for Classes (a MetaClass)

@pyfunc
def class_create(this_class: CObject, *args: CObject) -> CObject:
    """
    Default create method for `Class` (the base metaclass);
    Creates an empty instance of this_class (called from `Class.new`).
    """
    return CObject(this_class)

@pyfunc
def class_init(this_class: CObject, props: CObject) -> CObject:
    """
    init method for meta-class "Class" -- used to create new Classes.
    `props` is Dict holding properties (see doc/creating-classes.md and
    src/const.py CLASS_PROPS)
    """
    # XXX check props is a Dict!
    for key, val in props.getvalue().items():
        # XXX check key is a Str!
        # XXX check val is a Dict!
        kv = key.getvalue()
        if kv == 'props':
            # XXX check for overlap with methods?
            # XXX use descriptors for methods/members?!!!
            for pk, pv in val.getvalue().items():
                this_class.setprop(pk.value, pv)
            continue
        ikey = const.CLASS_PROPS.get(kv)
        if not ikey:
            metaclassname = this_class.classname()
            raise UError("Unknown %s property %s" % (metaclassname, key))
        this_class.props[ikey] = val # NOTE! stashes argument Dict value!!!

    if const.NAME not in this_class.props:
        raise UError("Class.new requires '%s'"  % const.NAME)

    # XXX complain if NAME doesn't start with a capitol letter??

    # XXX check if a metaclass: subclass_of(this_class, [Class])
    #   and insist that NAME ends with "Class"??

    if const.SUPERS not in this_class.props:
        # XXX complain??
        this_class.setprop(const.SUPERS, wrap([LCObject]))

    return null_value

@pyfunc
def class_call(this_class: CObject, *args: CObject) -> None:
    """
    `(` binop for Class -- fatal error
    (but common mistake if you have Python fingers) --
    tells you to use .new method!!
    """
    name = this_class.getprop(const.NAME).getvalue()
    raise UError("Called %s Class! Did you mean %s.new?" % (name, name))

@pyfunc
def class_subclass_of(this_class: CObject, c: CObject) -> CObject:
    """
    Return `true` if Class `this_class` is a subclass of
    Class (or CList of Classes) `c`
    """
    k = c.getclass()
    assert k is not None
    assert LCList is not None
    if subclass_of(k, [LCList]):
        cl = cast(List[CObject], c.getvalue()) # XXX .getlist
    else:
        cl = [c]                # make Python list
    return mkbool(subclass_of(this_class, cl))

@pyfunc
def class_clear_cache(this_class: CObject) -> CObject:
    """
    Clear the per-Class cache of methods and operators.
    """
    this_class.cache = {}
    return null_value

# Class: a meta-class: all Classes are instances of a meta-class
# (Class.new creates a new Class)
LCClass.setprop(const.METHODS, _mkdict({
    # Class.new in bootstrap.vmx
    'clear_cache': class_clear_cache,
    const.CREATE: class_create,
    const.INIT: class_init,     # Class.new creates new Classes
    # NOTE: "name" is a member, not a method!
    'subclass_of': class_subclass_of
}))

LCClass.setprop(const.BINOPS, _mkdict({
    '(': class_call
}))

################ PClass -- metaclass for PObjects

@pyfunc
def pclass_create(this_class: CObject) -> CObject:
    """
    'create' method for PClass metaclass
    makes an instance of this_class backed by a CPObject
    used to create PClass subclass objects (Number, CList, Dict, Bool, Null)
    """
    return CPObject(this_class)

LCPClass.setprop(const.METHODS, _mkdict({
   const.CREATE: pclass_create
}))

################ generic methods for PObject

@pyfunc
def pobj_len(this: CObject) -> CObject:
    """
    returns length (of String, CList or Dict)
    """
    return _new_pobj(LCNumber, len(this.getvalue())) # XXX look up by name?

@pyfunc
def pobj_str(this: CObject) -> CObject:
    """
    return human-friendly string representation of `this`
    (uses Python str function on value)
    """
    return mkstr(str(this.getvalue()))

@pyfunc
def pobj_repr(this: CObject) -> CObject:
    """
    return less human-friendly string representation of `this`
    (use Python repr function on value)
    """
    return mkstr(repr(this.getvalue()))

@pyfunc
def pobj_reprx(this: CObject) -> CObject:
    """
    for debug: show Class name, and Python repr
    """
    return mkstr("<%s: %s>" % (this.classname(), repr(this.getvalue())))

@pyfunc
def pobj_init(l: CObject, value: CObject) -> None:
    """
    default PObject init method
    (fatal error)
    """
    raise UError("{} missing init method".format(l.classname()))

@pyfunc
def pobj__init0(this: CObject, value: CObject) -> None:
    """
    default PObject init0 method
    (fatal error)
    """
    raise UError("{} missing init0 method".format(this.classname()))

@pyfunc
def pobj_ident(l: CPObject, r: CPObject) -> CObject:
    """
    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    """
    return mkbool(r.hasvalue and l.value is r.value)

@pyfunc
def pobj_differ(l: CPObject, r: CPObject) -> CObject:
    """
    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    """
    return mkbool(r.hasvalue and l.value is not r.value)

@pyfunc
def pobj__format(this: CObject, fmt: CObject) -> CObject:
    return mkstr(format(this.getvalue(), fmt.getvalue())) # XXX fmt.getstr()

LCPObject.setprop(const.METHODS, _mkdict({
    'repr': pobj_repr,
    'reprx': pobj_reprx,
    const.INIT: pobj_init,
    '__init0': pobj__init0,
    '__format': pobj__format
}))

LCPObject.setprop(const.BINOPS, _mkdict({
    '===': pobj_ident,
    '!==': pobj_differ,
    '==': pobj_ident,
    '!=': pobj_differ
}))

# common for CList and Str
@pyfunc
def pobj_slice(this: CPObject, start: CObject, end: Optional[CObject] = None) -> CPObject:
    """
    return a subrange (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to remainder)
    """
    startv = start.getvalue()   # XXX getint?
    v = cast(str, this.value)
    if end is not None:
        endv = end.getvalue()   # XXX getint?
        ret = v[startv:endv]
    else:
        ret = v[startv:]
    k = this.getclass()
    return _new_pobj(k, ret)

################ Callable base class

@pyfunc
def callable__args(this: CCallable) -> CObject:
    """
    currently private/hidden (to create docs)
    returns formatted string for args (as if a native function) with parens
    """
    return mkstr("(%s)" % ", ".join(this.args()))

@pyfunc
def callable__defn(this: CCallable) -> CObject:
    """
    currently private/hidden (to create docs)
    returns location (source file and line) of function definition
    """
    return mkstr(this.defn())

LCCallable.setprop(const.METHODS, _mkdict({
    '__args': callable__args,
    '__defn': callable__defn
}))

################ Continuation

@pyfunc
def continuation__backtrace_list(this: CContinuation) -> CObject:
    """
    return CList of Str return locations on Continuation stack.
    """
    return wrap(this.backtrace())

LCContinuation.setprop(const.METHODS, _mkdict({
    '__backtrace_list': continuation__backtrace_list
    # XXX have a visible method to print? replace xxl_backtrace??
}))

################ Iterable

# mixin/protocol
# Iterable classes must implement "iter" (Interator factory)

# for_each, each_for, map, map2 in bootstrap.xxl
LCIterable.setprop(const.METHODS, _mkdict({
}))

################ PyIterable

# subclass of Iterable, PObject
# superclass of CList, Dict, Str, Set!
# also created by mkiterable, used in:
#       Dict.{item,key,value}s()
#       Object.props()
#       PyIterable.range()

@pyfunc
def pyiterable_iter(this: CObject) -> CObject:
    """
    Return forward iterator.
    """
    return pyiterator(iter(this.getvalue()))

@pyfunc
def pyiterable_reversed(this: CObject) -> CObject:
    """
    Return reverse iterator.
    """
    # TypeError for "not reversible" (dict pre Python 3.8)
    return pyiterator(reversed(this.getvalue()))

@pyfunc
def pyiterable_sorted(this: CPObject, reverse: CObject = false_value) -> CObject:
    """
    Return sorted CList of iterator values.
    `reverse` is Bool to sort in reverse order (defaults to `false`).
    """
    v = this.value
    # XXX test for v.__iter__??
    return wrap(sorted(v, reverse=is_true(reverse)))

LCPyIterable.setprop(const.METHODS, _mkdict({
    'iter': pyiterable_iter,
    'reversed': pyiterable_reversed,
    'sorted': pyiterable_sorted
}))


@pyfunc
def pyiterable_range(*args: CPObject) -> CObject:
    """
    Static method:
    returns PyIterable for an integer range;
    iter() method generates fresh Iterators.

    range(10): returns Iterable for 0..9;
    range(1,10): returns Iterable for 1..9;
    range(1,10,2): returns Iterable for odd numbers 1..9
    """
    n = len(args)
    if n < 1 or n > 3:
        raise UError("range requires one to three arguments") 
    a0 = args[0].getint()
    if n == 1:
        r = range(a0)
    else:
        a1 = args[1].getint()
        if n == 2:
            r = range(a0, a1)
        else:
            r = range(a0, a1, args[2].getint())
    return mkiterable(r)

LCPyIterable.setprop('range', pyiterable_range) # static method

################ Dict

@pyfunc
def dict_putitem(l: CPObject, r: CObject, value: CObject) -> CObject:
    """
    `l[r] = value`
    """
    d = cast(Dict[CObject,CObject], l.value)
    d[r] = value
    return value                # lhsop MUST return value

@pyfunc
def dict_getitem(l: CPObject, r: CObject) -> CObject:
    """
    `l[r]`
    """
    d = cast(Dict[CObject,CObject], l.value)
    v = d.get(r, null_value)
    return v

@pyfunc
def dict__init0(this: CPObject) -> CObject:
    """
    Called by Dict.init (in bootstrap.xxl).
    Dodges needing private metaclass for Dict.
    """
    this.value = {}
    return null_value

@pyfunc
def dict_pop(obj: CPObject, key: CObject) -> CObject:
    """
    Remove Dict item with specified `key`.
    """
    d = cast(Dict[CObject, CObject],obj.value)
    return d.pop(key)

@pyfunc
def dict_items(this: CObject) -> CObject:
    """
    Return PyIterable for [key, value] value pairs.
    """
    return mkiterable(this.getvalue().items())

@pyfunc
def dict_keys(this: CObject) -> CObject:
    """
    Return PyIterable for Dict keys.
    """
    return mkiterable(this.getvalue().keys())

@pyfunc
def dict_values(this: CObject) -> CObject:
    """
    Return PyIterable for Dict values.
    """
    return mkiterable(this.getvalue().values())

LCDict.setprop(const.METHODS, _mkdict({
    '__init0': dict__init0,
    'items': dict_items,
    'keys': dict_keys,
    'len': pobj_len,
    'pop': dict_pop,
    'values': dict_values,
}))
LCDict.setprop(const.BINOPS, _mkdict({
    '[': dict_getitem
}))
LCDict.setprop(const.LHSOPS, _mkdict({
    '[': dict_putitem
}))

################ List

@pyfunc
def list__init0(l: CPObject) -> CObject:
    """
    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    """
    l.value = []
    return null_value

@pyfunc
def list_append(this: CPObject, item: CObject) -> CObject:
    """
    append `item`.
    """
    l = cast(List[CObject], this.value)
    l.append(item)
    return null_value

@pyfunc
def list_pop(this: CPObject, index: Optional[CPObject] = None) -> CObject:
    """
    Remove and return item at `index` (default last).
    """
    l = cast(List[CObject], this.value)
    if index is None:
        return l.pop()
    return l.pop(index.getint())

@pyfunc
def list_get(this: CPObject, item: CPObject) -> CObject:
    """
    `l[r]`
    """
    l = cast(List[CObject], this.value)
    return l[item.getint()]

@pyfunc
def list_insert(this: CPObject, index: CPObject, object: CObject) -> CObject:
    """
    Insert `object` at `index` (0 is first, -1 is last); Returns `null`.
    """
    l = cast(List[CObject], this.value)
    l.insert(index.getint(), object)
    return null_value

@pyfunc
def list_put(this: CPObject, r: CPObject, value: CObject) -> CObject:
    """
    `l[r] = value`
    """
    l = cast(List[CObject], this.value)
    l[r.getint()] = value
    return value		# lhsop MUST return value

# str, repr, for_each, each_for, map, map2 from Iterable (in bootstrap.xxl)
LCList.setprop(const.METHODS, _mkdict({
    '__init0': list__init0,
    'append': list_append,
    'insert': list_insert,
    'len': pobj_len,
    'pop': list_pop,
    'slice': pobj_slice,
}))
LCList.setprop(const.BINOPS, _mkdict({
    '[': list_get
}))
LCList.setprop(const.LHSOPS, _mkdict({
    '[': list_put
}))

################ Number

# XXX TEMP? replace with Int and Real?

@pyfunc
def neg(x: CObject) -> CPObject:
    """
    Return negative of `x`
    """
    return _new_pobj(x.getclass(), -x.getvalue())

@pyfunc
def add(l: CPObject, r: CPObject) -> CPObject:
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
def sub(l: CPObject, r: CPObject) -> CPObject:
    """
    subtract `r` from `l`
    """
    lv = l.value
    rv = r.value
    if rv == 0:
        return l
    return _new_pobj(l.getclass(), lv - rv)

@pyfunc
def mul(l: CPObject, r: CPObject) -> CPObject:
    """
    multiply `l` and `r`
    """
    lv = l.value
    rv = r.value
    if lv == 1:
        return r
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), lv * rv)

@pyfunc
def div(l: CPObject, r: CPObject) -> CPObject:
    """
    Divide `l` by `r`; always creates float.
    """
    lv = l.value
    rv = r.value
    if rv == 1:
        return l
    return _new_pobj(l.getclass(), lv / rv)

@pyfunc
def eq(l: CPObject, r: CObject) -> CObject:
    """
    return `true` if value of `l` is the same as value of `r`
    """
    # fail sliently if r is not PObject
    return mkbool(r.hasvalue and l.value == r.getvalue())

@pyfunc
def ne(l: CPObject, r: CObject) -> CObject:
    """
    return `true` if value of `l` is different from the value of `r`
    """
    # fail sliently if r is not PObject
    return mkbool(r.hasvalue and l.value != r.getvalue())

@pyfunc
def ge(l: CPObject, r: CPObject) -> CObject:
    """
    return `true` if value of `l` is >= the value of `r`
    """
    return mkbool(l.value >= r.getvalue())

@pyfunc
def lt(l: CPObject, r: CObject) -> CObject:
    """
    return `true` if value of `l` is < the value of `r`
    """
    return mkbool(l.value < r.getvalue())

@pyfunc
def le(l: CPObject, r: CObject) -> CObject:
    """
    return `true` if value of `l` is <= the value of `r`
    """
    return mkbool(l.value <= r.getvalue())

@pyfunc
def gt(l: CPObject, r: CObject) -> CObject:
    """
    return `true` if value of `l` is > the value of `r`
    (implemented as `!(l <= r)`)
    """
    return mkbool(l.value > r.getvalue())

@pyfunc
def bitand(l: CPObject, r: CObject) -> CObject:
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
def bitor(l: CPObject, r: CObject) -> CObject:
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
def bitnot(this: CObject) -> CObject:
    """
    return bitwise (binary) "not" (complement) of `this`
    """
    return _new_pobj(this.getclass(), ~this.getvalue())

@pyfunc
def num_to_float(this: CObject) -> CObject:
    """
    If value is a float, return `this`
    If value is an int, return a new Number object
    """
    if isinstance(this.getvalue(), float):
        return this
    return _new_pobj(this.getclass(), float(this.getvalue()))

@pyfunc
def num_to_int(this: CPObject) -> CObject:
    """
    If value is an int, return `this`
    If value is a float, return a new Number object
    """
    if isinstance(this.value, int):
        return this
    return _new_pobj(this.getclass(), int(this.value))

@pyfunc
def num_to_number(this: CObject) -> CObject:
    """
    identity method; returns `this`
    """
    return this

LCNumber.setprop(const.METHODS, _mkdict({
    'to_float': num_to_float,
    'to_int': num_to_int,
    'to_number': num_to_number,
}))

LCNumber.setprop(const.UNOPS, _mkdict({
    '-': neg,
    '~': bitnot,                # Int only!!
}))
LCNumber.setprop(const.BINOPS, _mkdict({
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

################ Set

@pyfunc
def set__init0(this: CPObject) -> CObject:
    """
    Called by Set.init (in bootstrap.xxl).
    Dodges needing private metaclass for Set.
    """
    this.value = set()
    return null_value

LCSet.setprop(const.METHODS, _mkdict({
    '__init0': set__init0,
    'len': pobj_len
}))

# XXX define '+', '-', '&', '|' binops!!?

################ Str

@pyfunc
def str_concat(x: CPObject, y: CObject) -> CObject:
    """
    String concatenation
    """
    xv = x.value                # XXX getstr
    yv = y.getvalue()           # XXX getstr
    if xv == "":
        return y
    if yv == "":
        return x
    return _new_pobj(x.getclass(), xv + yv)

@pyfunc
def str_get(l: CPObject, r: CObject) -> CObject:        # [] operator
    """
    Str l[r]
    return `r`'th character of Str `l`
    """
    # XXX check if r is integer
    return _new_pobj(l.getclass(), l.value[r.getvalue()])

@pyfunc
def str_split(this: CPObject,
              sep: Optional[CPObject] = None,
              limit: Optional[CPObject] = None) -> CObject:
    """
    Return a CList of the words in the string,
    using sep as the delimiter string (default to `null` -- any whitespace).
    Limit to `limit` return values (defaults to -1 -- no limit)
    """
    if sep is not None:
        sep = sep.value         # XXX getstr
    if limit is None:
        il = -1
    else:
        il = limit.getint()
    # will use current "Str" defn:
    return wrap(this.value.split(sep, il))

@pyfunc
def str_ends_with(this: CPObject, suff: CPObject) -> CObject:
    """
    Return `true` if `this` ends with the suffix `suff`, `false` otherwise.
    """
    return mkbool(this.value.endswith(suff.value))

@pyfunc
def str__join(this: CPObject, arg: CPObject) -> CObject:
    """
    Concatenate list of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    """
    return _new_pobj(this.getclass(),
                     this.value.join(unwrap(arg)))

@pyfunc
def str_ord(this: CPObject) -> CObject:
    """
    Return the Unicode code point for a one-character string `this`
    """
    return mknumber(ord(this.value)) # XXX getstr

@pyfunc
def str_starts_with(this: CPObject, pref: CPObject) -> CObject:
    """
    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    """
    return mkbool(this.value.startswith(pref.value))

@pyfunc
def str_str(this: CPObject) -> CPObject:
    """
    Identity method
    """
    return this                 # identity

@pyfunc
def str_strip(this: CPObject) -> CPObject:
    """
    Return a copy of the string with leading and trailing whitespace removed.
    """
    return _new_pobj(this.getclass(), this.value.strip()) # XXX getstr

@pyfunc
def str_to_float(this: CPObject) -> CObject:
    """
    Convert string to a floating point Number
    """
    return mknumber(float(this.value))

@pyfunc
def str_to_int(this: CPObject,
               base: Optional[CPObject] = None) -> CObject:
    """
    Convert string to integer Number.
    Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).
    """
    if base is None:
        ib = 0
    else:
        ib = base.getint()
    return mknumber(int(this.value, ib))

@pyfunc
def str_to_number(this: CPObject) -> CObject:
    """
    Convert string to a Number
    """
    try:
        return mknumber(int(this.value))
    except ValueError:
        return mknumber(float(this.value))

# static methods (plain function)
@pyfunc
def str_chr(i: CPObject) -> CPObject:
    """
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff
    """
    return mkstr(chr(i.getint()))

LCStr.setprop(const.METHODS, _mkdict({
    'ends_with': str_ends_with,
    '__join': str__join,
    'len': pobj_len,
    'ord': str_ord,
    'slice': pobj_slice,
    'split': str_split,
    'starts_with': str_starts_with,
    'strip': str_strip,
    'to_float': str_to_float,
    'to_int': str_to_int,
    'to_number': str_to_number,
    'to_str': str_str,
    const.INIT: pobj_init
}))
LCStr.setprop(const.BINOPS, _mkdict({
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
LCStr.setprop('chr', str_chr)

################ Null

@pyfunc
def null_str(this: CObject) -> CObject:
    """
    to_string/repr method for Null Class: returns "null"
    """
    return mkstr("null")

@pyfunc
def null_call(this: CObject, *args: CObject) -> CObject:
    """
    `(` method for `null` value (fatal error)
    """
    raise UError("'null' called")

LCNull.setprop(const.METHODS, _mkdict({
    'repr': null_str
}))
LCNull.setprop(const.BINOPS, _mkdict({
    '(': null_call
}))

################ Nullish

@pyfunc
def nullish_getprop(l: CPObject, r: CPObject) -> CObject:
    """
    `.` method for Nullish (null, undefined) values.
    Fatal error if unknown property.

    Allows all Object methods (JavaScript is stricter, Python is not).
    """
    # XXX check r is Str
    if l.hasprop(r.value):
        return l.getprop(r.value)

    ILLEGAL_VALUE = nullish_getprop           # can NEVER be seen
    val = find_in_class(l, r, ILLEGAL_VALUE) # may return BoundMethod
    if val is ILLEGAL_VALUE:
        raise UError("unknown property '%s' of %s" % (r.value, l.classname()))
    return val

@pyfunc
def nullish_setprop(l: CPObject, r: CObject, value: CObject) -> None:
    """
    Nullish Object setprop method/operator
    """
    rv = r.getvalue()              # XXX must be Str
    raise UError("Cannot set property '%s' of %s" % (rv, l.classname()))

LCNullish.setprop(const.METHODS, _mkdict({
    'getprop': nullish_getprop,
    'setprop': nullish_setprop
}))
LCNullish.setprop(const.BINOPS, _mkdict({
    '.': nullish_getprop
}))
LCNullish.setprop(const.LHSOPS, _mkdict({
    '.': nullish_setprop
}))

################ Bool

@pyfunc
def bool_str(this: CPObject) -> CObject:
    """
    return Str representation: "true" or "false"
    """
    if this.value:
        return mkstr("true")
    else:
        return mkstr("false")

# XXX have own MetaClass "new" to return one of the doubleton values?
# XXX subclass into True and False singleton classes????
LCBool.setprop(const.METHODS, _mkdict({
    'repr': bool_str
}))

def mkbool(val: Any) -> CObject:
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

LCPyObject = defclass(LCPClass, const.PYOBJECT, [LCObject],
                    doc="""
    Built-in Class for a wrapper around an arbitrary Python Object
    (returned by pyimport, or operations on PyObjects)
    """)

def unwrap(x: CObject) -> Any:
    """
    recursively unwrap an Object, to pass to PyObject on call
    (Pythonify value)
    """
    if x.hasvalue:
        xv = x.getvalue()
        if isinstance(xv, list): # XXX handle any iterable?
            return [unwrap(y) for y in xv]
        elif isinstance(xv, dict): # XXX handle any mapping?
            return {unwrap(key): unwrap(val) for key, val in xv.items()} # keys Python
        return xv
    if x is undef_value:
        return None
    return x

@pyfunc
def pyobj_getprop(l: CPObject, r: CObject) -> CObject:
    """
    PyObject `.` binop -- proxies to Python object getattr
    """
    # XXX r must be Str
    #   for access to Object properties?
    rv = r.getvalue()                  # XXX check Str
    if hasattr(l.value, rv):
        v = getattr(l.value, rv) # get Python object attribute
    elif l.hasprop(rv):  # check Object properties (most likely empty)
        v = l.getprop(rv)
    else:
        # allow 'to_str' method so Object can be printed!!
        v = find_in_class(l, r, undef_value) # may return BoundMethod
    return wrap(v)

@pyfunc
def pyobj_props(this: CPObject) -> CObject:
    """
    return dir() of wrapped Python object
    """
    return wrap(dir(this.value))

@pyfunc
def pyobj_getitem(l: CPObject, r: CObject) -> CObject:
    """
    PyObject `[` binop
    """
    v = l.value[r.getvalue()]   # XXX index PyObject w/ Python value??
    return wrap(v)

@pyfunc
def pyobj_call(this: CPObject, *args: CPObject) -> CObject:
    a2 = [unwrap(x) for x in args]
    ret = this.value(*a2)
    return wrap(ret) # may create another PyObject!

# searched AFTER wrapped Python object attrs
LCPyObject.setprop(const.METHODS, _mkdict({
    const.INIT: pobj_init,
    'props': pyobj_props
}))
LCPyObject.setprop(const.BINOPS, _mkdict({
    '.': pyobj_getprop,         # gets Python object attr!
    '[': pyobj_getitem,
    '(': pyobj_call,
}))

# XXX TODO LHSOPS for '.' and '[' ?!!! need to unwrap values!

################ PyIterator

@pyfunc
def pyiterator_iter(this: CPyIterator) -> CObject:
    """
    Returns `this.`

    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method.
    """
    return this

@pyvmfunc
def pyiterator_next(vm: vmx.VM, this: CPyIterator, finished: CCallable) -> CObject:
    """
    Returns next value; calls `finished`
    (a block leave label or `return` Continuation)
    to call when iterator exhausted.
    """
    try:
        return wrap(next(this.value))
    except StopIteration:
        # here to avoid check on each iteration:
        if not isinstance(finished, CContinuation):
            raise UError("iterator .next takes Continuation")
        vm.args = []            # will be defaulted to null
        finished.invoke(vm)     # alters VM state; RETURN IMMEDIATELY!
    return null_value

LCPyIterator.setprop(const.METHODS, _mkdict({
    'iter': pyiterator_iter,    # see above
    'next': pyiterator_next
}))

################ Undefined

@pyfunc
def undef_str(this: CObject) -> CObject:
    """
    to_string/repr method for Undefined Class: returns `"undefined"`
    """
    return mkstr("undefined")

@pyfunc
def undef_call(this: CPObject, *args: CObject) -> CObject:
    """
    `(` method for `undefined` value (fatal error).
    commonly happens when a bad method name is used,
    so output a "helpful" message.
    """
    raise UError("'undefined' called; bad method name?")

LCUndefined.setprop(const.METHODS, _mkdict({
    'repr': undef_str
}))
LCUndefined.setprop(const.BINOPS, _mkdict({
    '(': undef_call
}))

################################################################

# Module is what "import" function returns
#       properties are the namespace of the target Module

# XXX need ModuleClass metaclass (unless/until Scope objects visible!!)
#       in order to allow .new
LCModule = defclass(LCClass, 'Module', [LCObject],
                    doc="Built-in class for a Module (from import function)")
LCModule.setprop('modules', _mkdict({})) # Class variable

class CModule(CObject):
    __slots__ = ['scope', 'modinfo']

    def __init__(self, scope: vmx.Scope):
        super().__init__(LCModule)
        self.scope = scope      # HIDDEN!
        #self.modinfo = None     # convenience; '__modinfo' should suffice
        self.props = scope.get_vars() # XXX THWACK (stealing Scope dict)!!

# ModInfo is the Class of the '__modinfo' variable inside each Module
#       (meta-info about the module-- Module properties are the
#        the contents of the Module namespace/Scope)
LCModInfo = defclass(LCClass, 'ModInfo', [LCObject],
                   doc="Built-in Class for __modinfo Objects (inside Modules)")

# called from new_module -- should be modinfo_init (ModInfo.init method)?
def new_modinfo(main: bool, module: CModule, fname: str,
                parser_vmx: Optional[str] = None) -> CObject:
    """
    bool `main`
    CModule `module`
    str `fname`
    str `parser_vmx`
    """
    mi = CObject(LCModInfo)
    mi.setprop(const.MODINFO_MAIN, mkbool(main)) # is main program
    mi.setprop(const.MODINFO_MODULE, module)     # pointer to Module
    if XXL_DEBUG_BOOTSTRAP:
        mi.setprop(const.MODINFO_DEBUG_BOOTSTRAP, true_value)

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
def new_module(fname: str,
               main: bool = False,
               parser_vmx: Optional[str] = None) -> Tuple[CModule, Optional[CClosure]]:
    """
    `fname` is Python str (empty for internal Module)
    `main` is Python True for main program (from command line)
    `argv` is Python list of str (if main is True)
    `parser_vmx` is Python str for parser VMX file to use
    returns (CModule, CClosure) if newly loaded module
        the Closure is the (bootstrap) code to populate the Module
    returns (CModule, None) if previously loaded (or internal Module)
    """

    sfname = mkstr(fname)

    md = LCModule.getprop('modules') # Module Dict/directory (Class variable)
    mdd = md.getvalue()            # module directory dict

    if fname and sfname in mdd:  # previously loaded?
        return mdd[sfname], None # yes; return it, no bootstrap needed

    scope = vmx.Scope(root_scope) # create base scope for module
    mod = CModule(scope)

    scope.defvar(const.DOC, null_value)
    scope.defvar('__xxl', CObject(class_by_name('XXLObject')))

    if fname:
        mdd[sfname] = mod   # save as previously loaded

    mi = new_modinfo(main=main, module=mod, fname=fname, parser_vmx=parser_vmx)
    #mod.modinfo = mi

    scope.defvar(const.MODINFO, mi) # make ModInfo visible in module namespace

    if fname is None:           # internal module?
        return mod, None

    bootstrap_vmx = xxlobj.find_in_lib_path(os.environ.get('XXL_BOOTSTRAP',
                                                           'bootstrap.vmx'))

    # XXX handle Exceptions for I/O, bad JSON, bad instructions
    code = vmx.load_vm_json(bootstrap_vmx)

    boot = CClosure(code, mod.scope) # CClosure with bootstrap_vmx code

    return mod, boot

# called by bootstrap.vmx to load __modinfo.vmxfile (if set)
# NOTE! This _could_ be replaced by native code in bootstrap.xxl
# (reading JSON and calling modinfo_assemble)
# *BUT* load_vm_json has to exist to load the bootstrap anyway!
@pyfunc
def modinfo_load_vmx(this: CObject, fname: CObject) -> CClosure:
    """
    Load compiled `.vmx` file;
    Returns Closure in __modinfo.module top level scope.
    """
    mod = this.getprop(const.MODINFO_MODULE) # XXX check return
    assert isinstance(mod, CModule)

    code = vmx.load_vm_json(fname.getvalue()) # XXX getstr
    return CClosure(code, mod.scope)

@pyfunc
def modinfo_assemble(this: CObject, tree: CObject, srcfile: CObject) -> CClosure:
    """
    Assemble List of Lists representing VM code.
    `tree`: List of Lists.
    `srcfile`: source of code (for output only).
    Returns Closure in __modinfo.module top level scope.
    """
    code = vmx.assemble(tree, srcfile)

    # turn into Closure in scope
    #   (any variables created are globals):
    mod = this.getprop(const.MODINFO_MODULE) # XXX check
    assert isinstance(mod, CModule)
    return CClosure(code, mod.scope)

LCModInfo.setprop(const.METHODS, _mkdict({
    'load_vmx': modinfo_load_vmx,  # create Closure from .vmx file
    'assemble': modinfo_assemble # create Closure from List of inst. Lists
}))

################################################################

LCPyIteratorObject = defclass(LCPClass, const.PYITERATOROBJECT,
                              [LCPyObject,LCPyIterator],
                              doc="""
    Built-in Class for a wrapper around an arbitrary Python Object that is an iterator
    (has a __next__ method -- should also have __iter__ method).
    """)

LCPyIterableObject = defclass(LCPClass, const.PYITERABLEOBJECT,
                              [LCPyObject,LCPyIterable],
                    doc="""
    Built-in Class for a wrapper around an arbitrary Python Object that is an iterable
    (has an __iter__ method -- an iterator factory).
    """)

# XXX maybe take second arg PObject orig, and return if "value is orig.value"??
def wrap(value: Any) -> CObject:
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
        # should also have __iter__
        return new_by_name(const.PYITERATOROBJECT, value)

    if hasattr(value, '__iter__'):
        return new_by_name(const.PYITERABLEOBJECT, value)

    return new_by_name(const.PYOBJECT, value)

################################################################

def defmodule(name: str, mod: CModule) -> None:
    """
    declare an internal Module by name
    `name` is Python str
    `mod` is CModule
    """
    assert(isinstance(mod, CModule))
    md = LCModule.getprop('modules') # module Dict
    md.getvalue()[mkstr(name)] = mod

def classes_init(argv: List[str], parser_vmx: str) -> None:
    """
    call once on startup; initialize "root" scope, including __xxl object
    """

    # init root_scope
    root_scope.defvar('true', true_value)
    root_scope.defvar('false', false_value)
    root_scope.defvar('null', null_value)
    root_scope.defvar('undefined', undef_value)
    root_scope.defvar('Class', LCClass)

    xxlobj.create_xxl_class(argv=argv, parser_vmx=parser_vmx)

    # UTTERLY VILE: either hide in a "make_internal_module"
    #   or do it more cleanly!!!!
    #   declare classes_module up top???????????
    classes_module, _ = new_module("")
    classes_module.scope = classes_scope # XXX YUK
    # NOTE: below crushes classes_module __modinfo!!!??? (do we care???)
    classes_module.props = classes_scope.vars # XXX XXX DOUBLY SO
    defmodule('classes', classes_module)      # XXX __classes?

################################################################

def def_wrappers(cname: str,
                 ptype: type,    # ??
                 methods: List[Union[str, Tuple[str,str]]]) -> None:
    """
    Define a language class as a wrapper around a Python class.
    str `cname` is XXL Class name.
    Python type `ptype`
    list `methods` is list of str and/or 2-tuple of str (pymeth, xxlmeth)
    """
    # find Class with cname, find or create methods Dict
    c = classes_scope.lookup(cname)
    if not c.hasprop(const.METHODS):
        mdict = _mkdict({})
        c.setprop(const.METHODS, mdict)
    else:
        mdict = cast(CPObject, c.getprop(const.METHODS))

    for pmname in methods:
        if isinstance(pmname, (list, tuple)):
            pmname, mname = pmname # (Python_name, XXL_NAME)
        else:
            mname = pmname

        try:
            getattr(ptype, pmname)
        except AttributeError:
            continue            # not in this version of Python

        def def_wrapper(_pmname: str, _mname: str) -> None:
            # closure with private names, pmethod (not loop variables!)
            pmethod = getattr(ptype, _pmname)
            def wrapper(*args: CObject) -> CObject:
                return wrap(pmethod(*[unwrap(x) for x in args]))
            wrapper.__name__ = _mname # crock for CPyFunc.defn()
            pf = CPyFunc(wrapper, pmethod) # second arg crock for CPyFunc.args()
            pf.setprop(const.DOC, _mkstr(pmethod.__doc__ or ""))
            mdict.value[mkstr(mname)] = pf
        def_wrapper(pmname, mname)

################

def_wrappers('Set', set, ['add', 'clear', 'copy',
                          'difference', 'difference_update', 'discard',
                          'intersection', 'intersection_update',
                          ('isdisjoint', 'is_disjoint'),
                          ('issubset', 'is_subset'),
                          ('issuperset', 'is_superset'),
                          'pop', 'remove',
                          'symmetric_difference',
                          'symmetric_difference_update',
                          'union']) # update in bootstrap.xxl

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

# more classes here?

################################################################

OPEN_PAREN = mkstr('(')

classes_scope.defvar(const.DOC, mkstr("Built-in Classes for XXL"))
