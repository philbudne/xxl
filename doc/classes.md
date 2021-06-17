# `classes` Module

## Class `Bool`


> Built-in Class for `true` and `false` values

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1748*

> return Str representation: "true" or "false"

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Bool`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `BoundMethod`


> Built-in Class for a method bound to an Object

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `BoundMethod`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Callable`


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Callable`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Class`


> Base Metaclass, home of the default 'new' method

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Class`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Closure`


> Built-in Class for a native function bound to a scope

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Closure`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Continuation`


> Built-in Class for a Continuation

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Continuation`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Dict`


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
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:127:38*

> init method for Dict: takes Iterable returning two-item lists, OR an Iterable returning keys, and implementing '['

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `items (this)`
*PyFunc at classes.py:1255*

> return Iterable for [key, value] value pairs

#### `iter (this)`
*PyFunc at classes.py:1160*

> return forward iterator

#### `keys (this)`
*PyFunc at classes.py:1262*

> return Iterable for Dict keys

#### `len (this)`
*PyFunc at classes.py:1053*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `pop (obj, arg)`
*PyFunc at classes.py:1248*

> remove Dict with specified key

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*Closure at bootstrap.xxl:154:38*

> return representation of Dict

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1167*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1175*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

#### `values (this)`
*PyFunc at classes.py:1269*

> return Iterable for Dict values

### Members

### `name`

Value: `Dict`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1230*

> get entry `r` Dict from dict `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1221*

> put `value` into Dict `l` index `r`

## Class `Iterable`


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
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1160*

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
*PyFunc at classes.py:1068*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1167*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1175*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Iterable`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `List`


> Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc at classes.py:1302*

> append `item` to `this` List

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `extend (this, iterable)`
*Closure at bootstrap.xxl:189:40*

