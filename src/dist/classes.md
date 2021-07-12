<h1>Module `classes`</h1>


> Built-in Classes for XXL

---

<a name="class-Bool"></a>
<h2>`[PClass](#class-PClass)` `Bool` subclass of `[PObject](#class-PObject)`</h2>


> Built-in Class for `true` and `false` values

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (x)`</h3>
*Closure at bootstrap.xxl:93:21*

> Return truthiness of `x` (as Bool). NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method `repr (this)`</h3>
*PyFunc at classes.py:1922 (bool_str)*

> return Str representation: &quot;true&quot; or &quot;false&quot;

<font color="slategray">
<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Bool&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-BoundMethod"></a>
<h2>`[Class](#class-Class)` `BoundMethod` subclass of `[Callable](#class-Callable)`</h2>


> Built-in Class for a method bound to an Object

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;BoundMethod&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Callable"></a>
<h2>`[Class](#class-Class)` `Callable` subclass of `[Object](#class-Object)`</h2>


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Callable&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Class"></a>
<h2>`[Class](#class-Class)` `Class` subclass of `[Object](#class-Object)`</h2>


> Base Metaclass, home of the default &#x27;new&#x27; method

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<font color="slategray">
<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Class&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<font color="slategray">
<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Closure"></a>
<h2>`[Class](#class-Class)` `Closure` subclass of `[Callable](#class-Callable)`</h2>


> Built-in Class for a native function bound to a scope

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Closure&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Continuation"></a>
<h2>`[Class](#class-Class)` `Continuation` subclass of `[Callable](#class-Callable)`</h2>


> Built-in Class for a Continuation

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Continuation&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Dict"></a>
<h2>`[PClass](#class-PClass)` `Dict` subclass of `[PyIterable](#class-PyIterable)`</h2>


> Built-in dictionary mapping Class

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (this, arg)`</h3>
*Closure at bootstrap.xxl:187:35*

> init method for Dict.  arg passed to this.update().

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `items (this)`</h3>
*PyFunc at classes.py:1393 (dict_items)*

> Return PyIterable for [key, value] value pairs.

<font color="slategray">
<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

</font>
<h3>Method `keys (this)`</h3>
*PyFunc at classes.py:1400 (dict_keys)*

> Return PyIterable for Dict keys.

<h3>Method `len (this)`</h3>
*PyFunc at classes.py:1151 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method `pop (obj, key)`</h3>
*PyFunc at classes.py:1386 (dict_pop)*

> Remove Dict item with specified `key`.

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method `repr (this)`</h3>
*Closure at bootstrap.xxl:225:35*

> return representation of Dict

<font color="slategray">
<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Method `update (this, arg)`</h3>
*Closure at bootstrap.xxl:197:37*

> Update `this` using `arg.iter()` legal iterator values: List w/ two elements: `this[l[0]] = l[1];` Non-list: `this[item] = arg[item];`

<h3>Method `values (this)`</h3>
*PyFunc at classes.py:1407 (dict_values)*

> Return PyIterable for Dict values.

<h3>Member `name`</h3>
*Str*
> `&#x27;Dict&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1368 (dict_getitem)*

> `l[r]`

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>LHS `[ (l, r, value)`</h3>
*PyFunc at classes.py:1359 (dict_putitem)*

> `l[r] = value`

---

<a name="class-Iterable"></a>
<h2>`[Class](#class-Class)` `Iterable` subclass of `[Object](#class-Object)`</h2>


> Mixin for Classes that can be iterated over

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font>
<h3>Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3>Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<font color="slategray">
<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `iter (this, func)`</h3>
*Closure at bootstrap.xxl:128:31*

> Default `iter` method for `Iterable` mixin; fatal error.

<h3>Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3>Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

</font>
<h3>Method `reversed (this)`</h3>
*Closure at bootstrap.xxl:167:43*

> Creates List from `this`, returns reverse PyIterator.

<font color="slategray">
<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `sorted (this, reverse)`</h3>
*Closure at bootstrap.xxl:175:41*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Iterable&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-List"></a>
<h2>`[PClass](#class-PClass)` `List` subclass of `[PyIterable](#class-PyIterable)`</h2>


> Built-in mutable sequence Class

<h3>Method `append (this, item)`</h3>
*PyFunc at classes.py:1440 (list_append)*

> append `item`.

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
<h3>Method `extend (this, iterable)`</h3>
*Closure at bootstrap.xxl:250:37*

> Create an iterator from `iterable`, and iterate appending values to `this`; Returns `null`

<font color="slategray">
<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (this, arg)`</h3>
*Closure at bootstrap.xxl:240:35*

> init method for List: takes Iterable

<h3>Method `insert (l, index, object)`</h3>
*PyFunc at classes.py:1465 (list_insert)*

> Insert `object` at `index` (0 is first, -1 is last); Returns `null`.

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

</font>
<h3>Method `len (this)`</h3>
*PyFunc at classes.py:1151 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method `pop (l, index)`</h3>
*PyFunc at classes.py:1448 (list_pop)*

> Remove and return item at `index` (default last).

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method `repr (this)`</h3>
*Closure at bootstrap.xxl:266:35*

> Return representation of `this` List as Str.

<font color="slategray">
<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `slice (this, start, end)`</h3>
*PyFunc at classes.py:1235 (pobj_slice)*

> return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)

<font color="slategray">
<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;List&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1457 (list_get)*

> `l[r]`

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>LHS `[ (l, r, value)`</h3>
*PyFunc at classes.py:1473 (list_put)*

> `l[r] = value`

---

<a name="class-ModInfo"></a>
<h2>`[Class](#class-Class)` `ModInfo` subclass of `[Object](#class-Object)`</h2>


> Built-in Class for __modinfo Objects (inside Modules)

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method `assemble (this, tree, srcfile)`</h3>
*PyFunc at classes.py:2198 (modinfo_assemble)*

> Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.

<font color="slategray">
<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `load_vmx (this, fname)`</h3>
*PyFunc at classes.py:2188 (modinfo_load_vmx)*

> Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;ModInfo&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Module"></a>
<h2>`[Class](#class-Class)` `Module` subclass of `[Object](#class-Object)`</h2>


> Built-in class for a Module (from import function)

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `modules`</h3>
*Dict*
> `{&#x27;classes&#x27;: &lt;Module&gt;, &#x27;lib/doc.xxl&#x27;: &lt;Module&gt;, &#x27;parser.vmx&#x27;: &lt;Module&gt;, &#x27;lib/markup.xxl&#x27;: &lt;Module&gt;}`

<h3>Member `name`</h3>
*Str*
> `&#x27;Module&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Null"></a>
<h2>`[Class](#class-Class)` `Null` subclass of `[Nullish](#class-Nullish),[PObject](#class-PObject)`</h2>


> Built-in Class of `null` value

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (x)`</h3>
*Closure at bootstrap.xxl:276:21*

> Return `null` value NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method `repr (this)`</h3>
*PyFunc at classes.py:1860 (null_str)*

> to_string/repr method for Null Class: returns &quot;null&quot;

<font color="slategray">
<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:1901 (nullish_setprop)*

> Nullish Object setprop method/operator

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Null&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
<h3>Binary `( (this, ...args)`</h3>
*PyFunc at classes.py:1867 (null_call)*

> `(` method for `null` value (fatal error)

<font color="slategray">
<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Nullish"></a>
<h2>`[Class](#class-Class)` `Nullish` subclass of `[Object](#class-Object)`</h2>


> Mixin for nullish classes.

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

</font>
<h3>Method `getprop (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

</font>
<h3>Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:1901 (nullish_setprop)*

> Nullish Object setprop method/operator

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Nullish&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (l, ...args)`</h3>
*PyFunc at classes.py:1001 (obj_call)*

> default Object `(` binop (fatal error)

</font>
<h3>Binary `. (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
<h3>LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:1901 (nullish_setprop)*

> Nullish Object setprop method/operator

---

<a name="class-Number"></a>
<h2>`[PClass](#class-PClass)` `Number` subclass of `[PObject](#class-PObject)`</h2>


> Built-in int/float wrapper Class

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (x)`</h3>
*Closure at bootstrap.xxl:287:23*

> Convert `x` to a `Number` NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:1166 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `to_float (this)`</h3>
*PyFunc at classes.py:1636 (num_to_float)*

> If value is a float, return `this` If value is an int, return a new Number object

<h3>Method `to_int (this)`</h3>
*PyFunc at classes.py:1646 (num_to_int)*

> If value is an int, return `this` If value is a float, return a new Number object

<h3>Method `to_number (this)`</h3>
*PyFunc at classes.py:1656 (num_to_number)*

> identity method; returns `this`

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Number&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Unary `- (x)`</h3>
*PyFunc at classes.py:1503 (neg)*

> Return negative of `x`

<h3>Unary `~ (this)`</h3>
*PyFunc at classes.py:1629 (bitnot)*

> return bitwise (binary) &quot;not&quot; (complement) of `this`

<h3>Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1566 (ne)*

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
<h3>Binary `&amp; (l, r)`</h3>
*PyFunc at classes.py:1603 (bitand)*

> return bitwise (binary) &quot;and&quot; (conjunction) of `l` and `r`

<font color="slategray">
<h3 color="slategray">Binary `( (l, ...args)`</h3>
*PyFunc at classes.py:1001 (obj_call)*

> default Object `(` binop (fatal error)

</font>
<h3>Binary `* (l, r)`</h3>
*PyFunc at classes.py:1534 (mul)*

> multiply `l` and `r`

<h3>Binary `+ (l, r)`</h3>
*PyFunc at classes.py:1510 (add)*

> add `l` and `r`

<h3>Binary `- (l, r)`</h3>
*PyFunc at classes.py:1523 (sub)*

> subtract `r` from `l`

<font color="slategray">
<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary `/ (l, r)`</h3>
*PyFunc at classes.py:1547 (div)*

> Divide `l` by `r`; always creates float.

<h3>Binary `&lt; (l, r)`</h3>
*PyFunc at classes.py:1581 (lt)*

> return `true` if value of `l` is &lt; the value of `r`

<h3>Binary `&lt;= (l, r)`</h3>
*PyFunc at classes.py:1588 (le)*

> return `true` if value of `l` is &lt;= the value of `r`

<h3>Binary `== (l, r)`</h3>
*PyFunc at classes.py:1558 (eq)*

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary `&gt; (l, r)`</h3>
*PyFunc at classes.py:1595 (gt)*

> return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)

<h3>Binary `&gt;= (l, r)`</h3>
*PyFunc at classes.py:1574 (ge)*

> return `true` if value of `l` is &gt;= the value of `r`

<h3>Binary `| (l, r)`</h3>
*PyFunc at classes.py:1616 (bitor)*

> return bitwise (binary) &quot;or&quot; (union) of `l` and `r`

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Object"></a>
<h2>`[Class](#class-Class)` `Object` subclass of `[Object](#class-Object)`</h2>


> Base Class

<h3>Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3>Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3>Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3>Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3>Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3>Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3>Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3>Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3>Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3>Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3>Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3>Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3>Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

<h3>Member `name`</h3>
*Str*
> `&#x27;Object&#x27;`

<h3>Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3>Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3>Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3>Binary `( (l, ...args)`</h3>
*PyFunc at classes.py:1001 (obj_call)*

> default Object `(` binop (fatal error)

<h3>Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3>Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3>Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3>Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3>LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

---

<a name="class-PClass"></a>
<h2>`[Class](#class-Class)` `PClass` subclass of `[Class](#class-Class)`</h2>


> Metaclass for Primitive/Python value Classes

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method `create (this_class)`</h3>
*PyFunc at classes.py:1136 (pclass_create)*

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<font color="slategray">
<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PClass&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PObject"></a>
<h2>`[PClass](#class-PClass)` `PObject` subclass of `[Object](#class-Object)`</h2>


> Base class for Primitive/Python value Classes

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method `repr (this)`</h3>
*PyFunc at classes.py:1166 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3>Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<font color="slategray">
<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PObject&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3>Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<font color="slategray">
<h3 color="slategray">Binary `( (l, ...args)`</h3>
*PyFunc at classes.py:1001 (obj_call)*

> default Object `(` binop (fatal error)

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3>Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyFunc"></a>
<h2>`[Class](#class-Class)` `PyFunc` subclass of `[Callable](#class-Callable)`</h2>


> Built-in Class for function implemented in Python

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyFunc&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterable"></a>
<h2>`[PClass](#class-PClass)` `PyIterable` subclass of `[PObject](#class-PObject),[Iterable](#class-Iterable)`</h2>


> Wrapper for Python &#x27;iterable&#x27; Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:1166 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

</font>
<h3>Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

<font color="slategray">
<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyIterable&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterableObject"></a>
<h2>`[PClass](#class-PClass)` `PyIterableObject` subclass of `[PyObject](#class-PyObject),[PyIterable](#class-PyIterable)`</h2>


> Built-in Class for a wrapper around an arbitrary Python Object that is an iterable (has an __iter__ method -- an iterator factory).

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class)`</h3>
*PyFunc at classes.py:1136 (pclass_create)*

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:1992 (pyobj_props)*

> return dir() of wrapped Python object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyIterableObject&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:1975 (pyobj_getprop)*

> PyObject `.` binop -- proxies to Python object getattr

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1999 (pyobj_getitem)*

> PyObject `[` binop

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterator"></a>
<h2>`[Class](#class-Class)` `PyIterator` subclass of `[Object](#class-Object),[Iterable](#class-Iterable)`</h2>


> Built-in Class for a wrapper around a Python iterator

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `iter (this)`</h3>
*PyFunc at classes.py:2029 (pyiterator_iter)*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method `next (this, finished_continuation)`</h3>
*PyFunc at classes.py:2039 (pyiterator_next)*

> Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `reversed (this)`</h3>
*Closure at bootstrap.xxl:167:43*

> Creates List from `this`, returns reverse PyIterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*Closure at bootstrap.xxl:175:41*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyIterator&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIteratorObject"></a>
<h2>`[PClass](#class-PClass)` `PyIteratorObject` subclass of `[PyObject](#class-PyObject),[PyIterator](#class-PyIterator)`</h2>


> Built-in Class for a wrapper around an arbitrary Python Object that is an iterator (has a __next__ method -- should also have __iter__ method).

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class)`</h3>
*PyFunc at classes.py:1136 (pclass_create)*

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:2029 (pyiterator_iter)*

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method `next (this, finished_continuation)`</h3>
*PyFunc at classes.py:2039 (pyiterator_next)*

> Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:1992 (pyobj_props)*

> return dir() of wrapped Python object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `reversed (this)`</h3>
*Closure at bootstrap.xxl:167:43*

> Creates List from `this`, returns reverse PyIterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*Closure at bootstrap.xxl:175:41*

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyIteratorObject&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:1975 (pyobj_getprop)*

> PyObject `.` binop -- proxies to Python object getattr

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1999 (pyobj_getitem)*

> PyObject `[` binop

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyObject"></a>
<h2>`[PClass](#class-PClass)` `PyObject` subclass of `[Object](#class-Object)`</h2>


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `props (this)`</h3>
*PyFunc at classes.py:1992 (pyobj_props)*

> return dir() of wrapped Python object

<font color="slategray">
<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyObject&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary `( (this, ...args)`</h3>
*PyFunc at classes.py:2007 (pyobj_call)*

> 

<h3>Binary `. (l, r)`</h3>
*PyFunc at classes.py:1975 (pyobj_getprop)*

> PyObject `.` binop -- proxies to Python object getattr

<font color="slategray">
<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

</font>
<h3>Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1999 (pyobj_getitem)*

> PyObject `[` binop

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyVMFunc"></a>
<h2>`[Class](#class-Class)` `PyVMFunc` subclass of `[Callable](#class-Callable)`</h2>


> Built-in Class for function implemented in Python with access to VM internals

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;PyVMFunc&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Set"></a>
<h2>`[PClass](#class-PClass)` `Set` subclass of `[PyIterable](#class-PyIterable)`</h2>


> Built-in unordered collection of unique elements.

<h3>Method `add (...args)`</h3>
*PyFunc at classes.py:2342 (add)*

> Add an element to a set. This has no effect if the element is already present.

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method `clear (...args)`</h3>
*PyFunc at classes.py:2342 (clear)*

> Remove all elements from this set.

<h3>Method `copy (...args)`</h3>
*PyFunc at classes.py:2342 (copy)*

> Return a shallow copy of a set.

<font color="slategray">
<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font>
<h3>Method `difference (...args)`</h3>
*PyFunc at classes.py:2342 (difference)*

> Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)

<h3>Method `difference_update (...args)`</h3>
*PyFunc at classes.py:2342 (difference_update)*

> Remove all elements of another set from this set.

<h3>Method `discard (...args)`</h3>
*PyFunc at classes.py:2342 (discard)*

> Remove an element from a set if it is a member. If the element is not a member, do nothing.

<font color="slategray">
<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `init (this, arg)`</h3>
*Closure at bootstrap.xxl:298:34*

> init method for Set.  arg passed to this.update().

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `intersection (...args)`</h3>
*PyFunc at classes.py:2342 (intersection)*

> Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)

<h3>Method `intersection_update (...args)`</h3>
*PyFunc at classes.py:2342 (intersection_update)*

> Update a set with the intersection of itself and another.

<h3>Method `is_disjoint (...args)`</h3>
*PyFunc at classes.py:2342 (is_disjoint)*

> Return True if two sets have a null intersection.

<h3>Method `is_subset (...args)`</h3>
*PyFunc at classes.py:2342 (is_subset)*

> Report whether another set contains this set.

<h3>Method `is_superset (...args)`</h3>
*PyFunc at classes.py:2342 (is_superset)*

> Report whether this set contains another set.

<font color="slategray">
<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

</font>
<h3>Method `len (this)`</h3>
*PyFunc at classes.py:1151 (pobj_len)*

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method `pop (...args)`</h3>
*PyFunc at classes.py:2342 (pop)*

> Remove and return an arbitrary set element. Raises KeyError if the set is empty.

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method `remove (...args)`</h3>
*PyFunc at classes.py:2342 (remove)*

> Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.

<h3>Method `repr (this)`</h3>
*Closure at bootstrap.xxl:322:34*

> return representation of Set

<font color="slategray">
<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font>
<h3>Method `symmetric_difference (...args)`</h3>
*PyFunc at classes.py:2342 (symmetric_difference)*

> Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)

<h3>Method `symmetric_difference_update (...args)`</h3>
*PyFunc at classes.py:2342 (symmetric_difference_update)*

> Update a set with the symmetric difference of itself and another.

<font color="slategray">
<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Method `union (...args)`</h3>
*PyFunc at classes.py:2342 (union)*

> Return the union of sets as a new set. (i.e. all elements that are in either set.)

<h3>Method `update (this, arg)`</h3>
*Closure at bootstrap.xxl:308:36*

> Update `this` using `arg.iter()`

<h3>Member `name`</h3>
*Str*
> `&#x27;Set&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-SingletonClass"></a>
<h2>`[Class](#class-Class)` `SingletonClass` subclass of `[Class](#class-Class)`</h2>


> Metaclass for Classes with singleton values. Invoke classes.SingletonClass.new instead of Class.new to create a singleton Class.

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:341:8*

> SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;SingletonClass&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Str"></a>
<h2>`[PClass](#class-PClass)` `Str` subclass of `[PyIterable](#class-PyIterable)`</h2>


> Built-in immutable Unicode string Class

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method `capitalize (self)`</h3>
*PyFunc at classes.py:2342 (capitalize)*

> Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.

<h3>Method `case_fold (self)`</h3>
*PyFunc at classes.py:2342 (case_fold)*

> Return a version of the string suitable for caseless comparisons.

<h3>Method `center (self, width, fillchar)`</h3>
*PyFunc at classes.py:2342 (center)*

> Return a centered string of length width. Padding is done using the specified fill character (default is a space).

<font color="slategray">
<h3 color="slategray">Method `chr (i)`</h3>
*PyFunc at classes.py:1823 (str_chr)*

> Return a Unicode string of one character with ordinal i; 0 &lt;= i &lt;= 0x10ffff

</font>
<h3>Method `count (...args)`</h3>
*PyFunc at classes.py:2342 (count)*

> S.count(sub[, start[, end]]) -&gt; int Return the number of non-overlapping occurrences of substring sub in string S[start:end].  Optional arguments start and end are interpreted as in slice notation.

<font color="slategray">
<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `each_for (this, func)`</h3>
*Closure at bootstrap.xxl:117:35*

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
<h3>Method `ends_with (this, suff)`</h3>
*PyFunc at classes.py:1747 (str_ends_with)*

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

<h3>Method `expand_tabs (self, tabsize)`</h3>
*PyFunc at classes.py:2342 (expand_tabs)*

> Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

<h3>Method `find (...args)`</h3>
*PyFunc at classes.py:2342 (find)*

> S.find(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

<font color="slategray">
<h3 color="slategray">Method `for_each (this, func)`</h3>
*Closure at bootstrap.xxl:107:35*

> Create Iterator from `this`, call `func` with each value.

</font>
<h3>Method `format (...args)`</h3>
*PyFunc at classes.py:2342 (format)*

> S.format(*args, **kwargs) -&gt; str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (&#x27;{&#x27; and &#x27;}&#x27;).

<font color="slategray">
<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method `index (...args)`</h3>
*PyFunc at classes.py:2342 (index)*

> S.index(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

<h3>Method `init (l, value)`</h3>
*PyFunc at classes.py:1181 (pobj_init)*

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method `is_alnum (self)`</h3>
*PyFunc at classes.py:2342 (is_alnum)*

> Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

<h3>Method `is_alpha (self)`</h3>
*PyFunc at classes.py:2342 (is_alpha)*

> Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

<h3>Method `is_ascii (self)`</h3>
*PyFunc at classes.py:2342 (is_ascii)*

> Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

<h3>Method `is_decimal (self)`</h3>
*PyFunc at classes.py:2342 (is_decimal)*

> Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

<h3>Method `is_digit (self)`</h3>
*PyFunc at classes.py:2342 (is_digit)*

> Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are digits and there is at least one character in the string.

<h3>Method `is_identifier (self)`</h3>
*PyFunc at classes.py:2342 (is_identifier)*

> Return True if the string is a valid Python identifier, False otherwise. Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as &quot;def&quot; or &quot;class&quot;.

<h3>Method `is_lower (self)`</h3>
*PyFunc at classes.py:2342 (is_lower)*

> Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

<h3>Method `is_numeric (self)`</h3>
*PyFunc at classes.py:2342 (is_numeric)*

> Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and there is at least one character in the string.

<h3>Method `is_printable (self)`</h3>
*PyFunc at classes.py:2342 (is_printable)*

> Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in repr() or if it is empty.

<h3>Method `is_space (self)`</h3>
*PyFunc at classes.py:2342 (is_space)*

> Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

<h3>Method `is_title (self)`</h3>
*PyFunc at classes.py:2342 (is_title)*

> Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

<h3>Method `is_upper (self)`</h3>
*PyFunc at classes.py:2342 (is_upper)*

> Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

<font color="slategray">
<h3 color="slategray">Method `iter (this)`</h3>
*PyFunc at classes.py:1302 (pyiterable_iter)*

> Return forward iterator.

</font>
<h3>Method `join (this, iterable)`</h3>
*Closure at bootstrap.xxl:361:34*

> Concatenate strings from `iterable` using `this` as the separator.

<h3>Method `len (this)`</h3>
*PyFunc at classes.py:1151 (pobj_len)*

> returns length (of String, List or Dict)

<h3>Method `ljust (self, width, fillchar)`</h3>
*PyFunc at classes.py:2342 (ljust)*

> Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).

<font color="slategray">
<h3 color="slategray">Method `map (this, func)`</h3>
*Closure at bootstrap.xxl:135:30*

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method `map2 (this, func, ignore)`</h3>
*Closure at bootstrap.xxl:150:31*

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method `new (arg)`</h3>
*Closure at bootstrap.xxl:377:20*

> Str Class new (static) method; calls arg.to_str method

</font>
<h3>Method `ord (this)`</h3>
*PyFunc at classes.py:1765 (str_ord)*

> Return the Unicode code point for a one-character string `this`

<font color="slategray">
<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `range (...args)`</h3>
*PyFunc at classes.py:1333 (pyiterable_range)*

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method `replace (self, old, new, count)`</h3>
*PyFunc at classes.py:2342 (replace)*

> Return a copy with all occurrences of substring old replaced by new. count Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences. If the optional argument count is given, only the first count occurrences are replaced.

<font color="slategray">
<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:1166 (pobj_repr)*

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method `reprx (this)`</h3>
*PyFunc at classes.py:1174 (pobj_reprx)*

> for debug: show Class name, and Python repr

<h3 color="slategray">Method `reversed (this)`</h3>
*PyFunc at classes.py:1309 (pyiterable_reversed)*

> Return reverse iterator.

</font>
<h3>Method `rfind (...args)`</h3>
*PyFunc at classes.py:2342 (rfind)*

> S.rfind(sub[, start[, end]]) -&gt; int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

<h3>Method `rsplit (self, sep, maxsplit)`</h3>
*PyFunc at classes.py:2342 (rsplit)*

> Return a list of the words in the string, using sep as the delimiter string. sep The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit. Splits are done starting at the end of the string and working to the front.

<h3>Method `rstrip (self, chars)`</h3>
*PyFunc at classes.py:2342 (rstrip)*

> Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

<font color="slategray">
<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method `slice (this, start, end)`</h3>
*PyFunc at classes.py:1235 (pobj_slice)*

> return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)

<font color="slategray">
<h3 color="slategray">Method `sorted (this, reverse)`</h3>
*PyFunc at classes.py:1318 (pyiterable_sorted)*

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font>
<h3>Method `split (this, sep, limit)`</h3>
*PyFunc at classes.py:1731 (str_split)*

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

<h3>Method `split_lines (self, keepends)`</h3>
*PyFunc at classes.py:2342 (split_lines)*

> Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

<h3>Method `starts_with (this, pref)`</h3>
*PyFunc at classes.py:1772 (str_starts_with)*

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

<h3>Method `strip (this)`</h3>
*PyFunc at classes.py:1786 (str_strip)*

> Return a copy of the string with leading and trailing whitespace removed.

<h3>Method `swap_case (self)`</h3>
*PyFunc at classes.py:2342 (swap_case)*

> Convert uppercase characters to lowercase and lowercase characters to uppercase.

<h3>Method `to_float (this)`</h3>
*PyFunc at classes.py:1793 (str_to_float)*

> Convert string to a floating point Number

<h3>Method `to_int (this, base)`</h3>
*PyFunc at classes.py:1800 (str_to_int)*

> Convert string to integer Number. Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).

<h3>Method `to_lower (self)`</h3>
*PyFunc at classes.py:2342 (to_lower)*

> Return a copy of the string converted to lowercase.

<h3>Method `to_number (this)`</h3>
*PyFunc at classes.py:1812 (str_to_number)*

> Convert string to a Number

<h3>Method `to_str (this)`</h3>
*PyFunc at classes.py:1779 (str_str)*

> Identity method

<h3>Method `to_upper (self)`</h3>
*PyFunc at classes.py:2342 (to_upper)*

> Return a copy of the string converted to uppercase.

<h3>Method `zfill (self, width)`</h3>
*PyFunc at classes.py:2342 (zfill)*

> Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.

<h3>Member `name`</h3>
*Str*
> `&#x27;Str&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Binary `!= (l, r)`</h3>
*PyFunc at classes.py:1566 (ne)*

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:1206 (pobj_differ)*

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font>
<h3>Binary `+ (x, y)`</h3>
*PyFunc at classes.py:1709 (str_concat)*

> String concatenation

<font color="slategray">
<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary `&lt; (l, r)`</h3>
*PyFunc at classes.py:1581 (lt)*

> return `true` if value of `l` is &lt; the value of `r`

<h3>Binary `&lt;= (l, r)`</h3>
*PyFunc at classes.py:1588 (le)*

> return `true` if value of `l` is &lt;= the value of `r`

<h3>Binary `== (l, r)`</h3>
*PyFunc at classes.py:1558 (eq)*

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:1197 (pobj_ident)*

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary `&gt; (l, r)`</h3>
*PyFunc at classes.py:1595 (gt)*

> return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)

<h3>Binary `&gt;= (l, r)`</h3>
*PyFunc at classes.py:1574 (ge)*

> return `true` if value of `l` is &gt;= the value of `r`

<h3>Binary `[ (l, r)`</h3>
*PyFunc at classes.py:1722 (str_get)*

> Str l[r] return `r`&#x27;th character of Str `l`

<font color="slategray">
<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Undefined"></a>
<h2>`[Class](#class-Class)` `Undefined` subclass of `[Nullish](#class-Nullish),[Object](#class-Object)`</h2>


> Class for undefined value.

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_obj, ...args)`</h3>
*PyFunc at classes.py:757 (obj_init)*

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (x)`</h3>
*Closure at bootstrap.xxl:387:26*

> Return `undefined` value NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method `repr (this)`</h3>
*PyFunc at classes.py:2062 (undef_str)*

> to_string/repr method for Undefined Class: returns `&quot;undefined&quot;`

<font color="slategray">
<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:1901 (nullish_setprop)*

> Nullish Object setprop method/operator

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member `name`</h3>
*Str*
> `&#x27;Undefined&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary `( (this, ...args)`</h3>
*PyFunc at classes.py:2069 (undef_call)*

> `(` method for `undefined` value (fatal error). commonly happens when a bad method name is used, so output a &quot;helpful&quot; message.

<font color="slategray">
<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:1883 (nullish_getprop)*

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-XXLObject"></a>
<h2>`[Class](#class-Class)` `XXLObject` subclass of `[Object](#class-Object)`</h2>


> Class for __xxl object

<font color="slategray">
<h3 color="slategray">Method `as_class (this, klass)`</h3>
*PyFunc at classes.py:990 (obj_as_class)*

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method `backtrace ()`</h3>
*PyFunc at xxlobj.py:59 (xxl_backtrace)*

> print VM backtrace to stderr

<h3 color="slategray">Method `break (x)`</h3>
*PyFunc at xxlobj.py:50 (xxl_break)*

> break to python debugger to debug VM argument (if any) available as `x`

<h3 color="slategray">Method `create (this_class, ...args)`</h3>
*PyFunc at classes.py:1054 (class_create)*

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method `delprop (this, name)`</h3>
*PyFunc at classes.py:828 (obj_delprop)*

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method `error (...args)`</h3>
*Closure at bootstrap.xxl:415:28*

> print args (as strings) to stderr

<h3 color="slategray">Method `exit (status)`</h3>
*PyFunc at xxlobj.py:212 (xxl_exit)*

> Exit the interpreter. `status` defaults to zero.

<h3 color="slategray">Method `getclass (this)`</h3>
*PyFunc at classes.py:976 (obj_getclass)*

> return Class for `this`

<h3 color="slategray">Method `getprop (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method `hasprop (l, r)`</h3>
*PyFunc at classes.py:922 (obj_hasprop)*

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method `init (this_class, props)`</h3>
*PyFunc at classes.py:1062 (class_init)*

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method `instance_of (this, c)`</h3>
*PyFunc at classes.py:1009 (obj_instance_of)*

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method `new (this_class, ...args)`</h3>
*Closure at bootstrap.xxl:78:35*

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method `print (...args)`</h3>
*Closure at bootstrap.xxl:408:28*

> print args (as strings) to stdout

<h3 color="slategray">Method `props (this)`</h3>
*PyFunc at classes.py:775 (obj_props)*

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method `pyimport (module)`</h3>
*PyFunc at xxlobj.py:349 (xxl_pyimport)*

> 

<h3 color="slategray">Method `repr (this)`</h3>
*PyFunc at classes.py:783 (obj_repr)*

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method `reprx (l)`</h3>
*PyFunc at classes.py:791 (obj_reprx)*

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method `setclass (this, klass)`</h3>
*PyFunc at classes.py:983 (obj_setclass)*

> set Class for `this`!!

<h3 color="slategray">Method `setprop (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method `subclass_of (this, c)`</h3>
*PyFunc at classes.py:1108 (class_subclass_of)*

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method `to_str (this)`</h3>
*Closure at bootstrap.xxl:67:39*

> Default `to`_str method: calls `this.repr()`.

<h3 color="slategray">Method `uerror (msg)`</h3>
*PyFunc at xxlobj.py:69 (xxl_uerror)*

> 

</font>
<h3>Member `argv`</h3>
*List*
> `[&#x27;--markdown&#x27;]`

<h3>Member `name`</h3>
*Str*
> `&#x27;XXLObject&#x27;`

<h3>Member `parser_vmx`</h3>
*Str*
> `&#x27;parser.vmx&#x27;`

<font color="slategray">
<h3 color="slategray">Unary `! (x)`</h3>
*PyFunc at classes.py:820 (obj_not)*

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary `!= (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `!== (l, r)`</h3>
*PyFunc at classes.py:805 (obj_differ)*

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary `( (this_class, ...args)`</h3>
*PyFunc at classes.py:1098 (class_call)*

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary `. (l, r)`</h3>
*PyFunc at classes.py:911 (obj_getprop)*

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary `.. (this, prop)`</h3>
*PyFunc at classes.py:965 (obj_get_in_supers)*

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary `== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary `=== (l, r)`</h3>
*PyFunc at classes.py:798 (obj_ident)*

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS `. (l, r, value)`</h3>
*PyFunc at classes.py:837 (obj_setprop)*

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

formatted by doc.xxl on 2021-07-12
