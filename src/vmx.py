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
Simple VM for ASAP (As Simple As Possible) / XXL

was vm.py, but renamed to vmx.py to allow passing "vm" args
in all files
"""
import sys                      # stderr
import json
import time
import collections

import classes
import system
import const

# opcodes where inst[2] is code list, used in system.py:
INST2CODE = ('close', 'bccall')

instr_class_by_name = {}        # Instr classes by name

class VMError(Exception):
    """
    exception class for VM instruction errors
    """

# VM frame pointer register "fp" points to a Frame, implementing a
# "parent pointer" (aka cactus/saguro/spaghetti) stack.

# In Python 3.7.9, namedtuple faster than class, and immutable!
# Regular tuple is even faster, but less scrutable.
# XXX save vm.args for backtrace?
Frame = collections.namedtuple('Frame', 'cb,pc,scope,fp,fn,where,show')

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
                 'bop_count', 'bop_time']

    def __init__(self, stats, trace):
        self.run = False
        self.ac = None          # CObject: Accumulator
        self.sp = None          # Stack Pointer (value, next) tuples
        self.cb = None          # Code Base (Python list of VMInstr)
        self.scope = None       # Scope: Current scope
        self.pc = 0             # int: offset into code base
        self.ir = None          # VMInstr: Instruction Register
        self.fp = None          # Frame: Frame pointer (for return)
        self.temp = None        # holds new Dict/List
        self.stats = stats      # bool: enable timing
        self.trace = trace      # bool: enable tracing

        # argument list from last call/method/op invocation
        # User defined functions (Python CClosure) pick up args with
        # "args" opcode before ANY other call/op can occur (so never
        # needs to be preserved).  Other CObject subclasses may
        # consume directly.
        self.args = []

    def start(self, code, scope):
        self.run = True         # cleared by 'exit' instr
        self.pc = 0
        self.cb = code
        self.scope = scope

        if self.stats:
            return self._start_stats()
        elif self.trace:
            return self._start_trace()

        while self.run:
            # XXX might be faster (avoid indexing a list) to
            #   create a "next" pointer on VM code "read-in"
            #   (run list in reverse;
            #    could also eliminate unconditional "jrst"?!)
            # NOTE! self.ir saved for debug.
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            ir.step(self)       # execute instruction

    def _start_trace(self):
        # XXX get terminal width, use to create format?
        while self.run:
            # NOTE! self.ir for debug.
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            ir.step(self)       # execute instruction
            irstr = str(ir)[1:-1] # remove []'s -- XXX remove quotes too???
            print("%-45.45s | %-32.32s" % (irstr, repr(self.ac)))

    def _start_stats(self):
        # stats
        self.op_count = {}
        self.op_time = {}
        self.bop_count = {}
        self.bop_time = {}

        for op in instr_class_by_name.keys():
            self.op_count[op] = self.op_time[op] = 0
        trace = self.trace
        # XXX inside try, to catch SystemExit??
        while self.run:
            self.ir = ir = self.cb[self.pc] # instruction register
            self.pc += 1        # jumps will overwrite
            t0 = time.time()
            ir.step(self)       # execute instruction
            # XXX save ir in history buf??
            ir.prof(self, time.time() - t0)
            if trace:
                print(ir, self.ac)

        ttime = tcount = 0
        for op in instr_class_by_name:
            ttime += self.op_time[op]
            tcount += self.op_count[op]

        s = sys.stderr
        print("insts", tcount, ttime, file=s)

        for op in self.op_count:
            pcount = 100*self.op_count[op]/tcount
            ptime = 100*self.op_time[op]/ttime
            # ratio of pct time spent to pct times called
            # >1.0 means time hog
            if pcount:
                ratio = ptime/pcount
            else:
                ratio = 0
            print(op, self.op_count[op], pcount, ptime, ratio, file=s)

        print("", file=s)
        bcount = 0
        btime = 0
        for op in self.bop_count:
            bcount += self.bop_count[op]
            btime += self.bop_time[op]
        print("binops", bcount, btime, file=s)

        for op in self.bop_count:
            pcount = 100 * self.bop_count[op] / bcount # percentage of calls
            ptime = 100 * self.bop_time[op] / btime # percentage of time

            # ratio of pct time spent to pct times called
            # >1.0 means time hog
            if pcount:
                ratio = ptime/pcount
            else:
                ratio = 0

            print(op, self.bop_count[op], pcount, ptime, ratio, file=s)

    def dump_stack(self):
        """
        dump (call argument) stack for debugging
        """
        t = self.sp
        while t:
            print("  ", t[0])
            t = t[1]

    def save_frame(self, show=True):
        # called from CClosure.invoke (always call before .invoke??)
        #       would need to call restore_frame inside all .invoke methods??
        #       would allow Python callees to use same VM???
        # called from CBClosure.invoke w/ show=False
        self.fp = Frame(cb=self.cb, pc=self.pc, scope=self.scope, fp=self.fp,
                        where=self.ir.where, fn=self.ir.fn, # for backtrace
                        show=show
        )

    def backtrace(self):        # XXX take file to write to?
        fp = self.fp
        while fp:
            if fp.show:
                sys.stderr.write(" called from {}:{}\n".format(
                    fp.fn, fp.where))
            fp = fp.fp

    # helper (inline once settled?)
    # make method of OpInstr parent class??
    def call_op(self, optype, inst):
        """
        invoke a method for an operator
        caller (Instr) has set up self.args (Python list in forward order)
        `optype` Python string, one of UNOPS, BINOPS, LHSOPS
        `inst.value` Python string for operator to look up
        object in self.ac
        """
        m = classes.find_op(self.ac, optype, inst.value)
        # XXX always create frame?
        m.invoke(self)

    def push(self, val):
        """
        push onto saguro/cactus/spaghetti stack,
        necessary for continuations.
        """
        self.sp = (val, self.sp) # MUST be immutable!

    def pop(self):
        """
        pop from cactus stack
        moves pointer in chain,
        does not modify existing entries.
        """
        val, self.sp = self.sp  # unpack top of stack
        return val

    def restore_frame(self, frame):
        """
        "return" using saved frame pointer
        helper used by ReturnInstr and CContinuation
        """
        self.cb = frame.cb
        self.pc = frame.pc
        self.scope = frame.scope
        self.fp = frame.fp

################################################################
# VM instructions

def reginstr(inst_class):
    """
    decorator for VMInst classes for reading in JSON representations
    """
    name = inst_class.name
    if name in instr_class_by_name:
        raise VMError("duplicate entry for %s instruction" % name)
    instr_class_by_name[name] = inst_class
    return inst_class           # not wrapped by decorator

class VMInstr0(object):
    """
    base class for VM instructions with zero arguments
    """
    __slots__ = ['name', 'where']

    def __init__(self, iscope, fn, where):
        self.fn = fn
        self.where = where

    def fn_where(self):         # for trace
        return "%s:%s" % (self.fn, self.where)

    def __repr__(self):
        return str(self.json())

    def json(self):
        return [self.fn_where(), self.name]

    def step(self, vm):
        raise VMError("'%s' has no step method" % type(self).__name__)

    def prof(self, vm, elapsed):
        vm.op_count[self.name] += 1
        vm.op_time[self.name] += elapsed

class VMInstr1(VMInstr0):
    """
    base for VM Instructions with one argument
    """
    __slots__ = ['name', 'where', 'value']

    def __init__(self, iscope, fn, where, value):
        super().__init__(iscope, fn, where)
        self.value = value

    def json(self):
        return [self.fn_where(), self.name, self.value]

class VMInstr2(VMInstr0):
    """
    base for VM Instructions with one argument
    """
    __slots__ = ['name', 'where', 'v1', 'v2']

    def __init__(self, iscope, fn, where, v1, v2):
        super().__init__(iscope, fn, where)
        self.v1 = v1
        self.v2 = v2

    def json(self):
        return [self.fn_where(), self.name, self.v1, self.v2]

@reginstr
class LitInstr(VMInstr1):
    """
    load literal (Number or Str) into AC
    """
    name = "lit"

    def __init__(self, iscope, fn, where, value):
        # convert to Class when code is loaded
        super().__init__(iscope, fn, where, classes.wrap(value, iscope))

    def step(self, vm):
        vm.ac = self.value

@reginstr
class PushLitInstr(LitInstr):
    """
    push literal (Number or Str) onto stack
    """
    name = "push_lit"

    # __init__ from LitInstr

    def step(self, vm):
        vm.push(self.value)

@reginstr
class PushInstr(VMInstr0):
    """
    save AC on stack
    """
    name = "push"

    def step(self, vm):
        vm.push(vm.ac)

@reginstr
class TempInstr(VMInstr0):
    """
    copy TEMP to AC
    (used with "new")
    """
    name = "temp"

    def step(self, vm):
        vm.ac = vm.temp

@reginstr
class PopTempInstr(VMInstr0):
    """
    copy TEMP to AC
    pop top of stack into TEMP
    (used with "new")
    """
    name = "pop_temp"

    def step(self, vm):
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

    def step(self, vm):
        vm.ac = vm.scope.lookup(self.value)

@reginstr
class BinOpInstr(VMInstr1):
    """
    execute (RHS) binary operator for object in AC
    pops RHS operand from stack
    sets VM args to [AC, operand]
    inst.value is Python string for operator
    lookup in lhsops for object and invoke
    """
    name = "binop"

    def step(self, vm):
        arg = vm.pop()
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, arg]
        vm.call_op(const.BINOPS, self)

    def prof(self, vm, secs):
        super().prof(vm, secs)
        op = self.value         # NOT a CObject!
        if op not in vm.bop_count:
            vm.bop_count[op] = vm.bop_time[op] = 0
        vm.bop_count[op] += 1
        vm.bop_time[op] += secs

@reginstr
class BinOpLitInstr(BinOpInstr): # NOTE! inherits special "prof" method!
    """
    RHS binary operator with literal LHS operand
    """
    name = "binop_lit"

    __slots__ = ['lit']
    def __init__(self, iscope, fn, where, op, lit):
        # convert to Class when code is loaded
        super().__init__(iscope, fn, where, op) # vm.call_op expects op in "value"
        self.lit = classes.wrap(lit, iscope)

    def step(self, vm):
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, self.lit]
        vm.call_op(const.BINOPS, self)

    def json(self):
        return [self.fn_where(), self.name, self.value, self.lit]

@reginstr
class LHSOpInstr(VMInstr1):
    """
    execute (LHS) binary operator for object in AC
    pops RHS operand (index/property) from stack
    pops value to store from stack
    sets VM args to [AC, operand, value]
    inst.value is Python string for operator
    lookup in lhsops for object and invoke
    """
    name = "lhsop"

    def step(self, vm):
        arg1 = vm.pop()         # index or property
        arg2 = vm.pop()         # value to store
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac, arg1, arg2]
        vm.call_op(const.LHSOPS, self)

@reginstr
class UnOpInstr(VMInstr1):
    """
    execute unary operator for object in AC
    sets VM args to [AC]
    inst.value is Python string for operator
    lookup in unops for object and invoke
    """
    name = "unop"

    def step(self, vm):
        # NOTE: find_op does not return BoundMethod:
        vm.args = [vm.ac]
        vm.call_op(const.UNOPS, self)

@reginstr
class CloseInstr(VMInstr1):
    """
    create a Closure (from code + current scope)
    inst.value contains VM code (as Python list of VMInstrs)
    """
    name = "close"

    def __init__(self, iscope, fn, where, value):
        super().__init__(iscope, fn, where, convert_instrs(value, iscope, fn))

    def step(self, vm):
        vm.ac = classes.CClosure(self.value, vm.scope)

@reginstr
class BCCallInstr(CloseInstr):
    """
    create a {} block closure and call it
    (hidden in backtraces)
    """
    name = "bccall"

    def step(self, vm):
        c = classes.CBClosure(self.value, vm.scope)
        c.invoke(vm)

@reginstr
class CallInstr(VMInstr1):
    """
    Calls CObject invoke method
        (CClosure, CPyFunc, CBoundMethod, CContinuation define this,
         CObject hands off to "(" binop)
    self.value is Python number of args on stack
    pops args from stack, creating Python list in vm.args
    calls CObject.invoke(vm)
    """
    name = "call"

    def step(self, vm):
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
    used for calls with spread arguments (...array)
    """
    name = "clargs"

    def step(self, vm):
        vm.args = []

