<h1 class="heading"><span class="name">Interfaces</span></h1>

*Interfaces* define additional sets of functionality that classes can implement; however, interfaces contain no implementation, except for static methods and static fields. An interface specifies a contract that a class implementing the interface must follow. Interfaces can contain shared (known as "static" in many compiled languages) or instance methods, shared fields, properties, and events. All interface members must be public. Interfaces cannot define constructors. The .NET runtime allows an interface to require that any class that implements it must also implement one or more other interfaces.

When you define a class, you list the interfaces which it supports following a colon after the class name. The value of `⎕USING` (possibly set by `:Using`) is used to locate Interface names.

If you specify that your class implements a certain `Interface`, you must provide all of the members (methods, properties, and so forth) defined for that `Interface`. However, some Interfaces are only marker Interfaces and do not actually specify any members.

An example is the `TemperatureControlCtl2` custom control described in Chapter 11, which derives from `System.Web.UI.Control`. The first line of this class definition reads:
```apl
:Class TemperatureConverterCtl2: System.Web.UI.Control,
    System.Web.UI.IPostBackDataHandler,
    System.Web.UI.IPostBackEventHandler
 
```

Following the colon, the first name is the base class. Following the (optional) base class name is the list of interfaces which are implemented. The `TemperatureControlCtl2` custom control implements two interfaces named `IPostBackDataHandler` and `IPostBackEventHandler`. These interfaces are required for a custom control that intends to render the HTML for its own form elements in a Web page. These interfaces define certain methods that get called at the appropriate time by the page framework when a Web page is constructed for the browser. It is therefore essential that the class implements all the methods specified by the interface, even if they do nothing.

The base class, `System.Web.UI.Control`, defines an optional Interface called `INamingContainer`. A class based on `Control` that implements `INamingContainer` specifies that its child controls are to be assigned unique ID attributes within an entire application. This is a marker interface with no methods or properties defined for it.

See these examples in Chapter 11 for further details.
