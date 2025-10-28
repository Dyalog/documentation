<h1 class="heading"><span class="name">Introduction</span></h1>

This manual describes the Dyalog interface to the Microsoft .NET Framework. This document does not attempt to explain the features of the .NET Framework, except in terms of their APL interfaces. For information concerning the .NET Framework, see the documentation, articles and help files, which are available from Microsoft and other sources.

The .NET interface features include:

- the ability to create and use objects that are instances of .NET Classes.
- the ability to define new .NET Classes in Dyalog that can then be used from other .NET languages such as C# and VB.NET.
- the ability to write Web Services in Dyalog.
- the ability to write ASP.NET web pages in Dyalog.

## .NET Classes

The .NET Framework defines a so-called Common Type System. This provides a set of data types, permitted values, and permitted operations. All cooperating languages are supposed to use these types so that operations and values can be checked (by the Common Language Runtime) at run time. The .NET Framework provides its own built-in class library that provides all the primitive data types, together with higher-level classes that perform useful operations.

Dyalog allows you to create and use instances of .NET Classes, thereby gaining access to a huge amount of component technology that is provided by the .NET Framework.

It is also possible to create Class Libraries (Assemblies) in Dyalog. This allows you to export APL technology packaged as .NET Classes, which can then be used from other .NET programming languages such as C# and Visual Basic.

The ability to create and use classes in Dyalog also provides you with the possibility to design APL applications built in terms of APL (and non-APL) components. Such an approach can provide benefits in terms of reliability, software management and re-usage, and maintenance.

## GUI Programming with System.Windows.Forms

One of the most important .NET class libraries is called `System.Windows.Forms`, which is designed to support traditional Windows GUI programming. Visual Studio .NET, which is used to develop GUI applications in Visual Basic and C#, produces code that uses `System.Windows.Forms`. Dyalog allows you to use `System.Windows.Forms`, instead of (and in some cases, in conjunction with) the built-in Dyalog GUI objects such as the Dyalog Grid, to program the Graphical User Interface.

## Web Services

Web Services are programmable components that can be called by different applications. Web Services have the same goal as COM, but are technically platform independent and use HTTP as the communications protocol with an application. A Web Service can be used either internally by a single application or exposed externally over the Internet for use by any number of applications.

## ASP.NET and WebForms

ASP.NET is a new version of Microsoft Active Server Page technology that makes it easier to develop and deploy dynamic Web applications. To supplement ASP.NET, there are some important new .NET class libraries, including WebForms which allow you to build browser-based user interfaces using the same object-oriented mechanism as you use `Windows.Forms` for the Windows GUI. The use of these component libraries replaces basic HTML programming.

ASP.NET pages are server-side scripts, that are usually written in C# or Visual Basic. However, you can also employ Dyalog directly as a scripting language (*APLScript*) to write ASP.NET web pages. In addition, you can call Dyalog workspaces directly from ASP.NET pages, and write custom server-side controls that can be incorporated into ASP.NET pages.

These features give you a wide range of possibilities for using Dyalog to build browser-based applications for the Internet, or for your corporate Intranet.
