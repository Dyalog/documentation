<h1 class="heading"><span class="name">Interfaces</span></h1>

_Interfaces_ define additional sets of functionality that classes can implement; however, interfaces contain no implementation except for static methods and static fields. An interface specifies a contract that a class implementing the interface must follow. Interfaces can contain shared (known as "static" in many compiled languages) or instance methods, shared fields, properties, and events. All interface members must be public. Interfaces cannot define constructors. The .NET runtime allows an interface to require that any class that implements it must also implement one or more other interfaces.

When you define a class, you list the interfaces which it supports following a colon after the class name. The value of [`⎕USING`](../../../language-reference-guide/system-functions/using/) (possibly set by `:Using`) is used to locate interface names.

If you specify that your class implements a certain <code class="language-nonAPL">interface</code>, you must provide all of the members (<code class="language-nonAPL">methods</code>, <code class="language-nonAPL">properties</code>, and so on) defined for that <code class="language-nonAPL">interface</code>. However, some interfaces are only marker interfaces and do not specify any members.

<h4 class="example">Example</h4>
```apl
:Class Names: Object, IEnumerable,IEnumerator
```

This class is illustrated in the **aplclasses8.apln** APL Source file in **[DYALOG]/Samples/aplclasses/aplclasses8**.

Following the colon, the first name is the base class; in this case it is the most basic .NET class, <code class="language-nonAPL">Object</code>. After the (optional) base class name is the list of interfaces that are implemented (omitted if there are no such interfaces). The <code class="language-nonAPL">Names</code> class implements two interfaces, <code class="language-nonAPL">IEnumerable</code> and <code class="language-nonAPL">IEnumerator</code>.

<code class="language-nonAPL">IEnumerable</code> and <code class="language-nonAPL">IEnumerator</code> are required interfaces for an object that allows itself to be enumerated, that is, its contents can be iterated though one at a time. They define certain methods that get called at the appropriate time by the calling code when enumeration is required (for example, the <code class="language-nonAPL">foreach</code> C# keyword or `:For`/`:In` in Dyalog APL. For more information, see [Microsoft's documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=net-8.0).
