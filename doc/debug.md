Advice for debugging internals:

1. Make a small test program.

2. Compile to VM code (this avoid tracing the compiler):
	./xxl.py -x parser.vmx test.xxl > test.vmx

3. Trace execution:
	./xxl.py -t -x test.vmx

4. If needed, add a call to System.break(value); and run:
	./xxl.py -x test.vmx

	when you break into pdb, variable "x"
	will have the value passed to System.break

	If you add the break BEFORE things go south,
	you can set breakpoints in the Python code
	and continue.
	