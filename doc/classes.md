# `classes` Module

## Class `Bool`

Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1698*


    return Str representation: "true" or "false"
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `BoundMethod`

Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Callable`


    Virtual base Class for built-in callable classes
    (BoundMethod, Continuation, PyFunc, PyVMFunc)
    

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*defined at classes.py:677*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Class`

Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Closure`

Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Continuation`

Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Dict`

Built-in dictionary mapping Class

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`
*defined at bootstrap.xxl:127:38*


	init method for Dict: takes Iterable returning two-item lists,
	OR an Iterable returning keys, and implementing '['
	
#### `init0 (obj)`
*defined at classes.py:1210*


    called by Dict.init (in bootstrap.xxl)
    Dodges needing private metaclass for Dict
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `items (this)`
*defined at classes.py:1226*


    return Iterable for [key, value] value pairs
    
#### `iter (this)`
*defined at classes.py:1131*


    return forward iterator
    
#### `keys (this)`
*defined at classes.py:1233*


    return Iterable for Dict keys
    
#### `len (this)`
*defined at classes.py:1033*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (obj, arg)`
*defined at classes.py:1219*


    remove Dict with specified key
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at bootstrap.xxl:154:38*


	return representation of Dict
	
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*defined at classes.py:1138*


    return reverse iterator
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `sorted (this)`
*defined at classes.py:1146*


    return sorted list values (or keys)
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
#### `values (this)`
*defined at classes.py:1240*


    return Iterable for Dict values
    
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`
*defined at classes.py:1201*


    get entry `r` Dict from dict `l`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`
*defined at classes.py:1192*


    put `value` into Dict `l` index `r`
    
## Class `Iterable`

Virtual base Class classes that can be iterated over

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*defined at classes.py:1131*


    return forward iterator
    
#### `map (this, func)`
*defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1048*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*defined at classes.py:1138*


    return reverse iterator
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `sorted (this)`
*defined at classes.py:1146*


    return sorted list values (or keys)
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `List`

Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*defined at classes.py:1273*


    append `item` to `this` List
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `extend (this, iterable)`
*defined at bootstrap.xxl:190:40*

#### `for_each (this, func)`
*defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`
*defined at bootstrap.xxl:170:38*


	init method for List: takes Iterable
	
#### `init0 (l)`
*defined at classes.py:1264*


    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*defined at classes.py:1131*


    return forward iterator
    
#### `len (this)`
*defined at classes.py:1033*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (l, index)`
*defined at classes.py:1281*


    Remove and return List item at `index` (default last)
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at bootstrap.xxl:183:38*


	return represtation of List
	
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*defined at classes.py:1138*


    return reverse iterator
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `sorted (this)`
*defined at classes.py:1146*


    return sorted list values (or keys)
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`
*defined at classes.py:1290*


    Return List item at index `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`
*defined at classes.py:1298*


    Set List item at index `r` to `value`
    
## Class `ModInfo`

Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*defined at classes.py:1945*


    `tree`: List of Lists of VM code
    `srcfile`: source of code
    returns Closure in __modinfo.module initial scope
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*defined at classes.py:677*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `load_vmx (this, fname)`
*defined at classes.py:1939*

#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Module`

Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Null`

Built-on Class of `null` value

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1673*


    to_string/repr method for Null Class: returns "null"
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this, ...args)`
*defined at classes.py:1680*


    "(" method for `null` value (fatal error)
    commonly happens when a bad method name is used
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Number`

Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (obj, value)`
*defined at classes.py:1437*


    initialize Number from Str value
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1048*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
#### `- (x)`
*defined at classes.py:1327*


    Return negative of `x`
    
#### `~ (this)`
*defined at classes.py:1482*


    return bitwise (binary) "not" (complement) of `this`
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1396*


    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `& (l, r)`
*defined at classes.py:1456*


    return bitwise (binary) "and" (conjunction) of `l` and `r`
    
#### `( (l, ...args)`
*defined at classes.py:900*


    default Object '(' binop
    (fatal error)
    
#### `* (l, r)`
*defined at classes.py:1358*


    multiple `l` and `r`
    
#### `+ (l, r)`
*defined at classes.py:1334*


    add `l` and `r`
    
#### `- (l, r)`
*defined at classes.py:1347*


    subtract `r` from `l`
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `/ (l, r)`
*defined at classes.py:1371*


    divide `l` by `r`
    
#### `< (l, r)`
*defined at classes.py:1413*


    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`
*defined at classes.py:1423*


    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`
*defined at classes.py:1389*


    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`
*defined at classes.py:1430*


    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`
*defined at classes.py:1406*


    return `true` if value of `l` is >= the value of `r`
    
#### `| (l, r)`
*defined at classes.py:1469*


    return bitwise (binary) "or" (union) of `l` and `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Object`

