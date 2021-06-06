Reminder on how to bootstrap new features:

Adding a new VM instruction:

1. add new instruction to VM (do not remove old instr!)
2. add code to parser to emit new instruction
3. run Makefile (compiler regression test)
	"a.vmx" (generated using parser.vmx) will generate old instr
	"b.vmx" (generated using "a.vmx") will generate new instr
	"c.vmx" (generated using "b.vmx") tests new instr
4. replace parser.vmx with "c.vmx"
5. remove old instr from vmx.py if no longer used.

Adding a new core language feature (not used in parser);

(add new VM instruction to VM if needed, see above)
1. modify parser.xxl to implement new construct
2. run Makefile to make sure compiler compiles & runs as before
3. write a regression test to use new feature
   a. compile w/ "c.vmx" from step 2:
	./vm.py c.vmx test.xxl > test.vmx
   b. make sure the generated code works as expected
	./vm.py test.vmx
   c. return to step 1 or 3 as needed
   d. add test to tests directory
6. replace parser.vmx with c.vmx from step 2

Additional steps to use new feature in parser:

7. save copy of parser.xxl as nparser.xxl
8. edit nparser.xxl
9. test nparser.xxl using parser.vmx
	./vm.py nparser.xxl > nparser.a
10. compile nparser.xxl using itself:
	./vm.py nparser.a nparser.xxl > nparser.b
11. compile nparser.xxl using self-generated code:
	./vm.py nparser.b nparser.xxl > nparser.c
12. compare output
13. return to step 8 as needed
14. replace parser.xxl with nparser.xxl
    replace parser.vmx with nparser.c
