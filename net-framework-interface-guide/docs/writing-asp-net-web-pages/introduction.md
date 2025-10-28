<h1 class="heading"><span class="name">Introduction</span></h1>

Under Microsoft IIS, a *static* web page is defined by a simple text file with the extension .htm or .html that contains simple HTML. When a browser requests such a page, IIS simply reads it and sends its content back to the client. The contents of a static web page are constant and, until somebody changes it, the page appears the same to all users at all times.

A *dynamic* web page is represented by a simple text file with the extension .aspx. Such a file may contain a mixture of (static) HTML, ASP.NET objects and a *server-side script*. ASP.NET objects are built-in .NET classes that generate HTML when the page is processed. Scripts contain functions and subroutines that are invoked by events (such as the Page_Load event) or by user interaction.

Typically, a script will generate HTML dynamically, when the page is loaded. For example, a script could perform a database operation and return an HTML table containing a list of products and prices. A script may also contain code to process user interaction, for example to process the contents of a Form that is filled in and then submitted by the user. These scripts are referred to as server-side scripts because they are executed on the server. The browser sees only the results produced by the scripts and not the scripts themselves. Code in a server-side script always involves the generation of a new page by the server for display in the browser.

The first time ASP.NET processes a .NET web page, it compiles the entire page into a .NET Assembly. Subsequently, it calls the code in the assembly directly. The language used to compile the page is defined in the &lt;script&gt; section, which is typically defined at the top of the page. If the &lt;script&gt; section is omitted, or if it fails to explicitly specify the language attribute, the page is compiled using the default scripting language. This is configurable, but is typically VB or C#.

This Chapter is made up almost entirely of examples, the source code of which is supplied in the samples\asp.net directory and the sub-directories it contains. This directory is mapped as an IIS Virtual Directory named `dyalog.net`, so you may execute the examples by specifying the URL `http://localhost/dyalog.net/` followed by the name of the sub-directory and page. You can get an overview of the samples by starting on the page `http://localhost/dyalog.net/index.htm` and follow links from there.

To use `APLScript` effectively in Web Pages, you need to have a thorough understanding of how ASP.NET works.

In the first example, an outline description ASP.NET technology is provided. For further information, see the Microsoft .NET Framework documentation and *Beginning ASP.NET using VB.NET*, Wrox Press Ltd, ISBN 1861005040.
