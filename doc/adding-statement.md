## Adding a statement

Example defining a C-style "do-while" statement to XXL:

```
    // define "do" statement
    var p = __modinfo.parser;   // Parser object

    var Do = Class.new({
        name: "Do",
        supers: [p.Stmt],
        methods: {
            std: function (this) {      // parse as statement
                this.first = p.block(); // parse { STATEMENTS... }
                p.check("while");
                p.scope.reserve(this.token);
                p.advance("while");
                p.advance("(");
                this.second = p.expression(0); // parse condition
                p.advance(")");
                p.advance(";");
                this.arity = "statement";
                return(this);
            },
            gen: function (this, vmcode) { // generate code
                // get current code location (offset)
                var top_label = vmcode.get_off();

                // generate code for body
                this.first.gen(vmcode);

                // generate code for condition expression
                // leaves value in VM "AC" (accumulator)
                this.second.gen(vmcode); // condition

                // if AC is true, jump to top of loop.
                vmcode.emit_iftrue(top_label, this);
            }
        }
    });
    p.add_symbol_class("do", Do);

    /// THAT'S IT!
    /// The statement is now available for use:

    var i = 4;
    do {
        System.print(i);
        i -= 1;
    } while (i > 0);
```

A label can be applied to the whole statement for `break`
or before the start of the "{" block for `continue`
