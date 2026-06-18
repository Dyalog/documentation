<h1 class="heading"><span class="name">Web Service (.asmx) Scripts</span></h1>

Web services can be written in a variety of languages, including the scripting version of Dyalog APL. For more information on APL source files, see [APL Source Files](../../apl-source-files/).

The first statement in the script file declares the language and the name of the service. For example, the following statement declares a Dyalog web service named <code class="language-nonAPL">GolfService</code>.
```nonAPL
<%@ WebService Language="Dyalog" Class="GolfService" %>
```

<code class="language-nonAPL">Language="Dyalog"</code> is specifically connected to the Dyalog .NET Compiler through the application's **web.config** file or through the global **ASP.NET** system file **Machine.config**.

!!! Legacy "Legacy"
    Prior to Dyalog v11.0, <code class="language-nonAPL">Language="APL"</code> was used instead.

The syntax of this first line is common to all web services, irrespective of the language in which they are written.

A Dyalog web service script starts with a `:Class` statement and ends with an `:EndClass` statement. These statements are directives used by the Dyalog .NET Compiler and are specific to Dyalog.

The `:Class` statement declares the name of the class (which must be the same as the name declared in the `WebService` statement) and the _base_ class from which it inherits, which is normally <code class="language-nonAPL">System.Web.Services.WebService</code>.
```apl
   :Class GolfService: System.Web.Services.WebService
```

Following the `:Class` statement can be any number of APL expressions and function bodies, at the end of which must be an `:EndClass` statement. Internal sub-classes (nested classes) can be inlcuded within the main `:Class ... :EndClass` block.

Functions usually take arguments and return results whose types must be known, therefore the statement `:Using System` must almost always appear immediately after the `:Class` statement to locate them.
