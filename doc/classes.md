# Module `classes`

## Class `Bool` subclass of `PObject`


> Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1749*

> return Str representation: "true" or "false"

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Bool`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `BoundMethod` subclass of `Callable`


> Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `BoundMethod`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Callable` subclass of `Object`


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Callable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Class` subclass of `Object`


> Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Class`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Closure` subclass of `Callable`


> Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Closure`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Continuation` subclass of `Callable`


> Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Continuation`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Dict` subclass of `Iterable`


> Built-in dictionary mapping Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:127:38*

> init method for Dict: takes Iterable returning two-item lists, OR an Iterable returning keys, and implementing '['

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `items (this)`
*PyFunc at classes.py:1256*

> return Iterable for [key, value] value pairs

#### `iter (this)`
*PyFunc at classes.py:1161*

> return forward iterator

#### `keys (this)`
*PyFunc at classes.py:1263*

> return Iterable for Dict keys

#### `len (this)`
*PyFunc at classes.py:1054*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `pop (obj, arg)`
*PyFunc at classes.py:1249*

> remove Dict with specified key

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*Closure at bootstrap.xxl:153:38*

> return representation of Dict

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1168*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1176*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

#### `values (this)`
*PyFunc at classes.py:1270*

> return Iterable for Dict values

### Members

#### `name`

> Value: `Dict`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1231*

> get entry `r` Dict from dict `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1222*

> put `value` into Dict `l` index `r`

## Class `Iterable` subclass of `PObject`


> Virtual base Class classes that can be iterated over

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1161*

> return forward iterator

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1069*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1168*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1176*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Iterable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `List` subclass of `Iterable`


> Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc at classes.py:1303*

> append `item` to `this` List

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `extend (this, iterable)`
*Closure at bootstrap.xxl:188:40*

> 

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:169:38*

> init method for List: takes Iterable

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1161*

> return forward iterator

#### `len (this)`
*PyFunc at classes.py:1054*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `pop (l, index)`
*PyFunc at classes.py:1311*

> Remove and return List item at `index` (default last)

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*Closure at bootstrap.xxl:181:38*

> return represtation of List

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1168*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1176*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `List`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1320*

> Return List item at index `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1328*

> Set List item at index `r` to `value`

## Class `ModInfo` subclass of `Object`


> Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc at classes.py:1992*

> `tree`: List of Lists of VM code `srcfile`: source of code returns Closure in __modinfo.module initial scope

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `load_vmx (this, fname)`
*PyFunc at classes.py:1986*

> 

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `ModInfo`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Module` subclass of `Object`


> Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `modules`

> Value: `{'classes': <Module>, 'doc.xxl': <Module>, 'parser.vmx': <Module>, 'markup.xxl': <Module>}`

#### `name`

