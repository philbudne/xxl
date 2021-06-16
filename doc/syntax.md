# SYNTAX

* Largely adopted wholesale from Doug Crockford's original parser:
	http://crockford.com/javascript/tdop/tdop.html

* ALL flow control statements should take a { block },
	except "else", which can take another "if"

* Statements which end with a block should NOT take a ";" terminator
	(all others should require it)

* An **informal** grammar
	(approximate, subject to change, including at runtime!)

### conventions:

* terminals inside angle quotes («»)
* non-terminals in upper case
* `|` means alternation
* `THING …` means one or more
* `[ THING ]` means zero or one
* `[ THING ]…` means zero or more
* `( stuff )` is a comment

```
FILE:   STMT …

STMT:	[ NAME ":"] UNLABELED_STMT

UNLABELED_STMT:
        «if» «(» EXPR «)» BLOCK
                [ «else» «if» «(» EXPR «)» BLOCK ]…
                [ «else» BLOCK ] |
        «while» «(» EXPR «)» BLOCK |
        «var» NAME [«=» EXPR] «;» |
        FUNCTION_CALL «;» |
        ASSIGNMENT «;»

BLOCK:	[NAME «:»] «{» STMT … «}»

EXPR:   NAME |
        NUMBER |
        STRING |
        «[» [ EXPR [«,» EXPR]… ] «]» |
        «{» [ KEY: EXPR [«,» KEY:EXPR ]… ] «}» |
        EXPR «.» NAME |                 (precedence 100)
        EXPR «..» NAME |                (precedence 100)
        «(» EXPR «)» |                  (precedence 100)
        EXPR «[» EXPR «]» |             (precedence 100)
        UNOP EXPR |                     (precedence 90)
        «function» [ NAME ] «(» [ FORMALS ] «)» «{» STMTS … «}» | (precedence 90)
        EXPR MULDIV EXPR |              (precedence 80)
        EXPR PLUSMINUS EXPR |           (precedence 70, left associative)
        EXPR «&» EXPR                   (precedence 60)
        EXPR «|» EXPR                   (precedence 50)
        EXPR RELOP EXPR |               (precedence 40)
        EXPR LBOOLOP EXPR |             (precedence 30)
        EXPR «?» EXPR «:» EXPR |        (precedence 20)
        LHS ASSIGNOP EXPR |             (precedence 10)
        EXPR «(» [ EXPR [«,» EXPR]… «)» | (precedence 0)

KEY:    NAME | STRING

UNOP:   «!» | «-» | «~»

FORMALS:
        NAME [ «,» NAME ]… [ «...» NAME ]

ASSIGNOP: «=» | «+=» | «-=»

LBOOLOP: «&&» | «||»

RELOP:  «===» | «!==» | «==» | «!=» | «<» | «<=» | «>» | «>=»

MULDIV: «*» | «/»

PLUSMINUS: «+» | «-»

LHS:    NAME
        EXPR «.» NAME
        EXPR «[» EXPR «]»

NUMBER: DIGIT… [«.» [DIGIT]…] [ E [PLUSMINUS] DIGIT… ]

E:      «e» | «E»

NAME:   LETTER_OR_UNDERSCORE [LETTER_UNDERSCORE_DIGIT_OR_UNICODE]…

STRING: «'» [ANYTHING_EXCEPT_NEWLINE_OR_SINGLE_QUOTE]… «'» |
        «"» [ANYTHING_EXCEPT_NEWLINE_OR_DOUBLE_QUOTE]… «"» |
	«'''» [ANYTHING_EXCEPT_TRIPLE_SINGLE_QUOTE]… «'''» |
	«"""» [ANYTHING_EXCEPT_TRIPLE_DOUBLE_QUOTE]… «"""»

	Double quoted strings accept the following escape sequences:
	\"	ASCII double quote character (34 decimal)
	\'	ASCII double quote character (39 decimal)
	\\	ASCII backslash character (92 decimal)
	\b	ASCII Back Space character (8 decimal)
	\n	ASCII Line Feed character (10 decimal)
	\r	ASCII Carriage Return character (13 decimal)
	\t	ASCII Horizontal Tab (9 decimal)
	\xXX	base-16 representation of an unsigned 8-bit Unicode code point
	\uXXXX	base-16 representation of an unsigned 16-bit Unicode code point
	\UXXXXXXXX base-16 representation of unsigned 32-bit Unicode code point
		(NOTE: not all code point values are legal! Unicode limited
		 to 21 bits)

	single quoted strings do not interpret '\' escapes

	Any string of characters from !@#$%^&*-=+<>\|:,./?~
	or *ANY* non-ASCII Unicode code point may be defined
	as an operator!!
```

## lexical conventions:

* spacing is ignored
* `//` makes the rest of the line a comment

***NOTE***

* Any NAME (identifier) may be declared as a variable (or function argument)
   regardless of whether it has a statement syntax defined.

   Once a NAME has been used as a variable, that statement is no
   longer available in that scope (or any nested scope).

   Once a NAME has been used as a statement keyword, it is reserved,
   and may not be used as a variable in that scope, or any nested scope.

* MOST operators (except "?", ASSIGNOPS, BOOLOPs)
	are methods looked up at runtime.

* All compile errors are fatal.

* Extra ";" are not accepted.

* Trailing "," in [] and {} are not accepted.

* "return" is *NOT* a statement, it's a variable containing a
	continuation (EVERY call is a "call with current continuation"),
	and "return(value)" must be used.

* All statement blocks inside braces are closures, with their own scope.
	There is not (currently) any way to expose/pass those closures.

* Statements and blocks may be labeled with NAME ":"

	The label will appear as a variable containing a continuation
	to leave the labeled construct.

	(labling a statement will cause it to be wrapped in a closure
	 that contains the new variable; all blocks are already closures).

	Calling the leave label on a "while" loop is equivalent to "break"

	Calling the leave label on the BLOCK of a "while" loop is "continue"

* All instances have a class

	available with .getclass
	modifiable with .setclass

* All classes have one or more superclasses, except Object, which has none.

* Objects have properties.

	The Object class implements getprop/setprop methods, and "."
	to access a compile time property name.  ".." is a
	method/member lookup operator that skips the object class (ie;
	lookup only in superclasses).

Only "false", "null", and zero are false(y)

	(early on tried having all classes have an is_true
	method called on each if/while, but the overhead was painful.

"Class" is an instance of the metaclass "Class"

	Class implements the "new" method.

	All Classes are subclasses of Class.

New instances of a class are created with MyClass.new(....),
	which calls the metaclass (typ. "Class") new method with the class
		as the first argument
	and then calls the class "init" method (if any) to initialize
		with the new instance (typ. named "this" as the first arg)
	the superclass init method can be called with "this..init(....)"

The Object "System" (which is not a class) contains the following members:
	types: an object with all predefined classes as properties
	parser: contains a preloaded copy the (compiled) parser
	import: a function to import another file (namespace returned as Object)
	pyimport: a function to import a Python module as a PyObj
		"." returns a wrapped value (Bool, Str, Number)
		or another PyObj.  PyObj's are callable.
	temporary(?) debug functions: break, print, error, print_repr
	exit: a function, takes an int
	argv: a list of strings

All "{" STMT... "}" code blocks have their own variable scope
	and are implemented as closures.

Variables MUST be declared using "var", or as function arguments.
