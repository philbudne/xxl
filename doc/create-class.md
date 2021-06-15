## Creating Classes

New classes are created with Class.new:
```
    var MyClass =
        Class.new({
            name: "MyClass",
            doc: "Description of MyClass",
            supers: [ SuperClass, .... ],
            methods: {
                name: function (this, ...) { ... }
                ...
            },
            unops: {
                "!": function (this) { ... }
                ...
            },
            binops: {
                "+": function (l, r) { ... }
                ...
            },
            lhsops: {
                ".": function(l, r, value) { ... }
                ...
            }
        })
```

* lhsops methods are called when the binary operator is on the left hand side
	of an ASSIGNOP, and are passed the value to store, and must
	return that value.

* "." on an Object (on the right hand side of an ASSIGNOP)
	will return a callable BoundMethod if the NAME is found as a method.

* All classes should provide "str" and "repr" methods, and an "init"
	method *IFF* you want to pass anything to MyClass.new
