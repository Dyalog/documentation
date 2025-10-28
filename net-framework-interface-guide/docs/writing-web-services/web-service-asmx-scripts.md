<h1 class="heading"><span class="name">Web Service (.asmx) Scripts</span></h1>

Web Services may be written in a variety of languages, including `APLScript`, the scripting version of Dyalog APL. See [APLScript](../aplscript/introduction.md).

The first statement in the script file declares the language and the name of the service. For example, the following statement declares a Dyalog APL Web Service named `GolfService`.
```xml
<%@ WebService Language="Dyalog" Class="GolfService" %>
```

Note that `Language="Dyalog"` is specifically connected to the Dyalog APL script compiler through the application's web.config file or through the global ASP.NET system file `Machine.config`. Note that versions of Dyalog prior to 11.0 used `Language="APL"`.

The syntax of this first line is common to all Web Services, regardless of the language in which they are written.

A Dyalog APL Web Service script starts with a `:Class` statement and ends with an `:EndClass` statement. These statements are directives used by the Dyalog APL script compiler and are specific to Dyalog APL.

The `:Class` statement declares the name of the Class (which must be the same as the name declared in the `WebService` statement) and the *Base Class* from which it inherits, which is normally `System.Web.Services.WebService`.
```apl
   :Class GolfService: System.Web.Services.WebService
```

Following the `:Class` statement, there may appear any number of APL expressions and function bodies. Following these there must be a `:EndClass` statement. Internal sub-classes (nested classes) may also be defined within the main `:Class ... :EndClass` block.

Because the functions usually take arguments and return results whose types must be known, the statement
```apl
   :Using System
```

must almost always appear **immediately** after the `:Class` statement to locate them.
