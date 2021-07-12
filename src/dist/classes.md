<h1>Module <code>classes</code></h1>


> Built-in Classes for XXL

---

<a name="class-Bool"></a>
<h2><code>[PClass](#class-PClass)</code> <code>Bool</code> subclass of <code>[PObject](#class-PObject)</code></h2>


> Built-in Class for `true` and `false` values

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:93:21</i>

> Return truthiness of `x` (as Bool). NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1922 (bool_str)</i>

> return Str representation: &quot;true&quot; or &quot;false&quot;

<font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Bool&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-BoundMethod"></a>
<h2><code>[Class](#class-Class)</code> <code>BoundMethod</code> subclass of <code>[Callable](#class-Callable)</code></h2>


> Built-in Class for a method bound to an Object

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;BoundMethod&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Callable"></a>
<h2><code>[Class](#class-Class)</code> <code>Callable</code> subclass of <code>[Object](#class-Object)</code></h2>


> Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Callable&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Class"></a>
<h2><code>[Class](#class-Class)</code> <code>Class</code> subclass of <code>[Object](#class-Object)</code></h2>


> Base Metaclass, home of the default &#x27;new&#x27; method

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Class&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Closure"></a>
<h2><code>[Class](#class-Class)</code> <code>Closure</code> subclass of <code>[Callable](#class-Callable)</code></h2>


> Built-in Class for a native function bound to a scope

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Closure&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Continuation"></a>
<h2><code>[Class](#class-Class)</code> <code>Continuation</code> subclass of <code>[Callable](#class-Callable)</code></h2>


> Built-in Class for a Continuation

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Continuation&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Dict"></a>
<h2><code>[PClass](#class-PClass)</code> <code>Dict</code> subclass of <code>[PyIterable](#class-PyIterable)</code></h2>


> Built-in dictionary mapping Class

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:187:35</i>

> init method for Dict.  arg passed to this.update().

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>items (this)</code></h3>
<i>PyFunc at classes.py:1393 (dict_items)</i>

> Return PyIterable for [key, value] value pairs.

<font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

</font>
<h3>Method <code>keys (this)</code></h3>
<i>PyFunc at classes.py:1400 (dict_keys)</i>

> Return PyIterable for Dict keys.

<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method <code>pop (obj, key)</code></h3>
<i>PyFunc at classes.py:1386 (dict_pop)</i>

> Remove Dict item with specified `key`.

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:225:35</i>

> return representation of Dict

<font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Method <code>update (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:197:37</i>

> Update `this` using `arg.iter()` legal iterator values: List w/ two elements: `this[l[0]] = l[1];` Non-list: `this[item] = arg[item];`

<h3>Method <code>values (this)</code></h3>
<i>PyFunc at classes.py:1407 (dict_values)</i>

> Return PyIterable for Dict values.

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Dict&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1368 (dict_getitem)</i>

> `l[r]`

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>LHS <code>[ (l, r, value)</code></h3>
<i>PyFunc at classes.py:1359 (dict_putitem)</i>

> `l[r] = value`

---

<a name="class-Iterable"></a>
<h2><code>[Class](#class-Class)</code> <code>Iterable</code> subclass of <code>[Object](#class-Object)</code></h2>


> Mixin for Classes that can be iterated over

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font>
<h3>Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3>Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<font color="slategray">
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>iter (this, func)</code></h3>
<i>Closure at bootstrap.xxl:128:31</i>

> Default `iter` method for `Iterable` mixin; fatal error.

<h3>Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3>Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

</font>
<h3>Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>

> Creates List from `this`, returns reverse PyIterator.

<font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Iterable&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-List"></a>
<h2><code>[PClass](#class-PClass)</code> <code>List</code> subclass of <code>[PyIterable](#class-PyIterable)</code></h2>


> Built-in mutable sequence Class

<h3>Method <code>append (this, item)</code></h3>
<i>PyFunc at classes.py:1440 (list_append)</i>

> append `item`.

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
<h3>Method <code>extend (this, iterable)</code></h3>
<i>Closure at bootstrap.xxl:250:37</i>

> Create an iterator from `iterable`, and iterate appending values to `this`; Returns `null`

<font color="slategray">
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:240:35</i>

> init method for List: takes Iterable

<h3>Method <code>insert (l, index, object)</code></h3>
<i>PyFunc at classes.py:1465 (list_insert)</i>

> Insert `object` at `index` (0 is first, -1 is last); Returns `null`.

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

</font>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method <code>pop (l, index)</code></h3>
<i>PyFunc at classes.py:1448 (list_pop)</i>

> Remove and return item at `index` (default last).

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:266:35</i>

> Return representation of `this` List as Str.

<font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>slice (this, start, end)</code></h3>
<i>PyFunc at classes.py:1235 (pobj_slice)</i>

> return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)

<font color="slategray">
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;List&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1457 (list_get)</i>

> `l[r]`

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>LHS <code>[ (l, r, value)</code></h3>
<i>PyFunc at classes.py:1473 (list_put)</i>

> `l[r] = value`

---

<a name="class-ModInfo"></a>
<h2><code>[Class](#class-Class)</code> <code>ModInfo</code> subclass of <code>[Object](#class-Object)</code></h2>


> Built-in Class for __modinfo Objects (inside Modules)

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method <code>assemble (this, tree, srcfile)</code></h3>
<i>PyFunc at classes.py:2198 (modinfo_assemble)</i>

> Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.

<font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>load_vmx (this, fname)</code></h3>
<i>PyFunc at classes.py:2188 (modinfo_load_vmx)</i>

> Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;ModInfo&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Module"></a>
<h2><code>[Class](#class-Class)</code> <code>Module</code> subclass of <code>[Object](#class-Object)</code></h2>


> Built-in class for a Module (from import function)

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>modules</code></h3>
<i>Dict</i>
> <code>{&#x27;classes&#x27;: &lt;Module&gt;, &#x27;lib/doc.xxl&#x27;: &lt;Module&gt;, &#x27;parser.vmx&#x27;: &lt;Module&gt;, &#x27;lib/markup.xxl&#x27;: &lt;Module&gt;}</code>

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Module&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Null"></a>
<h2><code>[Class](#class-Class)</code> <code>Null</code> subclass of <code>[Nullish](#class-Nullish),[PObject](#class-PObject)</code></h2>


> Built-in Class of `null` value

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:276:21</i>

> Return `null` value NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1860 (null_str)</i>

> to_string/repr method for Null Class: returns &quot;null&quot;

<font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>

> Nullish Object setprop method/operator

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Null&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:1867 (null_call)</i>

> `(` method for `null` value (fatal error)

<font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Nullish"></a>
<h2><code>[Class](#class-Class)</code> <code>Nullish</code> subclass of <code>[Object](#class-Object)</code></h2>


> Mixin for nullish classes.

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

</font>
<h3>Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

</font>
<h3>Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>

> Nullish Object setprop method/operator

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Nullish&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>

> default Object `(` binop (fatal error)

</font>
<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<font color="slategray">
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

</font>
<h3>LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>

> Nullish Object setprop method/operator

---

<a name="class-Number"></a>
<h2><code>[PClass](#class-PClass)</code> <code>Number</code> subclass of <code>[PObject](#class-PObject)</code></h2>


> Built-in int/float wrapper Class

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:287:23</i>

> Convert `x` to a `Number` NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>to_float (this)</code></h3>
<i>PyFunc at classes.py:1636 (num_to_float)</i>

> If value is a float, return `this` If value is an int, return a new Number object

<h3>Method <code>to_int (this)</code></h3>
<i>PyFunc at classes.py:1646 (num_to_int)</i>

> If value is an int, return `this` If value is a float, return a new Number object

<h3>Method <code>to_number (this)</code></h3>
<i>PyFunc at classes.py:1656 (num_to_number)</i>

> identity method; returns `this`

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Number&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Unary <code>- (x)</code></h3>
<i>PyFunc at classes.py:1503 (neg)</i>

> Return negative of `x`

<h3>Unary <code>~ (this)</code></h3>
<i>PyFunc at classes.py:1629 (bitnot)</i>

> return bitwise (binary) &quot;not&quot; (complement) of `this`

<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1566 (ne)</i>

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>&amp; (l, r)</code></h3>
<i>PyFunc at classes.py:1603 (bitand)</i>

> return bitwise (binary) &quot;and&quot; (conjunction) of `l` and `r`

<font color="slategray">
<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>

> default Object `(` binop (fatal error)

</font>
<h3>Binary <code>* (l, r)</code></h3>
<i>PyFunc at classes.py:1534 (mul)</i>

> multiply `l` and `r`

<h3>Binary <code>+ (l, r)</code></h3>
<i>PyFunc at classes.py:1510 (add)</i>

> add `l` and `r`

<h3>Binary <code>- (l, r)</code></h3>
<i>PyFunc at classes.py:1523 (sub)</i>

> subtract `r` from `l`

<font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary <code>/ (l, r)</code></h3>
<i>PyFunc at classes.py:1547 (div)</i>

> Divide `l` by `r`; always creates float.

<h3>Binary <code>&lt; (l, r)</code></h3>
<i>PyFunc at classes.py:1581 (lt)</i>

> return `true` if value of `l` is &lt; the value of `r`

<h3>Binary <code>&lt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1588 (le)</i>

> return `true` if value of `l` is &lt;= the value of `r`

<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1558 (eq)</i>

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>&gt; (l, r)</code></h3>
<i>PyFunc at classes.py:1595 (gt)</i>

> return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)

<h3>Binary <code>&gt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1574 (ge)</i>

> return `true` if value of `l` is &gt;= the value of `r`

<h3>Binary <code>| (l, r)</code></h3>
<i>PyFunc at classes.py:1616 (bitor)</i>

> return bitwise (binary) &quot;or&quot; (union) of `l` and `r`

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Object"></a>
<h2><code>[Class](#class-Class)</code> <code>Object</code> subclass of <code>[Object](#class-Object)</code></h2>


> Base Class

<h3>Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3>Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3>Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3>Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3>Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3>Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3>Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3>Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3>Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3>Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3>Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3>Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Object&#x27;</code>

<h3>Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3>Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3>Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>

> default Object `(` binop (fatal error)

<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3>Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3>Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3>LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

---

<a name="class-PClass"></a>
<h2><code>[Class](#class-Class)</code> <code>PClass</code> subclass of <code>[Class](#class-Class)</code></h2>


> Metaclass for Primitive/Python value Classes

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PClass&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PObject"></a>
<h2><code>[PClass](#class-PClass)</code> <code>PObject</code> subclass of <code>[Object](#class-Object)</code></h2>


> Base class for Primitive/Python value Classes

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3>Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PObject&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3>Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<font color="slategray">
<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>

> default Object `(` binop (fatal error)

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3>Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyFunc"></a>
<h2><code>[Class](#class-Class)</code> <code>PyFunc</code> subclass of <code>[Callable](#class-Callable)</code></h2>


> Built-in Class for function implemented in Python

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyFunc&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterable"></a>
<h2><code>[PClass](#class-PClass)</code> <code>PyIterable</code> subclass of <code>[PObject](#class-PObject),[Iterable](#class-Iterable)</code></h2>


> Wrapper for Python &#x27;iterable&#x27; Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

</font>
<h3>Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

<font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyIterable&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterableObject"></a>
<h2><code>[PClass](#class-PClass)</code> <code>PyIterableObject</code> subclass of <code>[PyObject](#class-PyObject),[PyIterable](#class-PyIterable)</code></h2>


> Built-in Class for a wrapper around an arbitrary Python Object that is an iterable (has an __iter__ method -- an iterator factory).

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>

> return dir() of wrapped Python object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyIterableObject&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>

> PyObject `.` binop -- proxies to Python object getattr

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>

> PyObject `[` binop

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIterator"></a>
<h2><code>[Class](#class-Class)</code> <code>PyIterator</code> subclass of <code>[Object](#class-Object),[Iterable](#class-Iterable)</code></h2>


> Built-in Class for a wrapper around a Python iterator

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:2029 (pyiterator_iter)</i>

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method <code>next (this, finished_continuation)</code></h3>
<i>PyFunc at classes.py:2039 (pyiterator_next)</i>

> Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>

> Creates List from `this`, returns reverse PyIterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyIterator&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyIteratorObject"></a>
<h2><code>[PClass](#class-PClass)</code> <code>PyIteratorObject</code> subclass of <code>[PyObject](#class-PyObject),[PyIterator](#class-PyIterator)</code></h2>


> Built-in Class for a wrapper around an arbitrary Python Object that is an iterator (has a __next__ method -- should also have __iter__ method).

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>

> &#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:2029 (pyiterator_iter)</i>

> Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.

<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method <code>next (this, finished_continuation)</code></h3>
<i>PyFunc at classes.py:2039 (pyiterator_next)</i>

> Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>

> return dir() of wrapped Python object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>

> Creates List from `this`, returns reverse PyIterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>

> Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyIteratorObject&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>

> PyObject `.` binop -- proxies to Python object getattr

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>

> PyObject `[` binop

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyObject"></a>
<h2><code>[PClass](#class-PClass)</code> <code>PyObject</code> subclass of <code>[Object](#class-Object)</code></h2>


> Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>

> return dir() of wrapped Python object

<font color="slategray">
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyObject&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:2007 (pyobj_call)</i>

> 

<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>

> PyObject `.` binop -- proxies to Python object getattr

<font color="slategray">
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

</font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>

> PyObject `[` binop

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-PyVMFunc"></a>
<h2><code>[Class](#class-Class)</code> <code>PyVMFunc</code> subclass of <code>[Callable](#class-Callable)</code></h2>


> Built-in Class for function implemented in Python with access to VM internals

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;PyVMFunc&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Set"></a>
<h2><code>[PClass](#class-PClass)</code> <code>Set</code> subclass of <code>[PyIterable](#class-PyIterable)</code></h2>


> Built-in unordered collection of unique elements.

<h3>Method <code>add (...args)</code></h3>
<i>PyFunc at classes.py:2342 (add)</i>

> Add an element to a set. This has no effect if the element is already present.

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method <code>clear (...args)</code></h3>
<i>PyFunc at classes.py:2342 (clear)</i>

> Remove all elements from this set.

<h3>Method <code>copy (...args)</code></h3>
<i>PyFunc at classes.py:2342 (copy)</i>

> Return a shallow copy of a set.

<font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

</font>
<h3>Method <code>difference (...args)</code></h3>
<i>PyFunc at classes.py:2342 (difference)</i>

> Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)

<h3>Method <code>difference_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (difference_update)</i>

> Remove all elements of another set from this set.

<h3>Method <code>discard (...args)</code></h3>
<i>PyFunc at classes.py:2342 (discard)</i>

> Remove an element from a set if it is a member. If the element is not a member, do nothing.

<font color="slategray">
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:298:34</i>

> init method for Set.  arg passed to this.update().

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>intersection (...args)</code></h3>
<i>PyFunc at classes.py:2342 (intersection)</i>

> Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)

<h3>Method <code>intersection_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (intersection_update)</i>

> Update a set with the intersection of itself and another.

<h3>Method <code>is_disjoint (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_disjoint)</i>

> Return True if two sets have a null intersection.

<h3>Method <code>is_subset (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_subset)</i>

> Report whether another set contains this set.

<h3>Method <code>is_superset (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_superset)</i>

> Report whether this set contains another set.

<font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

</font>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>

> returns length (of String, List or Dict)

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

</font>
<h3>Method <code>pop (...args)</code></h3>
<i>PyFunc at classes.py:2342 (pop)</i>

> Remove and return an arbitrary set element. Raises KeyError if the set is empty.

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method <code>remove (...args)</code></h3>
<i>PyFunc at classes.py:2342 (remove)</i>

> Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.

<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:322:34</i>

> return representation of Set

<font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font>
<h3>Method <code>symmetric_difference (...args)</code></h3>
<i>PyFunc at classes.py:2342 (symmetric_difference)</i>

> Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)

<h3>Method <code>symmetric_difference_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (symmetric_difference_update)</i>

> Update a set with the symmetric difference of itself and another.

<font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Method <code>union (...args)</code></h3>
<i>PyFunc at classes.py:2342 (union)</i>

> Return the union of sets as a new set. (i.e. all elements that are in either set.)

<h3>Method <code>update (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:308:36</i>

> Update `this` using `arg.iter()`

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Set&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-SingletonClass"></a>
<h2><code>[Class](#class-Class)</code> <code>SingletonClass</code> subclass of <code>[Class](#class-Class)</code></h2>


> Metaclass for Classes with singleton values. Invoke classes.SingletonClass.new instead of Class.new to create a singleton Class.

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:341:8</i>

> SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;SingletonClass&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Str"></a>
<h2><code>[PClass](#class-PClass)</code> <code>Str</code> subclass of <code>[PyIterable](#class-PyIterable)</code></h2>


> Built-in immutable Unicode string Class

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

</font>
<h3>Method <code>capitalize (self)</code></h3>
<i>PyFunc at classes.py:2342 (capitalize)</i>

> Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.

<h3>Method <code>case_fold (self)</code></h3>
<i>PyFunc at classes.py:2342 (case_fold)</i>

> Return a version of the string suitable for caseless comparisons.

<h3>Method <code>center (self, width, fillchar)</code></h3>
<i>PyFunc at classes.py:2342 (center)</i>

> Return a centered string of length width. Padding is done using the specified fill character (default is a space).

<font color="slategray">
<h3 color="slategray">Method <code>chr (i)</code></h3>
<i>PyFunc at classes.py:1823 (str_chr)</i>

> Return a Unicode string of one character with ordinal i; 0 &lt;= i &lt;= 0x10ffff

</font>
<h3>Method <code>count (...args)</code></h3>
<i>PyFunc at classes.py:2342 (count)</i>

> S.count(sub[, start[, end]]) -&gt; int Return the number of non-overlapping occurrences of substring sub in string S[start:end].  Optional arguments start and end are interpreted as in slice notation.

<font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>

> Create reverse Iterator from `this`, call `func` with each value. returns `null`

</font>
<h3>Method <code>ends_with (this, suff)</code></h3>
<i>PyFunc at classes.py:1747 (str_ends_with)</i>

> Return `true` if `this` ends with the suffix `suff`, `false` otherwise.

<h3>Method <code>expand_tabs (self, tabsize)</code></h3>
<i>PyFunc at classes.py:2342 (expand_tabs)</i>

> Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

<h3>Method <code>find (...args)</code></h3>
<i>PyFunc at classes.py:2342 (find)</i>

> S.find(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

<font color="slategray">
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>

> Create Iterator from `this`, call `func` with each value.

</font>
<h3>Method <code>format (...args)</code></h3>
<i>PyFunc at classes.py:2342 (format)</i>

> S.format(*args, **kwargs) -&gt; str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (&#x27;{&#x27; and &#x27;}&#x27;).

<font color="slategray">
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

</font>
<h3>Method <code>index (...args)</code></h3>
<i>PyFunc at classes.py:2342 (index)</i>

> S.index(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.

<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>

> default PObject init method (fatal error)

<font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

</font>
<h3>Method <code>is_alnum (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_alnum)</i>

> Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

<h3>Method <code>is_alpha (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_alpha)</i>

> Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

<h3>Method <code>is_ascii (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_ascii)</i>

> Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

<h3>Method <code>is_decimal (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_decimal)</i>

> Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

<h3>Method <code>is_digit (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_digit)</i>

> Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are digits and there is at least one character in the string.

<h3>Method <code>is_identifier (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_identifier)</i>

> Return True if the string is a valid Python identifier, False otherwise. Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as &quot;def&quot; or &quot;class&quot;.

<h3>Method <code>is_lower (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_lower)</i>

> Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

<h3>Method <code>is_numeric (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_numeric)</i>

> Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and there is at least one character in the string.

<h3>Method <code>is_printable (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_printable)</i>

> Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in repr() or if it is empty.

<h3>Method <code>is_space (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_space)</i>

> Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

<h3>Method <code>is_title (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_title)</i>

> Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

<h3>Method <code>is_upper (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_upper)</i>

> Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

<font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>

> Return forward iterator.

</font>
<h3>Method <code>join (this, iterable)</code></h3>
<i>Closure at bootstrap.xxl:361:34</i>

> Concatenate strings from `iterable` using `this` as the separator.

<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>

> returns length (of String, List or Dict)

<h3>Method <code>ljust (self, width, fillchar)</code></h3>
<i>PyFunc at classes.py:2342 (ljust)</i>

> Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).

<font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>

> Create Iterator from `this`; Return List of results of `func` passed each iterator item.

<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>

> Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).

<h3 color="slategray">Method <code>new (arg)</code></h3>
<i>Closure at bootstrap.xxl:377:20</i>

> Str Class new (static) method; calls arg.to_str method

</font>
<h3>Method <code>ord (this)</code></h3>
<i>PyFunc at classes.py:1765 (str_ord)</i>

> Return the Unicode code point for a one-character string `this`

<font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>

> Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9

</font>
<h3>Method <code>replace (self, old, new, count)</code></h3>
<i>PyFunc at classes.py:2342 (replace)</i>

> Return a copy with all occurrences of substring old replaced by new. count Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences. If the optional argument count is given, only the first count occurrences are replaced.

<font color="slategray">
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>

> return less human-friendly string representation of `this` (use Python repr function on value)

<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>

> for debug: show Class name, and Python repr

<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>

> Return reverse iterator.

</font>
<h3>Method <code>rfind (...args)</code></h3>
<i>PyFunc at classes.py:2342 (rfind)</i>

> S.rfind(sub[, start[, end]]) -&gt; int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

<h3>Method <code>rsplit (self, sep, maxsplit)</code></h3>
<i>PyFunc at classes.py:2342 (rsplit)</i>

> Return a list of the words in the string, using sep as the delimiter string. sep The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit. Splits are done starting at the end of the string and working to the front.

<h3>Method <code>rstrip (self, chars)</code></h3>
<i>PyFunc at classes.py:2342 (rstrip)</i>

> Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

<font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
<h3>Method <code>slice (this, start, end)</code></h3>
<i>PyFunc at classes.py:1235 (pobj_slice)</i>

> return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)

<font color="slategray">
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>

> Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).

</font>
<h3>Method <code>split (this, sep, limit)</code></h3>
<i>PyFunc at classes.py:1731 (str_split)</i>

> Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)

<h3>Method <code>split_lines (self, keepends)</code></h3>
<i>PyFunc at classes.py:2342 (split_lines)</i>

> Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

<h3>Method <code>starts_with (this, pref)</code></h3>
<i>PyFunc at classes.py:1772 (str_starts_with)</i>

> Return `true` if `this` starts with prefix `pref, `false` otherwise.

<h3>Method <code>strip (this)</code></h3>
<i>PyFunc at classes.py:1786 (str_strip)</i>

> Return a copy of the string with leading and trailing whitespace removed.

<h3>Method <code>swap_case (self)</code></h3>
<i>PyFunc at classes.py:2342 (swap_case)</i>

> Convert uppercase characters to lowercase and lowercase characters to uppercase.

<h3>Method <code>to_float (this)</code></h3>
<i>PyFunc at classes.py:1793 (str_to_float)</i>

> Convert string to a floating point Number

<h3>Method <code>to_int (this, base)</code></h3>
<i>PyFunc at classes.py:1800 (str_to_int)</i>

> Convert string to integer Number. Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).

<h3>Method <code>to_lower (self)</code></h3>
<i>PyFunc at classes.py:2342 (to_lower)</i>

> Return a copy of the string converted to lowercase.

<h3>Method <code>to_number (this)</code></h3>
<i>PyFunc at classes.py:1812 (str_to_number)</i>

> Convert string to a Number

<h3>Method <code>to_str (this)</code></h3>
<i>PyFunc at classes.py:1779 (str_str)</i>

> Identity method

<h3>Method <code>to_upper (self)</code></h3>
<i>PyFunc at classes.py:2342 (to_upper)</i>

> Return a copy of the string converted to uppercase.

<h3>Method <code>zfill (self, width)</code></h3>
<i>PyFunc at classes.py:2342 (zfill)</i>

> Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Str&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

</font>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1566 (ne)</i>

> return `true` if value of `l` is different from the value of `r`

<font color="slategray">
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>

> Check if value of PObject `l` is not the same Python Object as value of PObject `r`

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

</font>
<h3>Binary <code>+ (x, y)</code></h3>
<i>PyFunc at classes.py:1709 (str_concat)</i>

> String concatenation

<font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

</font>
<h3>Binary <code>&lt; (l, r)</code></h3>
<i>PyFunc at classes.py:1581 (lt)</i>

> return `true` if value of `l` is &lt; the value of `r`

<h3>Binary <code>&lt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1588 (le)</i>

> return `true` if value of `l` is &lt;= the value of `r`

<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1558 (eq)</i>

> return `true` if value of `l` is the same as value of `r`

<font color="slategray">
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>

> Check if value of PObject `l` is the same Python Object as value of PObject `r`

</font>
<h3>Binary <code>&gt; (l, r)</code></h3>
<i>PyFunc at classes.py:1595 (gt)</i>

> return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)

<h3>Binary <code>&gt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1574 (ge)</i>

> return `true` if value of `l` is &gt;= the value of `r`

<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1722 (str_get)</i>

> Str l[r] return `r`&#x27;th character of Str `l`

<font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-Undefined"></a>
<h2><code>[Class](#class-Class)</code> <code>Undefined</code> subclass of <code>[Nullish](#class-Nullish),[Object](#class-Object)</code></h2>


> Class for undefined value.

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>

> default init method for Object class a fatal error if any arguments given

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:387:26</i>

> Return `undefined` value NOTE!! A static method, not a metaclass method!!!

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

</font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:2062 (undef_str)</i>

> to_string/repr method for Undefined Class: returns `&quot;undefined&quot;`

<font color="slategray">
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>

> Nullish Object setprop method/operator

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

</font>
<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;Undefined&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

</font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:2069 (undef_call)</i>

> `(` method for `undefined` value (fatal error). commonly happens when a bad method name is used, so output a &quot;helpful&quot; message.

<font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>

> `.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

<a name="class-XXLObject"></a>
<h2><code>[Class](#class-Class)</code> <code>XXLObject</code> subclass of <code>[Object](#class-Object)</code></h2>


> Class for __xxl object

<font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>

> return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.

<h3 color="slategray">Method <code>backtrace ()</code></h3>
<i>PyFunc at xxlobj.py:59 (xxl_backtrace)</i>

> print VM backtrace to stderr

<h3 color="slategray">Method <code>break (x)</code></h3>
<i>PyFunc at xxlobj.py:50 (xxl_break)</i>

> break to python debugger to debug VM argument (if any) available as `x`

<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>

> Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).

<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>

> Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)

<h3 color="slategray">Method <code>error (...args)</code></h3>
<i>Closure at bootstrap.xxl:415:28</i>

> print args (as strings) to stderr

<h3 color="slategray">Method <code>exit (status)</code></h3>
<i>PyFunc at xxlobj.py:212 (xxl_exit)</i>

> Exit the interpreter. `status` defaults to zero.

<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>

> return Class for `this`

<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>

> Return `true` if object `l` has own (Str) property `r` (not interited).

<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>

> init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)

<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>

> return `true` if Object `this` is an instance of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>

> Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).

<h3 color="slategray">Method <code>print (...args)</code></h3>
<i>Closure at bootstrap.xxl:408:28</i>

> print args (as strings) to stdout

<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>

> returns an Iterable for (String) property names of `this` Object

<h3 color="slategray">Method <code>pyimport (module)</code></h3>
<i>PyFunc at xxlobj.py:349 (xxl_pyimport)</i>

> 

<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>

> Default Object string representation method (calls Python repr(this))

<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>

> for debug: show Class, and Python value (which may include id?)

<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>

> set Class for `this`!!

<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>

> Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`

<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>

> Default `to`_str method: calls `this.repr()`.

<h3 color="slategray">Method <code>uerror (msg)</code></h3>
<i>PyFunc at xxlobj.py:69 (xxl_uerror)</i>

> 

</font>
<h3>Member <code>argv</code></h3>
<i>List</i>
> <code>[&#x27;--markdown&#x27;]</code>

<h3>Member <code>name</code></h3>
<i>Str</i>
> <code>&#x27;XXLObject&#x27;</code>

<h3>Member <code>parser_vmx</code></h3>
<i>Str</i>
> <code>&#x27;parser.vmx&#x27;</code>

<font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>

> Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)

<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>

> Test if `l` and `r` refer to different Objects

<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>

> `(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!

<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>

> Object getprop method/operator return `r` (String) property of object `l`

<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>

> Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.

<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>

> Test if `l` and `r` refer to the same Object

<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>

> Object setprop method/operator store `value` as `r` (String) property of object `l`

</font>
---

formatted by doc.xxl on 2021-07-12
