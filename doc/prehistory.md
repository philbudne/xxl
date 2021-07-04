The seeds:

In the fall of 1978 a friend and mentor went to Harvard and
brought back information on "PPL"
https://en.wikipedia.org/wiki/Polymorphic_Programming_Language
(used for instruction for non-CS students).

In the fall of 1979 I went off to (start) college at Stevens Tech and
was exposed to SITBOL (an implementation of SNOBOL4 which allowed
arbitrary operators (any string of characters from other operators?)
to be defined).  I also tinkered with MacLISP and was intrigued by
Vaughn Pratt's CGOL https://en.wikipedia.org/wiki/CGOL (an ALGOL-like
language front end).  I also was given the (then new-ish) GLS/GJS
"Lambda the Ultimate Imperative" (MIT AI Memo 353), and had my first
exposure to Scheme and continuations.

I'm not sure when I first saw Douglas Crockford's JavaScript subset
parser using Vaughn Pratt's Top Down Precedence parser technique used
in CGOL, written in itself (a "Good Parts" subset of JavaScript),
included in the 2007 book "Beautiful Code".

In November 2013 on a long drive, I pondered what language extension
features that would allow me to add SNOBOL4 pattern matching features.
When I returned, I translated Crockford's parser to Python to play
with, called jsparse.py

In December 2013 I made notes about a type system, and thoughts about
"sc2k", a SNOBOL4 for the 2000's, entiled "ASAP (as simple as
possible) but not simpler" where code in brace enclosed blocks
generated a closure.

LULL

October 2015: wrote Python code to play with implementing Python-style
argument passing.

Late January 2016: started work on asap.py:
	interpreter for jsparse.py JSON output
	(recursively performing lazy evaluation).

Early February 2016:
	jsparse.js running in asap.py interpreter (native Python types)

Mid February 2016: Python mockup of techniques for Continuations
		from Kent Dybvig's dissertation
		["Three Implementation Models for Scheme" (pdf)](https://www.cs.unm.edu/~williams/cs491/three-imp.pdf)
	last modifications to ppo.js (PrattParser as object)

Late February 2016: last changes to jsparse.py

**LULL**

Early April 2021:
	ported code to Python3
	first attempt to generate VM code in ppo.js
	modified to jsparse.py to generate VM code (never used)

Mid April 2021:
	second attempt at generating VM code in ppo.js, running under asap.py
	ppo.js self-generated code running under VM

Late April 2021:
	ppo.js using Class.new, called ppoc.js self compiling
	import & pyimport restored to working order

Early May 2021:
	code checked into
	[github xxl repository](https://github.com/philbudne/xxl/).
