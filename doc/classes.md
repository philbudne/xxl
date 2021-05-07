## Built-in Classes:

* Object (base class)
* Class (metaclass for all classes)
* Str (unicode string, using Python3 str)
* Number (using Python3 int or real)
* List (using Python3 list)
* Dict (using Python3 dict)
	fetch of a non-existent entry returns Null.
* Bool (using Python3 bool)
* Null (using Python3 NoneType)
* Closure (a "function"; VM Code + scope)
* PyFunc (a Python3 callable)
* BoundMethod (a function bound to an Object)
	passes object as first (this) argument
* PyObj (created by System.pyimport)
* Continuation (created when calling a Closure or BoundMethod)
	available as `return` variable

All intrinsic Classes are available as System.types.ClassName

## Creating Classes

New classes are created with Class.new:
```
    var MyClass =
        Class.new({
            name: "MyClass",
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
