# Module `classes`


> Built-in Classes for XXL

---
## PClass `Bool` subclass of `PObject`


> Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:82:24*

> Return truthiness of `x` (as Bool). NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1844 (bool_str)*

> return Str representation: "true" or "false"

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Bool'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `BoundMethod` subclass of `Callable`


> Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'BoundMethod'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Callable` subclass of `Object`


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Callable'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Class` subclass of `Object`


> Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Class'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Closure` subclass of `Callable`


> Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Closure'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Continuation` subclass of `Callable`


> Built-in Class for a Continuation

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Continuation'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `Dict` subclass of `PyIterable`


> Built-in dictionary mapping Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:176:38*

> init method for Dict: takes Iterable returning two-item lists, OR an Iterable returning keys, and implementing '['

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `items (this)`
*PyFunc at classes.py:1326 (dict_items)*

> Return PyIterable for [key, value] value pairs.

#### `iter (this)`
*PyFunc at classes.py:1235 (pyiterable_iter)*

> Return forward iterator.

#### `keys (this)`
*PyFunc at classes.py:1333 (dict_keys)*

> Return PyIterable for Dict keys.

#### `len (this)`
*PyFunc at classes.py:1090 (pobj_len)*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `pop (obj, key)`
*PyFunc at classes.py:1319 (dict_pop)*

> Remove Dict item with specified `key`.

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1266 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*Closure at bootstrap.xxl:202:38*

> return representation of Dict

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1242 (pyiterable_reversed)*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1251 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

#### `values (this)`
*PyFunc at classes.py:1340 (dict_values)*

> Return PyIterable for Dict values.

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Dict'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1301 (dict_get)*

> `l[r]`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1292 (dict_put)*

> `l[r] = value`

---
## Class `Iterable` subclass of `Object`


> Mixin for Classes that can be iterated over

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this, func)`
*Closure at bootstrap.xxl:117:34*

> Default `iter` method for `Iterable` mixin; fatal error.

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `reversed (this)`
*Closure at bootstrap.xxl:156:46*

> Creates List from `this`, returns reverse PyIterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:164:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Iterable'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `List` subclass of `PyIterable`


> Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc at classes.py:1373 (list_append)*

> append `item`.

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `extend (this, iterable)`
*Closure at bootstrap.xxl:237:40*

> Create an iterator from `iterable` and iterate appending values to `this` returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:218:38*

> init method for List: takes Iterable

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1235 (pyiterable_iter)*

> Return forward iterator.

#### `len (this)`
*PyFunc at classes.py:1090 (pobj_len)*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `pop (l, index)`
*PyFunc at classes.py:1381 (list_pop)*

> Remove and return item at `index` (default last).

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1266 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*Closure at bootstrap.xxl:230:38*

> return representation of List

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1242 (pyiterable_reversed)*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1251 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'List'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1390 (list_get)*

> `l[r]`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1398 (list_put)*

> `l[r] = value`

---
## Class `ModInfo` subclass of `Object`


> Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc at classes.py:2121 (modinfo_assemble)*

> Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `load_vmx (this, fname)`
*PyFunc at classes.py:2111 (modinfo_load_vmx)*

> Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'ModInfo'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Module` subclass of `Object`


> Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `modules`
*Dict*
> `{'classes': <Module>, 'lib/doc.xxl': <Module>, 'parser.vmx': <Module>, 'lib/markup.xxl': <Module>}`

#### `name`
*Str*
> `'Module'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Null` subclass of `Nullish,PObject`


> Built-in Class of `null` value

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:252:24*

> Return `null` value NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1792 (null_str)*

> to_string/repr method for Null Class: returns "null"

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `true`

#### `name`
*Str*
> `'Null'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this, ...args)`
*PyFunc at classes.py:1799 (null_call)*

