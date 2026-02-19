# General Principles of APL Source Files

The layout of an APL Source file differs according to what it defines. However, within the APL Source file, the code layout rules are basically the same.

An APL Source file contains a sequence of function bodies and executable statements that assign values to variables. In addition, the file typically contains statements that are directives to the Dyalog .NET Compiler. These all start with a colon symbol (`:`) in the manner of control structures. For example, the `:Namespace` statement tells the Dyalog .NET Compiler to create, and change into, a new namespace. The `:EndNamespace` statement terminates the definition of the contents of a namespace and changes back from whence it came.

Assignment statements are used to configure system variables, such as `⎕ML`, `⎕IO`, `⎕USING` and arbitrary APL variables. For example:
```apl
      ⎕ML←2
      ⎕IO←0
      ⎕USING∪←⊂'System.Data'
```
```apl
      A←88
      B←'Hello World'
```
```apl
      ⎕CY'MYWS'
```

These statements are extracted from the APL Source file and executed by the Dyalog .NET Compiler in the order in which they appear.

 The statements are executed at compile time, and not at run-time, and can, therefore, only be used for initialisation.

It is acceptable to execute `⎕CY` to bring functions and variables that are to be incorporated into the code in from a workspace. This is especially useful to import a set of utilities. It is also possible to export these functions as methods of .NET classes if the functions contain the appropriate colon statements.

The Dyalog .NET Compiler will execute any valid APL expression that you include. However, the results might not be useful and could terminate the compiler. For example, it is not sensible to execute statements such as `⎕LOAD` or `⎕OFF`.

Function bodies are defined between opening and closing del (`∇`) characters. These are fixed by the Dyalog .NET Compiler using `⎕FX`. Line numbers and white space formatting are ignored.
