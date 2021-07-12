<h1>Module <code>classes</code></h1>
<p>
<p>
<blockquote>Built-in Classes for XXL</blockquote>
<hr>
<a name="class-Bool"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>Bool</code> subclass of <code><a href="#class-PObject">PObject</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for `true` and `false` values</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:93:21</i>
<p>
<blockquote>Return truthiness of `x` (as Bool). NOTE!! A static method, not a metaclass method!!!</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1922 (bool_str)</i>
<p>
<blockquote>return Str representation: &quot;true&quot; or &quot;false&quot;</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Bool&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-BoundMethod"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>BoundMethod</code> subclass of <code><a href="#class-Callable">Callable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a method bound to an Object</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;BoundMethod&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Callable"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Callable</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Virtual base Class for built-in callable classes (BoundMethod, Continuation, PyFunc, PyVMFunc)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Callable&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Class"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Class</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Base Metaclass, home of the default &#x27;new&#x27; method</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Class&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote></font>
<h3>Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Closure"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Closure</code> subclass of <code><a href="#class-Callable">Callable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a native function bound to a scope</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Closure&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Continuation"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Continuation</code> subclass of <code><a href="#class-Callable">Callable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a Continuation</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Continuation&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Dict"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>Dict</code> subclass of <code><a href="#class-PyIterable">PyIterable</a></code></h2>
<p>
<p>
<blockquote>Built-in dictionary mapping Class</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:187:35</i>
<p>
<blockquote>init method for Dict.  arg passed to this.update().</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>items (this)</code></h3>
<i>PyFunc at classes.py:1393 (dict_items)</i>
<p>
<blockquote>Return PyIterable for [key, value] value pairs.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote></font>
<h3>Method <code>keys (this)</code></h3>
<i>PyFunc at classes.py:1400 (dict_keys)</i>
<p>
<blockquote>Return PyIterable for Dict keys.</blockquote>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>
<p>
<blockquote>returns length (of String, List or Dict)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote></font>
<h3>Method <code>pop (obj, key)</code></h3>
<i>PyFunc at classes.py:1386 (dict_pop)</i>
<p>
<blockquote>Remove Dict item with specified `key`.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:225:35</i>
<p>
<blockquote>return representation of Dict</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Method <code>update (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:197:37</i>
<p>
<blockquote>Update `this` using `arg.iter()` legal iterator values: List w/ two elements: `this[l[0]] = l[1];` Non-list: `this[item] = arg[item];`</blockquote>
<h3>Method <code>values (this)</code></h3>
<i>PyFunc at classes.py:1407 (dict_values)</i>
<p>
<blockquote>Return PyIterable for Dict values.</blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Dict&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1368 (dict_getitem)</i>
<p>
<blockquote>`l[r]`</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>LHS <code>[ (l, r, value)</code></h3>
<i>PyFunc at classes.py:1359 (dict_putitem)</i>
<p>
<blockquote>`l[r] = value`</blockquote>
<hr>
<a name="class-Iterable"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Iterable</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Mixin for Classes that can be iterated over</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote></font>
<h3>Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3>Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>iter (this, func)</code></h3>
<i>Closure at bootstrap.xxl:128:31</i>
<p>
<blockquote>Default `iter` method for `Iterable` mixin; fatal error.</blockquote>
<h3>Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3>Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote></font>
<h3>Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>
<p>
<blockquote>Creates List from `this`, returns reverse PyIterator.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>
<p>
<blockquote>Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Iterable&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-List"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>List</code> subclass of <code><a href="#class-PyIterable">PyIterable</a></code></h2>
<p>
<p>
<blockquote>Built-in mutable sequence Class</blockquote>
<h3>Method <code>append (this, item)</code></h3>
<i>PyFunc at classes.py:1440 (list_append)</i>
<p>
<blockquote>append `item`.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote></font>
<h3>Method <code>extend (this, iterable)</code></h3>
<i>Closure at bootstrap.xxl:250:37</i>
<p>
<blockquote>Create an iterator from `iterable`, and iterate appending values to `this`; Returns `null`</blockquote><font color="slategray">
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:240:35</i>
<p>
<blockquote>init method for List: takes Iterable</blockquote>
<h3>Method <code>insert (l, index, object)</code></h3>
<i>PyFunc at classes.py:1465 (list_insert)</i>
<p>
<blockquote>Insert `object` at `index` (0 is first, -1 is last); Returns `null`.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote></font>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>
<p>
<blockquote>returns length (of String, List or Dict)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote></font>
<h3>Method <code>pop (l, index)</code></h3>
<i>PyFunc at classes.py:1448 (list_pop)</i>
<p>
<blockquote>Remove and return item at `index` (default last).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:266:35</i>
<p>
<blockquote>Return representation of `this` List as Str.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>slice (this, start, end)</code></h3>
<i>PyFunc at classes.py:1235 (pobj_slice)</i>
<p>
<blockquote>return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;List&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1457 (list_get)</i>
<p>
<blockquote>`l[r]`</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>LHS <code>[ (l, r, value)</code></h3>
<i>PyFunc at classes.py:1473 (list_put)</i>
<p>
<blockquote>`l[r] = value`</blockquote>
<hr>
<a name="class-ModInfo"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>ModInfo</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for __modinfo Objects (inside Modules)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Method <code>assemble (this, tree, srcfile)</code></h3>
<i>PyFunc at classes.py:2198 (modinfo_assemble)</i>
<p>
<blockquote>Assemble List of Lists representing VM code. `tree`: List of Lists. `srcfile`: source of code (for output only). Returns Closure in __modinfo.module top level scope.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>load_vmx (this, fname)</code></h3>
<i>PyFunc at classes.py:2188 (modinfo_load_vmx)</i>
<p>
<blockquote>Load compiled `.vmx` file; Returns Closure in __modinfo.module top level scope.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;ModInfo&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Module"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Module</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Built-in class for a Module (from import function)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>modules</code></h3>
<i>Dict</i>
<blockquote><code>{&#x27;classes&#x27;: &lt;Module&gt;, &#x27;lib/doc.xxl&#x27;: &lt;Module&gt;, &#x27;parser.vmx&#x27;: &lt;Module&gt;, &#x27;lib/markup.xxl&#x27;: &lt;Module&gt;}</code></blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Module&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Null"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Null</code> subclass of <code><a href="#class-Nullish">Nullish</a>,<a href="#class-PObject">PObject</a></code></h2>
<p>
<p>
<blockquote>Built-in Class of `null` value</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:276:21</i>
<p>
<blockquote>Return `null` value NOTE!! A static method, not a metaclass method!!!</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1860 (null_str)</i>
<p>
<blockquote>to_string/repr method for Null Class: returns &quot;null&quot;</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>
<p>
<blockquote>Nullish Object setprop method/operator</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Null&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:1867 (null_call)</i>
<p>
<blockquote>`(` method for `null` value (fatal error)</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Nullish"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Nullish</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Mixin for nullish classes.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote></font>
<h3>Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote></font>
<h3>Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>
<p>
<blockquote>Nullish Object setprop method/operator</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Nullish&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>
<p>
<blockquote>default Object `(` binop (fatal error)</blockquote></font>
<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote></font>
<h3>LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>
<p>
<blockquote>Nullish Object setprop method/operator</blockquote>
<hr>
<a name="class-Number"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>Number</code> subclass of <code><a href="#class-PObject">PObject</a></code></h2>
<p>
<p>
<blockquote>Built-in int/float wrapper Class</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:287:23</i>
<p>
<blockquote>Convert `x` to a `Number` NOTE!! A static method, not a metaclass method!!!</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>
<p>
<blockquote>return less human-friendly string representation of `this` (use Python repr function on value)</blockquote>
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>to_float (this)</code></h3>
<i>PyFunc at classes.py:1636 (num_to_float)</i>
<p>
<blockquote>If value is a float, return `this` If value is an int, return a new Number object</blockquote>
<h3>Method <code>to_int (this)</code></h3>
<i>PyFunc at classes.py:1646 (num_to_int)</i>
<p>
<blockquote>If value is an int, return `this` If value is a float, return a new Number object</blockquote>
<h3>Method <code>to_number (this)</code></h3>
<i>PyFunc at classes.py:1656 (num_to_number)</i>
<p>
<blockquote>identity method; returns `this`</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Number&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote></font>
<h3>Unary <code>- (x)</code></h3>
<i>PyFunc at classes.py:1503 (neg)</i>
<p>
<blockquote>Return negative of `x`</blockquote>
<h3>Unary <code>~ (this)</code></h3>
<i>PyFunc at classes.py:1629 (bitnot)</i>
<p>
<blockquote>return bitwise (binary) &quot;not&quot; (complement) of `this`</blockquote>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1566 (ne)</i>
<p>
<blockquote>return `true` if value of `l` is different from the value of `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>&amp; (l, r)</code></h3>
<i>PyFunc at classes.py:1603 (bitand)</i>
<p>
<blockquote>return bitwise (binary) &quot;and&quot; (conjunction) of `l` and `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>
<p>
<blockquote>default Object `(` binop (fatal error)</blockquote></font>
<h3>Binary <code>* (l, r)</code></h3>
<i>PyFunc at classes.py:1534 (mul)</i>
<p>
<blockquote>multiply `l` and `r`</blockquote>
<h3>Binary <code>+ (l, r)</code></h3>
<i>PyFunc at classes.py:1510 (add)</i>
<p>
<blockquote>add `l` and `r`</blockquote>
<h3>Binary <code>- (l, r)</code></h3>
<i>PyFunc at classes.py:1523 (sub)</i>
<p>
<blockquote>subtract `r` from `l`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Binary <code>/ (l, r)</code></h3>
<i>PyFunc at classes.py:1547 (div)</i>
<p>
<blockquote>Divide `l` by `r`; always creates float.</blockquote>
<h3>Binary <code>&lt; (l, r)</code></h3>
<i>PyFunc at classes.py:1581 (lt)</i>
<p>
<blockquote>return `true` if value of `l` is &lt; the value of `r`</blockquote>
<h3>Binary <code>&lt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1588 (le)</i>
<p>
<blockquote>return `true` if value of `l` is &lt;= the value of `r`</blockquote>
<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1558 (eq)</i>
<p>
<blockquote>return `true` if value of `l` is the same as value of `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>&gt; (l, r)</code></h3>
<i>PyFunc at classes.py:1595 (gt)</i>
<p>
<blockquote>return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)</blockquote>
<h3>Binary <code>&gt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1574 (ge)</i>
<p>
<blockquote>return `true` if value of `l` is &gt;= the value of `r`</blockquote>
<h3>Binary <code>| (l, r)</code></h3>
<i>PyFunc at classes.py:1616 (bitor)</i>
<p>
<blockquote>return bitwise (binary) &quot;or&quot; (union) of `l` and `r`</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Object"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Object</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Base Class</blockquote>
<h3>Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3>Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3>Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3>Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3>Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3>Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3>Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3>Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3>Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3>Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3>Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3>Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Object&#x27;</code></blockquote>
<h3>Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3>Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3>Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>
<p>
<blockquote>default Object `(` binop (fatal error)</blockquote>
<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3>Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3>Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3>LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<hr>
<a name="class-PClass"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>PClass</code> subclass of <code><a href="#class-Class">Class</a></code></h2>
<p>
<p>
<blockquote>Metaclass for Primitive/Python value Classes</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>
<p>
<blockquote>&#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PClass&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PObject"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>PObject</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Base class for Primitive/Python value Classes</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>
<p>
<blockquote>return less human-friendly string representation of `this` (use Python repr function on value)</blockquote>
<h3>Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote><font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PObject&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote></font>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3>Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>( (l, ...args)</code></h3>
<i>PyFunc at classes.py:1001 (obj_call)</i>
<p>
<blockquote>default Object `(` binop (fatal error)</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3>Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyFunc"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>PyFunc</code> subclass of <code><a href="#class-Callable">Callable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for function implemented in Python</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyFunc&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyIterable"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>PyIterable</code> subclass of <code><a href="#class-PObject">PObject</a>,<a href="#class-Iterable">Iterable</a></code></h2>
<p>
<p>
<blockquote>Wrapper for Python &#x27;iterable&#x27; Objects (Dict, List, Str); Also returned by Dict.items(), Dict.keys(), Dict.values(), Object.props(), static method PyIterable.range().</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>
<p>
<blockquote>return less human-friendly string representation of `this` (use Python repr function on value)</blockquote>
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote></font>
<h3>Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyIterable&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyIterableObject"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>PyIterableObject</code> subclass of <code><a href="#class-PyObject">PyObject</a>,<a href="#class-PyIterable">PyIterable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a wrapper around an arbitrary Python Object that is an iterable (has an __iter__ method -- an iterator factory).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>
<p>
<blockquote>&#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote>
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>
<p>
<blockquote>return dir() of wrapped Python object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyIterableObject&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>
<p>
<blockquote>PyObject `.` binop -- proxies to Python object getattr</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>
<p>
<blockquote>PyObject `[` binop</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyIterator"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>PyIterator</code> subclass of <code><a href="#class-Object">Object</a>,<a href="#class-Iterable">Iterable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a wrapper around a Python iterator</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:2029 (pyiterator_iter)</i>
<p>
<blockquote>Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote></font>
<h3>Method <code>next (this, finished_continuation)</code></h3>
<i>PyFunc at classes.py:2039 (pyiterator_next)</i>
<p>
<blockquote>Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>
<p>
<blockquote>Creates List from `this`, returns reverse PyIterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>
<p>
<blockquote>Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyIterator&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyIteratorObject"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>PyIteratorObject</code> subclass of <code><a href="#class-PyObject">PyObject</a>,<a href="#class-PyIterator">PyIterator</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a wrapper around an arbitrary Python Object that is an iterator (has a __next__ method -- should also have __iter__ method).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class)</code></h3>
<i>PyFunc at classes.py:1136 (pclass_create)</i>
<p>
<blockquote>&#x27;create&#x27; method for PClass metaclass makes an instance of this_class backed by a CPObject used to create PClass subclass objects (Number, List, Dict, Bool, Null)</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:2029 (pyiterator_iter)</i>
<p>
<blockquote>Returns `this.` https://docs.python.org/3/library/stdtypes.html#typeiter says an iterator should have an __iter__ method.</blockquote>
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote>
<h3 color="slategray">Method <code>next (this, finished_continuation)</code></h3>
<i>PyFunc at classes.py:2039 (pyiterator_next)</i>
<p>
<blockquote>Returns next value; calls `finished_continuation` (eg; block leave label or `return`) to call when iterator exhausted.</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>
<p>
<blockquote>return dir() of wrapped Python object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>Closure at bootstrap.xxl:167:43</i>
<p>
<blockquote>Creates List from `this`, returns reverse PyIterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>Closure at bootstrap.xxl:175:41</i>
<p>
<blockquote>Return sorted List of values from iterator (creates List first). `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyIteratorObject&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>
<p>
<blockquote>PyObject `.` binop -- proxies to Python object getattr</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>
<p>
<blockquote>PyObject `[` binop</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyObject"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>PyObject</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for a wrapper around an arbitrary Python Object (returned by pyimport, or operations on PyObjects)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:1992 (pyobj_props)</i>
<p>
<blockquote>return dir() of wrapped Python object</blockquote><font color="slategray">
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyObject&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote></font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:2007 (pyobj_call)</i>
<p>
<blockquote></blockquote>
<h3>Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1975 (pyobj_getprop)</i>
<p>
<blockquote>PyObject `.` binop -- proxies to Python object getattr</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote></font>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1999 (pyobj_getitem)</i>
<p>
<blockquote>PyObject `[` binop</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-PyVMFunc"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>PyVMFunc</code> subclass of <code><a href="#class-Callable">Callable</a></code></h2>
<p>
<p>
<blockquote>Built-in Class for function implemented in Python with access to VM internals</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;PyVMFunc&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Set"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>Set</code> subclass of <code><a href="#class-PyIterable">PyIterable</a></code></h2>
<p>
<p>
<blockquote>Built-in unordered collection of unique elements.</blockquote>
<h3>Method <code>add (...args)</code></h3>
<i>PyFunc at classes.py:2342 (add)</i>
<p>
<blockquote>Add an element to a set. This has no effect if the element is already present.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Method <code>clear (...args)</code></h3>
<i>PyFunc at classes.py:2342 (clear)</i>
<p>
<blockquote>Remove all elements from this set.</blockquote>
<h3>Method <code>copy (...args)</code></h3>
<i>PyFunc at classes.py:2342 (copy)</i>
<p>
<blockquote>Return a shallow copy of a set.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote></font>
<h3>Method <code>difference (...args)</code></h3>
<i>PyFunc at classes.py:2342 (difference)</i>
<p>
<blockquote>Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)</blockquote>
<h3>Method <code>difference_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (difference_update)</i>
<p>
<blockquote>Remove all elements of another set from this set.</blockquote>
<h3>Method <code>discard (...args)</code></h3>
<i>PyFunc at classes.py:2342 (discard)</i>
<p>
<blockquote>Remove an element from a set if it is a member. If the element is not a member, do nothing.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote>
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>init (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:298:34</i>
<p>
<blockquote>init method for Set.  arg passed to this.update().</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>intersection (...args)</code></h3>
<i>PyFunc at classes.py:2342 (intersection)</i>
<p>
<blockquote>Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)</blockquote>
<h3>Method <code>intersection_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (intersection_update)</i>
<p>
<blockquote>Update a set with the intersection of itself and another.</blockquote>
<h3>Method <code>is_disjoint (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_disjoint)</i>
<p>
<blockquote>Return True if two sets have a null intersection.</blockquote>
<h3>Method <code>is_subset (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_subset)</i>
<p>
<blockquote>Report whether another set contains this set.</blockquote>
<h3>Method <code>is_superset (...args)</code></h3>
<i>PyFunc at classes.py:2342 (is_superset)</i>
<p>
<blockquote>Report whether this set contains another set.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote></font>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>
<p>
<blockquote>returns length (of String, List or Dict)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote></font>
<h3>Method <code>pop (...args)</code></h3>
<i>PyFunc at classes.py:2342 (pop)</i>
<p>
<blockquote>Remove and return an arbitrary set element. Raises KeyError if the set is empty.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote></font>
<h3>Method <code>remove (...args)</code></h3>
<i>PyFunc at classes.py:2342 (remove)</i>
<p>
<blockquote>Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.</blockquote>
<h3>Method <code>repr (this)</code></h3>
<i>Closure at bootstrap.xxl:322:34</i>
<p>
<blockquote>return representation of Set</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote></font>
<h3>Method <code>symmetric_difference (...args)</code></h3>
<i>PyFunc at classes.py:2342 (symmetric_difference)</i>
<p>
<blockquote>Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)</blockquote>
<h3>Method <code>symmetric_difference_update (...args)</code></h3>
<i>PyFunc at classes.py:2342 (symmetric_difference_update)</i>
<p>
<blockquote>Update a set with the symmetric difference of itself and another.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Method <code>union (...args)</code></h3>
<i>PyFunc at classes.py:2342 (union)</i>
<p>
<blockquote>Return the union of sets as a new set. (i.e. all elements that are in either set.)</blockquote>
<h3>Method <code>update (this, arg)</code></h3>
<i>Closure at bootstrap.xxl:308:36</i>
<p>
<blockquote>Update `this` using `arg.iter()`</blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Set&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-SingletonClass"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>SingletonClass</code> subclass of <code><a href="#class-Class">Class</a></code></h2>
<p>
<p>
<blockquote>Metaclass for Classes with singleton values. Invoke classes.SingletonClass.new instead of Class.new to create a singleton Class.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:341:8</i>
<p>
<blockquote>SingletonClass new method: invoke to create a new class with a single value. First time: calls `this_class.create` to create obj, then calls obj.init(); After: returns previous value.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;SingletonClass&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Str"></a>
<h2><code><a href="#class-PClass">PClass</a></code> <code>Str</code> subclass of <code><a href="#class-PyIterable">PyIterable</a></code></h2>
<p>
<p>
<blockquote>Built-in immutable Unicode string Class</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Method <code>capitalize (self)</code></h3>
<i>PyFunc at classes.py:2342 (capitalize)</i>
<p>
<blockquote>Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.</blockquote>
<h3>Method <code>case_fold (self)</code></h3>
<i>PyFunc at classes.py:2342 (case_fold)</i>
<p>
<blockquote>Return a version of the string suitable for caseless comparisons.</blockquote>
<h3>Method <code>center (self, width, fillchar)</code></h3>
<i>PyFunc at classes.py:2342 (center)</i>
<p>
<blockquote>Return a centered string of length width. Padding is done using the specified fill character (default is a space).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>chr (i)</code></h3>
<i>PyFunc at classes.py:1823 (str_chr)</i>
<p>
<blockquote>Return a Unicode string of one character with ordinal i; 0 &lt;= i &lt;= 0x10ffff</blockquote></font>
<h3>Method <code>count (...args)</code></h3>
<i>PyFunc at classes.py:2342 (count)</i>
<p>
<blockquote>S.count(sub[, start[, end]]) -&gt; int Return the number of non-overlapping occurrences of substring sub in string S[start:end].  Optional arguments start and end are interpreted as in slice notation.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>each_for (this, func)</code></h3>
<i>Closure at bootstrap.xxl:117:35</i>
<p>
<blockquote>Create reverse Iterator from `this`, call `func` with each value. returns `null`</blockquote></font>
<h3>Method <code>ends_with (this, suff)</code></h3>
<i>PyFunc at classes.py:1747 (str_ends_with)</i>
<p>
<blockquote>Return `true` if `this` ends with the suffix `suff`, `false` otherwise.</blockquote>
<h3>Method <code>expand_tabs (self, tabsize)</code></h3>
<i>PyFunc at classes.py:2342 (expand_tabs)</i>
<p>
<blockquote>Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.</blockquote>
<h3>Method <code>find (...args)</code></h3>
<i>PyFunc at classes.py:2342 (find)</i>
<p>
<blockquote>S.find(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>for_each (this, func)</code></h3>
<i>Closure at bootstrap.xxl:107:35</i>
<p>
<blockquote>Create Iterator from `this`, call `func` with each value.</blockquote></font>
<h3>Method <code>format (...args)</code></h3>
<i>PyFunc at classes.py:2342 (format)</i>
<p>
<blockquote>S.format(*args, **kwargs) -&gt; str Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (&#x27;{&#x27; and &#x27;}&#x27;).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote></font>
<h3>Method <code>index (...args)</code></h3>
<i>PyFunc at classes.py:2342 (index)</i>
<p>
<blockquote>S.index(sub[, start[, end]]) -&gt; int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.</blockquote>
<h3>Method <code>init (l, value)</code></h3>
<i>PyFunc at classes.py:1181 (pobj_init)</i>
<p>
<blockquote>default PObject init method (fatal error)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote></font>
<h3>Method <code>is_alnum (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_alnum)</i>
<p>
<blockquote>Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.</blockquote>
<h3>Method <code>is_alpha (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_alpha)</i>
<p>
<blockquote>Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.</blockquote>
<h3>Method <code>is_ascii (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_ascii)</i>
<p>
<blockquote>Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.</blockquote>
<h3>Method <code>is_decimal (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_decimal)</i>
<p>
<blockquote>Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.</blockquote>
<h3>Method <code>is_digit (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_digit)</i>
<p>
<blockquote>Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are digits and there is at least one character in the string.</blockquote>
<h3>Method <code>is_identifier (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_identifier)</i>
<p>
<blockquote>Return True if the string is a valid Python identifier, False otherwise. Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as &quot;def&quot; or &quot;class&quot;.</blockquote>
<h3>Method <code>is_lower (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_lower)</i>
<p>
<blockquote>Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.</blockquote>
<h3>Method <code>is_numeric (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_numeric)</i>
<p>
<blockquote>Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and there is at least one character in the string.</blockquote>
<h3>Method <code>is_printable (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_printable)</i>
<p>
<blockquote>Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in repr() or if it is empty.</blockquote>
<h3>Method <code>is_space (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_space)</i>
<p>
<blockquote>Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.</blockquote>
<h3>Method <code>is_title (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_title)</i>
<p>
<blockquote>Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.</blockquote>
<h3>Method <code>is_upper (self)</code></h3>
<i>PyFunc at classes.py:2342 (is_upper)</i>
<p>
<blockquote>Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>iter (this)</code></h3>
<i>PyFunc at classes.py:1302 (pyiterable_iter)</i>
<p>
<blockquote>Return forward iterator.</blockquote></font>
<h3>Method <code>join (this, iterable)</code></h3>
<i>Closure at bootstrap.xxl:361:34</i>
<p>
<blockquote>Concatenate strings from `iterable` using `this` as the separator.</blockquote>
<h3>Method <code>len (this)</code></h3>
<i>PyFunc at classes.py:1151 (pobj_len)</i>
<p>
<blockquote>returns length (of String, List or Dict)</blockquote>
<h3>Method <code>ljust (self, width, fillchar)</code></h3>
<i>PyFunc at classes.py:2342 (ljust)</i>
<p>
<blockquote>Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).</blockquote><font color="slategray">
<h3 color="slategray">Method <code>map (this, func)</code></h3>
<i>Closure at bootstrap.xxl:135:30</i>
<p>
<blockquote>Create Iterator from `this`; Return List of results of `func` passed each iterator item.</blockquote>
<h3 color="slategray">Method <code>map2 (this, func, ignore)</code></h3>
<i>Closure at bootstrap.xxl:150:31</i>
<p>
<blockquote>Return List of results of `func` passed each iterator item, ignores any returns with value `ignore` (defaults to `null`).</blockquote>
<h3 color="slategray">Method <code>new (arg)</code></h3>
<i>Closure at bootstrap.xxl:377:20</i>
<p>
<blockquote>Str Class new (static) method; calls arg.to_str method</blockquote></font>
<h3>Method <code>ord (this)</code></h3>
<i>PyFunc at classes.py:1765 (str_ord)</i>
<p>
<blockquote>Return the Unicode code point for a one-character string `this`</blockquote><font color="slategray">
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>range (...args)</code></h3>
<i>PyFunc at classes.py:1333 (pyiterable_range)</i>
<p>
<blockquote>Static method: returns PyIterable for an integer range; iter() method generates fresh Iterators. range(10): returns Iterable for 0..9; range(1,10): returns Iterable for 1..9; range(1,10,2): returns Iterable for odd numbers 1..9</blockquote></font>
<h3>Method <code>replace (self, old, new, count)</code></h3>
<i>PyFunc at classes.py:2342 (replace)</i>
<p>
<blockquote>Return a copy with all occurrences of substring old replaced by new. count Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences. If the optional argument count is given, only the first count occurrences are replaced.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:1166 (pobj_repr)</i>
<p>
<blockquote>return less human-friendly string representation of `this` (use Python repr function on value)</blockquote>
<h3 color="slategray">Method <code>reprx (this)</code></h3>
<i>PyFunc at classes.py:1174 (pobj_reprx)</i>
<p>
<blockquote>for debug: show Class name, and Python repr</blockquote>
<h3 color="slategray">Method <code>reversed (this)</code></h3>
<i>PyFunc at classes.py:1309 (pyiterable_reversed)</i>
<p>
<blockquote>Return reverse iterator.</blockquote></font>
<h3>Method <code>rfind (...args)</code></h3>
<i>PyFunc at classes.py:2342 (rfind)</i>
<p>
<blockquote>S.rfind(sub[, start[, end]]) -&gt; int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.</blockquote>
<h3>Method <code>rsplit (self, sep, maxsplit)</code></h3>
<i>PyFunc at classes.py:2342 (rsplit)</i>
<p>
<blockquote>Return a list of the words in the string, using sep as the delimiter string. sep The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit. Splits are done starting at the end of the string and working to the front.</blockquote>
<h3>Method <code>rstrip (self, chars)</code></h3>
<i>PyFunc at classes.py:2342 (rstrip)</i>
<p>
<blockquote>Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<h3>Method <code>slice (this, start, end)</code></h3>
<i>PyFunc at classes.py:1235 (pobj_slice)</i>
<p>
<blockquote>return a subrange (slice) of `this` starting at position `start` ending at position `end` (defaults to remainder)</blockquote><font color="slategray">
<h3 color="slategray">Method <code>sorted (this, reverse)</code></h3>
<i>PyFunc at classes.py:1318 (pyiterable_sorted)</i>
<p>
<blockquote>Return sorted List of iterator values. `reverse` is Bool to sort in reverse order (defaults to `false`).</blockquote></font>
<h3>Method <code>split (this, sep, limit)</code></h3>
<i>PyFunc at classes.py:1731 (str_split)</i>
<p>
<blockquote>Return a List of the words in the string, using sep as the delimiter string (default to `null` -- any whitespace). Limit to `limit` return values (defaults to -1 -- no limit)</blockquote>
<h3>Method <code>split_lines (self, keepends)</code></h3>
<i>PyFunc at classes.py:2342 (split_lines)</i>
<p>
<blockquote>Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.</blockquote>
<h3>Method <code>starts_with (this, pref)</code></h3>
<i>PyFunc at classes.py:1772 (str_starts_with)</i>
<p>
<blockquote>Return `true` if `this` starts with prefix `pref, `false` otherwise.</blockquote>
<h3>Method <code>strip (this)</code></h3>
<i>PyFunc at classes.py:1786 (str_strip)</i>
<p>
<blockquote>Return a copy of the string with leading and trailing whitespace removed.</blockquote>
<h3>Method <code>swap_case (self)</code></h3>
<i>PyFunc at classes.py:2342 (swap_case)</i>
<p>
<blockquote>Convert uppercase characters to lowercase and lowercase characters to uppercase.</blockquote>
<h3>Method <code>to_float (this)</code></h3>
<i>PyFunc at classes.py:1793 (str_to_float)</i>
<p>
<blockquote>Convert string to a floating point Number</blockquote>
<h3>Method <code>to_int (this, base)</code></h3>
<i>PyFunc at classes.py:1800 (str_to_int)</i>
<p>
<blockquote>Convert string to integer Number. Int `base` defaults to zero (accept 0xXXX, 0oOOO, 0bBBB).</blockquote>
<h3>Method <code>to_lower (self)</code></h3>
<i>PyFunc at classes.py:2342 (to_lower)</i>
<p>
<blockquote>Return a copy of the string converted to lowercase.</blockquote>
<h3>Method <code>to_number (this)</code></h3>
<i>PyFunc at classes.py:1812 (str_to_number)</i>
<p>
<blockquote>Convert string to a Number</blockquote>
<h3>Method <code>to_str (this)</code></h3>
<i>PyFunc at classes.py:1779 (str_str)</i>
<p>
<blockquote>Identity method</blockquote>
<h3>Method <code>to_upper (self)</code></h3>
<i>PyFunc at classes.py:2342 (to_upper)</i>
<p>
<blockquote>Return a copy of the string converted to uppercase.</blockquote>
<h3>Method <code>zfill (self, width)</code></h3>
<i>PyFunc at classes.py:2342 (zfill)</i>
<p>
<blockquote>Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.</blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Str&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote></font>
<h3>Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:1566 (ne)</i>
<p>
<blockquote>return `true` if value of `l` is different from the value of `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:1206 (pobj_differ)</i>
<p>
<blockquote>Check if value of PObject `l` is not the same Python Object as value of PObject `r`</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote></font>
<h3>Binary <code>+ (x, y)</code></h3>
<i>PyFunc at classes.py:1709 (str_concat)</i>
<p>
<blockquote>String concatenation</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote></font>
<h3>Binary <code>&lt; (l, r)</code></h3>
<i>PyFunc at classes.py:1581 (lt)</i>
<p>
<blockquote>return `true` if value of `l` is &lt; the value of `r`</blockquote>
<h3>Binary <code>&lt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1588 (le)</i>
<p>
<blockquote>return `true` if value of `l` is &lt;= the value of `r`</blockquote>
<h3>Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:1558 (eq)</i>
<p>
<blockquote>return `true` if value of `l` is the same as value of `r`</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:1197 (pobj_ident)</i>
<p>
<blockquote>Check if value of PObject `l` is the same Python Object as value of PObject `r`</blockquote></font>
<h3>Binary <code>&gt; (l, r)</code></h3>
<i>PyFunc at classes.py:1595 (gt)</i>
<p>
<blockquote>return `true` if value of `l` is &gt; the value of `r` (implemented as `!(l &lt;= r)`)</blockquote>
<h3>Binary <code>&gt;= (l, r)</code></h3>
<i>PyFunc at classes.py:1574 (ge)</i>
<p>
<blockquote>return `true` if value of `l` is &gt;= the value of `r`</blockquote>
<h3>Binary <code>[ (l, r)</code></h3>
<i>PyFunc at classes.py:1722 (str_get)</i>
<p>
<blockquote>Str l[r] return `r`&#x27;th character of Str `l`</blockquote><font color="slategray">
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-Undefined"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>Undefined</code> subclass of <code><a href="#class-Nullish">Nullish</a>,<a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Class for undefined value.</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_obj, ...args)</code></h3>
<i>PyFunc at classes.py:757 (obj_init)</i>
<p>
<blockquote>default init method for Object class a fatal error if any arguments given</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (x)</code></h3>
<i>Closure at bootstrap.xxl:387:26</i>
<p>
<blockquote>Return `undefined` value NOTE!! A static method, not a metaclass method!!!</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote></font>
<h3>Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:2062 (undef_str)</i>
<p>
<blockquote>to_string/repr method for Undefined Class: returns `&quot;undefined&quot;`</blockquote><font color="slategray">
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:1901 (nullish_setprop)</i>
<p>
<blockquote>Nullish Object setprop method/operator</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote></font>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;Undefined&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote></font>
<h3>Binary <code>( (this, ...args)</code></h3>
<i>PyFunc at classes.py:2069 (undef_call)</i>
<p>
<blockquote>`(` method for `undefined` value (fatal error). commonly happens when a bad method name is used, so output a &quot;helpful&quot; message.</blockquote><font color="slategray">
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:1883 (nullish_getprop)</i>
<p>
<blockquote>`.` method for Nullish (null, undefined) values. Fatal error if unknown property. Allows all Object methods (JavaScript is stricter, Python is not).</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
<a name="class-XXLObject"></a>
<h2><code><a href="#class-Class">Class</a></code> <code>XXLObject</code> subclass of <code><a href="#class-Object">Object</a></code></h2>
<p>
<p>
<blockquote>Class for __xxl object</blockquote><font color="slategray">
<h3 color="slategray">Method <code>as_class (this, klass)</code></h3>
<i>PyFunc at classes.py:990 (obj_as_class)</i>
<p>
<blockquote>return an Object of Class `klass`, sharing properties with `this`. Use for calling superclass methods: `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Method <code>backtrace ()</code></h3>
<i>PyFunc at xxlobj.py:59 (xxl_backtrace)</i>
<p>
<blockquote>print VM backtrace to stderr</blockquote>
<h3 color="slategray">Method <code>break (x)</code></h3>
<i>PyFunc at xxlobj.py:50 (xxl_break)</i>
<p>
<blockquote>break to python debugger to debug VM argument (if any) available as `x`</blockquote>
<h3 color="slategray">Method <code>create (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1054 (class_create)</i>
<p>
<blockquote>Default create method for `Class` (the base metaclass); Creates an empty instance of this_class (called from `Class.new`).</blockquote>
<h3 color="slategray">Method <code>delprop (this, name)</code></h3>
<i>PyFunc at classes.py:828 (obj_delprop)</i>
<p>
<blockquote>Delete property `name` from Object `this` (only effects `this` -- never Class or superclasses)</blockquote>
<h3 color="slategray">Method <code>error (...args)</code></h3>
<i>Closure at bootstrap.xxl:415:28</i>
<p>
<blockquote>print args (as strings) to stderr</blockquote>
<h3 color="slategray">Method <code>exit (status)</code></h3>
<i>PyFunc at xxlobj.py:212 (xxl_exit)</i>
<p>
<blockquote>Exit the interpreter. `status` defaults to zero.</blockquote>
<h3 color="slategray">Method <code>getclass (this)</code></h3>
<i>PyFunc at classes.py:976 (obj_getclass)</i>
<p>
<blockquote>return Class for `this`</blockquote>
<h3 color="slategray">Method <code>getprop (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>hasprop (l, r)</code></h3>
<i>PyFunc at classes.py:922 (obj_hasprop)</i>
<p>
<blockquote>Return `true` if object `l` has own (Str) property `r` (not interited).</blockquote>
<h3 color="slategray">Method <code>init (this_class, props)</code></h3>
<i>PyFunc at classes.py:1062 (class_init)</i>
<p>
<blockquote>init method for meta-class &quot;Class&quot; -- used to create new Classes. `props` is Dict holding properties (see doc/creating-classes.md and src/const.py CLASS_PROPS)</blockquote>
<h3 color="slategray">Method <code>instance_of (this, c)</code></h3>
<i>PyFunc at classes.py:1009 (obj_instance_of)</i>
<p>
<blockquote>return `true` if Object `this` is an instance of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>new (this_class, ...args)</code></h3>
<i>Closure at bootstrap.xxl:78:35</i>
<p>
<blockquote>Default metaclass (Class) new method; Manually invoked as `SomeClass.new`. Calls `this_class.create` to create obj, and then calls `obj.init()` (ie; the `SomeClass.init` method).</blockquote>
<h3 color="slategray">Method <code>print (...args)</code></h3>
<i>Closure at bootstrap.xxl:408:28</i>
<p>
<blockquote>print args (as strings) to stdout</blockquote>
<h3 color="slategray">Method <code>props (this)</code></h3>
<i>PyFunc at classes.py:775 (obj_props)</i>
<p>
<blockquote>returns an Iterable for (String) property names of `this` Object</blockquote>
<h3 color="slategray">Method <code>pyimport (module)</code></h3>
<i>PyFunc at xxlobj.py:349 (xxl_pyimport)</i>
<p>
<blockquote></blockquote>
<h3 color="slategray">Method <code>repr (this)</code></h3>
<i>PyFunc at classes.py:783 (obj_repr)</i>
<p>
<blockquote>Default Object string representation method (calls Python repr(this))</blockquote>
<h3 color="slategray">Method <code>reprx (l)</code></h3>
<i>PyFunc at classes.py:791 (obj_reprx)</i>
<p>
<blockquote>for debug: show Class, and Python value (which may include id?)</blockquote>
<h3 color="slategray">Method <code>setclass (this, klass)</code></h3>
<i>PyFunc at classes.py:983 (obj_setclass)</i>
<p>
<blockquote>set Class for `this`!!</blockquote>
<h3 color="slategray">Method <code>setprop (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Method <code>subclass_of (this, c)</code></h3>
<i>PyFunc at classes.py:1108 (class_subclass_of)</i>
<p>
<blockquote>Return `true` if Class `this` is a subclass of Class (or List of Classes) `c`</blockquote>
<h3 color="slategray">Method <code>to_str (this)</code></h3>
<i>Closure at bootstrap.xxl:67:39</i>
<p>
<blockquote>Default `to`_str method: calls `this.repr()`.</blockquote>
<h3 color="slategray">Method <code>uerror (msg)</code></h3>
<i>PyFunc at xxlobj.py:69 (xxl_uerror)</i>
<p>
<blockquote></blockquote></font>
<h3>Member <code>argv</code></h3>
<i>List</i>
<blockquote><code>[&#x27;--gh-markdown&#x27;]</code></blockquote>
<h3>Member <code>name</code></h3>
<i>Str</i>
<blockquote><code>&#x27;XXLObject&#x27;</code></blockquote>
<h3>Member <code>parser_vmx</code></h3>
<i>Str</i>
<blockquote><code>&#x27;parser.vmx&#x27;</code></blockquote><font color="slategray">
<h3 color="slategray">Unary <code>! (x)</code></h3>
<i>PyFunc at classes.py:820 (obj_not)</i>
<p>
<blockquote>Object unary logical &quot;not&quot; operator; returns `true` if `x` is &quot;falsey&quot; (false, zero, null, or undefined)</blockquote>
<h3 color="slategray">Binary <code>!= (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>!== (l, r)</code></h3>
<i>PyFunc at classes.py:805 (obj_differ)</i>
<p>
<blockquote>Test if `l` and `r` refer to different Objects</blockquote>
<h3 color="slategray">Binary <code>( (this_class, ...args)</code></h3>
<i>PyFunc at classes.py:1098 (class_call)</i>
<p>
<blockquote>`(` binop for Class -- fatal error (but common mistake if you have Python fingers) -- tells you to use .new method!!</blockquote>
<h3 color="slategray">Binary <code>. (l, r)</code></h3>
<i>PyFunc at classes.py:911 (obj_getprop)</i>
<p>
<blockquote>Object getprop method/operator return `r` (String) property of object `l`</blockquote>
<h3 color="slategray">Binary <code>.. (this, prop)</code></h3>
<i>PyFunc at classes.py:965 (obj_get_in_supers)</i>
<p>
<blockquote>Object `..` operator; for calling superclass methods Looks for `prop` as property or method of superclasses of `this`; can be used w/ `this.as_class(MyClass)..method`.</blockquote>
<h3 color="slategray">Binary <code>== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">Binary <code>=== (l, r)</code></h3>
<i>PyFunc at classes.py:798 (obj_ident)</i>
<p>
<blockquote>Test if `l` and `r` refer to the same Object</blockquote>
<h3 color="slategray">LHS <code>. (l, r, value)</code></h3>
<i>PyFunc at classes.py:837 (obj_setprop)</i>
<p>
<blockquote>Object setprop method/operator store `value` as `r` (String) property of object `l`</blockquote></font>
<hr>
formatted by doc.xxl on 2021-07-12