> 

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this, arg)`
*Closure at bootstrap.xxl:170:38*

> init method for List: takes Iterable

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1160*

> return forward iterator

#### `len (this)`
*PyFunc at classes.py:1053*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `pop (l, index)`
*PyFunc at classes.py:1310*

> Remove and return List item at `index` (default last)

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*Closure at bootstrap.xxl:182:38*

> return represtation of List

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1167*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1175*

> return sorted list values (or keys)

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `List`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `[ (l, r)`
*PyFunc at classes.py:1319*

> Return List item at index `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `[ (l, r, value)`
*PyFunc at classes.py:1327*

> Set List item at index `r` to `value`

## Class `ModInfo`


> Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc at classes.py:1991*

> `tree`: List of Lists of VM code `srcfile`: source of code returns Closure in __modinfo.module initial scope

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `load_vmx (this, fname)`
*PyFunc at classes.py:1985*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `ModInfo`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Module`


> Built-in class for a Module (from import function)

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `modules`

Value: `{'classes': <Module at 0x7f9f2d3ad7c0>, 'doc.xxl': <Module at 0x7f9f2d3ad800>, 'parser.vmx': <Module at 0x7f9f2d3595c0>}`
### `name`

Value: `Module`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Null`


> Built-on Class of `null` value

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1723*

> to_string/repr method for Null Class: returns "null"

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Null`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this, ...args)`
*PyFunc at classes.py:1730*

> `(` method for `null` value (fatal error) commonly happens when a bad method name is used

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Number`


> Built-in int/float wrapper Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `new (x)`
*Closure at bootstrap.xxl:200:26*

> Return a `Number` object with value `x` NOTE!! A static method, not a (Meta)class method!!!

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1068*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_float (this)`
*PyFunc at classes.py:1499*

> If value is a float, return `this` If value is an int, return a new Number object

#### `to_int (this)`
*PyFunc at classes.py:1509*

> If value is an int, return `this` If value is a float, return a new Number object

#### `to_number (this)`
*PyFunc at classes.py:1519*

> identity method; returns `this`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Number`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

#### `- (x)`
*PyFunc at classes.py:1356*

> Return negative of `x`

#### `~ (this)`
*PyFunc at classes.py:1492*

> return bitwise (binary) "not" (complement) of `this`

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1425*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `& (l, r)`
*PyFunc at classes.py:1466*

> return bitwise (binary) "and" (conjunction) of `l` and `r`

#### `( (l, ...args)`
*PyFunc at classes.py:920*

> default Object `(` binop (fatal error)

#### `* (l, r)`
*PyFunc at classes.py:1387*

> multiple `l` and `r`

#### `+ (l, r)`
*PyFunc at classes.py:1363*

> add `l` and `r`

#### `- (l, r)`
*PyFunc at classes.py:1376*

> subtract `r` from `l`

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `/ (l, r)`
*PyFunc at classes.py:1400*

> divide `l` by `r`

#### `< (l, r)`
*PyFunc at classes.py:1442*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1452*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1418*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1459*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1435*

> return `true` if value of `l` is >= the value of `r`

#### `| (l, r)`
*PyFunc at classes.py:1479*

> return bitwise (binary) "or" (union) of `l` and `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `Object`


> Base Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `Object`
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
*PyFunc at classes.py:920*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `PClass`


> Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc at classes.py:1038*

> 'create' method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PClass`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `PObject`


> Base class for Primitive/Python value Classes

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1068*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PObject`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (l, ...args)`
*PyFunc at classes.py:920*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyFunc`


> Built-in Class for function implemented in Python

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PyFunc`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `PyIterable`


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
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1160*

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
*PyFunc at classes.py:1196*

> return an Iterable for an integer range (an Iterable can be iterated over any number of times) range(10): returns Iterable for 0..9 range(1,10): returns Iterable for 1..9 range(1,10,2): returns Iterable for odd numbers 1..9

#### `repr (this)`
*PyFunc at classes.py:1068*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1167*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `sorted (this)`
*PyFunc at classes.py:1175*

> return sorted list values (or keys)

#### `to_str (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

### Members

### `name`

Value: `PyIterable`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyIterator`


> Built-in Class for a wrapper around a Python iterator

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_obj, ...args)`
*PyFunc at classes.py:692*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1845*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

#### `next (this, finished_continuation)`
*PyFunc at classes.py:1855*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PyIterator`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `PyObject`


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PyObject`
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
*PyFunc at classes.py:1824*

> 

#### `. (l, r)`
*PyFunc at classes.py:1799*

> PyObject "." binop -- proxies to Python object getattr

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:733*

> Test if `l` and `r` refer to the same Object

#### `[ (l, r)`
*PyFunc at classes.py:1816*

> PyObject "[" binop

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Class `PyVMFunc`


> Built-in Class for function implemented in Python with access to VM internals

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:684*

> default create method for Object (and therefore Class) makes an instance of this_class (called from default Object.new)

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (this_class, props)`
*PyFunc at classes.py:971*

> init method for meta-class "Class" -- used to create new Classes `props` is Dict holding properties (see const.CLASS_PROPS)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

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
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `subclass_of (this, c)`
*PyFunc at classes.py:1011*

> return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

#### `to_str (this)`
*Closure at bootstrap.xxl:45:42*

> default to_str method: calls this.repr

### Members

### `name`

Value: `PyVMFunc`
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
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

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

## Class `Str`


> Built-in immutable Unicode string Class

### Methods

#### `chr (i)`
*PyFunc at classes.py:1686*

> Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff

#### `delprop (this, name)`
*PyFunc at classes.py:763*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `each_for (this, func)`
*Closure at bootstrap.xxl:83:38*

> call `func` argument with each reverse iterator item

#### `ends_with (this, suff)`
*PyFunc at classes.py:1605*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

#### `for_each (this, func)`
*Closure at bootstrap.xxl:73:38*

> call `func` argument with each iterator item

#### `getclass (this)`
*PyFunc at classes.py:906*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `init (l, value)`
*PyFunc at classes.py:1083*

> default PObject init method (fatal error)

#### `instance_of (this, c)`
*PyFunc at classes.py:928*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `iter (this)`
*PyFunc at classes.py:1160*

> return forward iterator

#### `join (this, arg)`
*PyFunc at classes.py:1612*

> Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string.

#### `len (this)`
*PyFunc at classes.py:1053*

> returns length (of String, List or Dict)

#### `map (this, func)`
*Closure at bootstrap.xxl:93:33*

> return List of results of `func` passed each iterator item

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:107:34*

> return List of results of `func` passed each iterator item, ignore any returns with value `ignore` (defaults to `null`)

#### `ord (this)`
*PyFunc at classes.py:1625*

> Return the Unicode code point for a one-character string `this`

#### `props (this)`
*PyFunc at classes.py:710*

> returns an Iterable for (String) property names of `this` Object

#### `putprop (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

#### `repr (this)`
*PyFunc at classes.py:1068*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1076*

> for debug: show Class name, and Python repr

#### `reversed (this)`
*PyFunc at classes.py:1167*

> return reverse iterator

#### `setclass (this, klass)`
*PyFunc at classes.py:913*

> set Class for `this`!!

#### `slice (this, start, end)`
*PyFunc at classes.py:1576*

> return a substring (slice) of `this` starting at position `start` ending at position `end` (defaults to rest of string

#### `sorted (this)`
*PyFunc at classes.py:1175*

> return sorted list values (or keys)

#### `split (this, sep, limit)`
*PyFunc at classes.py:1591*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

#### `starts_with (this, pref)`
*PyFunc at classes.py:1635*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

#### `strip (this)`
*PyFunc at classes.py:1649*

> Return a copy of the string with leading and trailing whitespace removed.

#### `to_float (this)`
*PyFunc at classes.py:1656*

> Convert string to a floating point Number

#### `to_int (this, base)`
*PyFunc at classes.py:1663*

> Convert string to integer Number `base` defaults to zero (accept 0xXXX for base 16)

#### `to_number (this)`
*PyFunc at classes.py:1675*

> Convert string to a Number

#### `to_str (this)`
*PyFunc at classes.py:1642*

> Identity method

### Members

### `name`

Value: `Str`
### Unary operators

#### `! (x)`
*PyFunc at classes.py:755*

> Object unary logical "not" operator; returns `true` if `x` is "falsey" (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1425*

> return `true` if value of `l` is different from the value of `r`

#### `!== (l, r)`
*PyFunc at classes.py:1110*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `( (this_class, ...args)`
*PyFunc at classes.py:1002*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) tells you to use .new method!!

#### `+ (x, y)`
*PyFunc at classes.py:1554*

> String concatenation

#### `. (l, r)`
*PyFunc at classes.py:849*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:896*

> Object ".." operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `< (l, r)`
*PyFunc at classes.py:1442*

> return `true` if value of `l` is < the value of `r`

#### `<= (l, r)`
*PyFunc at classes.py:1452*

> return `true` if value of `l` is <= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1418*

> return `true` if value of `l` is the same as value of `r`

#### `=== (l, r)`
*PyFunc at classes.py:1099*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `> (l, r)`
*PyFunc at classes.py:1459*

> return `true` if value of `l` is > the value of `r`

#### `>= (l, r)`
*PyFunc at classes.py:1435*

> return `true` if value of `l` is >= the value of `r`

#### `[ (l, r)`
*PyFunc at classes.py:1567*

> Str l[r] return `r`'th character of Str `l`

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:772*

> Object putprop method/operator store `value` as `r` (String) property of object `l`

## Variables

### `false`

Value: `false`

### `null`

Value: `null`

### `true`

Value: `true`

---
formatted by doc.xxl on 2021-06-16