@reginstr
class PopArgInstr(VMInstr0):
    """
    pop one arg from stack, append to vm.args
    used for calls with spread arguments (...array)
    """
    name = "poparg"

    def step(self, vm):
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
    def step(self, vm):
        arg = vm.pop()            # pop argument
        #print("sparg", arg)
        vm.args.extend(arg.value) # XXX getlist

@reginstr
class Call0Instr(VMInstr0):
    """
    actual function call for calls with span arguments
    """
    name = "call0"

    def step(self, vm):
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

    def step(self, vm):
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

    def step(self, vm):
        vm.restore_frame(vm.fp)

@reginstr
class ExitInstr(VMInstr0):
    """
    halt VM.
    used by invoke_function.
    """
    name = "exit"               # XXX rename to "halt"???

    def step(self, vm):
        #sys.stderr.write("exit\n")
        vm.run = False

@reginstr
class VarInstr(VMInstr1):
    """
    declare a variable in current scope.
    Python string in self.value
    """
    name = "var"

    def step(self, vm):
        vm.scope.defvar(self.value, classes.null_value)

@reginstr
class ArgsInstr(VMInstr1):
    """
    first op executed in a closure (generated by "function" keyword)
    self.value is Python list of formals (argument names) as Python strings
    vm.args is Python list of actuals (argument values) as CObjects
    * creates a new scope
    * for each formal (argument name):
     * pops an actual from vm.args and creates variable
     * creates variable with null value if no actuals remain
    """
    name = "args"

    def step(self, vm):
        if len(vm.args) > len(self.value):
            # NOTE: Exception: a user error!
            raise Exception("%s: too many arguments. got %d, expected %d" % \
                            (self.where, len(vm.args), len(self.value)))
        # NOTE: scope.func_scope() creates a cactus stack of scopes;
        #       defines 'return' as a Continuation to prev frame
        vm.scope = vm.scope.func_scope(vm.fp)
        for formal in self.value:  # loop for formals
            if vm.args:            # actuals left?
                val = vm.args.pop(0) # yes: pop a value
            else:
                val = classes.null_value # no: use null
            vm.scope.defvar(formal, val) # declare as variable

