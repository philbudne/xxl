# STYLE

* Variable, member and method names in_snake_case.
	_names should be treated as private.
	__names are reserved.

* Class names in CamelCase (But, *sigh* the System object is not a Class)

* K&R style placement of {}'s

* intents levels at 4 spaces

* assume tab stops at 8 spaces

# SYNTAX

* Largely adopted from Doug Crockfor's TDOP demo:
http://crockford.com/javascript/tdop/tdop.html

* ALL flow control statements take a { block },
except "else", which can take another "if"

* An _approximate_ grammar (subject to change, including at runtime!):

FILE:   STMT ...

STMT:
        "if" "(" EXPR ")" "{" STMT ... "}"
                [ "else" "if" "(" EXPR ")" "{" STMT ... "}" ]...
                [ "else" "{" STMT ... "}" ]
        "while" "(" EXPR ")" "{" STMT ... "}"
        "var" NAME ["=" EXPR] ";"
        FUNCTION_CALL ";"
        ASSIGNMENT ";"

EXPR:   NAME
        NUMBER
        STRING
        "[" [ EXPR ["," ...] "]"
        "{" KEY: EXPR ["," ...] "}"
        EXPR "." NAME                   (precedence 80)
        EXPR ".." NAME                  (precedence 80)
        "(" EXPR ")"                    (precedence 80)
        EXPR "[" EXPR "]"               (precedence 80)
        PREFIX_EXPR                     (precedence 70)
        EXPR MULDIV EXPR                (precedence 60)
        EXPR ADDSUB EXPR                (precedence 50, left associative)
        EXPR RELOP EXPR                 (precedence 40)
        EXPR BOOLOP EXPR                (precedence 30)
        EXPR "?" EXPR ":" EXPR          (precedence 20)
        LHS ASSIGNOP EXPR               (precedence 10)
        EXPR "(" [ EXPR ["," ...] ")"   (precedence 0)

KEY:    NAME
        STRING

PREFIX_EXPR:
        UNOP EXPR                       
        "function" "(" FORMALS ")" { STMTS ... }

UNOP:   "!" | "-"

FORMALS:
        e
        NAME
        "..." NAME
        NAME "," FORMALS

ASSIGNOP: "=" | "+=" | "-="

BOOLOP: "&&" | "||"

RELOP:  "==" | "!=" | "<" | "<=" | ">" | ">="

MULDIV: "*" | "/"

ADDSUB: "+" | "-"

LHS:    NAME
        EXPR "." NAME
        EXPR "[" EXPR "]"

***NOTE***

All compile errors are fatal.
Extra ";" are not tolerated.
Trailing "," in [] and {} are not accepted.

"return" is *NOT* a statement, it's a variable containing a
continuation (EVERY call is a "call with current continuation").

All statement blocks inside braces are closures, with their own scope.

Each while loop is wrapped in a closure, and "leave_while" is a
variable available inside the loop which is a continuation to exit the
loop.

Similarly, "continue_while" is a variable with a continuation to continue
while loop

***NOTE!!*** {leave,continue}_while may be replaced with labeled
stmts)

All instances have a class (in __class property)

All classes have one or more superclasses, except Object, which has none.

Objects have properties. The Object class implements getprop/setprop
methods, and "." to access a compile time property name.  ".." is a
method/member lookup that skips the object class (ie; lookup only in
superclasses).

MOST operators (except "?", ASSIGNOPS, BOOLOPs)
are methods looked up at runtime.

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
