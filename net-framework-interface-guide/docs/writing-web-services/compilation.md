<h1 class="heading"><span class="name">Compilation</span></h1>

When the Web Service, specified by the `.asmx` file, is called **for the first time**, ASP.NET invokes the appropriate language compiler (in this case, the Dyalog Script compiler) whose job is to produce an Assembly that defines and describes a class. When the Web Service is used subsequently, the request is satisfied by creating and using an instance of the class. However, ASP.NET detects if the `.asmx` script has been modified, and recompiles it in this case.

The Dyalog Script compiler creates a `DLL` containing a workspace, which itself contains the Web Service class. The class contains all the functions, which are defined within the script, together with any variables that were established by expressions in the script. A single function comprises all the statements enclosed within a pair of del (`∇`) symbols.

For example, the following script would define a class, instances of which would run using `⎕ML←2`, containing a single function `FOO` and a variable `X`.
```apl
:Class MyClass
   ⎕ML←2
   X←10
   ∇ Z←FOO Y
     Z←Y+X
   ∇
:EndClass
```

Note that all expressions in the class script are executed by the script compiler when it creates the assembly. They are not executed when the Web Service is invoked.

If your script contains a `⎕CY` statement, it will be executed by the compiler when establishing the class. This may be used to import functions from other workspaces and obviate the need to include them in the `.asmx` file.
