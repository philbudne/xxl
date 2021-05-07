## Built-in Classes:

* Object (base class)
* Class (metaclass for all classes)
* Str (unicode string, using Python3 str)
* Number (Python3 int or real)
* List (Python3 list)
* Dict (Python3 dict)
* Bool (Python3 bool)
* Null (Python3 NonType)
* Closure (a "function")
* PyFunc (a Python3 function or bound method
* BoundMethod (a method (PyFunc or Closure) bound to an Object)
* PyObj (created by System.pyimport)
* Continuation (created when calling a Closure or BoundMethod)

All intrinsic Classes are available in System.types.ClassName

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
	of an ASSIGNOP, and are passed the value to store, and should
	return that value!!!

* "." on an Object (on the right hand side of an ASSIGNOP)
	will return a callable BoundMethod if the NAME is found as a method.

* All classes should provide "str" and "repr" methods, and an "init"
	method *IFF* you want to pass anything to MyClass.new
