#!/usr/bin/env python3

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
eXperimental/eXtensible Language Zero (XXL/0)
command line interface

a small file, hopefully it stays that way!

"""


# python libraries:
import os
import sys

# XXL:
import xxlobj                   # before classes
import classes                  # new_module
import vmx

# XXX Convert to native code, put in bootstrap.xxl??

argv = list(sys.argv)           # copy
argv.pop(0)                     # vmx.py

stats = trace = help = xcept = False
parser = None
# XXX use real arg parser!
while argv:
    if argv[0][0] != '-':
        break
    if argv[0] == '-h':
        help = True
        argv.pop(0)
    elif argv[0] == '-t':
        trace = True
        argv.pop(0)
    elif argv[0] == '-s':
        stats = True
        argv.pop(0)
    elif argv[0] == '-x':
        xcept = True
        argv.pop(0)
    elif argv[0] == '-P':
        argv.pop(0)
        parser = argv.pop(0)
    else:
        sys.stderr.write("unknown option {}\n".format(argv[0]))
        sys.exit(1)

if help:
    sys.stderr.write("""
Usage: xxl.py [-h][-s][-t][-x][-P parser.vmx] file args ...

file can be .xxl (source) or .vmx (VM code)

-h    display this message
-s    enable VM stats
-t    enable VM instruction trace
-P    load alternate parser.vmx file
-x    show python eXception backtraces
""")
    sys.exit(1)

if argv:
    fname = argv.pop(0)
else:
    fname = "-"

if not parser:
    # _COULD_ choose parser based on source file name!!!
    #  (bootstrap could read a file with SUFFIX => VMXFILE mappings)
    parser = os.environ.get('XXL_PARSER', 'parser.vmx') # XXX lib dir

classes.classes_init(argv=argv, parser_vmx=parser)

mod, boot = classes.new_module(fname=fname, main=True)

assert boot is not None         # for mypy
vmx.run(boot=boot, scope=mod.scope, stats=stats, trace=trace, xcept=xcept)
