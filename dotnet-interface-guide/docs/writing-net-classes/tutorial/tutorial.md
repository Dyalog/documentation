# Tutorial

All the examples in this tutorial are to be executed as simple console applications written in C#.

The code for all of the examples is provided in the **[DYALOG]/Samples/aplclasses/** directory:

- **aplclassesN/aplclassesN.dws** – workspaces containing the source code for the Dyalog classes

- **aplclassesN/net/project/Program.cs** – the corresponding C# source code for hosting the Dyalog classes.

Each workspace contains a .NET namespace called APLClasses which itself contains a single .NET class called Primitives that exports a single method called IndexGen. When executing each example, the workspace (**aplclassesN.dws** will be exported to the **/net/project/bin/Debug/net8.0** sub‑directory as a .NET assembly called  **aplclassesN.dll**.

The examples in the tutorial require write access to successfully build the samples. Dyalog Ltd recommends copying the **[DYALOG]/Samples/aplclasses** directory to somewhere you have write access; in this tutorial that location will be identified as **<your_dir>**.

To compile the C# source code

1. On the command line, navigate to **<your_dir>/aplclassesN/net**.
2. Run **build** (Linux and macOS)/**build.bat** (Microsoft Windows).This invokes the  Dyalog script compiler to  compile **aplclassesN.dws** to  **aplclassesN.dll**, and then invokes the C# compiler to compile the C# source code (**Program.cs**)  to produce an executable called **project.exe** in **<your_dir>/aplclassesN/net/project/bin/Debug/net8.0**.

The examples in this tutorial are:

- [Section ](dotnet-classes-eg1.md)

- [Section ](dotnet-classes-eg2.md)

- [Section ](dotnet-classes-eg3.md)

- [Section ](dotnet-classes-eg4.md)

- [Section ](dotnet-classes-eg5.md)
