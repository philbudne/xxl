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
Simple VM for ASAP (As Simple As Possible) / XXL

was vm.py, but renamed to vmx.py to allow passing "vm" args
in all files

Started from VM descriptions in
["Three Implementation Models for Scheme" (pdf)](https://legacy.cs.indiana.edu/~dyb/papers/3imp.pdf)

"""
import sys                      # stderr
import json
import collections
import time
from typing import Any, Dict, List, NamedTuple, Optional, TextIO, Tuple, Type, Union, TYPE_CHECKING, cast

import classes
import xxlobj
import const
import jslex                    # LexError

if TYPE_CHECKING:
    from classes import CObject

ArgNames = List[str]
VMInstrs = List["VMInstr0"]
IJSON = List[Any]               # FIXME! Python JSON repr of instr
IValue = Union[int, str, "CObject"] # instruction value

class Frame(NamedTuple):	# Immutable!
     cb: VMInstrs               # list of VMInstr
     pc: int                    # offset into cb
     scope: "Scope"
     fp: Optional["Frame"]
     function: str
     where: str
     show: bool

# opcodes where inst[2] is code list, used in xxlobj.py:
INST2CODE = ('close', 'bccall')

instr_class_by_name: Dict[str, Type["VMInstr0"]] = {}  # Instr classes by name

class VMError(Exception):
    """
    exception class for VM instruction errors
    """

# called from fp_backtrace (below), CContinuation.defn
def fp_where(fp: Frame) -> str:
    """
    Return "filename:line:col" for stack frame
    """
    # gives CALLER location (from VM IR register at time of call)
    return f"{fp.function}:{fp.where}"
    # gives return location (PC incremented before call)
    #return fp.cb[fp.pc].fn_where()

# called from VM.backtrace, CContinuation.backtrace
def fp_backtrace_list(fp: Optional[Frame]) -> List[str]:
    """
    Return Python list of str of CALLER locations in fp stack
    """
    ret = []
    while fp:
        if fp.show:
            ret.append(fp_where(fp))
        fp = fp.fp
    return ret

StackVal = Any                  # XXX
Stack = Tuple[StackVal, "SP"]
SP = Optional[Stack]

VarsDict = Dict[str, "classes.CObject"]

class Scope:
    """
    runtime scope.
    currently invisible (or at least opaque)
    """
    def __init__(self, parent: Optional["Scope"] = None) -> None:
        self.parent = parent
        self.vars: VarsDict = {}

    def new_scope(self) -> "Scope":
        """
        create a scope using current scope as parent
        """
        return Scope(self)

    def func_scope(self, fp: Frame) -> "Scope":
        s = Scope(self)
        s.defvar('return', classes.CContinuation(fp))
        return s

    def labeled_scope(self, fp: Frame, name: str) -> "Scope": # Closure with leave label
        s = Scope(self)
        s.defvar(name, classes.CContinuation(fp))
        return s

    def defvar(self, var: str, value: "classes.CObject") -> None:
        """
        `var` is Python string
        `value` is CObject
        """
        # duplicate var is fatal in compiler
        self.vars[var] = value

    # XXX the compiler could tell us how far up the ("static") scope chain
    # the variable lives (and could assign numeric slot ids for variable
    # lookup to avoid dict)
    def lookup(self, name: str) -> "classes.CObject":
        s: Optional[Scope] = self
        while s:
            if name in s.vars:
                return s.vars[name]
            s = s.parent
        raise classes.UError(f"Unknown variable {name}") # SNH

    # see note above "lookup" (compiler could tell us stuff)
    def store(self, name: str, val: "classes.CObject") -> "classes.CObject":
        """
        name: Python string
        val: CObject
        """
        s: Optional[Scope] = self
        while s:
            if name in s.vars:
                s.vars[name] = val
                return val
            s = s.parent
        raise classes.UError(f"Unknown variable {name}")

    def get_vars(self) -> VarsDict:  # UGH! used by new_module
        return self.vars

class VM:
    """
    VM state
    NOTE!!! Any/all stacks MUST be immutable (value, next) tuples!!!
    (see above note about cactus/saguro/spaghetti stack).
    """
    __slots__ = ['run', 'ac', 'sp', 'cb', 'pc', 'ir',
                 'scope', 'fp', 'temp', 'args',
                 # stats/trace:
                 'op_count', 'op_time', 'stats', 'trace',
                 'bop_count', 'bop_time',
                 'lop_count', 'lop_time',
                 'uop_count', 'uop_time']

    def __init__(self, ac: "classes.CObject", cb: VMInstrs, scope: Scope):
        # [dybvig VM register name]
        self.run = False
        self.ac  = ac         # [a] Accumulator
        self.sp: SP = None    # [s] Stack Pointer (value, next) tuples
        self.scope = scope    # [e] Current scope
        self.pc: int = 0      # [x] offset into code base
        self.cb: VMInstrs = cb  # Code Base (Python list of VMInstr)
        self.ir = self.cb[self.pc] # Instruction Register
        self.fp: Optional[Frame] = None # Frame: Frame pointer (for return)
        self.temp: "classes.CPObject" = classes.null_value # new Dict/List

        # argument list from last call/method/op invocation
        # User defined functions (Python CClosure) pick up args with
        # "args" opcode before ANY other call/op can occur (so never
        # needs to be preserved).  Other CObject subclasses may
        # consume directly.
        self.args: List["classes.CObject"] = [] # [r]

    def start(self, stats: bool, trace: bool) -> None:
        self.run = True         # cleared by 'exit' instr

        if stats:
            return self._start_stats(trace)
        elif trace:
            return self._start_trace()

        while self.run and self.cb:
            # XXX might be faster (avoid indexing a list) to
            #   create a "next" pointer on VM code "read-in"
            #   (run list in reverse;
            #    could also eliminate unconditional "jrst"?!)
            # NOTE! self.ir saved for debug.
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            ir.step(self)       # execute instruction

    def _getcols(self, f: TextIO = sys.stdout) -> int:
        try:
            import os
            import stat
            st = os.fstat(f.fileno())
            if stat.S_ISREG(st.st_mode):
                return 0
        except:
            pass

        try:
            # seems yukky, but POSIX now defines size and order!
            import fcntl
            import struct
            import termios
            rows, cols = struct.unpack(
                'hh', fcntl.ioctl(f.fileno(),
                                  termios.TIOCGWINSZ,
                                  b"\000"*8)[0:4]
            )
            #print("cols", cols, "rows", rows)
            return int(cols)
        except:
            pass

        try:
            # doesn't seem to honor any fd
            with os.popen("tput cols") as p:
                return int(p.readline().strip())
        except:
            pass
        return 0

    def _start_trace(self) -> None:
        cols = self._getcols()
        sep = ' | '
        #print("cols", cols)
        if cols > 20:
            acwid = int(cols * 3/8) - len(sep)
            irwid = min(cols - acwid - len(sep), 100)
            print(cols, acwid, irwid)
            format = f"%{-irwid}.{irwid}s{sep}%.{acwid}s"
        else:
            # output to file, width unavailable, or tiny
            format = f"%s{sep}%s"

        print("format", format)
        while self.run and self.cb:
            # NOTE! self.ir for debug.
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            ir.step(self)       # execute instruction
            irstr = str(ir)[1:-1] # remove []'s -- XXX remove quotes too???
            print(format % (irstr, str(self.ac)))

    def _start_stats(self, trace: bool) -> None:
        # stats
        CDict = Dict[str, int]
        TDict = Dict[str, float]
        # opcodes:
        self.op_count: CDict = {}
        self.op_time: TDict = {}
        # binary operators
        self.bop_count: CDict = {}
        self.bop_time: TDict = {}
        # LHS binops:
        self.lop_count: CDict = {}
        self.lop_time: TDict = {}
        # unops:
        self.uop_count: CDict = {}
        self.uop_time: TDict = {}

        for op in instr_class_by_name.keys():
            self.op_count[op] = self.op_time[op] = 0
        # XXX inside try, to catch SystemExit???
        # (so __xxl.exit() doesn't bypass stats)
        while self.run and self.cb:
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            t0 = time.time()
            ir.step(self)       # execute instruction
            # XXX save ir in history buf??
            ir.prof(self, time.time() - t0)
            if trace:
                print(ir, self.ac)

        s = sys.stderr

        def pr(what: str, times: TDict, counts: CDict) -> None:
            ttime = 0.0
            tcount = 0
            for op in counts:
                ttime += times[op]
                tcount += counts[op]

            print(f"{what} {tcount} {ttime:.6f}s", file=s)

            print(f"{'op':10.10s} {'count':>9} {'%count':>7.7s} {'%time':>7.7s} {'ratio':>6.6s}", file=s)
            for op in counts:
                pcount = 100*counts[op]/tcount # pct of total insts
                ptime = 100*times[op]/ttime    # pct of total time
                # ratio of pct time spent to pct times called
                # >1.0 means time hog
                if pcount:
                    ratio = ptime/pcount
                else:
                    ratio = 0
                print(f"{op:10.10s} {counts[op]:>9} {pcount:7.3f} {ptime:7.3f} {ratio:6.3f}", file=s)
            print("", file=s)

        pr("opcodes", self.op_time, self.op_count)
        pr("binops", self.bop_time, self.bop_count)
        pr("lhsops", self.lop_time, self.lop_count)
        pr("unops", self.uop_time, self.uop_count)

    def dump_stack(self) -> None:
        """
        dump (call argument) stack for debugging
        """
        t = self.sp
        while t:
            print("  ", t[0])
            t = t[1]

    def save_frame(self, show: bool = True) -> None:
        # called from CClosure.invoke (always call before .invoke??)
        #       would need to call restore_frame inside all .invoke methods??
        #       would allow Python callees to use same VM???
        # called from CBClosure.invoke w/ show=False
        # XXX save self.args for backtraces??
        self.fp = Frame(self.cb, self.pc, self.scope, self.fp,
                        self.ir.fn, self.ir.where, show)

    def backtrace(self) -> None: # XXX take file to write to?
        """
        Write return stack to stderr.
        """
        for return_location in fp_backtrace_list(self.fp):
            sys.stderr.write(f" called from {return_location}\n")

    def push(self, val: StackVal) -> None:
        """
        push onto saguro/cactus/spaghetti stack,
        necessary for continuations.
        """
        self.sp = (val, self.sp) # MUST be immutable!

    def pop(self) -> StackVal:
        """
        pop from cactus stack
        moves pointer in chain,
        does not modify existing entries.
        """
        assert self.sp is not None
        val, self.sp = self.sp  # unpack top of stack
        return val

    def restore_frame(self, fp: Frame) -> None:
        """
        "return" using saved frame pointer
        helper used by ReturnInstr and CContinuation.invoke
        """
        self.cb, self.pc, self.scope, self.fp, _, _, _ = fp

################################################################
# VM instructions

def reginstr(inst_class: Type["VMInstr0"]) -> Type["VMInstr0"]:
    """
    Decorator for VMInst classes for reading in JSON representations.
    Registers the instruction class in `instr_class_by_name` for the
    "assembler" (`convert_one_instr`) routine.
    """
    assert issubclass(inst_class, VMInstr0)
    name = inst_class.name
    if name in instr_class_by_name:
        raise VMError(f"duplicate entry for {name} instruction ({inst_class})")
    instr_class_by_name[name] = inst_class
    return inst_class           # unmodified class

class VMInstr0:
    """
    Base class for VM instructions.
    """
    __slots__ = ['fn', 'where']

    name: str

    def __init__(self, fn: str, where: str):
        self.fn = fn
        self.where = where

    def fn_where(self) -> str:  # for trace
        """
        Return str with "filename:line:position"
        """
        return f"{self.fn}:{self.where}"

    def json(self) -> IJSON:
        """
        Return a Python list representation of this instruction.
        """
        return [self.fn_where(), self.name]

    def step(self, vm: "VM") -> None:
        """
        Perform (execute) this instruction.
        """
        tn = type(self).__name__
        raise VMError(f"'{tn}' has no step method")

    def prof(self, vm: "VM", secs: float) -> None:
        vm.op_count[self.name] += 1
        vm.op_time[self.name] += secs

    def args(self) -> ArgNames:
        """
        For instructions that can appear as the first instruction
        in a Closure, return a Python list of str's for the
        Closure argument names (used to implement the `Callable.__args`
        method for use by doc.xxl, to generate documentation).
        """
        return []

    def __repr__(self) -> str:
        return str(self.json())

class VMInstr1(VMInstr0):
    """
    Base for VM Instructions with one argument.
    """
    __slots__ = ['value']

    def __init__(self, fn: str, where: str, value: IValue):
        super().__init__(fn, where)
        self.value = value

    def json(self) -> IJSON:
        return [self.fn_where(), self.name, self.value]

class WrapInstr1(VMInstr1):
    """
    base for VM Instructions with one argument, wrapped on input
    """
    value: "classes.CPObject"

    def __init__(self, fn: str, where: str, value: IValue):
        # convert to CObject when code is loaded
        super().__init__(fn, where, classes.wrap(value))

class IntInstr(VMInstr1):
    """
    base for VM instructions with one integer argument
    """
    value: int

    def __init__(self, fn: str, where: str, value: int):
        super().__init__(fn, where, value)


class StrInstr(VMInstr1):
    """
    base for VM instructions with one string argument
    """
    value: str

    def __init__(self, fn: str, where: str, value: str):
        super().__init__(fn, where, value)

################

@reginstr
class LitInstr(WrapInstr1):
    """
    load literal (Number or Str) into AC
    """
    name = "lit"

    def step(self, vm: "VM") -> None:
        vm.ac = self.value

@reginstr
class PushLitInstr(LitInstr):
    """
    push literal (Number or Str) onto stack
    """
    name = "push_lit"

    # __init__ from LitInstr

    def step(self, vm: "VM") -> None:
        vm.push(self.value)

@reginstr
class PushInstr(VMInstr0):
    """
    Save AC on stack.
    """
    name = "push"

    def step(self, vm: "VM") -> None:
        vm.push(vm.ac)

@reginstr
class TempInstr(VMInstr0):
    """
    copy TEMP to AC
    (used with "new")
    """
    name = "temp"

    def step(self, vm: "VM") -> None:
        vm.ac = vm.temp

@reginstr
class PopTempInstr(VMInstr0):
    """
    copy TEMP to AC
    pop top of stack into TEMP
    (used with "new")
    """
    name = "pop_temp"

    def step(self, vm: "VM") -> None:
        vm.ac = vm.temp
        vm.temp = vm.pop()

@reginstr
class LoadInstr(VMInstr1):
    """
    load AC from a variable (searches scopes)
    (compiler could tell us how far up,
     and even give us a slot number)
    """
    name = "load"
    value: str

    def __init__(self, fn: str, where: str, value: str):
        super().__init__(fn, where, value)

    def step(self, vm: "VM") -> None:
        vm.ac = vm.scope.lookup(self.value)

@reginstr
class BinOpInstr(WrapInstr1):
    """
    execute (RHS) binary operator for object in AC

    pops RHS operand from stack
    sets VM args to [AC, operand]
    inst.value is Python string for operator
    lookup in binops for object and invoke
    """
    name = "binop"

    def step(self, vm: "VM") -> None:
        arg = vm.pop()
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, arg]  # explicitly pass "this" object
        m = classes.find_op(vm.ac, const.BINOPS, self.value)
        m.invoke(vm)            # XXX always create frame???

    def prof(self, vm: "VM", secs: float) -> None:
        super().prof(vm, secs)
        op: str = cast(str,self.value.value) # getstr??
        if op not in vm.bop_count:
            vm.bop_time[op] = 0.0
            vm.bop_count[op] = 0
        vm.bop_count[op] += 1
        vm.bop_time[op] += secs

@reginstr
class BinOpLitInstr(BinOpInstr): # NOTE! inherits special "prof" method!
    """
    RHS binary operator with literal LHS operand
    """
    name = "binop_lit"

    __slots__ = ['lit']

    def __init__(self, fn: str, where: str, op: str, lit: str):
        super().__init__(fn, where, op) # vm.call_op expects op in "value"
        # convert to Class when code is loaded
        self.lit = classes.wrap(lit)

    def step(self, vm: "VM") -> None:
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, self.lit] # explicitly pass "this" object
        m = classes.find_op(vm.ac, const.BINOPS, self.value)
        m.invoke(vm)            # XXX always create frame???

    def json(self) -> IJSON:
        return [self.fn_where(), self.name, self.value, self.lit]

@reginstr
class LHSOpInstr(WrapInstr1):
    """
    execute (LHS) binary operator for object in AC
    pops RHS operand (index/property) from stack
    pops value to store from stack
    sets VM args to [AC, operand, value]
    inst.value is Python string for operator
    lookup in lhsops for object and invoke
    """
    name = "lhsop"

    def step(self, vm: "VM") -> None:
        arg1 = vm.pop()         # index or property
        arg2 = vm.pop()         # value to store
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, arg1, arg2] # explicitly pass "this" object
        m = classes.find_op(vm.ac, const.LHSOPS, self.value)
        m.invoke(vm)            # XXX always create frame???

    def prof(self, vm: "VM", secs: float) -> None:
        super().prof(vm, secs)
        op: str = cast(str,self.value.value) # getstr??
        if op not in vm.lop_count:
            vm.lop_time[op] = 0.0
            vm.lop_count[op] = 0
        vm.lop_count[op] += 1
        vm.lop_time[op] += secs

@reginstr
class UnOpInstr(WrapInstr1):
    """
    execute unary operator for object in AC
    sets VM args to [AC]
    inst.value is Python string for operator
    lookup in unops for object and invoke
    """
    name = "unop"

    def step(self, vm: "VM") -> None:
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac]       # pass "this" object
        m = classes.find_op(vm.ac, const.UNOPS, self.value)
        m.invoke(vm)            # XXX always create frame???

    def prof(self, vm: "VM", secs: float) -> None:
        super().prof(vm, secs)
        op: str = cast(str,self.value.value) # getstr??
        if op not in vm.uop_count:
            vm.uop_time[op] = 0.0
            vm.uop_count[op] = 0
        vm.uop_count[op] += 1
        vm.uop_time[op] += secs

@reginstr
class CloseInstr(VMInstr0):
    """
    create a Closure (from code + current scope)
    inst.value contains VM code (as Python list of VMInstrs)
    """
    name = "close"
    __slots__ = ['value', 'doc']
    value: VMInstrs

    def __init__(self, fn: str, where: str,
                 value: VMInstrs,
                 doc: Optional[str] = None):
        super().__init__(fn, where)
        self.value = convert_instrs(value, fn)
        self.doc = doc

    def step(self, vm: "VM") -> None:
        vm.ac = classes.CClosure(self.value, vm.scope, self.doc)

    def json(self) -> IJSON:
        return [self.fn_where(), self.name, self.value, self.doc]

@reginstr
class BCCallInstr(CloseInstr):
    """
    create a {} block closure and call it
    (hidden in backtraces)
    """
    name = "bccall"

    def step(self, vm: "VM") -> None:
        c = classes.CBClosure(self.value, vm.scope)
        c.invoke(vm)

@reginstr
class CallInstr(IntInstr):
    """
    Calls CObject invoke method
        (CClosure, CPyFunc, CBoundMethod, CContinuation define this,
         CObject hands off to "(" binop)
    self.value is Python number of args on stack
    pops args from stack, creating Python list in vm.args
    calls CObject.invoke(vm)
    """
    name = "call"

    def step(self, vm: "VM") -> None:
        nargs = self.value
        vm.args = []
        while nargs > 0:
            arg = vm.pop()      # pop argument
            vm.args.append(arg)
            nargs -= 1
        #print("call", vm.args)

        # save_frame here, so same VM can be used for any invokes from 
        # Python code (and better tracebacks)?
        # CPyFunc (et al) would need to restore_frame at end of invoke method.
        vm.ac.invoke(vm)

@reginstr
class ClearArgsInstr(VMInstr0):
    """
    clear vm.args

    first instruction for calls with spread arguments (...array) [python *arg]
    because not all .invoke methods clear vm.args.
    """
    name = "clargs"

    def step(self, vm: "VM") -> None:
        vm.args = []

@reginstr
class PopArgInstr(VMInstr0):
    """
    pop one arg from stack, append to vm.args
    used for calls with spread arguments (...array)
    """
    name = "poparg"

    def step(self, vm: "VM") -> None:
        arg = vm.pop()          # pop argument
        #print("poparg", arg)
        vm.args.append(arg)

@reginstr
class SpreadArgInstr(VMInstr0):
    """
    pop List from stack, append (as List) to args
    used for calls with spread arguments (...array)
    """
    name = "sprarg"
    def step(self, vm: "VM") -> None:
        arg = vm.pop()            # pop argument
        #print("sparg", arg)
        vm.args.extend(arg.value) # XXX getlist

@reginstr
class Call0Instr(VMInstr0):
    """
    actual function call for calls with spread arguments
    (does not alter vm.args)
    """
    name = "call0"

    def step(self, vm: "VM") -> None:
        #print("call0", vm.args)
        vm.ac.invoke(vm)

@reginstr
class AppendInstr(VMInstr0):
    """
    append to List for '[' construct
    replaced "method" instruction
    XXX explicitly invoke vm.temp "append" method??
    """
    name = "append"

    def step(self, vm: "VM") -> None:
        assert (isinstance(vm.temp, classes.CPObject) and
                isinstance(vm.temp.value, list))
        vm.temp.value.append(vm.ac)

# No longer used for return statement (it no longer exists), BUT, is
# generated by VMCode.finish() end closures, and blocks depend on
# this, because they don't have a return variable!
@reginstr
class ReturnInstr(VMInstr0):
    """
    return from a Closure call
    restores context from (Python) Frame object in FP
    """
    name = "return"

    def step(self, vm: "VM") -> None:
        assert vm.fp
        vm.restore_frame(vm.fp)

@reginstr
class ExitInstr(VMInstr0):
    """
    halt VM.
    used by invoke_function.
    """
    name = "exit"               # XXX rename to "halt"???

    def step(self, vm: "VM") -> None:
        #sys.stderr.write("exit\n")
        vm.run = False

@reginstr
class VarInstr(StrInstr):
    """
    declare a variable in current scope.
    Python string in self.value
    """
    name = "var"

    def step(self, vm: "VM") -> None:
        # XXX maybe explicitly generate "load undefined",
        #       and remove assignment w/ initializer?
        vm.ac = classes.undef_value
        vm.scope.defvar(self.value, vm.ac)

@reginstr
class ArgsInstr(VMInstr0):
    """
    first op executed in a closure (generated by "function" keyword)
    self.value is Python list of formals (argument names) as Python strings
    vm.args is Python list of actuals (argument values) as CObjects
    * creates a new scope
    * for each formal (argument name):
     + pops an actual from vm.args and creates variable
     + creates variable with null value if no actuals remain
    """
    name = "args"

    __slots__ = ['formals']
    formals: ArgNames

    def __init__(self, fn: str, where: str, formals: ArgNames):
        super().__init__(fn, where)
        self.formals = formals

    def json(self) -> IJSON:
        return [self.fn_where(), self.name, self.formals]

    def _bind_args(self, vm: "VM") -> None:
        """
        common code for ArgsInstr and Args2Instr
        """
        assert vm.fp
        # NOTE: scope.func_scope() creates a cactus stack of scopes;
        #       defines 'return' as a Continuation to prev frame
        vm.scope = vm.scope.func_scope(vm.fp)
        for formal in self.formals:     # loop for formals
            if vm.args:              # actuals left?
                val = vm.args.pop(0) # yes: pop a value
            else:
                # NOTE! originally used undefined in Args2Instr?!!
                val = classes.null_value # no: use null
            vm.scope.defvar(formal, val) # declare as variable

    def step(self, vm: "VM") -> None:
        if len(vm.args) > len(self.formals):
            v = len(vm.args)
            f = len(self.formals)
            raise classes.UError(f"too many arguments. got {v}, expected {f}")
        self._bind_args(vm)

    def args(self) -> ArgNames:
        """
        return list of str for arguments, for docs
        """
        return self.formals

@reginstr
class Args2Instr(ArgsInstr):
    """
    first op executed in a closure ("function") w/ a final ...rest argument
    self.formals is Python list of formals (argument names) as Python strings
    self.rest is Python string for ...rest argument name
    vm.args is Python list of actuals (argument values) as CObjects
    * creates a new scope
    * for each formal (argument name):
     + pops an actual from vm.args and creates variable
     + creates variable with null value if no actuals remain
    * creates a variable w/ List of remaining args (if any) in vm.args
    """
    name = "args2"

    __slots__ = ['rest']

    def __init__(self, fn: str, where: str, formals: ArgNames, rest: str):
        super().__init__(fn, where, formals)
        self.rest = rest

    def json(self) -> IJSON:
        return [self.fn_where(), self.name, self.formals, self.rest]

    def step(self, vm: "VM") -> None:
        self._bind_args(vm)

        # create List from remaining args
        l = classes.new_by_name('List', vm.args) # XXX want frozen?
        vm.scope.defvar(self.rest, l)  # declare as variable

    def args(self) -> ArgNames:
        """
        return list of str for arguments, for docs
        """
        return self.formals + ["..." + self.rest]

@reginstr
class LScopeInstr(StrInstr):
    """
    first op executed in a scope closure with a leave label
    """
    name = "lscope"

    def step(self, vm: "VM") -> None:
        # creates new scope, w/ named Continuation to leave it
        assert vm.fp
        vm.scope = vm.scope.labeled_scope(vm.fp, self.value)

@reginstr
class UScopeInstr(VMInstr0):
    """
    first op executed in an unlabled scope closure
    """
    name = "uscope"

    def step(self, vm: "VM") -> None:
        vm.scope = vm.scope.new_scope()

@reginstr
class StoreInstr(StrInstr):
    """
    store AC in a variable
    self.value contains Python string for variable name
    (see "LoadInstr" for discussion how compiler could help)
    """
    name = "store"

    def step(self, vm: "VM") -> None:
        vm.scope.store(self.value, vm.ac)

@reginstr
class JrstInstr(IntInstr):
    """
    Unconditional jump.
    sets PC (offset into code block) from self.value (Python int)
    (see VMCode object in parser for origin of name)
    """
    name = "jrst"

    def step(self, vm: "VM") -> None:
        vm.pc = self.value

@reginstr
class JumpNInstr(IntInstr):
    """
    Jump if true.
    If AC is truthy, sets PC (offset into code block) from self.value
    (see VMCode object in parser for origin of name)
    """
    name = "jumpn"

    def step(self, vm: "VM") -> None:
        if classes.is_true(vm.ac):
            vm.pc = self.value

@reginstr
class JumpEInstr(IntInstr):
    """
    Jump if true.
    If AC is falsey, sets PC (offset into code block) from self.value
    (see VMCode object in parser for origin of name)
    """
    name = "jumpe"

    def step(self, vm: "VM") -> None:
        if not classes.is_true(vm.ac):
            vm.pc = self.value

@reginstr
class NewInstr(StrInstr):
    """
    for [ ... ] and { .... } sugar (from compiler) *ONLY*
    push VM TEMP register onto stack (so nestable)
    "arg" contains Python string of name of container class to create
    leave new, empty container in VM TEMP register
    """
    name = "new"

    def step(self, vm: "VM") -> None:
        vm.push(vm.temp)
        if self.value == 'Dict':
            vm.temp = classes.new_by_name(self.value, {})
        elif self.value == 'List':
            vm.temp = classes.new_by_name(self.value, [])
        elif self.value == 'Set':
            vm.temp = classes.new_by_name(self.value, set())
        else:
            VMError(f"new Instr unknown type {self.value}")

################
# convert Python list into XxxInstr(ruction) instances
# (this is the .vmx file assembler!)

def convert_one_instr(i: List[str], fn: str) -> VMInstr0:
    """
    take single instruction in JSON form and assemble.
    i[0] is "line:char"
    i[1] is opcode
    fn is filename
    """
    op = i.pop(1)
    # create new instruction instance
    return instr_class_by_name[op](fn, *i)

def convert_instrs(il: IJSON, fn: str) -> VMInstrs:
    """
    assemble a list of instructions in JSON form
    fn is filename
    used by CloseInstr and load_vm_json
    """
    return [convert_one_instr(x, fn) for x in il]

# called by classes.new_module (w/ bootstrap.vmx) and ModInfo.load_vmx method
def load_vm_json(fname: str) -> VMInstrs:
    with open(fname) as f:
        l = f.readline()

        # allow "#!/usr/bin/env ..../xxl.py" to work (w/ .vmx files)
        if l and l[0:2] == '#!':
            l = f.readline()     # discard

        # parse metadata
        metadata = json.loads(l.strip())

        # check metadata
        if not isinstance(metadata, dict) or 'v' not in metadata:
            raise classes.UError("bad vmx file")
        v = float(metadata['v'])
        if v < 1.0 or v >= 2.0:
            raise classes.UError(f"unsupported vmx file version {v}")

        # load list of instructions
        j = json.load(f)

    return convert_instrs(j, metadata.get('fn', '?'))

################

# helper for ModInfo.assemble
def assemble(tree: "classes.CObject", srcfile: "classes.CObject") -> VMInstrs:
    """
    List of Lists `tree` of instructions to assemble
    str `srcfile` source file name for trimming "where" fields
    """
    js = xxlobj.obj2python_json(tree) # get Python list of lists
    fn = srcfile.getvalue()           # XXX getstr?
    xxlobj.trim_where(js, fn)

    # convert into Python list of Instrs (scope for type name lookup):
    return convert_instrs(js, fn)

################

def run(boot: "classes.CClosure",
        scope: Scope,
        stats: bool,
        trace: bool,
        xcept: bool) -> None:
    """
    cold start (from xxl.py)
    `boot` is Closure w/ bootstrap.vmx code for main module
    """

    ExList = Tuple[Type[BaseException], ...]
    always_user_errors: ExList = (classes.UError,)
    user_errors = always_user_errors
    internal_errors: ExList = (VMError, AssertionError)
    errors: ExList = (KeyboardInterrupt, Exception) # too many to list!

    if xcept:                               # -x option
        internal_errors += errors           # show IR, Python traceback
    else:
        user_errors += errors

    b0 = [["0", "call0"],       # call Closure (in AC)
          ["1", "exit"]]        # quit VM
    code = convert_instrs(b0, "@boot0")
    vm = VM(ac=boot, cb=code, scope=scope)
    try:
        vm.start(stats=stats, trace=trace)
    except SystemExit:          # from os.exit
        raise
    except internal_errors as e: # an internal error
        # NOTE: displays VM Instr, Python backtrace
        sys.stderr.write("VM Error @ {}: {}\n".format(vm.ir, e))
        # XXX dump VM registers?
        vm.backtrace()

        # print Python traceback
        import traceback
        traceback.print_exc()

        if 'pdb' in sys.modules:
            breakpoint()
        sys.exit(1)
    except user_errors as e:
        # NOTE: user error: just displays "where" and VM backtrace
        if vm.ir:
            sys.stderr.write("{}: {}\n".format(vm.ir.fn_where(), e))
        else:
            sys.stderr.write("???: {}\n".format(e))
        vm.backtrace()
        if not xcept and not isinstance(e, always_user_errors):
            sys.stderr.write("\n(Use -x option to get Python traceback)\n")
        if 'pdb' in sys.modules:
            breakpoint()
        sys.exit(1)
