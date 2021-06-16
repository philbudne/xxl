# `classes` Module

## Class `Bool`

Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1743*


    return Str representation: "true" or "false"
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `BoundMethod`

Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Callable`


    Virtual base Class for built-in callable classes
    (BoundMethod, Continuation, PyFunc, PyVMFunc)
    

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*PyFunc defined at classes.py:692*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Class`

Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Closure`

Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Continuation`

Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Dict`

Built-in dictionary mapping Class

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*Closure defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*Closure defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`
*Closure defined at bootstrap.xxl:127:38*


	init method for Dict: takes Iterable returning two-item lists,
	OR an Iterable returning keys, and implementing '['
	
#### `init0 (obj)`
*PyFunc defined at classes.py:1234*


    called by Dict.init (in bootstrap.xxl)
    Dodges needing private metaclass for Dict
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `items (this)`
*PyFunc defined at classes.py:1250*


    return Iterable for [key, value] value pairs
    
#### `iter (this)`
*PyFunc defined at classes.py:1155*


    return forward iterator
    
#### `keys (this)`
*PyFunc defined at classes.py:1257*


    return Iterable for Dict keys
    
#### `len (this)`
*PyFunc defined at classes.py:1048*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*Closure defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*Closure defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (obj, arg)`
*PyFunc defined at classes.py:1243*


    remove Dict with specified key
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*Closure defined at bootstrap.xxl:154:38*


	return representation of Dict
	
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*PyFunc defined at classes.py:1162*


    return reverse iterator
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `sorted (this)`
*PyFunc defined at classes.py:1170*


    return sorted list values (or keys)
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
#### `values (this)`
*PyFunc defined at classes.py:1264*


    return Iterable for Dict values
    
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`
*PyFunc defined at classes.py:1225*


    get entry `r` Dict from dict `l`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`
*PyFunc defined at classes.py:1216*


    put `value` into Dict `l` index `r`
    
## Class `Iterable`

Virtual base Class classes that can be iterated over

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*Closure defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*Closure defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*PyFunc defined at classes.py:1155*


    return forward iterator
    
#### `map (this, func)`
*Closure defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*Closure defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1063*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*PyFunc defined at classes.py:1162*


    return reverse iterator
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `sorted (this)`
*PyFunc defined at classes.py:1170*


    return sorted list values (or keys)
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `List`

Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc defined at classes.py:1297*


    append `item` to `this` List
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*Closure defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `extend (this, iterable)`
*Closure defined at bootstrap.xxl:190:40*

#### `for_each (this, func)`
*Closure defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this, arg)`
*Closure defined at bootstrap.xxl:170:38*


	init method for List: takes Iterable
	
#### `init0 (l)`
*PyFunc defined at classes.py:1288*


    called by List.init (in bootstrap.xxl)
    Dodges needing private metaclass for List
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*PyFunc defined at classes.py:1155*


    return forward iterator
    
