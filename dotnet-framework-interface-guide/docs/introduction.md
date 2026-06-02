<h1 class="heading"><span class="name">Introduction</span></h1>

Dyalog's .NET Framework Interface features include:

- the ability to create and use objects that are instances of .NET classes.

    The .NET Framework defines a [_Common Type System_](https://learn.microsoft.com/en-us/dotnet/standard/base-types/common-type-system). This provides a set of data types, permitted values, and permitted operations. All co‑operating languages are supposed to use these types so that operations and values can be checked (by the Common Language Runtime) at run time. The .NET Framework provides its own built-in class library that provides all the primitive data types, together with higher-level classes that perform useful operations.

- the ability to define new .NET classes in Dyalog that can then be used from other .NET languages such as C# and VB.NET.

    Dyalog allows you to create and use instances of .NET classes, thereby granting access to the huge amount of component technology that is provided by the .NET Framework. It is also possible to create class libraries (assemblies) in Dyalog. Assemblies enable you to export APL technology packaged as .NET classes, which can then be used from other .NET programming languages such as C# and Visual Basic.

    The ability to create and use classes in Dyalog also means that you can design APL applications built using APL (and non-APL) components. Such an approach can provide benefits in terms of reliability, software management and re-usage, and maintenance.

    One of the most important .NET class libraries is called <code class="language-nonAPL">System.Windows.Forms</code>, which is designed to support traditional Windows GUI programming. Visual Studio .NET, which is used to develop GUI applications in Visual Basic and C#, produces code that uses <code class="language-nonAPL">System.Windows.Forms</code>. Dyalog allows you to use <code class="language-nonAPL">System.Windows.Forms</code> instead of (and in some cases, in conjunction with) the built-in Dyalog GUI objects such as the Dyalog Grid, to program the Graphical User Interface.

- the ability to write web services in Dyalog.

    Web services are programmable components that can be called by different applications. Web services have the same goal as COM, but they are technically platform‑independent and use HTTP as the communications protocol with an application. A web service can be used either internally by a single application or exposed externally over the Internet for use by any number of applications.

- the ability to write ASP.NET web pages in Dyalog.

    ASP.NET is a new version of Microsoft Active Server Page technology, and makes it easier to develop and deploy dynamic web applications. To supplement ASP.NET, there are some important new .NET class libraries, including WebForms which allow you to build browser-based user interfaces using the same object-oriented mechanism as used with <code class="language-nonAPL">Windows.Forms</code> for the Windows GUI. The use of these component libraries replaces basic HTML programming.

    ASP.NET pages are server-side scripts that are usually written in C# or Visual Basic. However, you can also employ Dyalog directly as a scripting language (APL source files) to write ASP.NET web pages. In addition, you can call Dyalog workspaces directly from ASP.NET pages, and write custom server-side controls that can be incorporated into ASP.NET pages.

These features give you a wide range of possibilities for using Dyalog to build browser-based applications.
