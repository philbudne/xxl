# `classes` Module

## Class `Bool`

Built-in Class for `true` and `false` values

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return Str representation: "true" or "false"
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `BoundMethod`

Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Callable`


    Virtual base Class for built-in callable classes
    (BoundMethod, Continuation, PyFunc, PyVMFunc)
    

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`

    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Class`

Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Closure`

Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Continuation`

Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Dict`

Built-in dictionary mapping Class

### Methods

#### `each_for (this, func)`

	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`

	call `func` argument for each iterator item
	
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`

	init method for Dict: takes Iterable returning two-item lists,
	OR an Iterable returning keys, and implementing '['
	
#### `init0 (obj)`

    called by Dict.init (in bootstrap.xxl)
    Dodges needing private metaclass for Dict
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `items (this)`

    return Iterable for [key, value] value pairs
    
#### `iter (this)`

    return forward iterator
    
#### `keys (this)`

    return Iterable for Dict keys
    
#### `len (this)`

    returns length (of String, List or Dict)
    
#### `map (this, func)`

	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`

	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (obj, arg)`

    remove Dict with specified key
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

	return representation of Dict
	
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `reversed (this)`

    return reverse iterator
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `sorted (this)`

    return sorted list values (or keys)
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
#### `values (this)`

    return Iterable for Dict values
    
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`

    get entry `r` Dict from dict `l`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`

    put `value` into Dict `l` index `r`
    
## Class `Iterable`

Virtual base Class classes that can be iterated over

### Methods

#### `each_for (this, func)`

	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`

	call `func` argument for each iterator item
	
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`

    return forward iterator
    
#### `map (this, func)`

	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`

	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `reversed (this)`

    return reverse iterator
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `sorted (this)`

    return sorted list values (or keys)
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `List`

Built-in mutable sequence Class

### Methods

#### `append (this, item)`

    append `item` to `this` List
    
#### `each_for (this, func)`

	call `func` argument for each reverse iterator item
	
#### `extend (this, iterable)`

#### `for_each (this, func)`

	call `func` argument for each iterator item
	
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`

	init method for List: takes Iterable
	
#### `init0 (l)`

    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`

    return forward iterator
    
#### `len (this)`

    returns length (of String, List or Dict)
    
#### `map (this, func)`

	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`

	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (l, index)`

    Remove and return List item at `index` (default last)
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

	return represtation of List
	
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `reversed (this)`

    return reverse iterator
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `sorted (this)`

    return sorted list values (or keys)
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`

    Return List item at index `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`

    Set List item at index `r` to `value`
    
## Class `ModInfo`

Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`

    `tree`: List of Lists of VM code
    `srcfile`: source of code
    returns Closure in __modinfo.module initial scope
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`

    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `load_vmx (this, fname)`

#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Module`

Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Null`

Built-on Class of `null` value

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    to_string/repr method for Null Class: returns "null"
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this, ...args)`

    "(" method for `null` value (fatal error)
    commonly happens when a bad method name is used
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Number`

Built-in int/float wrapper Class

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (obj, value)`

    initialize Number from Str value
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
#### `- (x)`

    Return negative of `x`
    
#### `~ (this)`

    return bitwise (binary) "not" (complement) of `this`
    
### Binary operators

#### `!= (l, r)`

    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `& (l, r)`

    return bitwise (binary) "and" (conjunction) of `l` and `r`
    
#### `( (l, ...args)`

    default Object '(' binop
    (fatal error)
    
#### `* (l, r)`

    multiple `l` and `r`
    
#### `+ (l, r)`

    add `l` and `r`
    
#### `- (l, r)`

    subtract `r` from `l`
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `/ (l, r)`

    divide `l` by `r`
    
#### `< (l, r)`

    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`

    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`

    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`

    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`

    return `true` if value of `l` is >= the value of `r`
    
#### `| (l, r)`

    return bitwise (binary) "or" (union) of `l` and `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Object`

