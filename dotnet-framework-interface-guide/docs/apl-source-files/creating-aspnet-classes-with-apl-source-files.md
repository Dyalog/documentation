<h1 class="heading"><span class="name">Creating ASP.NET Classes with APL Source Files</span></h1>

One of the purposes of APL Source files is to provide the ability to write ASP.NET web pages and web services in Dyalog; both these applications are based on script files.

## Web Page Layout

An ASP.NET web page typically consists of a mixture of HTML and code written in a scripting language. The script code is separated from the HTML by being embedded within <code class="language-nonAPL">&lt;script>...&lt;/script></code> tags, and normally appears in the <code class="language-nonAPL">&lt;head>...&lt;/head></code> section of the page. Only one block of script is allowed in a page. The script block normally consists of a collection of functions, which are invoked by some event on the page, or on an element of the page.

APL source file code starts with a statement:
```apl
<script language="Dyalog" runat=server>
```

and finishes with:
```apl
</script>

```

Typically, the APL source file code consists of callback functions that are attached to server-side events on the page.

## Web Service Layout

The first line in a web service script must be a declaration statement such as:
```apl
<%@ WebService Language="Dyalog" Class="ServiceName" %>
```

where `ServiceName` is an arbitrary name that identifies your web service.

The next statement must be a `:Class` statement that declares the name of the web service and the base class from which it inherits. The base class will normally be <code class="language-nonAPL">System.Web.Services.WebService</code>. For example:
```apl
:Class ServiceName: System.Web.Services.WebService
```

The last line in the script must be:
```apl
:EndClass
```

Although it might appear awkward to have to specify the name of your web service twice, this is necessary because the two statements are processed separately by different software components. The first statement is processed by ASP.NET; when it sees <code class="language-nonAPL">Language="Dyalog"</code>, it calls the Dyalog .NET compiler, passing it the remainder of the script file. The `:Class` statement tells the Dyalog .NET Compiler the name of the web service and its base class. The `:Class` and `:EndClass` statements are private directives to the Dyalog .NET Compiler and are not relevant to ASP.NET.

## How An APL Source File is Processed by ASP.NET

Like any other web page or web service, an APL Source file is processed by ASP.NET.

The first time ASP.NET processes a script file, it first performs a compilation process whose output is a .NET assembly. ASP.NET then calls the code in this assembly to generate the HTML (for a web page) or to run a method (for a web service).

ASP.NET associates the compiled assembly with the script file, and only recompiles it if/when it has changed.

ASP.NET does not itself compile a script; it delegates this task to a specialised compiler that is associated with the language declared in the script. This association is made either in the application's **web.config** file or in the global **machine.config** file. Dyalog installs a default **web.config** file that includes these settings in the **[DYALOG]\Samples\asp.net** folder; for additional information, see [The web.config File](../../implementation-details/the-webconfig-file/).

The Dyalog .NET Compiler is written in Dyalog.

Although the compilation process takes some time, it is typically only performed once, so the performance of a web service or web page is not compromised. Once it has been compiled, ASP.NET redirects all subsequent requests for an APLsource file to its compiled assembly.

!!! Info "Information"
    The word _compile_ in this process does not imply that your APL code is compiled into Microsoft Intermediate Language (MSIL). Although the process does generate some MSIL, your APL code will still be interpreted by the Dyalog DLL engine at run-time. The word _compile_ is used only to be consistent with the messages displayed by ASP.NET when it first processes the script.
