<h1 class="heading"><span class="name">Tutorial</span></h1>

!!! Legacy "Legacy"
    This tutorial was originally designed (for Dyalog v10.0) to be exercised in a console window, with the user invoking the C# compiler directly using a command-line interface. It was originally envisaged to be run within the **[DYALOG]\Samples\aplclasses\** directory, but this directory is now read-only.In addition, dependent Dyalog DLLs must now reside in the same directory as the host program. The tutorial has, therefore, been re-factored to use command line tools in a writeable directory.

All the examples in this tutorial are to be executed as simple console applications written in C# in the framework of _Microsoft Visual Studio Professional 2022_ (hereafter referred to as VS); to run this tutorial you should install VS.

Start VS and create a new _C# Console Application (.NET Framework)_ – this creates a project for creating a command-line application. You can chose the name and location; this tutorial chooses the name **DyApp** and the directory **C:\**, so VS creates a directory called **C:\DyApp** containing several other files and directories.

When the application is executed (in debug mode) by VS it will be run in the application's **bin\Debug** sub‑directory.

!!! Info "Information"
    The Dyalog .NET class, and all the Dyalog DLLs on which it depends, must reside in the same directory as the host program.

First, copy the requisite Dyalog DLLs to the **bin\Debug** sub-directory. These are:

- Development DLL and/or Run-Time DLL (this tutorial uses the Development DLL)
- Bridge DLL
- DyalogNet DLL

For the names of these files corresponding to the version of Dyalog that you are using, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_.

If you are running the 64-bit version of Dyalog, you must ensure that the **Platform target** is set to x64 in VS. To do this, select **Project** > **DyApp Properties**, go to the **Build** section, choose _x64_ from the **Platform target** drop-down list, and **Save** your changes.

Following these steps, the contents of the **C:\DyApp\bin\Debug** sub-directory should be similar to this:
```

20/12/2022  10:12    <DIR>          .
20/12/2022  10:10    <DIR>          ..
13/09/2022  19:19         2,378,752 bridge182-64_unicode.dll
13/09/2022  19:21        12,887,552 dyalog182_64rt_unicode.dll
13/09/2022  19:22        12,887,552 dyalog182_64_unicode.dll
13/09/2022  19:19            19,456 dyalognet.dll
```

The code for all of the examples is provided in the **[DYALOG]\Samples\aplclasses\** directory:

- **aplclassesN.dws** – workspaces containing the source code for the Dyalog classes

- **aplfnsN.cs** – the corresponding C# source code for hosting the Dyalog classes.

To execute each example, the workspace **aplclassesN.dws** will be exported to the **bin\Debug** sub‑directory as a Microsoft .NET assembly called (in all cases) **aplclasses.dll**.

Each workspace contains a .NET namespace called <code class="language-nonAPL">APLClasses</code> which itself contains a single .NET class called <code class="language-nonAPL">Primitives</code> that exports a single method called <code class="language-nonAPL">IndexGen</code>.

The examples in this tutorial start by replacing the main program in the VS application with imported C# code, executing it, and displaying the results in a simple console window ([Section ](dotnet-classes-eg1.md)). Subsequent examples edit this code, either directly or by copying and pasting code from the other (supplied) C# source code files.

## Example 1

Load the **aplclasses1.dws** workspace from **[DYALOG]\Samples\aplclasses\aplclasses1**, then view the `Primitives` class:
```apl
      )ED ○APLClasses.Primitives

:Class Primitives
:using System
∇R←IndexGen N
:access public
:signature Int32[]←IndexGen Int32
R←⍳N
∇
:EndClass ⍝ Primitives
```

!!! Info "Information"
    The `○` character before the name `APLClasses.Primitives` instructs the editor to edit a class.

`Primitives` contains one public method/function, called `IndexGen`.

The public characteristics for the exported method are included in the definition of the class and its functions, as specified in the `:Signature` statement. This has the following syntax:
```apl
:Signature [rslttype←] name [arg1type [arg1name] [,argNtype [argNname]]*]
```

