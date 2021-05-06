## Adding a statement

Example defining a C-style "do-while" statement to XXL:

```
    // define "do" statement
    var p = System.parser.parser;	// active Parser object

    var Do = Class.new({
	name: "Do",
	supers: [p.Stmt],
	methods: {
	    id: function (this) { return("do"); }, // XXX want member!
	    std: function (this) {	// parse as statement
		this.first = p.block();
		p.advance("while");
		p.advance("(");
		this.second = p.expression(0);
		p.advance(")");
		p.advance(";");
		this.arity = "statement";
		return(this);
	    },
	    gen: function (this, vmcode) { // generate code
		var top_label = vmcode.get_off();
		this.first.gen(vmcode);
		this.second.gen(vmcode); // condition
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
