# Module `classes`


> Built-in Classes for XXL

---
## Class `Bool` subclass of `PObject`


> Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:71:24*

> Return truthiness of `x` (as Bool). NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1775*

> return Str representation: "true" or "false"

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Bool`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `BoundMethod` subclass of `Callable`


> Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `BoundMethod`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Callable` subclass of `Object`


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:705*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Callable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Class` subclass of `Object`


> Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Class`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Closure` subclass of `Callable`


> Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Closure`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Continuation` subclass of `Callable`


> Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Continuation`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Dict` subclass of `PyIterable`


> Built-in dictionary mapping Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:158:38*

> init method for Dict: takes Iterable returning two-item lists, OR an Iterable returning keys, and implementing '['

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `items (this)`
*PyFunc at classes.py:1281*

> Return PyIterable for [key, value] value pairs.

#### `iter (this)`
*PyFunc at classes.py:1189*

> Return forward iterator.

#### `keys (this)`
*PyFunc at classes.py:1288*

> Return PyIterable for Dict keys.

#### `len (this)`
*PyFunc at classes.py:1063*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `pop (obj, key)`
*PyFunc at classes.py:1274*

> Remove Dict item with specified `key`.

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1221*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*Closure at bootstrap.xxl:184:38*

> return representation of Dict

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1196*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1205*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

#### `values (this)`
*PyFunc at classes.py:1295*

> Return PyIterable for Dict values.

### Members

#### `name`

> Value: `Dict`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1256*

> `l[r]`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1247*

> `l[r] = value`

---
## Class `Iterable` subclass of `Object`


> Mixin for Classes that can be iterated over

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:705*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `reversed (this)`
*Closure at bootstrap.xxl:138:46*

> Creates List from `this`, returns reverse PyIterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:146:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Iterable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `List` subclass of `PyIterable`


> Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc at classes.py:1328*

> append `item`.

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `extend (this, iterable)`
*Closure at bootstrap.xxl:219:40*

> Create an iterator from `iterable` and iterate appending values to `this` returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:200:38*

> init method for List: takes Iterable

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1189*

> Return forward iterator.

#### `len (this)`
*PyFunc at classes.py:1063*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `pop (l, index)`
*PyFunc at classes.py:1336*

> Remove and return item at `index` (default last).

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1221*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*Closure at bootstrap.xxl:212:38*

> return representation of List

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1196*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1205*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `List`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1345*

> `l[r]`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1353*

> `l[r] = value`

---
## Class `ModInfo` subclass of `Object`


> Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc at classes.py:2030*

> Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:705*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `load_vmx (this, fname)`
*PyFunc at classes.py:2020*

> Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `ModInfo`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Module` subclass of `Object`


> Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `modules`

> Value: `{'classes': <Module>, 'doc.xxl': <Module>, 'parser.vmx': <Module>, 'markup.xxl': <Module>}`

#### `name`

