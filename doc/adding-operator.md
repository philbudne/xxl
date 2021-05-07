## Adding a statement

Example defining an infix operator:

```
    var math = System.pyimport("math");

    var p = System.parser.parser;	// Parser object

    // add operator, at precedence higher than * and /
    p.add_infix("Exp", "^", true, 65);

    // add binary operator method to Number type:
    System.types.Number.__binops["^"] = math.pow;

    // first test:
    System.print(2^3);

    // higher precedence than division:
    System.print(2^3/2);

    // right associative:
    System.print(2^2^3);
```
