<h1 class="heading"><span class="name">General Principles of APL Source Files</span></h1>

The layout of an APL source file differs according to whether the script defines a web page, a web service, a .NET class, or an APL application that might have nothing to do with the .NET Framework. However, within the APL source file, the code layout rules are basically the same.

An APL source file contains a sequence of function bodies and executable statements that assign values to variables. In addition, the file typically contains statements that are directives to the Dyalog .NET Compiler. If the script is a Web Page or Web Service, it may also contain directives to ASP.NET. The former all start with a colon symbol (:) in the manner of control structures. For example, the `:Namespace` statement tells the Dyalog .NET Compiler to create, and change into, a new namespace. The `:EndNamespace` statement terminates the definition of the contents of a namespace and changes back from whence it came.

Assignment statements are used to configure system variables, such as `⎕ML`, `⎕IO`, `⎕USING`, and arbitrary APL variables. For example:
```apl
      ⎕ML←2
      ⎕IO←0
      ⎕USING∪←⊂'System.Data'

      A←88
      B←'Hello World'

      ⎕CY'MYWS'
```

These statements are extracted from the APL source file and executed by the Dyalog .NET Compiler in the order in which they appear.

!!! Info "Information"
    The statements are executed at compile time, and not at run-time, and can, therefore, only be used for initialisation.

It is acceptable to execute [`⎕CY`](../../language-reference-guide/system-functions/cy/) to bring functions and variables that are to be incorporated into the code in from a workspace. This is especially useful to import a set of utilities. It is also possible to export these functions as methods of .NET classes if the functions contain the appropriate colon statements.

The Dyalog .NET Compiler will execute any valid APL expression that you include. However, the results might not be useful and could terminate the Dyalog .NET Compiler. For example, it is not sensible to execute statements such as [`⎕LOAD`](../../language-reference-guide/system-functions/load/) or [`⎕OFF`](../../language-reference-guide/system-functions/off/).

Function bodies are defined between opening and closing _del_ (`∇`) characters. These are fixed by the Dyalog .NET Compiler using [`⎕FX`](../../language-reference-guide/system-functions/fx/). Line numbers and white space formatting are ignored.
