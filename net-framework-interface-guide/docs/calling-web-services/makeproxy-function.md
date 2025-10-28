<h1 class="heading"><span class="name">The MakeProxy function</span></h1>

The `MakeProxy` function is provided in the supplied workspace `samples\asp.net\webservices\webservices.dws`.

`MakeProxy` is monadic and its argument specifies the URL of the Web Service to which you want to connect. For example, the following expressions uses `MakeProxy` to connect to the LoanService sample Web Service provided with Dyalog .NET:
```apl
   MakeProxy'http://localhost/dyalog.net/Loan/Loan.asmx'
```

`MakeProxy` runs the Microsoft utility `WSDL.EXE` passing the name of your URL to it as an argument. The utility then creates a C# source code file in your current directory that contains the code necessary to create a proxy class. The name of the C# file is the name of the Web Service (as declared in its header line) followed by the extension .cs.

`MakeProxy` then calls the C# compiler to compile this file, creating an assembly with the same name, but with a .dll extension, in your current directory. This assembly contains a .NET class of the same name.

`MakeProxy` attempts to determine the correct path for `WSDL.EXE` and `CSC.EXE`, but future versions of Microsoft.NET or Visual Studio require changes, in which case you will have to modify this function to locate these tools.