@reginstr
class Args2Instr(VMInstr2):
    """
    first op executed in a closure ("function") w/ a ...rest argument
    self.v1 is Python list of formals (argument names) as Python strings
    self.v2 is Python string for rest argument
    vm.args is Python list of actuals (argument values) as CObjects
    * creates a new scope
    * for each formal (argument name):
     * pops an actual from vm.args and creates variable
     * creates variable with null value if no actuals remain
    * creates a List with anything remaining in vm.args
    """
    name = "args2"

    def step(self, vm):
        # NOTE: scope.func_scope() creates a cactus stack of scopes
        vm.scope = vm.scope.func_scope(vm.fp)
        for formal in self.v1:       # loop for formals
            if vm.args:              # actuals left?
                val = vm.args.pop(0) # yes: pop a value
            else:
                val = classes.null_value # no: use null
            vm.scope.defvar(formal, val) # declare as variable

        # create List from remaining args
        l = system.create_sys_type('List', vm.scope, vm.args) # XXX want frozen?
        vm.scope.defvar(self.v2, l)  # declare as variable

@reginstr
class LScopeInstr(VMInstr1):
    """
    first op executed in a scope closure with a leave label
    """
    name = "lscope"

    def step(self, vm):
        # creates new scope, w/ named Continuation to leave it
        vm.scope = vm.scope.labeled_scope(vm.fp, self.value)