Base Class

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`

    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (l, ...args)`

    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PClass`

Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`

    'create' method for PClass metaclass
    makes an instance of this_class backed by a CPObject
    used to create PClass subclass objects (Number, List, Dict, Bool, Null)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PObject`

Base class for Primitive/Python value Classes

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (l, ...args)`

    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyFunc`

Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterable`


    Wrapper for Python 'iterable' Objects
    (classes which can generate iterators)
    returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), PyIterable.range(),
    

### Methods

#### `each_for (this, func)`

	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`

	call `func` argument for each iterator item
	
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`

    return forward iterator
    
#### `map (this, func)`

	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`

	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `reversed (this)`

    return reverse iterator
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `sorted (this)`

    return sorted list values (or keys)
    
#### `to_str (this)`

    for debug: show Class name, and Python repr
    
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterator`

Built-in Class for a wrapper around a Python iterator

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`

    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`

    Python iterators are also iterables (return self)
    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method:

    Return the iterator object itself. This is required to allow
    both containers and iterators to be used with the for and in
    statements. This method corresponds to the tp_iter slot of the
    type structure for Python objects in the Python/C API.
    
#### `next (this, finished_continuation)`

    `finished` should be a CContinuation
    (eg; block leave label or "return")
    to call when iterator exhausted
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyObject`


    Built-in Class for a wrapper around an arbitrary Python Object
    (returned by pyimport, or operations on PyObjects)
    

### Methods

#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this, ...args)`

#### `. (l, r)`

    PyObject "." binop -- proxies to Python object getattr
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `[ (l, r)`

    PyObject "[" binop
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyVMFunc`


   Built-in Class for function implemented in Python
   with access to VM internals
   

### Methods

#### `create (this_class, ...args)`

    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`

    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`

	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`

    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `subclass_of (l, c)`

    return `true` if Class `l` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`

	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`

    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`

    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`

    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Str`

Built-in immutable Unicode string Class

### Methods

#### `each_for (this, func)`

	call `func` argument for each reverse iterator item
	
#### `ends_with (this, suff)`

    Return True if `this` ends with the suffix `suff`, False otherwise.
    
#### `for_each (this, func)`

	call `func` argument for each iterator item
	
#### `getclass (this)`

    return Class for `this`
    
#### `getprop (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`

    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`

    default PObject init0 method
    (fatal error)
    
#### `instance_of (l, c)`

    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`

    return forward iterator
    
#### `join (this, arg)`

    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
#### `len (this)`

    returns length (of String, List or Dict)
    
#### `map (this, func)`

	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`

	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `ord (this)`

    Return the Unicode code point for a one-character string `this`
    
#### `props (this)`

    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`

    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`

    for debug: show Class name, and Python repr
    
#### `reversed (this)`

    return reverse iterator
    
#### `setclass (this, klass)`

    set Class for `this`!!
    
#### `slice (this, start, end)`

    return a substring (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to rest of string
    
#### `sorted (this)`

    return sorted list values (or keys)
    
#### `split (this, sep, limit)`

    Return a List of the words in the string,
    using sep as the delimiter string (default to `null` -- any whitespace).
    Limit to `limit` return values (defaults to -1 -- no limit)
    
#### `starts_with (this, pref)`

    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    
#### `strip (this)`

    Return a copy of the string with leading and trailing whitespace removed.
    
#### `to_float (this)`

    Convert string to a floating point Number
    
#### `to_int (this, base)`

    Convert string to integer Number
    `base` defaults to zero (accept 0xXXX for base 16)
    
#### `to_str (this)`

    Identity method
    
### Unary operators

#### `! (x)`

    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`

    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`

    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`

    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `+ (x, y)`

    String concatenation
    
#### `. (l, r)`

    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`

    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `< (l, r)`

    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`

    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`

    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`

    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`

    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`

    return `true` if value of `l` is >= the value of `r`
    
#### `[ (l, r)`

    return `r`'th character of Str `l`
    r[l]
    
### LHS Binary operators

#### `. (l, r, value)`

    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Variables

### `false`

Value: `false`

### `null`

Value: `null`

### `true`

Value: `true`


---

formatted by doc.xxl on 2021-06-16
