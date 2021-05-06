
While my goal (at least in part) was to have some of Scheme
flexibility, C family (eg JavaScript) syntax, and Pythonish datatypes
and library leverage, PLUS sane scoping rules (and a clean namespace),
but in the end it's neither fish not fowl.

Brendan Eich has said the original goal of JavaScript was to implement
as much of Scheme as possible in the browser with Java-like syntax in
10 days(*), and this is in that vein (only it's taken me 5 years)....
In particular, adding continuations.

(*)https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/

NOTE: many of my complaints below may be obsolete, but I try to write
in portable subsets, rather than requiring the user to run out and
install the latest release: "Fixed in version n+1" rarely erases
original misfeatures.

### Things I like about Python:
* reasonably powerful and regular
* not too many ways to do the same thing
	(though comprehensions have erased this to a great degree).
* reasonably flexible argument handling (keywords, *args, **kws)
* large and powerful ecosystem (both included and PyPI)
* hope/possibility of speedups using PyPy/RPython?
* explicit "self" argument (no mystery about where value came from)
* bound methods (no magic regarding how methods are called)
* full unicode characters (no UTF-16 surrogacy)

### Dislikes about Python:
* yes, spacing IS sufficent,
	but don't answer the phone while cutting and pasting.
* limited lambda (see above)
* too many intrinsic functions (len, str, repr) that could be methods
	(and often are, just with funny names)
* experimental fun with operator redefinition has limits
	(eg by built-in knowledge of what ops return boolean values)
* lack of explicit variable declarations
* lack of explicit member declarations
* painful scope rules
* it keeps growing
* can't override "new" -- painful to make a singleton
	(not that I'm a big fan of the Gang of Four,
	 and singletons are the global variables, of the 1990's)

### Likes about JavaScript:
* reuse of C-syntax neurons & explicit block syntax
* fast runtime environment available
	(not that it was enough to win me over)
* simple import function
* transparency

### Dislikes about JavaScript:
* "everything is an Object" is an interesting experiment
      (much as "spacing alone is sufficient"), but for the weak
      minded (like myself), it's easy to wind up with Objects
      that are chimeras (fish with wings, and chickens with fins),
      and don't have clearly delimited function, purpose or origin.
      If I wanted to be a LISP programmer, I would be!
* painful scope rules
* much may have been "fixed" in later versions of the language,
      but at the expense of having many ways to do things,
      and an ever more confusingly large language.
* Node.js callback oriented constructions hide explicit state,
      make it hard to know what's going on.
* implicit "this" makes it hard to know where it came from
      (especially with deeply nested closure declarations)
* method calls are magical (no bound methods)
* painful (initial) list/object "for" iteration behavior
* UTF-16 (surrogate pairs for anything outside unicode basic plane)

### Ruby influences:
* blocks as closures

### Ruby dislikes:
* yet another language with painful scoping (I heave when I see $global)