> Value: `Module`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Null` subclass of `PObject`


> Built-on Class of `null` value

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1724*

> to_string/repr method for Null Class: returns "null"

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Null`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this, ...args)`
*PyFunc at classes.py:1731*

> `(` method for `null` value (fatal error) commonly happens when a bad method name is used

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Number` subclass of `PObject`


> Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:199:26*

> Return a `Number` object with value `x` NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1069*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_float (this)`
*PyFunc at classes.py:1500*

> If value is a float, return `this` If value is an int, return a new Number object

#### `to_int (this)`
*PyFunc at classes.py:1510*

> If value is an int, return `this` If value is a float, return a new Number object

#### `to_number (this)`
*PyFunc at classes.py:1520*

> identity method; returns `this`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Number`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

#### `- (x)`
*PyFunc at classes.py:1357*

> Return negative of `x`

#### `~ (this)`
*PyFunc at classes.py:1493*

> return bitwise (binary) "not" (complement) of `this`

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1426*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `& (l, r)`
*PyFunc at classes.py:1467*

> return bitwise (binary) "and" (conjunction) of `l` and `r`

#### `( (l, ...args)`
*PyFunc at classes.py:921*

> default Object `(` binop (fatal error)

#### `* (l, r)`
*PyFunc at classes.py:1388*

> multiple `l` and `r`

#### `+ (l, r)`
*PyFunc at classes.py:1364*

> add `l` and `r`

#### `- (l, r)`
*PyFunc at classes.py:1377*

> subtract `r` from `l`

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `/ (l, r)`
*PyFunc at classes.py:1401*

> divide `l` by `r`

#### `< (l, r)`
*PyFunc at classes.py:1443*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1453*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1419*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1460*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1436*

> return `true` if value of `l` is >= the value of `r`

#### `| (l, r)`
*PyFunc at classes.py:1480*

> return bitwise (binary) "or" (union) of `l` and `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Object` subclass of `Object`


> Base Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `Object`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (l, ...args)`
*PyFunc at classes.py:921*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PClass` subclass of `Class`


> Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc at classes.py:1039*

> 'create' method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PClass`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PObject` subclass of `Object`


> Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1069*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PObject`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (l, ...args)`
*PyFunc at classes.py:921*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyFunc` subclass of `Callable`


> Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PyFunc`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyIterable` subclass of `Iterable`


> Wrapper for Python 'iterable' Objects (classes which can generate iterators) returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), PyIterable.range(),

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1161*

> return forward iterator

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1197*

> return an Iterable for an integer range (an Iterable can be iterated over any number of times) range(10): returns Iterable for 0..9 range(1,10): returns Iterable for 1..9 range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1069*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1168*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1176*

> return sorted list values (or keys)

#### `to_str (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

### Members

#### `name`

> Value: `PyIterable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyIterator` subclass of `Object`


> Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1846*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

#### `next (this, finished_continuation)`
*PyFunc at classes.py:1856*

> `finished` should be a CContinuation (eg; block leave label or "return") to call when iterator exhausted

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PyIterator`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyObject` subclass of `Object`


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PyObject`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this, ...args)`
*PyFunc at classes.py:1825*

> 

#### `. (l, r)`
*PyFunc at classes.py:1800*

> PyObject "." binop -- proxies to Python object getattr

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `[ (l, r)`
*PyFunc at classes.py:1817*

> PyObject "[" binop

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyVMFunc` subclass of `Callable`


> Built-in Class for function implemented in Python with access to VM internals

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:972*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> default metaclass (Class) new method manually invoked as SomeClass.new calls this_class.create to create obj and then calls obj.init()

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:718*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:726*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1012*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

#### `name`

> Value: `PyVMFunc`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:740*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Str` subclass of `Iterable`


> Built-in immutable Unicode string Class

### Methods

#### `chr (i)`
*PyFunc at classes.py:1687*

> Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `ends_with (this, suff)`
*PyFunc at classes.py:1606*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:907*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1084*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:929*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1161*

> return forward iterator

#### `join (this, iterable)`
*Closure at bootstrap.xxl:210:37*

> 

#### `len (this)`
*PyFunc at classes.py:1054*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `ord (this)`
*PyFunc at classes.py:1626*

> Return the Unicode code point for a one-character string `this`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1069*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1077*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1168*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:914*

> set Class for `this`!!

#### `slice (this, start, end)`
*PyFunc at classes.py:1577*

> return a substring (slice) of `this` starting at position `start` ending at position `end` (defaults to rest of string

#### `sorted (this)`
*PyFunc at classes.py:1176*

> return sorted list values (or keys)

#### `split (this, sep, limit)`
*PyFunc at classes.py:1592*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

#### `starts_with (this, pref)`
*PyFunc at classes.py:1636*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

#### `strip (this)`
*PyFunc at classes.py:1650*

> Return a copy of the string with leading and trailing whitespace removed.

#### `to_float (this)`
*PyFunc at classes.py:1657*

> Convert string to a floating point Number

#### `to_int (this, base)`
*PyFunc at classes.py:1664*

> Convert string to integer Number `base` defaults to zero (accept 0xXXX for base 16)

#### `to_number (this)`
*PyFunc at classes.py:1676*

> Convert string to a Number

#### `to_str (this)`
*PyFunc at classes.py:1643*

> Identity method

### Members

#### `name`

> Value: `Str`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1426*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1111*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1003*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `+ (x, y)`
*PyFunc at classes.py:1555*

> String concatenation

#### `. (l, r)`
*PyFunc at classes.py:850*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:897*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `< (l, r)`
*PyFunc at classes.py:1443*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1453*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1419*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1100*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1460*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1436*

> return `true` if value of `l` is >= the value of `r`

#### `[ (l, r)`
*PyFunc at classes.py:1568*

> Str l[r] return `r`'th character of Str `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Variables

### `false`

> Value: `false`


### `null`

> Value: `null`


### `true`

> Value: `true`


---
formatted by doc.xxl on 2021-06-17
