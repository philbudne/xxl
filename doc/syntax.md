# SYNTAX

* Largely adopted wholesale from Doug Crockford's original parser:
        http://crockford.com/javascript/tdop/tdop.html
        (a subset of the "good parts" of JavaScript).

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
FILE:   [ STMT ]…

STMT:   [ NAME ":"] UNLABELED_STMT

UNLABELED_STMT:
        «if» «(» EXPR «)» BLOCK
                [ «else» «if» «(» EXPR «)» BLOCK ]…
                [ «else» BLOCK ] |
        «while» «(» EXPR «)» BLOCK |
        «var» NAME [ «=» EXPR ] «;» |
        «const» NAME «=» EXPR «;» |
        FUNCTION_CALL «;» |
        ASSIGNMENT «;»

BLOCK:  [NAME «:»] «{» STMT … «}»

EXPR:   NAME |
        NUMBER |
        STRING |
        «[» [ EXPR [«,» EXPR]… ] [«,»] «]» |
        «{» [ KEY: EXPR [«,» KEY:EXPR ]… ] [«,»] «}» |
        «(» EXPR «)» |
        EXPR «.» NAME |                 (precedence 110)
        EXPR «..» NAME |                (precedence 110)
        FUNCTION_CALL |                 (precendence 110)
        EXPR «[» EXPR «]» |             (precedence 110)
        UNOP EXPR |                     (precedence 100)
        «function» [ NAME ] «(» FORMALS «)» «{» STMTS … «}» | (precedence 100)
        EXPR MULDIV EXPR |              (precedence 90)
        EXPR PLUSMINUS EXPR |           (precedence 80, left associative)
        EXPR «&» EXPR |                 (precedence 70)
        EXPR «|» EXPR |                 (precedence 60)
        EXPR RELOP EXPR |               (precedence 50)
        EXPR «&&» EXPR |                (precedence 40)
        EXPR «||» EXPR |                (precedence 30)
        EXPR «?» EXPR «:» EXPR |        (precedence 20)
        ASSIGNMENT                      (precedence 10)

KEY:    NAME | NUMBER

FUNCTION_CALL:
        EXPR «(» [ ACTUAL [«,» ACTUAL]… ] «)»

UNOP:   «!» | «-» | «~»

FORMALS:
        [ NAME [ «,» NAME ]… ] [ «...» NAME ]

RELOP:  «===» | «!==» | «==» | «!=» | «<» | «<=» | «>» | «>=»

MULDIV: «*» | «/»

PLUSMINUS: «+» | «-»

ASSIGNMENT:
        LHS ASSIGNOP EXPR

ASSIGNOP: «=» | «+=» | «-=»

LHS:    NAME
        EXPR «.» NAME
        EXPR «[» EXPR «]»

ACTUAL: EXPR |
        «...» EXPR

NUMBER: DIGIT… [«.» [DIGIT]…] [ E [PLUSMINUS] DIGIT… ]

E:      «e» | «E»

NAME:   LETTER_OR_UNDERSCORE [LETTER_UNDERSCORE_DIGIT_OR_UNICODE]…

STRING: «'» [ANYTHING_EXCEPT_NEWLINE_OR_SINGLE_QUOTE]… «'» |
        «"» [ANYTHING_EXCEPT_NEWLINE_OR_DOUBLE_QUOTE]… «"» |
        «'''» [ANYTHING_EXCEPT_TRIPLE_SINGLE_QUOTE]… «'''» |
        «"""» [ANYTHING_EXCEPT_TRIPLE_DOUBLE_QUOTE]… «"""»

        Double quoted strings interpret the following escape sequences:
        \"      ASCII double quote character (34 decimal)
        \'      ASCII double quote character (39 decimal)
        \\      ASCII backslash character (92 decimal)
        \b      ASCII Back Space character (8 decimal)
        \n      ASCII Line Feed character (10 decimal)
        \r      ASCII Carriage Return character (13 decimal)
        \t      ASCII Horizontal Tab (9 decimal)
        \v      ASCII Vertical Tab (11 decimal)
        \xXX    base-16 representation of an unsigned 8-bit Unicode code point
        \uXXXX  base-16 representation of an unsigned 16-bit Unicode code point
        \UXXXXXXXX base-16 representation of unsigned 32-bit Unicode code point
                (NOTE: not all code point values are legal!
                 Unicode limited to 21 bits)

        single quoted strings do not interpret '\' escapes

        // makes the rest of the line a comment

        White space characters (CR, LF, TAB, FF) are ignored.

        Any string of characters from !#$%&*+-./:;<=>?@\^|~
        or *ANY* non-ASCII Unicode code point may be defined
        as an operator!!

        All other non alphanumeric printing ASCII characters are stand-alone
        (operator) tokens: (),[]`{}
```

## lexical conventions:

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

* Extra ";" are not accepted (and none are optional).

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

The Object "__xxl" contains the following members:
        import: a function to import another file (namespace returned as Object)
        pyimport: a function to import a Python module as a PyObject
                "." returns a wrapped value (Bool, Str, Number)
                or another PyObj.  PyObj's are callable.
        exit: a function, takes an int, exit process with integer status value
        argv: a list of strings of arguments following the program path
        uerror: a function, takes a string, causes fatal error
        debug functions:
                break: break to Python debugger, with optional value (available in pdb as x)
                print: convert arguments to Str, concatenate and print to stdout
                error: convert arguments to Str, concatenate and print to stderr
                backtrace: print xxl return stack to stderr

Base classes are available via `var classes = import("classes");`

All "{" STMT... "}" code blocks have their own variable scope
        and are implemented as closures.

Variables MUST be declared using "var", "const", or as function arguments.

NOTE! Enforcement of "const" is currently implemented only in the parser,
        and const values in other Modules can be changed!!