Base Class

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*defined at classes.py:677*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (l, ...args)`
*defined at classes.py:900*


    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PClass`

Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*defined at classes.py:1018*


    'create' method for PClass metaclass
    makes an instance of this_class backed by a CPObject
    used to create PClass subclass objects (Number, List, Dict, Bool, Null)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PObject`

Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1048*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (l, ...args)`
*defined at classes.py:900*


    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyFunc`

Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterable`


    Wrapper for Python 'iterable' Objects
    (classes which can generate iterators)
    returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), PyIterable.range(),
    

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*defined at classes.py:1131*


    return forward iterator
    
#### `map (this, func)`
*defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1048*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*defined at classes.py:1138*


    return reverse iterator
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `sorted (this)`
*defined at classes.py:1146*


    return sorted list values (or keys)
    
#### `to_str (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterator`

Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*defined at classes.py:677*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*defined at classes.py:1795*


    Python iterators are also iterables (return self)
    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method:

    Return the iterator object itself. This is required to allow
    both containers and iterators to be used with the for and in
    statements. This method corresponds to the tp_iter slot of the
    type structure for Python objects in the Python/C API.
    
#### `next (this, finished_continuation)`
*defined at classes.py:1809*


    `finished` should be a CContinuation
    (eg; block leave label or "return")
    to call when iterator exhausted
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyObject`


    Built-in Class for a wrapper around an arbitrary Python Object
    (returned by pyimport, or operations on PyObjects)
    

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this, ...args)`
*defined at classes.py:1774*

#### `. (l, r)`
*defined at classes.py:1749*


    PyObject "." binop -- proxies to Python object getattr
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `[ (l, r)`
*defined at classes.py:1766*


    PyObject "[" binop
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyVMFunc`


   Built-in Class for function implemented in Python
   with access to VM internals
   

### Methods

#### `create (this_class, ...args)`
*defined at classes.py:669*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*defined at classes.py:951*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:703*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*defined at classes.py:711*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*defined at classes.py:991*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*defined at classes.py:725*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*defined at classes.py:718*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Str`

Built-in immutable Unicode string Class

### Methods

#### `delprop (this, name)`
*defined at classes.py:748*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `ends_with (this, suff)`
*defined at classes.py:1566*


    Return `true` if `this` ends with the suffix `suff`, `false` otherwise.
    
#### `for_each (this, func)`
*defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*defined at classes.py:886*


    return Class for `this`
    
#### `getprop (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*defined at classes.py:1063*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*defined at classes.py:1071*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*defined at classes.py:908*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*defined at classes.py:1131*


    return forward iterator
    
#### `join (this, arg)`
*defined at classes.py:1573*


    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
#### `len (this)`
*defined at classes.py:1033*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `ord (this)`
*defined at classes.py:1586*


    Return the Unicode code point for a one-character string `this`
    
#### `props (this)`
*defined at classes.py:695*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*defined at classes.py:757*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*defined at classes.py:1048*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*defined at classes.py:1056*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*defined at classes.py:1138*


    return reverse iterator
    
#### `setclass (this, klass)`
*defined at classes.py:893*


    set Class for `this`!!
    
#### `slice (this, start, end)`
*defined at classes.py:1537*


    return a substring (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to rest of string
    
#### `sorted (this)`
*defined at classes.py:1146*


    return sorted list values (or keys)
    
#### `split (this, sep, limit)`
*defined at classes.py:1552*


    Return a List of the words in the string,
    using sep as the delimiter string (default to `null` -- any whitespace).
    Limit to `limit` return values (defaults to -1 -- no limit)
    
#### `starts_with (this, pref)`
*defined at classes.py:1596*


    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    
#### `strip (this)`
*defined at classes.py:1610*


    Return a copy of the string with leading and trailing whitespace removed.
    
#### `to_float (this)`
*defined at classes.py:1617*


    Convert string to a floating point Number
    
#### `to_int (this, base)`
*defined at classes.py:1624*


    Convert string to integer Number
    `base` defaults to zero (accept 0xXXX for base 16)
    
#### `to_str (this)`
*defined at classes.py:1603*


    Identity method
    
### Unary operators

#### `! (x)`
*defined at classes.py:740*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*defined at classes.py:1396*


    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`
*defined at classes.py:1090*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*defined at classes.py:982*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `+ (x, y)`
*defined at classes.py:1515*


    String concatenation
    
#### `. (l, r)`
*defined at classes.py:829*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*defined at classes.py:876*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `< (l, r)`
*defined at classes.py:1413*


    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`
*defined at classes.py:1423*


    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`
*defined at classes.py:1389*


    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`
*defined at classes.py:1079*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`
*defined at classes.py:1430*


    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`
*defined at classes.py:1406*


    return `true` if value of `l` is >= the value of `r`
    
#### `[ (l, r)`
*defined at classes.py:1528*


    Str l[r]
    return `r`'th character of Str `l`
    
### LHS Binary operators

#### `. (l, r, value)`
*defined at classes.py:757*


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