> Value: `Module`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Null` subclass of `PObject`


> Built-in Class of `null` value

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:234:24*

> Return `null` value NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1749*

> to_string/repr method for Null Class: returns "null"

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Null`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this, ...args)`
*PyFunc at classes.py:1756*

> `(` method for `null` value (fatal error) commonly happens when a bad method name is used, so output a "helpful" message.

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Number` subclass of `PObject`


> Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:245:26*

> Convert `x` to a `Number` NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1078*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_float (this)`
*PyFunc at classes.py:1525*

> If value is a float, return `this` If value is an int, return a new Number object

#### `to_int (this)`
*PyFunc at classes.py:1535*

> If value is an int, return `this` If value is a float, return a new Number object

#### `to_number (this)`
*PyFunc at classes.py:1545*

> identity method; returns `this`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Number`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

#### `- (x)`
*PyFunc at classes.py:1382*

> Return negative of `x`

#### `~ (this)`
*PyFunc at classes.py:1518*

> return bitwise (binary) "not" (complement) of `this`

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1451*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `& (l, r)`
*PyFunc at classes.py:1492*

> return bitwise (binary) "and" (conjunction) of `l` and `r`

#### `( (l, ...args)`
*PyFunc at classes.py:930*

> default Object `(` binop (fatal error)

#### `* (l, r)`
*PyFunc at classes.py:1413*

> multiply `l` and `r`

#### `+ (l, r)`
*PyFunc at classes.py:1389*

> add `l` and `r`

#### `- (l, r)`
*PyFunc at classes.py:1402*

> subtract `r` from `l`

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `/ (l, r)`
*PyFunc at classes.py:1426*

> Divide `l` by `r`; always creates float.

#### `< (l, r)`
*PyFunc at classes.py:1468*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1478*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1444*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1485*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1461*

> return `true` if value of `l` is >= the value of `r`

#### `| (l, r)`
*PyFunc at classes.py:1505*

> return bitwise (binary) "or" (union) of `l` and `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Object` subclass of `Object`


> Base Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:705*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `Object`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (l, ...args)`
*PyFunc at classes.py:930*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PClass` subclass of `Class`


> Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc at classes.py:1048*

> 'create' method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PClass`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PObject` subclass of `Object`


> Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1078*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PObject`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (l, ...args)`
*PyFunc at classes.py:930*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyFunc` subclass of `Callable`


> Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PyFunc`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyIterable` subclass of `PObject,Iterable`


> Wrapper for Python 'iterable' Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1189*

> Return forward iterator.

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1221*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1078*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1196*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1205*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PyIterable`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyIterator` subclass of `Object,Iterable`


> Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:705*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1880*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `next (this, finished_continuation)`
*PyFunc at classes.py:1890*

> `finished` should be a CContinuation (eg; block leave label or "return") to call when iterator exhausted

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `reversed (this)`
*Closure at bootstrap.xxl:138:46*

> Creates List from `this`, returns reverse PyIterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:146:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PyIterator`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyObject` subclass of `Object`


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:1843*

> return dir() of wrapped Python object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PyObject`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this, ...args)`
*PyFunc at classes.py:1858*

> 

#### `. (l, r)`
*PyFunc at classes.py:1826*

> PyObject `.` binop -- proxies to Python object getattr

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `[ (l, r)`
*PyFunc at classes.py:1850*

> PyObject `[` binop

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyVMFunc` subclass of `Callable`


> Built-in Class for function implemented in Python with access to VM internals

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:56:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `PyVMFunc`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `SingletonClass` subclass of `Class`


> Metaclass for Classes with singleton values

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:697*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:981*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:258:47*

> SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:731*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:739*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1021*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> Default to_str method: calls this.repr().

### Members

#### `name`

> Value: `SingletonClass`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:753*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:746*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Str` subclass of `PyIterable`


> Built-in immutable Unicode string Class

### Methods

#### `chr (i)`
*PyFunc at classes.py:1712*

> Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff

#### `delprop (this, name)`
*PyFunc at classes.py:776*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:95:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `ends_with (this, suff)`
*PyFunc at classes.py:1631*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

#### `for_each (this, func)`
*Closure at bootstrap.xxl:85:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:916*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1093*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:938*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1189*

> Return forward iterator.

#### `join (this, iterable)`
*Closure at bootstrap.xxl:276:37*

> 

#### `len (this)`
*PyFunc at classes.py:1063*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:106:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:121:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `new (arg)`
*Closure at bootstrap.xxl:289:23*

> Str Class new (static) method; calls arg.to_str method

#### `ord (this)`
*PyFunc at classes.py:1651*

> Return the Unicode code point for a one-character string `this`

#### `props (this)`
*PyFunc at classes.py:723*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1221*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1078*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1086*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1196*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:923*

> set Class for `this`!!

#### `slice (this, start, end)`
*PyFunc at classes.py:1602*

> return a substring (slice) of `this` starting at position `start` ending at position `end` (defaults to rest of string

#### `sorted (this, reverse)`
*PyFunc at classes.py:1205*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `split (this, sep, limit)`
*PyFunc at classes.py:1617*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

#### `starts_with (this, pref)`
*PyFunc at classes.py:1661*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

#### `strip (this)`
*PyFunc at classes.py:1675*

> Return a copy of the string with leading and trailing whitespace removed.

#### `to_float (this)`
*PyFunc at classes.py:1682*

> Convert string to a floating point Number

#### `to_int (this, base)`
*PyFunc at classes.py:1689*

> Convert string to integer Number `base` defaults to zero (accept 0xXXX for base 16)

#### `to_number (this)`
*PyFunc at classes.py:1701*

> Convert string to a Number

#### `to_str (this)`
*PyFunc at classes.py:1668*

> Identity method

### Members

#### `name`

> Value: `Str`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:768*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1451*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1120*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1012*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `+ (x, y)`
*PyFunc at classes.py:1580*

> String concatenation

#### `. (l, r)`
*PyFunc at classes.py:859*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:906*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `< (l, r)`
*PyFunc at classes.py:1468*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1478*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1444*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1109*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1485*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1461*

> return `true` if value of `l` is >= the value of `r`

#### `[ (l, r)`
*PyFunc at classes.py:1593*

> Str l[r] return `r`'th character of Str `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:785*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Variables

### `false`

> Value: `false`


### `null`

> Value: `null`


### `true`

> Value: `true`


---
formatted by doc.xxl on 2021-06-19
