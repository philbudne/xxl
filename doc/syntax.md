# STYLE

* Variable, member and method names in_snake_case.
	_names should be treated as private.
	__names are reserved.

* Class names in CamelCase (But, *sigh* the System object is not a Class)

* Indent and line breakage:
  * indent at four spaces
  * assume tab stops at eight spaces
  * no spaces before or between tabs
  * a statement that ends with a block does not take a ";"
  * "{" on the same line as the statement
  * "}" on a line by itself, at same indent as opening statement
	(unless tokens after the "}" are part of the statement,
	 in which case they should follow the "}",
	and the statement should be terminated with ";")
  * *NOT* currently consistent line breakage and operators!!
	(but probably should be)

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
        «[» [ EXPR [«,» EXPR]… «]» |
        «{» KEY: EXPR [«,» KEY:EXPR ]… «}» |
        EXPR «.» NAME |                 (precedence 80)
        EXPR «..» NAME |                (precedence 80)
        «(» EXPR «)» |                  (precedence 80)
        EXPR «[» EXPR «]» |             (precedence 80)
        UNOP EXPR |                     (precedence 70)
        «function» [ NAME ] «(» [ FORMALS ] «)» «{» STMTS … «}» | (precedence 70)
        EXPR MULDIV EXPR |              (precedence 60)
        EXPR ADDSUB EXPR |              (precedence 50, left associative)
        EXPR RELOP EXPR |               (precedence 40)
        EXPR BOOLOP EXPR |              (precedence 30)
        EXPR «?» EXPR «:» EXPR |        (precedence 20)
        LHS ASSIGNOP EXPR |             (precedence 10)
        EXPR «(» [ EXPR [«,» EXPR]… «)» | (precedence 0)

KEY:    NAME | STRING

UNOP:   «!» | «-»

FORMALS:
        NAME [ «,» NAME ]… [ «...» NAME ]

ASSIGNOP: «=» | «+=» | «-=»

BOOLOP: «&&» | «||»

RELOP:  «==» | «!=» | «<» | «<=» | «>» | «>=»

MULDIV: «*» | «/»

ADDSUB: «+» | «-»

LHS:    NAME
        EXPR «.» NAME
        EXPR «[» EXPR «]»

NUMBER:
        DIGIT… [«.» DIGIT…] [ E [ADDSUB] DIGIT… ]

E:      «e» | «E»

NAME:   LETTER_OR_UNDERSCORE [LETTER_UNDERSCORE_OR_DIGIT]…

STRING: «'» [ANYTHING_EXCEPT_NEWLINE_OR_SINGLE_QUOTE]… «'» |
        «"» [ANYTHING_EXCEPT_NEWLINE_OR_DOUBLE_QUOTE]… «"»

```

## lexical conventions:

* spacing is ignored
* `//` makes the rest of the line a comment

***NOTE***

* MOST operators (except "?", ASSIGNOPS, BOOLOPs) are methods looked up at runtime.
* All compile errors are fatal.

* Extra ";" are not tolerated.

* Trailing "," in [] and {} are not accepted.

* "return" is *NOT* a statement, it's a variable containing a
	continuation (EVERY call is a "call with current continuation")!!!

* All statement blocks inside braces are closures, with their own scope.

* Statements and blocks may be labeled.

	The label will appear as a variable containing a continuation
	to leave the labeled construct.

	(labling a statements will cause it to be wrapped in a closure;
	 blocks are already closures).

* All instances have a class (in __class property)

* All classes have one or more superclasses, except Object, which has none.

* Objects have properties.

	The Object class implements getprop/setprop
	methods, and "." to access a compile time property name.  ".." is a
	method/member lookup that skips the object class (ie; lookup only in
	superclasses).


Only "false", "null", and zero are false(y)
	(early on tried having all classes have an is_true
	method, but it was painful).

"Class" is an instance of the metaclass Class, which implements the
"new" method.  All classes are instances of a metaclass.

New instances of a class are created with MyClass.new(....),
	which calls the metaclass (typ. "Class") new method with the class
		as the first argument
	and then calls the class "init" method (if any) to initialize
		with the new instance (typ. named "this" as the first arg)
	the superclass init method can be called with "this..init(....)"

New classes are created with Class.new:
    var MyClass =
        Class.new({
            name: "MyClass",
            supers: [ SuperClass, .... ],
            methods: {
                name: function (this, ...) { }
                ...
            },
            unops: {
                "!": function (this) { }
                ...
            },
            binops: {
                "+": function (l, r) { }
                ...
            },
            lhsops: {
                ".": function(l, r, value) { }
                ...
            }
        })

lhsops methods are called when the binary operator is on the left hand side
	of an ASSIGNOP, and are passed the value to store, and should
	return that value!!!

"." on an Object (on the right hand side of an ASSIGNOP)
	will return a callable BoundMethod if the NAME is found as a method.

All classes should provide "str" and "repr" methods, and an "init"
	method *IFF* you want to pass anything to MyClass.new

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
