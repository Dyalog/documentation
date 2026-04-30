# Example 3

As write access is required to successfully build the samples, this example assumes that you have copied the **[DYALOG]/Samples/aplclasses** directory to **<your_dir>**, where you have write access.

The correct .NET behaviour when an APL function fails with an error is to generate an exception; this example shows how this is achieved.

In .NET, exceptions are implemented as .NET classes. The base exception is implemented by the System.Exception class, but there are a number of super classes, such as System.ArgumentException and System.ArithmeticException that inherit from it.

`⎕SIGNAL` can be used to generate an exception. To do this, its right argument should be 90 and its left argument should be an object of type `System.Exception` or an object that inherits from `System.Exception`.

When you create the instance of the `Exception` class, you can specify a string (which will be its `Message` property) containing information about the error.

Load the **aplclasses3.dws** workspace from **<your_dir>/aplclasses3**, then view its  improved  (compared with that in [Section ](dotnet-classes-eg2.md)) `CTOR` constructor function:
```apl
     ∇ CTOR IO;EX
[1]   :Implements constructor
[2]   :Access public
[3]   :Signature CTOR Int32 IO
[4]   :If IO∊0 1
[5]     ⎕IO←IO
[6]   :Else
[7]      EX←⎕NEW ArgumentException,⊂⊂'IndexOrigin must be 0 or  1'
[8]      EX ⎕SIGNAL 90
[9]   :EndIf
     ∇

```

## aplclasses3

The C# source code (**<your_dir>/aplclasses3/net/project/Program.cs**)    contains code to catch the exception and display the exception message:
```
using System;
using APLClasses;
public class MainClass
    {
    public static void Main()
        {
try
    {
        Primitives apl = new Primitives(2);
        int[] rslt = apl.IndexGen(10);

        for (int i=0;i<rslt.Length;i++)
        Console.WriteLine(rslt[i]);
}
catch (Exception e)
    {
    Console.WriteLine(e.Message);
    }
        }
    }	
```

To compile the C# source code

1. On the command line, navigate to **<your_dir>/aplclasses3/net**.
2. Run **build** (Linux and macOS)/**build.bat** (Microsoft Windows).This invokes the  Dyalog script compiler to  compile **aplclasses3.dws** to  **aplclasses3.dll**, and then invokes the C# compiler to compile the C# source code (**Program.cs**)  to produce an executable called **project.exe** in **<your_dir>/aplclasses3/net/project/bin/Debug/net8.0**.

The output when the program is run is displayed in a console window:

![s_dotnet_classes_eg3_output](../../img/s-dotnet-classes-eg3-output.png)

Program output in console window
