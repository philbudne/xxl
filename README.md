## eXtensible eXperimenal Language version Zero (XXL/0) [*](#intended-jokes)

A self-hosting extensible language, VM/type system in Python3.

**WARNING** the code and laguage are *HIGHLY* fluid!

*Please consider this a toy, not suitable for serious projects,
until further notice!!!*

### Overall:

* Based on [Douglas Crockford's](http://crockford.com/)
	[JavaScript parser](http://crockford.com/javascript/tdop/tdop.html)
	based on [Vaughan Pratt's](http://boole.stanford.edu/pratt.html)
	[Top Down Operator Precedence Parsing](http://web.archive.org/web/20151223215421/http://hall.org.ua/halls/wizzard/pdf/Vaughan.Pratt.TDOP.pdf) technique.

* JavaScript-like syntax, Python3-like types,
	new statements, operators and classes can be created at runtime.

* A sandbox for testing out ideas for "little languages"

* The base language contains enough to write the compiler;
	(the compiler gives itself good coverage),
	plus a regression test suite.

* [Syntax](doc/syntax.md) -- core language syntax

* [Classes](doc/classes.md) -- built in classes, and making new ones

* [Adding a statement](doc/adding-statement.md) -- example of adding new statement syntax

* [Adding an operator](doc/adding-operator.md) -- example of adding an operator

* [Priorities](doc/priorities.md) -- a loose ordering of design priorities

* [Influences](doc/influences.md) -- language influences

* [Python](doc/python.md) -- interfacing with Python code

* [Style](doc/style.md) -- language style guide

* [Contributing](doc/contributing.md) -- please read this before creating a bug report, or a pull request

* [Bootstrapping](doc/bootstrapping.md) -- reminder on bootstrapping features

* [Prehistory](doc/prehistory.md) -- early influences and pre-github history

#### Intended jokes

* PL/1 was IBM's "One Language to Rule Them All" for System/360
     (the one computer architecture anyone would ever need).
     PL/1 was meant to replace both FORTRAN for scientific code
     and COBOL for business applications; it was a large
     language which had no reserved words, and all numeric
     variables were declared with their precision.

* Intended to be the smallest possible core language,
  one that no one "needs" to use.

* XXL is the U.S. clothing size two sizes larger than "large".