where:

- `rslttype` is the type of the result returned by the function – in this example, the function returns an array of 32-bit integers

- `name` is the exported name (it can be different from the APL function name but it must be provided) – in the example, the name of the exported method is `IndexGen`

- `argNtype [argNname]` are any arguments are to be supplied, each type-name pair separated from the next by a comma. In this example, the function takes a single integer as its argument.

!!! Info "Information"
    For more information on `:Signature`, see the _Dyalog Programming Reference Guide_.

When the class is fixed, APL will try to find the .NET data types that have been specified for the result and for the parameters. If one or more of the data types are not recognised as available .NET types, then a warning will be displayed in the status window and APL will not fix the class. If you see such a warning, you have either entered an incorrect data type name, or you have not set `:using` correctly, or some other syntax problem has been detected (for example, the function could be missing a terminating `∇`). In this example, the only data type used is `System.Int32`; as `:using System` is included in the definition, `Int32` is correctly located.

The assembly can now be created. This is done in one of the following ways:

- Select **File** > **Export…** – this displays the **Create bound file** dialog box.<br />For this example, set the **File name** to _aplclasses_. The **Runtime application** checkbox allows you to choose to which of the two versions of the Dyalog dynamic link library the assembly will be bound – this example will use the Development version, so the checkbox should be cleared. The **Isolation Mode** drop-down list allows you to choose the [isolation mode](../implementation-details/isolation-mode.md)) – in this example, each host process will have a single workspace. Click **Save**. APL now makes the assembly; as it does this, information is displayed in the **Status** window. If any errors occur during this process, they will be reported in the **Status** window.

- Use the [Bind method](../assemblies-namespaces-and-classes/#the-bind-method.md).

### aplclasses1.cs

The C# source code (**[DYALOG]\Samples\aplclasses\aplclasses1\net\project\Program.cs**) can be used to call the Dyalog.NET class. The <code class="language-nonAPL">using</code> statements specify the names of .NET namespaces to be searched for unqualified class names. The program creates an object called <code class="language-nonAPL">apl</code> of type <code class="language-nonAPL">Primitives</code> by calling the <code class="language-nonAPL">new</code> operator on that class. Then it calls the `IndexGen` method with a parameter of 10.
```nonAPL
      using System;
      using APLClasses;
      public class MainClass
          {
          public static void Main()
              {
                  Primitives apl = new Primitives();
                  int[] rslt = apl.IndexGen(10);
                  for (int i=0;i<rslt.Length;i++)
                  Console.WriteLine(rslt[i]);
               }
          }
```

In VS, select **Project** > **Add Existing Item...** and add **[DYALOG]\Samples\aplclasses\aplfns1.cs**. Use the **Solution Explorer* to rename **aplfns1.cs** to **aplfns.cs** and delete the dummy program **Program.cs** (this prevents there being two <code class="language-nonAPL">Main()</code> entry-points in the application.

Open **aplfns.cs** in the VS code editor (double-click its name in the **Solution Explorer**) and add the following two lines of code:
```nonAPL
      Console.Write("Press <Enter> to exit... ");
      while (Console.ReadKey().Key != ConsoleKey.Enter) { }
```

These allow you to view the contents of the console window before it disappears when the program ends.

<code class="language-nonAPL">APLClasses</code> and <code class="language-nonAPL">Primitives</code> are marked as being in error. This is because VS does not yet know what they are. To resolve this, select **Project** > **Add Reference...**, select the **Browse** tab from the left-hand menu, and click **Browse...**, then navigate to **C:\DyApp\bin\Debug** and add **aplclasses.dll**.

The final code is:

![Program code in Visual Studio](../../img/s-dotnet-classes-eg1-1.png)

Click **Start** to run the program. The results are displayed in a console window:

![Program output in console window](../../img/s-dotnet-classes-eg1-2.png)