@reginstr
class UScopeInstr(VMInstr0):
    """
    first op executed in an unlabled scope closure
    """
    name = "uscope"

    def step(self, vm):
        vm.scope = vm.scope.new_scope()

@reginstr
class StoreInstr(VMInstr1):
    """
    store AC in a variable
    self.value contains Python string for variable name
    (see "LoadInstr" for discussion how compiler could help)
    """
    name = "store"

    def step(self, vm):
        vm.scope.store(self.value, vm.ac)

@reginstr
class JrstInstr(VMInstr1):
    """
    Unconditional jump.
    sets PC (offset into code block) from self.value (Python int)
    (see VMCode object in parser for origin of name)
    """
    name = "jrst"

    def step(self, vm):
        vm.pc = self.value

@reginstr
class JumpNInstr(VMInstr1):
    """
    Jump if true.
    If AC is truthy, sets PC (offset into code block) from self.value
    (see VMCode object in parser for origin of name)
    """
    name = "jumpn"

    def step(self, vm):
        if classes.is_true(vm.ac):
            vm.pc = self.value

@reginstr
class JumpEInstr(VMInstr1):
    """
    Jump if true.
    If AC is falsey, sets PC (offset into code block) from self.value
    (see VMCode object in parser for origin of name)
    """
    name = "jumpe"

    def step(self, vm):
        if not classes.is_true(vm.ac):
            vm.pc = self.value

