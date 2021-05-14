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

argv = list(sys.argv)           # copy
argv.pop(0)                     # vmx.py

fname_arg = "src_file"         # import_worker argument name for fname
stats = trace = trace_parser = help = False
parser = None
# XXX use real arg parser!
while argv:
    if argv[0][0] != '-':
        break
    if argv[0] == '-h':
        help = True
        argv.pop(0)
    elif argv[0] == '-T':
        trace_parser = True
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
    elif argv[0] == '-x':
        fname_arg = "vmx_file"  # load .vmx (JSON VM code) file
        argv.pop(0)
    else:
        sys.stderr.write("unknown option {}\n".format(argv[0]))
        sys.exit(1)

if not argv:
    # XXX XXX XXX want Read/Eval/Print Loop!!!
    help = True

if help:
    sys.stderr.write("Usage: xxl.py [-h][-s][-t][-T][-x][-P parser.vmx] file args ...\n")
    sys.exit(1)

fname = argv.pop(0)

# common arguments:
import_args = {
    fname_arg: fname,           # vmx_file or src_file
    "argv": argv,               # remains of the argv
    "main": True,
    "parser_vmx": parser,
    "stats": stats,
    "trace": trace,
    "trace_parser": trace_parser
}
system.import_worker(**import_args)
