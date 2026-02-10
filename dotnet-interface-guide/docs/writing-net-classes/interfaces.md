# Interfaces

Interfaces define additional sets of functionality that classes can implement; however, interfaces contain no implementation except for static methods and static fields. An interface specifies a contract that a class implementing the interface must follow. Interfaces can contain shared (known as "static" in many compiled languages) or instance methods, shared fields, properties, and events. All interface members must be public. Interfaces cannot define constructors. The .NET runtime allows an interface to require that any class that implements it must also implement one or more other interfaces.

When you define a class, you list the interfaces which it supports following a colon after the class name. The value of `⎕USING` (possibly set by `:Using`) is used to locate interface names.

If you specify that your class implements a certain interface, you must provide all of the members (methods, properties, and so on) defined for that interface. However, some interfaces are only marker interfaces and do not specify any members.

Example
```apl
:Class Names: Object, IEnumerable,IEnumerator
```

This class is illustrated in the **aplclasses8.apln** APL Source file in **[DYALOG]/Samples/aplclasses/aplclasses8**.

Following the colon, the first name is the base class; in this case it is the most basic .NET class, Object. After the (optional) base class name is the list of interfaces that are implemented (omitted if there are no such interfaces). The Names class implements two interfaces, IEnumerable and IEnumerator.

IEnumerable and IEnumerator are required interfaces for an object that allows itself to be enumerated, that is, its contents can be iterated though one at a time. They define certain methods that get called at the appropriate time by the calling code when enumeration is required (for example, the `foreach` C# keyword or `:For`/`:In` in Dyalog APL. For more information, see [https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=net-8.0](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=net-8.0).
