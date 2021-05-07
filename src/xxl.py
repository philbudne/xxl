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

# VM:
import system                   # import_worker

args = list(sys.argv)           # copy
args.pop(0)                     # vmx.py

fname_arg = "src_file"         # import_worker argument name for fname
stats = trace = trace_parser = help = False
dump = None
# XXX use real arg parser!
while args:
    if args[0][0] != '-':
        break
    if args[0] == '-h':
        help = True
        args.pop(0)
    elif args[0] == '-T':
        trace_parser = True
        args.pop(0)
    elif args[0] == '-t':
        trace = True
        args.pop(0)
    elif args[0] == '-s':
        stats = True
        args.pop(0)
    elif args[0] == '-x':
        fname_arg = "vmx_file"  # load .vmx (JSON VM code) file
        args.pop(0)
    else:
        sys.stderr.write("unknown option {}\n".format(args[0]))
        sys.exit(1)

if not args:
    # XXX XXX XXX want Read/Eval/Print Loop!!!
    help = True

if help:
    sys.stderr.write("Usage: xxl.py [-h][-s][-t][-T][-x] file args ...\n")
    sys.exit(1)

fname = args.pop(0)

# common arguments:
import_args = {
    fname_arg: fname,           # vmx_file or src_file
    "args": args,               # remains of the argv
    "main": True,
    "stats": stats,
    "trace": trace,
    "trace_parser": trace_parser
}
system.import_worker(**import_args)