> `(` method for `null` value (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Nullish` subclass of `Object`


> Mixin for nullish classes.

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Nullish'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (l, ...args)`
*PyFunc at classes.py:956 (obj_call)*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `Number` subclass of `PObject`


> Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:263:26*

> Convert `x` to a `Number` NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1105 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_float (this)`
*PyFunc at classes.py:1570 (num_to_float)*

> If value is a float, return `this` If value is an int, return a new Number object

#### `to_int (this)`
*PyFunc at classes.py:1580 (num_to_int)*

> If value is an int, return `this` If value is a float, return a new Number object

#### `to_number (this)`
*PyFunc at classes.py:1590 (num_to_number)*

> identity method; returns `this`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Number'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

#### `- (x)`
*PyFunc at classes.py:1427 (neg)*

> Return negative of `x`

#### `~ (this)`
*PyFunc at classes.py:1563 (bitnot)*

> return bitwise (binary) "not" (complement) of `this`

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1496 (ne)*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `& (l, r)`
*PyFunc at classes.py:1537 (bitand)*

> return bitwise (binary) "and" (conjunction) of `l` and `r`

#### `( (l, ...args)`
*PyFunc at classes.py:956 (obj_call)*

> default Object `(` binop (fatal error)

#### `* (l, r)`
*PyFunc at classes.py:1458 (mul)*

> multiply `l` and `r`

#### `+ (l, r)`
*PyFunc at classes.py:1434 (add)*

> add `l` and `r`

#### `- (l, r)`
*PyFunc at classes.py:1447 (sub)*

> subtract `r` from `l`

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `/ (l, r)`
*PyFunc at classes.py:1471 (div)*

> Divide `l` by `r`; always creates float.

#### `< (l, r)`
*PyFunc at classes.py:1513 (lt)*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1523 (le)*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1489 (eq)*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1530 (gt)*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1506 (ge)*

> return `true` if value of `l` is >= the value of `r`

#### `| (l, r)`
*PyFunc at classes.py:1550 (bitor)*

> return bitwise (binary) "or" (union) of `l` and `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Object` subclass of `Object`


> Base Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Object'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (l, ...args)`
*PyFunc at classes.py:956 (obj_call)*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PClass` subclass of `Class`


> Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc at classes.py:1075 (pclass_create)*

> 'create' method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PClass'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `PObject` subclass of `Object`


> Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1105 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PObject'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (l, ...args)`
*PyFunc at classes.py:956 (obj_call)*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyFunc` subclass of `Callable`


> Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PyFunc'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `PyIterable` subclass of `PObject,Iterable`


> Wrapper for Python 'iterable' Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1235 (pyiterable_iter)*

> Return forward iterator.

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1266 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1105 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1242 (pyiterable_reversed)*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `sorted (this, reverse)`
*PyFunc at classes.py:1251 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PyIterable'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyIterator` subclass of `Object,Iterable`


> Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1950 (pyiterator_iter)*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `next (this, finished_continuation)`
*PyFunc at classes.py:1960 (pyiterator_next)*

> `finished` should be a CContinuation (eg; block leave label or "return") to call when iterator exhausted

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `reversed (this)`
*Closure at bootstrap.xxl:156:46*

> Creates List from `this`, returns reverse PyIterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:164:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PyIterator'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `PyObject` subclass of `Object`


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:1913 (pyobj_props)*

> return dir() of wrapped Python object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PyObject'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this, ...args)`
*PyFunc at classes.py:1928 (pyobj_call)*

> 

#### `. (l, r)`
*PyFunc at classes.py:1896 (pyobj_getprop)*

> PyObject `.` binop -- proxies to Python object getattr

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `[ (l, r)`
*PyFunc at classes.py:1920 (pyobj_getitem)*

> PyObject `[` binop

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `PyVMFunc` subclass of `Callable`


> Built-in Class for function implemented in Python with access to VM internals

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:67:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'PyVMFunc'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `SingletonClass` subclass of `Class`


> Metaclass for Classes with singleton values. Invoke classes.SingletonClass.new instead of Class.new.

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:723 (obj_create)*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:1008 (class_init)*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:282:11*

> SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:757 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1048 (class_subclass_of)*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'SingletonClass'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## PClass `Str` subclass of `PyIterable`


> Built-in immutable Unicode string Class

### Methods

#### `chr (i)`
*PyFunc at classes.py:1755 (str_chr)*

> Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:106:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `ends_with (this, suff)`
*PyFunc at classes.py:1676 (str_ends_with)*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

#### `for_each (this, func)`
*Closure at bootstrap.xxl:96:38*

> Create Iterator from `this`, call `func` with each value.

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1120 (pobj_init)*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1235 (pyiterable_iter)*

> Return forward iterator.

#### `join (this, iterable)`
*Closure at bootstrap.xxl:302:37*

> Concatenate strings from `iterable` using `this` as the separator.

#### `len (this)`
*PyFunc at classes.py:1090 (pobj_len)*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:124:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:139:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

#### `new (arg)`
*Closure at bootstrap.xxl:318:23*

> Str Class new (static) method; calls arg.to_str method

#### `ord (this)`
*PyFunc at classes.py:1694 (str_ord)*

> Return the Unicode code point for a one-character string `this`

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `range (...args)`
*PyFunc at classes.py:1266 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1105 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1113 (pobj_reprx)*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1242 (pyiterable_reversed)*

> Return reverse iterator.

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `slice (this, start, end)`
*PyFunc at classes.py:1647 (str_slice)*

> return a substring (slice) of `this` starting at position `start` ending at position `end` (defaults to rest of string

#### `sorted (this, reverse)`
*PyFunc at classes.py:1251 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

#### `split (this, sep, limit)`
*PyFunc at classes.py:1662 (str_split)*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

#### `starts_with (this, pref)`
*PyFunc at classes.py:1704 (str_starts_with)*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

#### `strip (this)`
*PyFunc at classes.py:1718 (str_strip)*

> Return a copy of the string with leading and trailing whitespace removed.

#### `to_float (this)`
*PyFunc at classes.py:1725 (str_to_float)*

> Convert string to a floating point Number

#### `to_int (this, base)`
*PyFunc at classes.py:1732 (str_to_int)*

> Convert string to integer Number `base` defaults to zero (accept 0xXXX for base 16)

#### `to_number (this)`
*PyFunc at classes.py:1744 (str_to_number)*

> Convert string to a Number

#### `to_str (this)`
*PyFunc at classes.py:1711 (str_str)*

> Identity method

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `'Str'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1496 (ne)*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1147 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1039 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

#### `+ (x, y)`
*PyFunc at classes.py:1625 (str_concat)*

> String concatenation

#### `. (l, r)`
*PyFunc at classes.py:885 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `< (l, r)`
*PyFunc at classes.py:1513 (lt)*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1523 (le)*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1489 (eq)*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1136 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1530 (gt)*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1506 (ge)*

> return `true` if value of `l` is >= the value of `r`

#### `[ (l, r)`
*PyFunc at classes.py:1638 (str_get)*

> Str l[r] return `r`'th character of Str `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
## Class `Undefined` subclass of `Nullish,Object`


> Class for undefined value.

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:802 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:942 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `init (this_obj, ...args)`
*PyFunc at classes.py:731 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:964 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:328:29*

> Return `undefined` value NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:749 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1984 (undef_str)*

> to_string/repr method for Undefined Class: returns `"undefined"`

#### `reprx (l)`
*PyFunc at classes.py:765 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:949 (obj_setclass)*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:56:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `true`

#### `name`
*Str*
> `'Undefined'`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:794 (obj_not)*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:779 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (this, ...args)`
*PyFunc at classes.py:1991 (undef_call)*

> `(` method for `undefined` value (fatal error). commonly happens when a bad method name is used, so output a "helpful" message.

#### `. (l, r)`
*PyFunc at classes.py:1816 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

#### `.. (this, prop)`
*PyFunc at classes.py:932 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:772 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:811 (obj_putprop)*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

---
formatted by doc.xxl on 2021-06-22
