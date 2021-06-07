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
import sys

# XXL:
import system                   # before classes
import classes                  # new_module
import vmx

# XXX Convert to native code, put in bootstrap.xxl??

argv = list(sys.argv)           # copy
argv.pop(0)                     # vmx.py

stats = trace = help = False
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
    elif argv[0] == '-P':
        argv.pop(0)
        parser = argv.pop(0)
    else:
        sys.stderr.write("unknown option {}\n".format(argv[0]))
        sys.exit(1)

if not argv:
    # XXX XXX XXX want Read/Eval/Print Loop!!!
    help = True

if help:
    sys.stderr.write("""Usage: xxl.py [-h][-s][-t][-P parser.vmx] file args ...

file can be .xxl (source) or .vmx (VM code)

-h    display this message
-s    enable VM stats
-t    enable VM instruction trace
-P    load alternate parser.vmx file
""")
    sys.exit(1)

fname = argv.pop(0)

mod, boot = classes.new_module(fname=fname, argv=argv, main=True,
                               parser_vmx=parser)

vmx.run(boot=boot, scope=mod.scope, stats=stats, trace=trace)
