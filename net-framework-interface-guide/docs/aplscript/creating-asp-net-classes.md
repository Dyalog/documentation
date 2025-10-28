<h1 class="heading"><span class="name">Creating ASP.NET Classes with APLScript</span></h1>

As mentioned previously, the original purpose of APLScript was to provide the ability to write ASP.NET Web Pages and Web Services in Dyalog. Both these applications are based upon script files.

## Web Page Layout

An ASP.NET Web Page typically consists of a mixture of HTML and code written in a scripting language. The script code is separated from the HTML by being embedded within <script> and </script> tags and normally appears in the <head> </head> section of the page. Only one block of script is allowed in a page. The script block normally consists of a collection of functions, which are invoked by some event on the page, or on an element of the page.

`APLScript` code starts with a statement:
```apl
<script language="Dyalog" runat=server>
```

and finishes with:
```apl
</script>
 
```

Typically, the APLScript code consists of callback functions that are attached to server-side events on the page.

For further information, see [The web.config file](../implementation-details/asp-net-configuration-file.md).

## Web Service Layout

The first line in a Web Service script must be a declaration statement such as:
```apl
<%@ WebService Language="Dyalog" Class="ServiceName" %>
```

where `ServiceName` is an arbitrary name that identifies your Web Service.

The next statement must be a `:Class` statement that declares the name of the Web Service and its Base Class from which it inherits. The base class will normally be `System.Web.Services.WebService`. For example:
```apl
:Class ServiceName: System.Web.Services.WebService
```

The last line in the script must be:
```apl
:EndClass
```

Although it may appear awkward to have to specify the name of your Web Service twice, this is necessary because the two statements are being processed quite separately by different software components. The first statement is processed by ASP.NET. When it sees `Language="Dyalog"`, it then calls the Dyalog `APLScript` compiler, passing it the remainder of the script file. The `:Class` statement tells the `APLScript` compiler the name of the Web Service and its base class. `:Class` and `:EndClass` statements are private directives to the `APLScript` compiler and are not relevant to ASP.NET.

## How APLScript is processed by ASP.NET

Like any other Web Page or Web Service, an `APLScript` file is processed by ASP.NET.

The first time ASP.NET processes a script file, it first performs a compilation process whose output is a .NET assembly. ASP.NET then calls the code in this assembly to generate the HTML (for a Web Page) or to run a method (for a Web Service).

ASP.NET associates the compiled assembly with the script file, and only recompiles it if/when it has changed.

ASP.NET does not itself compile a script; it delegates this task to a specialised compiler that is associated with the language declared in the script. This association is made either in the application's web.config file or in the global `machine.config` file. Dyalog Installs a default web.config file which includes these settings in the `samples\asp.net` folder.

The `APLScript` compiler is itself written in Dyalog.

Although the compilation process takes some time, it is typically only performed once, so the performance of an `APLScript` Web Service or Web Page is not compromised. Once it has been compiled, ASP.NET redirects all subsequent requests for an `APLScript` to its compiled assembly.

Please note that the use of the word *compile* in this process does not imply that your APL code is actually compiled into Microsoft Intermediate Language (MSIL). Although the process does in fact generate *some* MSIL, your APL code will still be interpreted by the Dyalog DLL engine at run-time. The word *compile* is used only to be consistent with the messages displayed by ASP.NET when it first processes the script.
