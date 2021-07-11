## eXtensible eXperimenal Language version Zero (XXL/0) [<sup><sup>intended jokes</sup></sup>](#intended-jokes)

A self-hosting extensible language, VM/type system in Python3.

**WARNING** the code and laguage are *HIGHLY* fluid!

*Please consider this a toy, not suitable for serious projects,
until further notice!!!*

Tested under Python 3.7.9 and PyPy3 7.3.1 (needs `export PYTHONIOENCODING=utf8`).

### Overall:

* Based on [Douglas Crockford's](http://crockford.com/)
	[TDOP JavaScript parser](http://crockford.com/javascript/tdop/tdop.html)
	based on [Vaughan Pratt's](http://boole.stanford.edu/pratt.html)
	[Top Down Operator Precedence Parsing](http://web.archive.org/web/20151223215421/http://hall.org.ua/halls/wizzard/pdf/Vaughan.Pratt.TDOP.pdf) (PDF) technique.

* JavaScript-like syntax, Python3-like types,
	new statements, operators and classes can be created at runtime.

* A sandbox for testing out ideas for "little languages"

* The base language contains enough to write the compiler;
	(the compiler gives itself good coverage),
	plus a regression test suite.

* [Syntax](doc/syntax.md) -- core language syntax

<!-- DOUBLE BLEH: no way to link to HTML!?!! no relative link!!!!! -->
<!-- also https://htmlpreview.github.io/ -->
<!-- HTML file w/o "head" section is acceptable .md file?? -->
* [Classes](https://raw.githack.com/philbudne/xxl/main/src/dist/classes.html) -- built in classes (machine generated HTML, *delivered by external CDN*)

* [Creating a new Class](doc/create-class.md)

* Adding operators
    + [example of adding "^" operator](doc/adding-operator.md)
    + [extension adding "nullish" operators](src/lib/ext/nullish.xxl)

* Adding statements
    + [extension for "do" statement](src/lib/ext/do.xxl)
    + [extension for "switch" statement](src/lib/ext/switch.xxl)

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

* The first extensible language I heard of was Harvard's PPL
     [Polymorphic Programming Language](https://en.wikipedia.org/wiki/Polymorphic_Programming_Language).

* Intended to be the smallest possible core language,
     one that no one "needs" to use.

* XXL is the U.S. clothing size two sizes larger than "large".
