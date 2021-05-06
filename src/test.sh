#!/bin/sh

# run test suite (numbered files in test directory)
#	each file has a .ref file with expected (std)output

# take CMD & OPTIONS from environment (passed by Makefile)

if [ "x$CMD" = x ]; then
    CMD=./xxl.py
fi

for x in test/[0-9]*.xxl; do
    $CMD $OPTIONS $x > $x.tmp 2>&1
    if cmp $x.tmp $x.ref; then
	echo $x: OK
	rm -f $x.tmp
    else
	echo $x: FAILED
	exit 1
    fi
done