#### `len (this)`
*PyFunc defined at classes.py:1048*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*Closure defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*Closure defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `pop (l, index)`
*PyFunc defined at classes.py:1305*


    Remove and return List item at `index` (default last)
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*Closure defined at bootstrap.xxl:183:38*


	return represtation of List
	
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*PyFunc defined at classes.py:1162*


    return reverse iterator
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `sorted (this)`
*PyFunc defined at classes.py:1170*


    return sorted list values (or keys)
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `[ (l, r)`
*PyFunc defined at classes.py:1314*


    Return List item at index `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `[ (l, r, value)`
*PyFunc defined at classes.py:1322*


    Set List item at index `r` to `value`
    
## Class `ModInfo`

Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc defined at classes.py:1990*


    `tree`: List of Lists of VM code
    `srcfile`: source of code
    returns Closure in __modinfo.module initial scope
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*PyFunc defined at classes.py:692*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `load_vmx (this, fname)`
*PyFunc defined at classes.py:1984*

#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Module`

Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Null`

Built-on Class of `null` value

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1718*


    to_string/repr method for Null Class: returns "null"
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this, ...args)`
*PyFunc defined at classes.py:1725*


    "(" method for `null` value (fatal error)
    commonly happens when a bad method name is used
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Number`

Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1063*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_float (this)`
*PyFunc defined at classes.py:1494*


    If value is a float, return `this`
    If value is an int, return a new Number object
    
#### `to_int (this)`
*PyFunc defined at classes.py:1504*


    If value is an int, return `this`
    If value is a float, return a new Number object
    
#### `to_number (this)`
*PyFunc defined at classes.py:1514*


    identity method; returns `this`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
#### `- (x)`
*PyFunc defined at classes.py:1351*


    Return negative of `x`
    
#### `~ (this)`
*PyFunc defined at classes.py:1487*


    return bitwise (binary) "not" (complement) of `this`
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1420*


    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `& (l, r)`
*PyFunc defined at classes.py:1461*


    return bitwise (binary) "and" (conjunction) of `l` and `r`
    
#### `( (l, ...args)`
*PyFunc defined at classes.py:915*


    default Object '(' binop
    (fatal error)
    
#### `* (l, r)`
*PyFunc defined at classes.py:1382*


    multiple `l` and `r`
    
#### `+ (l, r)`
*PyFunc defined at classes.py:1358*


    add `l` and `r`
    
#### `- (l, r)`
*PyFunc defined at classes.py:1371*


    subtract `r` from `l`
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `/ (l, r)`
*PyFunc defined at classes.py:1395*


    divide `l` by `r`
    
#### `< (l, r)`
*PyFunc defined at classes.py:1437*


    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`
*PyFunc defined at classes.py:1447*


    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1413*


    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`
*PyFunc defined at classes.py:1454*


    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`
*PyFunc defined at classes.py:1430*


    return `true` if value of `l` is >= the value of `r`
    
#### `| (l, r)`
*PyFunc defined at classes.py:1474*


    return bitwise (binary) "or" (union) of `l` and `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Object`

Base Class

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*PyFunc defined at classes.py:692*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (l, ...args)`
*PyFunc defined at classes.py:915*


    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PClass`

Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc defined at classes.py:1033*


    'create' method for PClass metaclass
    makes an instance of this_class backed by a CPObject
    used to create PClass subclass objects (Number, List, Dict, Bool, Null)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PObject`

Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1063*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (l, ...args)`
*PyFunc defined at classes.py:915*


    default Object '(' binop
    (fatal error)
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyFunc`

Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterable`


    Wrapper for Python 'iterable' Objects
    (classes which can generate iterators)
    returned by Dict.items(), Dict.keys(), Dict.values(),
    Object.props(), PyIterable.range(),
    

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*Closure defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `for_each (this, func)`
*Closure defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*PyFunc defined at classes.py:1155*


    return forward iterator
    
#### `map (this, func)`
*Closure defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*Closure defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1063*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*PyFunc defined at classes.py:1162*


    return reverse iterator
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `sorted (this)`
*PyFunc defined at classes.py:1170*


    return sorted list values (or keys)
    
#### `to_str (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyIterator`

Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_obj, ...args)`
*PyFunc defined at classes.py:692*


    default init method for Object class
    a fatal error if any arguments given
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*PyFunc defined at classes.py:1840*


    Python iterators are also iterables (return self)
    https://docs.python.org/3/library/stdtypes.html#typeiter says
    an iterator should have an __iter__ method:

    Return the iterator object itself. This is required to allow
    both containers and iterators to be used with the for and in
    statements. This method corresponds to the tp_iter slot of the
    type structure for Python objects in the Python/C API.
    
#### `next (this, finished_continuation)`
*PyFunc defined at classes.py:1854*


    `finished` should be a CContinuation
    (eg; block leave label or "return")
    to call when iterator exhausted
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyObject`


    Built-in Class for a wrapper around an arbitrary Python Object
    (returned by pyimport, or operations on PyObjects)
    

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this, ...args)`
*PyFunc defined at classes.py:1819*

#### `. (l, r)`
*PyFunc defined at classes.py:1794*


    PyObject "." binop -- proxies to Python object getattr
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `[ (l, r)`
*PyFunc defined at classes.py:1811*


    PyObject "[" binop
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `PyVMFunc`


   Built-in Class for function implemented in Python
   with access to VM internals
   

### Methods

#### `create (this_class, ...args)`
*PyFunc defined at classes.py:684*


    default create method for Object (and therefore Class)
    makes an instance of this_class (called from default Object.new)
    
#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (this_class, props)`
*PyFunc defined at classes.py:966*


    init method for meta-class "Class" -- used to create new Classes
    `props` is Dict holding properties (see const.CLASS_PROPS)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `new (this_class, ...args)`
*Closure defined at bootstrap.xxl:56:38*


	default metaclass (Class) new method
	manually invoked as SomeClass.new
	calls this_class.create to create obj
	and then calls obj.init()
	
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:718*


    Default Object string representation method
    (calls Python repr(this))
    
#### `reprx (l)`
*PyFunc defined at classes.py:726*


    for debug: show Class, and Python value (which may include id?)
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `subclass_of (this, c)`
*PyFunc defined at classes.py:1006*


    return `true` if Class `this` is a subclass of
    Class (or List of Classes) `c`
    
#### `to_str (this)`
*Closure defined at bootstrap.xxl:45:42*


	default to_str method: calls this.repr
	
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `!== (l, r)`
*PyFunc defined at classes.py:740*


    Test if `l` and `r` refer to different Objects
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
#### `=== (l, r)`
*PyFunc defined at classes.py:733*


    Test if `l` and `r` refer to the same Object
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
## Class `Str`

Built-in immutable Unicode string Class

### Methods

#### `delprop (this, name)`
*PyFunc defined at classes.py:763*


    Delete property `name` from Object `this`
    (only effects `this` -- never Class or superclasses)
    
#### `each_for (this, func)`
*Closure defined at bootstrap.xxl:83:38*


	call `func` argument for each reverse iterator item
	
#### `ends_with (this, suff)`
*PyFunc defined at classes.py:1600*


    Return `true` if `this` ends with the suffix `suff`, `false` otherwise.
    
#### `for_each (this, func)`
*Closure defined at bootstrap.xxl:73:38*


	call `func` argument for each iterator item
	
#### `getclass (this)`
*PyFunc defined at classes.py:901*


    return Class for `this`
    
#### `getprop (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `init (l, value)`
*PyFunc defined at classes.py:1078*


    default PObject init method
    (fatal error)
    
#### `init0 (l, value)`
*PyFunc defined at classes.py:1086*


    default PObject init0 method
    (fatal error)
    
#### `instance_of (this, c)`
*PyFunc defined at classes.py:923*


    return `true` if Object `l` is an instance of
    Class (or List of Classes) `c`
    
#### `iter (this)`
*PyFunc defined at classes.py:1155*


    return forward iterator
    
#### `join (this, arg)`
*PyFunc defined at classes.py:1607*


    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
#### `len (this)`
*PyFunc defined at classes.py:1048*


    returns length (of String, List or Dict)
    
#### `map (this, func)`
*Closure defined at bootstrap.xxl:93:33*


	return List of results of `func` passed each iterator item
	
#### `map2 (this, func, ignore)`
*Closure defined at bootstrap.xxl:107:34*


	return List of results of `func` passed each iterator item,
	ignore any returns with value `ignore` (defaults to `null`)
	
#### `ord (this)`
*PyFunc defined at classes.py:1620*


    Return the Unicode code point for a one-character string `this`
    
#### `props (this)`
*PyFunc defined at classes.py:710*


    returns an Iterable for (String) property names
    of `this` Object
    
#### `putprop (l, r, value)`
*PyFunc defined at classes.py:772*


    Object putprop method/operator
    store `value` as `r` (String) property of object `l`
    
#### `repr (this)`
*PyFunc defined at classes.py:1063*


    return less human-friendly string representation of `this`
    (use Python repr function on value)
    
#### `reprx (this)`
*PyFunc defined at classes.py:1071*


    for debug: show Class name, and Python repr
    
#### `reversed (this)`
*PyFunc defined at classes.py:1162*


    return reverse iterator
    
#### `setclass (this, klass)`
*PyFunc defined at classes.py:908*


    set Class for `this`!!
    
#### `slice (this, start, end)`
*PyFunc defined at classes.py:1571*


    return a substring (slice) of `this`
    starting at position `start`
    ending at position `end` (defaults to rest of string
    
#### `sorted (this)`
*PyFunc defined at classes.py:1170*


    return sorted list values (or keys)
    
#### `split (this, sep, limit)`
*PyFunc defined at classes.py:1586*


    Return a List of the words in the string,
    using sep as the delimiter string (default to `null` -- any whitespace).
    Limit to `limit` return values (defaults to -1 -- no limit)
    
#### `starts_with (this, pref)`
*PyFunc defined at classes.py:1630*


    Return `true` if `this` starts with prefix `pref, `false` otherwise.
    
#### `strip (this)`
*PyFunc defined at classes.py:1644*


    Return a copy of the string with leading and trailing whitespace removed.
    
#### `to_float (this)`
*PyFunc defined at classes.py:1651*


    Convert string to a floating point Number
    
#### `to_int (this, base)`
*PyFunc defined at classes.py:1658*


    Convert string to integer Number
    `base` defaults to zero (accept 0xXXX for base 16)
    
#### `to_number (this)`
*PyFunc defined at classes.py:1670*


    Convert string to a Number
    
#### `to_str (this)`
*PyFunc defined at classes.py:1637*


    Identity method
    
### Unary operators

#### `! (x)`
*PyFunc defined at classes.py:755*


    Object unary logical "not" operator; returns `true` if `x` is "falsey"
    (false, null, or zero)
    
### Binary operators

#### `!= (l, r)`
*PyFunc defined at classes.py:1420*


    return `true` if value of `l` is different from the value of `r`
    
#### `!== (l, r)`
*PyFunc defined at classes.py:1105*


    Check if value of PObject `l`
    is not the same Python Object
    as value of PObject `r`
    
#### `( (this_class, ...args)`
*PyFunc defined at classes.py:997*


    "(" binop for Class -- fatal error
    (but common mistake if you have Python fingers)
    tells you to use .new method!!
    
#### `+ (x, y)`
*PyFunc defined at classes.py:1549*


    String concatenation
    
#### `. (l, r)`
*PyFunc defined at classes.py:844*


    Object getprop method/operator
    return `r` (String) property of object `l`
    
#### `.. (this, prop)`
*PyFunc defined at classes.py:891*


    Object ".." operator; for calling superclass methods
    looks for `prop` as property or method of superclasses of `this`
    
#### `< (l, r)`
*PyFunc defined at classes.py:1437*


    return `true` if value of `l` is < the value of `r`
    
#### `<= (l, r)`
*PyFunc defined at classes.py:1447*


    return `true` if value of `l` is <= the value of `r`
    
#### `== (l, r)`
*PyFunc defined at classes.py:1413*


    return `true` if value of `l` is the same as value of `r`
    
#### `=== (l, r)`
*PyFunc defined at classes.py:1094*


    Check if value of PObject `l`
    is the same Python Object
    as value of PObject `r`
    
#### `> (l, r)`
*PyFunc defined at classes.py:1454*


    return `true` if value of `l` is > the value of `r`
    
#### `>= (l, r)`
*PyFunc defined at classes.py:1430*


    return `true` if value of `l` is >= the value of `r`
    
#### `[ (l, r)`
*PyFunc defined at classes.py:1562*


    Str l[r]
    return `r`'th character of Str `l`
    
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc defined at classes.py:772*


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
