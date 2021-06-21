## Adding an operator

Example defining an infix operator by subclassing:

```
    var math = __xxl.pyimport("math");
    var classes = __xxl.import("classes");

    var p = __modinfo.parser;	// Parser object

    // add infix operator, right associative, precedence higher than * and /
    p.add_infix("Exp", "^", true, p.PMUL + 4);

    // Subclass Number, adding operator, and use from here on out
    // (previously created values/results will NOT get new defn):
    classes.Number = Class.new({
	name: "MyNumber",
	supers: [classes.Number],
	binops: {
	    "^": math.pow
	}
    });

    // first test:
    __xxl.print(2^3);

    // higher precedence than division:
    __xxl.print(2^3/2);

    // right associative:
    __xxl.print(2^2^3);
```

A somewhat blunter approach is to modify the existing `Number` class,
adding the new binary operator:

```
    ...
    // add binary operator method to Number type:
   classes.Number.__binops["^"] = math.pow;
   ...
```

NOTE!  The parser uses `precedence-1` as right binding power for right
associative binary operators, so even `add_infix` precedence values
are advised!
