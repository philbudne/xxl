# Module `classes`


> Built-in Classes for XXL

---

<a name="class-Bool"></a>
## PClass `Bool` subclass of `[PObject](#class-PObject)`


> Built-in Class for `true` and `false` values

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (x)`
*Closure at bootstrap.xxl:116:24*

> Return truthiness of `x` (as Bool). NOTE!! A static method, not a metaclass method!!!

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
#### `repr (this)`
*PyFunc at classes.py:1873 (bool_str)*

> return Str representation: &quot;true&quot; or &quot;false&quot;

<font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Bool&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-BoundMethod"></a>
## Class `BoundMethod` subclass of `[Callable](#class-Callable)`


> Built-in Class for a method bound to an Object

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;BoundMethod&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Callable"></a>
## Class `Callable` subclass of `[Object](#class-Object)`


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Callable&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Class"></a>
## Class `Class` subclass of `[Object](#class-Object)`


> Base Metaclass, home of the default &#x27;new&#x27; method

### Methods

#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Class&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Closure"></a>
## Class `Closure` subclass of `[Callable](#class-Callable)`


> Built-in Class for a native function bound to a scope

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Closure&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Continuation"></a>
## Class `Continuation` subclass of `[Callable](#class-Callable)`


> Built-in Class for a Continuation

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Continuation&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Dict"></a>
## PClass `Dict` subclass of `[PyIterable](#class-PyIterable)`


> Built-in dictionary mapping Class

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font><font color="slategray">
#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (this, arg)`
*Closure at bootstrap.xxl:210:38*

> init method for Dict: takes Iterable returning two-item lists, OR an Iterable returning keys, and implementing &#x27;[&#x27;

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `items (this)`
*PyFunc at classes.py:1347 (dict_items)*

> Return PyIterable for [key, value] value pairs.

<font color="slategray">
#### `iter (this)`
*PyFunc at classes.py:1256 (pyiterable_iter)*

> Return forward iterator.

</font>
#### `keys (this)`
*PyFunc at classes.py:1354 (dict_keys)*

> Return PyIterable for Dict keys.

#### `len (this)`
*PyFunc at classes.py:1111 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

</font><font color="slategray">
#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
#### `pop (obj, key)`
*PyFunc at classes.py:1340 (dict_pop)*

> Remove Dict item with specified `key`.

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `range (...args)`
*PyFunc at classes.py:1287 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
#### `repr (this)`
*Closure at bootstrap.xxl:236:38*

> return representation of Dict

<font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `reversed (this)`
*PyFunc at classes.py:1263 (pyiterable_reversed)*

> Return reverse iterator.

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `sorted (this, reverse)`
*PyFunc at classes.py:1272 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
#### `values (this)`
*PyFunc at classes.py:1361 (dict_values)*

> Return PyIterable for Dict values.

### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Dict&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
#### `[ (l, r)`
*PyFunc at classes.py:1322 (dict_get)*

> `l[r]`

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `[ (l, r, value)`
*PyFunc at classes.py:1313 (dict_put)*

> `l[r] = value`

---

<a name="class-Iterable"></a>
## Class `Iterable` subclass of `[Object](#class-Object)`


> Mixin for Classes that can be iterated over

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font>
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

<font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `iter (this, func)`
*Closure at bootstrap.xxl:151:34*

> Default `iter` method for `Iterable` mixin; fatal error.

#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font>
#### `reversed (this)`
*Closure at bootstrap.xxl:190:46*

> Creates List from `this`, returns reverse PyIterator.

<font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:198:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Iterable&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-List"></a>
## PClass `List` subclass of `[PyIterable](#class-PyIterable)`


> Built-in mutable sequence Class

### Methods

#### `append (this, item)`
*PyFunc at classes.py:1394 (list_append)*

> append `item`.

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
#### `extend (this, iterable)`
*Closure at bootstrap.xxl:271:40*

> Create an iterator from `iterable` and iterate appending values to `this` returns `null`

<font color="slategray">
#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (this, arg)`
*Closure at bootstrap.xxl:252:38*

> init method for List: takes Iterable

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `iter (this)`
*PyFunc at classes.py:1256 (pyiterable_iter)*

> Return forward iterator.

</font>
#### `len (this)`
*PyFunc at classes.py:1111 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

</font><font color="slategray">
#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
#### `pop (l, index)`
*PyFunc at classes.py:1402 (list_pop)*

> Remove and return item at `index` (default last).

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `range (...args)`
*PyFunc at classes.py:1287 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
#### `repr (this)`
*Closure at bootstrap.xxl:264:38*

> return representation of List

<font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `reversed (this)`
*PyFunc at classes.py:1263 (pyiterable_reversed)*

> Return reverse iterator.

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `sorted (this, reverse)`
*PyFunc at classes.py:1272 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;List&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
#### `[ (l, r)`
*PyFunc at classes.py:1411 (list_get)*

> `l[r]`

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `[ (l, r, value)`
*PyFunc at classes.py:1419 (list_put)*

> `l[r] = value`

---

<a name="class-ModInfo"></a>
## Class `ModInfo` subclass of `[Object](#class-Object)`


> Built-in Class for __modinfo Objects (inside Modules)

### Methods

#### `assemble (this, tree, srcfile)`
*PyFunc at classes.py:2149 (modinfo_assemble)*

> Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `load_vmx (this, fname)`
*PyFunc at classes.py:2139 (modinfo_load_vmx)*

> Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;ModInfo&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Module"></a>
## Class `Module` subclass of `[Object](#class-Object)`


> Built-in class for a Module (from import function)

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `modules`
*Dict*
> `{&#x27;classes&#x27;: &lt;Module&gt;, &#x27;lib/doc.xxl&#x27;: &lt;Module&gt;, &#x27;parser.vmx&#x27;: &lt;Module&gt;, &#x27;lib/markup.xxl&#x27;: &lt;Module&gt;}`

#### `name`
*Str*
> `&#x27;Module&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Null"></a>
## Class `Null` subclass of `[Nullish](#class-Nullish),[PObject](#class-PObject)`


> Built-in Class of `null` value

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (x)`
*Closure at bootstrap.xxl:286:24*

> Return `null` value NOTE!! A static method, not a metaclass method!!!

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
#### `repr (this)`
*PyFunc at classes.py:1810 (null_str)*

> to_string/repr method for Null Class: returns &quot;null&quot;

<font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:1852 (nullish_setprop)*

> Nullish Object setprop method/operator

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

#### `is_nullish`
*Bool*
> `true`

#### `name`
*Str*
> `&#x27;Null&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
#### `( (this, ...args)`
*PyFunc at classes.py:1817 (null_call)*

> `(` method for `null` value (fatal error)

<font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Nullish"></a>
## Class `Nullish` subclass of `[Object](#class-Object)`


> Mixin for nullish classes.

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font>
#### `getprop (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font>
#### `setprop (l, r, value)`
*PyFunc at classes.py:1852 (nullish_setprop)*

> Nullish Object setprop method/operator

<font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Nullish&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (l, ...args)`
*PyFunc at classes.py:965 (obj_call)*

> default Object `(` binop (fatal error)

</font>
#### `. (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:1852 (nullish_setprop)*

> Nullish Object setprop method/operator

---

<a name="class-Number"></a>
## PClass `Number` subclass of `[PObject](#class-PObject)`


> Built-in int/float wrapper Class

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (x)`
*Closure at bootstrap.xxl:297:26*

> Convert `x` to a `Number` NOTE!! A static method, not a metaclass method!!!

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:1126 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

</font><font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `to_float (this)`
*PyFunc at classes.py:1591 (num_to_float)*

> If value is a float, return `this` If value is an int, return a new Number object

#### `to_int (this)`
*PyFunc at classes.py:1601 (num_to_int)*

> If value is an int, return `this` If value is a float, return a new Number object

#### `to_number (this)`
*PyFunc at classes.py:1611 (num_to_number)*

> identity method; returns `this`

<font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Number&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
#### `- (x)`
*PyFunc at classes.py:1448 (neg)*

> Return negative of `x`

#### `~ (this)`
*PyFunc at classes.py:1584 (bitnot)*

> return bitwise (binary) &quot;not&quot; (complement) of `this`

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1517 (ne)*

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
#### `&amp; (l, r)`
*PyFunc at classes.py:1558 (bitand)*

> return bitwise (binary) &quot;and&quot; (conjunction) of `l` and `r`

<font color="slategray">
#### `( (l, ...args)`
*PyFunc at classes.py:965 (obj_call)*

> default Object `(` binop (fatal error)

</font>
#### `* (l, r)`
*PyFunc at classes.py:1479 (mul)*

> multiply `l` and `r`

#### `+ (l, r)`
*PyFunc at classes.py:1455 (add)*

> add `l` and `r`

#### `- (l, r)`
*PyFunc at classes.py:1468 (sub)*

> subtract `r` from `l`

<font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font>
#### `/ (l, r)`
*PyFunc at classes.py:1492 (div)*

> Divide `l` by `r`; always creates float.

#### `&lt; (l, r)`
*PyFunc at classes.py:1534 (lt)*

> return `true` if value of `l` is &lt; the value of `r`

#### `&lt;= (l, r)`
*PyFunc at classes.py:1544 (le)*

> return `true` if value of `l` is &lt;= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1510 (eq)*

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
#### `&gt; (l, r)`
*PyFunc at classes.py:1551 (gt)*

> return `true` if value of `l` is &gt; the value of `r`

#### `&gt;= (l, r)`
*PyFunc at classes.py:1527 (ge)*

> return `true` if value of `l` is &gt;= the value of `r`

#### `| (l, r)`
*PyFunc at classes.py:1571 (bitor)*

> return bitwise (binary) &quot;or&quot; (union) of `l` and `r`

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Object"></a>
## Class `Object` subclass of `[Object](#class-Object)`


> Base Class

### Methods

#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

### Members

#### `is_nullish`
*Bool*
> `false`

#### `name`
*Str*
> `&#x27;Object&#x27;`

### Unary operators

#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

#### `( (l, ...args)`
*PyFunc at classes.py:965 (obj_call)*

> default Object `(` binop (fatal error)

#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

### LHS Binary operators

#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

---

<a name="class-PClass"></a>
## Class `PClass` subclass of `[Class](#class-Class)`


> Metaclass for Primitive/Python value Classes

### Methods

#### `create (this_class)`
*PyFunc at classes.py:1096 (pclass_create)*

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PClass&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PObject"></a>
## PClass `PObject` subclass of `[Object](#class-Object)`


> Base class for Primitive/Python value Classes

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
#### `repr (this)`
*PyFunc at classes.py:1126 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

<font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PObject&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<font color="slategray">
#### `( (l, ...args)`
*PyFunc at classes.py:965 (obj_call)*

> default Object `(` binop (fatal error)

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font>
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyFunc"></a>
## Class `PyFunc` subclass of `[Callable](#class-Callable)`


> Built-in Class for function implemented in Python

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PyFunc&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterable"></a>
## PClass `PyIterable` subclass of `[PObject](#class-PObject),[Iterable](#class-Iterable)`


> Wrapper for Python &#x27;iterable&#x27; Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font><font color="slategray">
#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `iter (this)`
*PyFunc at classes.py:1256 (pyiterable_iter)*

> Return forward iterator.

<font color="slategray">
#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

</font><font color="slategray">
#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `range (...args)`
*PyFunc at classes.py:1287 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:1126 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

</font><font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font>
#### `reversed (this)`
*PyFunc at classes.py:1263 (pyiterable_reversed)*

> Return reverse iterator.

<font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `sorted (this, reverse)`
*PyFunc at classes.py:1272 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PyIterable&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterator"></a>
## Class `PyIterator` subclass of `[Object](#class-Object),[Iterable](#class-Iterable)`


> Built-in Class for a wrapper around a Python iterator

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font><font color="slategray">
#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `iter (this)`
*PyFunc at classes.py:1979 (pyiterator_iter)*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

<font color="slategray">
#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

</font><font color="slategray">
#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
#### `next (this, finished_continuation)`
*PyFunc at classes.py:1989 (pyiterator_next)*

> Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `reversed (this)`
*Closure at bootstrap.xxl:190:46*

> Creates List from `this`, returns reverse PyIterator.

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `sorted (this, reverse)`
*Closure at bootstrap.xxl:198:44*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PyIterator&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyObject"></a>
## PClass `PyObject` subclass of `[Object](#class-Object)`


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `props (this)`
*PyFunc at classes.py:1942 (pyobj_props)*

> return dir() of wrapped Python object

<font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PyObject&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
#### `( (this, ...args)`
*PyFunc at classes.py:1957 (pyobj_call)*

> 

#### `. (l, r)`
*PyFunc at classes.py:1925 (pyobj_getprop)*

> PyObject `.` binop -- proxies to Python object getattr

<font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
#### `[ (l, r)`
*PyFunc at classes.py:1949 (pyobj_getitem)*

> PyObject `[` binop

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyVMFunc"></a>
## Class `PyVMFunc` subclass of `[Callable](#class-Callable)`


> Built-in Class for function implemented in Python with access to VM internals

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:101:38*

> Default metaclass (Class) new method; Manually invoked as SomeClass.new. Calls this_class.create to create obj, and then calls obj.init().

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;PyVMFunc&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-SingletonClass"></a>
## Class `SingletonClass` subclass of `[Class](#class-Class)`


> Metaclass for Classes with singleton values. Invoke classes.SingletonClass.new instead of Class.new to create a singleton Class.

### Methods

<font color="slategray">
#### `create (this_class, ...args)`
*PyFunc at classes.py:1018 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_class, props)`
*PyFunc at classes.py:1026 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
#### `new (this_class, ...args)`
*Closure at bootstrap.xxl:317:11*

> SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:759 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

</font><font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font><font color="slategray">
#### `subclass_of (this, c)`
*PyFunc at classes.py:1068 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;SingletonClass&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font><font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Str"></a>
## PClass `Str` subclass of `[PyIterable](#class-PyIterable)`


> Built-in immutable Unicode string Class

### Methods

<font color="slategray">
#### `chr (i)`
*PyFunc at classes.py:1773 (str_chr)*

> Return a Unicode string of one character with ordinal i; 0 &lt;= i &lt;= 0x10ffff

</font><font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `each_for (this, func)`
*Closure at bootstrap.xxl:140:38*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
#### `ends_with (this, suff)`
*PyFunc at classes.py:1697 (str_ends_with)*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

<font color="slategray">
#### `for_each (this, func)`
*Closure at bootstrap.xxl:130:38*

> Create Iterator from `this`, call `func` with each value.

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
#### `init (l, value)`
*PyFunc at classes.py:1141 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `iter (this)`
*PyFunc at classes.py:1256 (pyiterable_iter)*

> Return forward iterator.

</font>
#### `join (this, iterable)`
*Closure at bootstrap.xxl:337:37*

> Concatenate strings from `iterable` using `this` as the separator.

#### `len (this)`
*PyFunc at classes.py:1111 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
#### `map (this, func)`
*Closure at bootstrap.xxl:158:33*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

</font><font color="slategray">
#### `map2 (this, func, ignore)`
*Closure at bootstrap.xxl:173:34*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font><font color="slategray">
#### `new (arg)`
*Closure at bootstrap.xxl:353:23*

> Str Class new (static) method; calls arg.to_str method

</font>
#### `ord (this)`
*PyFunc at classes.py:1715 (str_ord)*

> Return the Unicode code point for a one-character string `this`

<font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font><font color="slategray">
#### `range (...args)`
*PyFunc at classes.py:1287 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font><font color="slategray">
#### `repr (this)`
*PyFunc at classes.py:1126 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

</font><font color="slategray">
#### `reprx (this)`
*PyFunc at classes.py:1134 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font><font color="slategray">
#### `reversed (this)`
*PyFunc at classes.py:1263 (pyiterable_reversed)*

> Return reverse iterator.

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
#### `slice (this, start, end)`
*PyFunc at classes.py:1668 (str_slice)*

> return a substring (slice) of `this` starting at position `start` ending at position `end` (defaults to rest of string

<font color="slategray">
#### `sorted (this, reverse)`
*PyFunc at classes.py:1272 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font>
#### `split (this, sep, limit)`
*PyFunc at classes.py:1683 (str_split)*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

#### `starts_with (this, pref)`
*PyFunc at classes.py:1722 (str_starts_with)*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

#### `strip (this)`
*PyFunc at classes.py:1736 (str_strip)*

> Return a copy of the string with leading and trailing whitespace removed.

#### `to_float (this)`
*PyFunc at classes.py:1743 (str_to_float)*

> Convert string to a floating point Number

#### `to_int (this, base)`
*PyFunc at classes.py:1750 (str_to_int)*

> Convert string to integer Number. Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).

#### `to_number (this)`
*PyFunc at classes.py:1762 (str_to_number)*

> Convert string to a Number

#### `to_str (this)`
*PyFunc at classes.py:1729 (str_str)*

> Identity method

### Members

<font color="slategray">
#### `is_nullish`
*Bool*
> `false`

</font>
#### `name`
*Str*
> `&#x27;Str&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

#### `!= (l, r)`
*PyFunc at classes.py:1517 (ne)*

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:1168 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font><font color="slategray">
#### `( (this_class, ...args)`
*PyFunc at classes.py:1058 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font>
#### `+ (x, y)`
*PyFunc at classes.py:1646 (str_concat)*

> String concatenation

<font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:887 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font>
#### `&lt; (l, r)`
*PyFunc at classes.py:1534 (lt)*

> return `true` if value of `l` is &lt; the value of `r`

#### `&lt;= (l, r)`
*PyFunc at classes.py:1544 (le)*

> return `true` if value of `l` is &lt;= the value of `r`

#### `== (l, r)`
*PyFunc at classes.py:1510 (eq)*

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:1157 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
#### `&gt; (l, r)`
*PyFunc at classes.py:1551 (gt)*

> return `true` if value of `l` is &gt; the value of `r`

#### `&gt;= (l, r)`
*PyFunc at classes.py:1527 (ge)*

> return `true` if value of `l` is &gt;= the value of `r`

#### `[ (l, r)`
*PyFunc at classes.py:1659 (str_get)*

> Str l[r] return `r`&#x27;th character of Str `l`

### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Undefined"></a>
## Class `Undefined` subclass of `[Nullish](#class-Nullish),[Object](#class-Object)`


> Class for undefined value.

### Methods

<font color="slategray">
#### `delprop (this, name)`
*PyFunc at classes.py:804 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font><font color="slategray">
#### `getclass (this)`
*PyFunc at classes.py:951 (obj_getclass)*

> return Class for `this`

</font><font color="slategray">
#### `getprop (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

</font><font color="slategray">
#### `hasprop (l, r)`
*PyFunc at classes.py:898 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font><font color="slategray">
#### `init (this_obj, ...args)`
*PyFunc at classes.py:733 (obj_init)*

> default init method for Object class a fatal error if any arguments given

</font><font color="slategray">
#### `instance_of (this, c)`
*PyFunc at classes.py:973 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font><font color="slategray">
#### `new (x)`
*Closure at bootstrap.xxl:363:29*

> Return `undefined` value NOTE!! A static method, not a metaclass method!!!

</font><font color="slategray">
#### `props (this)`
*PyFunc at classes.py:751 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
#### `repr (this)`
*PyFunc at classes.py:2012 (undef_str)*

> to_string/repr method for Undefined Class: returns `&quot;undefined&quot;`

<font color="slategray">
#### `reprx (l)`
*PyFunc at classes.py:767 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font><font color="slategray">
#### `setclass (this, klass)`
*PyFunc at classes.py:958 (obj_setclass)*

> set Class for `this`!!

</font><font color="slategray">
#### `setprop (l, r, value)`
*PyFunc at classes.py:1852 (nullish_setprop)*

> Nullish Object setprop method/operator

</font><font color="slategray">
#### `to_str (this)`
*Closure at bootstrap.xxl:90:42*

> Default to_str method: calls this.repr().

</font>
### Members

#### `is_nullish`
*Bool*
> `true`

#### `name`
*Str*
> `&#x27;Undefined&#x27;`

### Unary operators

<font color="slategray">
#### `! (x)`
*PyFunc at classes.py:796 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, null, or zero)

</font>
### Binary operators

<font color="slategray">
#### `!= (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font><font color="slategray">
#### `!== (l, r)`
*PyFunc at classes.py:781 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
#### `( (this, ...args)`
*PyFunc at classes.py:2019 (undef_call)*

> `(` method for `undefined` value (fatal error). commonly happens when a bad method name is used, so output a &quot;helpful&quot; message.

<font color="slategray">
#### `. (l, r)`
*PyFunc at classes.py:1834 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

</font><font color="slategray">
#### `.. (this, prop)`
*PyFunc at classes.py:941 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods looks for `prop` as property or method of superclasses of `this`

</font><font color="slategray">
#### `== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font><font color="slategray">
#### `=== (l, r)`
*PyFunc at classes.py:774 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
### LHS Binary operators

<font color="slategray">
#### `. (l, r, value)`
*PyFunc at classes.py:813 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

formatted by doc.xxl on 2021-06-26
