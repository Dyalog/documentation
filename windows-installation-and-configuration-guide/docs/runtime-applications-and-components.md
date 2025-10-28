<h1 class="heading"><span class="name">Run-Time Applications and Components</span></h1>

Using Dyalog APL you may create different types of run-time applications and components. Note that the distribution of run-time applications and components requires a Dyalog APL Run-Time Agreement. Please contact Dyalog or your distributor, or see the Dyalog web page for more information.

For a list of the distributable components and their corresponding file names, for the different versions of Dyalog, see [Files](files-and-directories.md). These components are referred to in hereafter by the name shown in the first column of the table. It is essential that you distribute the components that are appropriate for the Edition you are using.

The various types of run-time applications and components are as follows:

1. Workspace or source code run-time
2. Stand-alone run-time
3. Bound run-time
4. Out-of-Process COM Server
5. In-Process COM Server
6. ActiveX Control
7. Microsoft .NET Assembly

All but the first of these are made using the *Export* dialog box accessed from the *File/Export* menu item of the Session window.

## Configuration Parameters

Configuration parameters for these run-time applications, both for the Dyalog engine and for your own application settings, may be specified in a number of ways. See [Configuration Parameters](configuration-parameters/configuration-parameters.md).

Nevertheless, it is strongly recommended that you use Configuration files. In this section we will discuss only Application Configuration files, although User Configuration files may be used as well.

## Workspace or source code based run-time

A workspace or source code based run-time application consists of the Dyalog APL Run-Time Program (Run-Time EXE), a separate workspace or text file containing APL source code, and an optional configuration file. To distribute your application, you need to supply and install:

1. your workspace or source code
2. the Run-Time EXE
3. a configuration file (optional)
4. whatever additional files that may be required by your application
5. a command-line to start the application

The command-line for your application invokes the Run-Time EXE and directly or indirectly specifies the name of the workspace or source code file and the optional configuration file. You will need to associate your own icon with your application during its installation.

The name of the workspace or source code file may be specified by the **Load** parameter on the command line. If the application uses a workspace, the name of the workspace may instead be supplied as the last item on the command-line.

The name of the configuration file may be specified on the application command-line, using  the **ConfigFile** parameter. Alternatively, the name of the configuration file is derived from the name of the workspace or source code file.

The action to start the application when a workspace or source code file is loaded is specified by the **LX** parameter or, for a workspace, by its latent expression (`⎕LX`).

In the command-line examples that follow, the name of the Run-Time EXE has been shortened to `dyalogrt.exe` for brevity.

## Using a workspace
```apl
     dyalogrt.exe myapp.dws
```

The application starts by running `⎕LX` in `myapp.dws`. If a configuration file named `myapp.dcfg` in the same directory, it is loaded and applied.

## Using a source code file
```apl
     dyalogrt.exe Load=myfn.aplf
```

The application loads the file named `myfn.aplf` which contains the source code for a function, and executes the expression `(myfn 0⍴⊂'')` (see [Load](configuration-parameters/load.md)).  If a configuration file named `myfn.dcfg` in the same directory, it is loaded and applied.

If your application uses any component of the Microsoft .NET Framework, you must distribute the Bridge DLL and DyalogNet DLLs. These DLLs must be placed in the same directory as your EXE.

## Stand-alone and Bound run-times

A  stand-alone run-time is a single .EXE that contains a workspace and a copy of the Run-Time version of the Dyalog APL interpreter. It is the simplest type of run-time to install because it has the fewest number of dependencies.

A  bound run-time is a workspace packaged as a .EXE that relies upon and requires the separate installation of the Run-Time DLL. Compared with the stand-alone executable option, bound run-times may save disk space and memory if your customer installs and runs several different Dyalog applications.

Both these run-times are created using the *File/Export* menu item on the Session window.

To distribute your application, you need to supply and install:

1. your stand-alone or bound .EXE
2. the Run-Time DLL (bound .EXE only)
3. a configuration file (optional)
4. whatever additional files that may be required by your application
5. a command-line to start the application

When you build your .EXE using the Export dialog, you may specify the name(s) of the configuration file(s) using the **ConfigFile** and/or **UserConfigFile** parameters in the field labelled *Command Line*.

An alternative is to specify these parameters in the command-line that you use to run your .EXE (note that this is not the same as the *Command Line* in the *Export* dialog box). If so, the Dyalog parameter(s) must be preceded by the **-apl** option.

If your application uses any component of the Microsoft .NET Framework, you must distribute the Bridge DLL and DyalogNet DLLs. These DLLs must be placed in the same directory as your EXE.

## Out-of-process COM Server

To make an out-of-process COM Server, you must:

1. establish one or more OLEServer namespaces in your workspace, populated with functions and variables that you wish to export as methods, properties and events.
2. use the *File/Export …* menu item on the Session window to register the COM Server on your computer so that it is ready for use.

The command-line for your COM Server must be specified in the field labelled *Command Line* in the *Export* dialog box. The field is initialised to invoke the Run-Time EXE with the name of your workspace in the same fashion as the workspace-based run-time discussed above. This command-line is recorded in the Windows Registry to be invoked when a client application requests it.

You may change the contents of the *Command Line* field to use a configuration file, in the same way as for a workspace-based runtime. The following example uses the Loan COM Server. See [The LOAN Workspace](../../interface-guide/ole-server/the-loan-workspace).

<h2 class="example">Example</h2>
```apl
      dyalog.exe C:\Dyalog18.0\myloan.dws
```

The command-line above will, on invocation, cause Dyalog to load the `myloan.dws` workspace together with the configuration file `myloan.dcfg` if it exists in that directory.

To distribute an out-of-process COM Server, you need to supply and install the following files:

1. your workspace
2. the associated Type Library (.tlb) file (created by *File/Export*)
3. the Run-Time EXE
4. a configuration file (optional)
5. whatever additional files that may be required by your application

To install an out-of-process COM Server you must set up the appropriate Windows registry entries. See Interface Guide for details.

## In-process COM Server

To make an in-process COM Server, you must:

1. establish one or more OLEServer namespaces in your workspace, populated with functions and variables that you wish to export as methods, properties and events.
2. use the *File/Export …* menu item on the Session window to create an in-process COM Server (DLL) which contains your workspace bound to the Run-Time DLL. This operation also registers the COM Server on your computer so that it is ready for use.

As there is no command-line available, to specify a configuration file for an in-process COM server, it is necessary to define the **ConfigFile** parameter and/or the **UserConfigFile** parameter as an environment variable or in the registry.

To distribute your component, you need to supply and install

1. Your COM Server file (DLL)
2. the Run-Time DLL
3. a configuration file (optional) and the means to define **ConfigFile** and/or **UserConfigFile**
4. whatever additional files that may be required by your COM Server.

Note that you must register your COM Server on the target computer using the `regsvr32.exe` utility.

### ActiveX Control

To make an ActiveX Control, you must:

1. establish an ActiveXControl namespace in your workspace, populated with functions and variables that you wish to export as methods, properties and events.
2. use the *File/Export …* menu item on the Session window to create an ActiveX Control file (OCX) which contains your workspace bound to the Run-Time DLL. This operation also registers the ActiveX Control on your computer so that it is ready for use.

As there is no command-line available, to specify a configuration file for an in-process COM server, it is necessary to define the **ConfigFile** parameter and/or the **UserConfigFile** parameter as an environment variable or in the registry.

To distribute your component, you need to supply and install

1. Your ActiveX Control file (OCX)
2. the Run-Time DLL
3. a configuration file (optional) and the means to define **ConfigFile** and/or **UserConfigFile**
4. whatever additional files that may be required by your ActiveX Control.

Note that you must register your ActiveX Control on the target computer using the `regsvr32.exe` utility.

### Microsoft .NET Assembly

A Microsoft .NET Assembly contains one or more .NET Classes. To make a Microsoft .NET Assembly, you must:

1. establish one or more NetType namespaces in your workspace, populated with functions and variables that you wish to export as methods, properties and events.
2. use the *File/Export …* menu item on the Session window to create a Microsoft .NET Assembly (DLL) which contains your workspace bound to the Run-Time DLL.

If the option selected in the *Isolation Mode* field of the *Export* dialog is either:

- Each assembly has its own workspace, or
- Each assembly attempts to use local bridge and interpreter libraries

you may enter configuration parameters or specify a Configuration file for your Dyalog assembly in the field labelled *Command Line*.

For the other isolation modes, this is not appropriate because only the command line from the first assembly loaded into the interpreter could be honoured, and the order in which assemblies are loaded is unpredictable. However, configuration files may be specified using the **ConfigFile** parameter and/or the **UserConfigFile** parameter specified as an environment variable or in the registry.

For more information, see [Isolation Mode](../../net-framework-interface-guide/implementation-details/isolation-mode).

To distribute your .NET Classes, you need to supply and install

1. your Assembly file (DLL)
2. the Run-Time DLL
3. the Bridge DLL
4. the DyalogNet DLL
5. a configuration file (optional) and, depending upon the isolation mode, the means to define **ConfigFile** and/or **UserConfigFile**
6. whatever additional files that may be required by your .NET Assembly.

All the DLLs and subsidiary files must be installed in the same directory as the .NET Assembly.