@reginstr
class NewInstr(VMInstr1):
    """
    for [ ... ] and { .... } sugar (from compiler) *ONLY*
    push VM TEMP register onto stack (so nestable)
    "arg" contains Python string of name of container class to create
    leave new, empty container in VM TEMP register
    """
    name = "new"

    def step(self, vm):
        vm.push(vm.temp)
        if self.value == 'Dict':
            v = {}
        elif self.value == 'List':
            v = []
        else:
            VMError("new Instr unknown type %s" % self.value)
        vm.temp = system.create_sys_type(self.value, vm.scope, v)

################
# convert Python list into XxxInstr(ruction) instances
# (this is the .vmx file assembler!)

def convert_one_instr(i, iscope, fn):
    """
    take single instruction in JSON form and assemble.
    i[0] is "line:char"
    i[1] is opcode
    fn is filename
    """
    op = i.pop(1)
    # create new instruction instance
    return instr_class_by_name[op](iscope, fn, *i)

def convert_instrs(il, iscope, fn):
    """
    assemble a list of instructions in JSON form
    fn is filename
    used by CloseInstr and load_vm_json
    """
    return [convert_one_instr(x, iscope, fn) for x in il]

# called only by system.import_worker
def load_vm_json(fname, iscope):
    with open(fname) as f:
        l = f.readline()
        if l and l[0:1] == '#!': # hash bang?
            l = f.readline()     # discard

        # parse metadata
        metadata = json.loads(l.strip())

        # load list of instructions
        j = json.load(f)

    return convert_instrs(j, iscope, metadata.get('fn'))

################

def breakpoint_if_debugging():
    """
    call from exception handlers
    drop into pdb if it's loaded
    (previous breakpoint, or -mpdb on command line)
    """
    if 'pdb' in sys.modules:
        breakpoint()

# XXX make a VM method?!!!
def run(boot, scope, stats, trace):
    """
    cold start (from xxl.py)
    `boot` is Closure w/ bootstrap.vmx code for main module
    """
    vm = VM(stats=stats, trace=trace)

    vm.ac = boot                # Closure
    b0 = [["0", "call0"],       # call Closure
          ["1", "exit"]]        # quit VM
    code = convert_instrs(b0, scope, "@boot0")
    try:
        vm.start(code, scope)
    except SystemExit:          # from os.exit
        raise
    except (VMError, AssertionError) as e: # an internal error
        # NOTE: displays VM Instr
        sys.stderr.write("VM Error @ {}: {}\n".format(vm.ir, e))
        # XXX dump VM registers?
        vm.backtrace()

        # print Python traceback
        import traceback
        traceback.print_exc()

        breakpoint_if_debugging()
        sys.exit(1)
    except classes.UError as e: # handle ValueError??
        # NOTE: user error: just displays "where" and VM backtrace
        if vm.ir:
            sys.stderr.write("Error @ {}:{}: {}\n".format(
                vm.ir.fn, vm.ir.where, e))
        else:
            sys.stderr.write("Error @ ???: {}\n".format(e))
        vm.backtrace()
        breakpoint_if_debugging()
        sys.exit(1)
