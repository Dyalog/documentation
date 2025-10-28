<h1 class="heading"><span class="name">General principles of APLScript</span></h1>

The layout of an `APLScript` file differs according to whether the script defines a Web Page, a Web Service, a .NET class, or an APL application that may have nothing to do with the .NET Framework. However, within the `APLScript`, the code layout rules are basically the same.

An APLScript file contains a sequence of function bodies and executable statements that assign values to variables. In addition, the file typically contains statements that are directives to the APLScript compiler. If the script is a Web Page or Web Service, it may also contain directives to ASP.NET. The former all start with a colon symbol (:) in the manner of control structures. For example, the `:Namespace` statement tells the APLScript compiler to create, and change into, a new namespace. The `:EndNamespace` statement terminates the definition of the contents of a namespace and changes back from whence it came.

Assignment statements are used to set up system variables, such as `⎕ML`, `⎕IO`, `⎕USING` and arbitrary APL variables. For example:
```apl
      ⎕ML←2
      ⎕IO←0
      ⎕USING∪←⊂'System.Data'
 
      A←88
      B←'Hello World'
 
      ⎕CY'MYWS'
```

These statements are extracted from the `APLScript` and executed by the compiler in the order that they appear. It is important to recognise that they are executed at compile time, and not at run-time, and may therefore only be used for initialisation.

Notice that it **is** acceptable to execute `⎕CY` to bring in functions and variables from a workspace that are to be incorporated into the code. This is especially useful to import a set of utilities. Note also that it is possible to export these functions as methods of .NET classes if the functions contain the appropriate colon statements.

The `APLScript` compiler will in fact execute any valid APL expression that you include. However, the results may not be useful and may indeed simply terminate the compiler. For example, it is not sensible to execute statements such as `⎕LOAD`, or `⎕OFF`.

Function bodies are defined between opening and closing del (`∇`) symbols. These are fixed by the `APLScript` compiler using `⎕FX`. Line numbers and white space formatting are ignored.
