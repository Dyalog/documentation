<h1 class="heading"><span class="name">Getting Started</span></h1>

**This tutorial, as provided, supports the 64-bit Unicode version of Dyalog only.**

The tutorial  described in this Chapter was originally designed (for Dyalog Version 10) to be exercised in a console window, with the user invoking the C# compiler directly using a command-line interface. It was originally envisaged to be run *in-situ* in the `samples\aplclasses` sub-directory.

Today, the `samples\aplclasses` sub-directory is read-only, and direct access to the C# compiler via a command-line interface is problematical. Another consideration is the change in requirement for dependent Dyalog DLLs, which must now reside in the same directory as the host program.

The tutorial has therefore been re-factored to use Microsoft Visual Studio. The `samples\aplclasses` sub-directory has been expanded to support .NET Core (now renamed simply .NET) which is cross-platform as well as the original .NET Framework which is Windows only.

All the examples are to be executed as simple console applications written in C# in the framework of *Microsoft Visual Studio Community 2022* (hereafter referred to as VS). To run the examples as described herein, you should install VS, taking care to include all the components needed to create a C# console application. suitable VS project files are included in the `samples\aplclasses` sub-directory.

## Initialisation

The first step is to copy the `samples\aplclasses` sub-directory into a directory to which you have write access. For example, into `d:\aplclasses`.

Each of the sub-directories contained in `aplclasses`, namely `aplclasses1` - `aplclasses7`, represents a separate example application. Within each one the file structure is as follows:

|---------------------------|--------------------------------------------|
|`aplclasses[n].dws`        |APL workspace                               |
|`Framework`                |Files for the .NET Framework                |
|`Framework\program.cs`     |C# program                                  |
|`Framework\project.sln`    |VS solution file                            |
|`Framework\project.csproj.`|C# project file                             |
|`Framework\bin`            |Directory containing the C# program and DLLs|

When the application is executed by VS it will be run  in the `bin` sub-diredctory.

**It is mandatory that the Dyalog .NET class, and all the Dyalog DLLs on which it depends, reside in the same directory as the host program.**

Therefore, copies of the requisite Dyalog DLLs are provided in the `bin`sub-directory. These DLLs are:

- Development DLL and/or Run-Time DLL (this tutorial uses the Development DLL)
- Bridge DLL
- DyalogNet DLL

## Running the Tutorial

Each example consists of two parts. First you will `)LOAD` a workspace, examine the code, and then export it as a DLL. The second (optional) part is to run the VS solution that hosts the DLL and view the results.

Each workspace contains a .NET Namespace called `APLClasses` which itself contains a single .NET Class called `Primitives` that exports a single method called `IndexGen`.
