<h1 class="heading"><span class="name">Compilation</span></h1>

When the web service, specified by the **.asmx** file, is called for the first time, ASP.NET invokes the appropriate language compiler (in this case, the Dyalog .NET Compiler) whose job is to produce an assembly that defines and describes a class. When the web service is used subsequently, the request is satisfied by creating and using an instance of the class. However, ASP.NET detects if the **.asmx** script has been modified, and recompiles it in this case.

The Dyalog .NET compiler creates a DLL containing a workspace, which itself contains the web service class. The class contains all the functions that are defined within the script, and any variables that were established by expressions in the script. A single function comprises all the statements enclosed within a pair of _del_ (`∇`) characters.

<h4 class="example">Example</h4>

The following script defines a class, instances of which would run using `⎕ML←2`, containing a single function `FOO` and a variable `X`.
```apl
:Class MyClas
   ⎕ML←2
   X←10
   ∇ Z←FOO Y
     Z←Y+X
   ∇
:EndClass
```

All expressions in the class script are executed by the Dyalog .NET Compiler when it creates the assembly. They are not executed when the web service is invoked.

If your script contains a `⎕CY` statement, it will be executed by the Dyalog .NET Compiler when establishing the class. This can be used to import functions from other workspaces and remove the need to include them in the **.asmx** file.
