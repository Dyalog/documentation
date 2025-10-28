<h1 class="heading"><span class="name">Creating Programs (.exe) with APLScript</span></h1>

The following examples, which illustrate how you can create an executable program (`.exe`) direct from an APLScript file, may be found in the directory `samples\aplscript`.

## A simple GUI example

The following APLScript illustrates the simplest possible GUI application that displays a message box containing the string "Hello World".
```apl
:Namespace N
⎕LX←'N.RUN' 
∇RUN;M 
'M'⎕WC'MsgBox' 'A GUI exe' 'Hello World'
⎕DQ'M' 
∇ 
:EndNamespace
```

This example, which is saved in the file `eg1.apl`, is compiled to a Windows executable (`.exe`) using `dyalogc.exe` and run from the same command window as shown below. Notice that it is essential to surround the code with `:Namespace / :EndNamespace` statements and to define a `⎕LX` either in the APLScript itself, or as a parameter to the `dyalogc` command.

![](../img/aplscript1.png)

![](../img/aplscript2.png)

You can associate the `.exe` with a desktop icon, and it will run stand-alone, without a Command Prompt window. Furthermore, any default APL output that would normally be displayed in the session window will simply be ignored.

## A simple console example

The following APLScript illustrates the simplest possible application that displays the text "Hello World".

This example, which is saved in the file `eg2.apl`, is compiled to a Windows executable (`.exe`) and run from a command window as shown below. Notice that the `/console` flag is used to tell the APLScript compiler to create a *console* application that runs from a command prompt. In this case, default APL output that would normally be displayed in the session window turns up in the command window from which the program was run.
```apl
:Namespace N
⎕LX←'N.RUN'
∇RUN
'Hello World'
∇
:EndNamespace
```

Once more, it is essential to surround the code with `:Namespace/:EndNamespace` statements and to define a `⎕LX` either in the APLScript itself, or as a parameter to the `dyalogc` command.

![](../img/aplscript3.png)

## Defining Namespaces

Namespaces are specified in an APLScript using the `:Namespace` and :`EndNamespace` statements. Although you may use `⎕NS` and `⎕CS` within functions inside an APLScript, you should not use these system functions outside function bodies. Note that such use is not *prevented*, but that the results will be unpredictable.
```apl
:Namespace Name
```

introduces a new namespace called `Name` relative to the current space.
```apl
:EndNamespace
```

terminates the definition of the current namespace. Subsequent statements and function bodies are processed in the context of the original space.

It is imperative that at least ONE namespace be specified.

All functions specified between the `:Namespace` and `:EndNamespace` statements are fixed in that namespace. Similarly, all assignments define variables inside that namespace.

The following example illustrates how APL namespace usage is handled in APLScript. The program, contained in the file `eg3.apl`, is as follows:
```apl
:Namespace N
⎕LX←'N.RUN'
 
∇RUN
⎕PATH←'↑'
NS.START
END
∇
∇R←CURSPACE
R←⊃⎕NSI
∇
∇END
'Ending in ',CURSPACE
∇
 
:NameSpace NS
∇START
'Starting in ',CURSPACE
∇
:EndNameSpace
:EndNameSpace
```

This somewhat contrived example illustrates how a namespace is defined inside another namespace using `:NameSpace` and `:EndNamespace` statements. The namespace `NS` contains a single function called `START`, which is called from the main function `RUN`.

Notice that `⎕`PATH is defined *dynamically* in function RUN. If it were defined outside a function in a static statement in the script (say, after the statement that sets `⎕`LX), it would not be honoured when the application was run.

This program is shown, compiled and run as a console application, below.

![](../img/aplscript4.png)
