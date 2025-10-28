<h1 class="heading"><span class="name">Debugging an APL.NET Class</span></h1>

All DYALOG.NET objects are executed by the Dyalog DLL. The full development version of the Dyalog DLL contains all of the development and debug facilities of the APL Session, including the Editors and Tracer. The run-time version contains no debugging facilities at all. The choice of which version of the Dyalog DLL is used is made when the assembly is exported from APL using the *File|Export* menu, or compiled using `dyalogc.exe`.

If an APL .NET object that is bound to the full development version generates an untrapped APL error (such as a `VALUE ERROR`) **and** the client application is configured so that it is allowed to interact with the desktop, the APL code will suspend and the APL Session window will be displayed. Otherwise, it will throw an exception.

If an APL .NET object that is bound to the run-time version of the Dyalog DLL generates an untrapped APL error it will throw an exception.

## Specifying the DLL

There are a number of different ways that you choose to which of the two versions of the Dyalog DLL your DYALOG.NET class will be bound. Note that the appropriate DLL must be available when the class is subsequently invoked. If the DLL to which the APL .NET class is bound is not present, it will throw an exception.

If you build a .NET class from a workspace using the *File/Export* menu item, you use the *Runtime application* checkbox. If *Runtime application* is unchecked, the .NET Class will be bound to the full development version. If *Runtime application* is checked, the .NET Class will be bound to the run-time version.

If you build a .NET class using the APLScript compiler, it will by default be bound to the full development version. If you specify the `/runtime` flag, it will be bound to the run-time version.

If your APL .NET class is a Web Page or a Web Service, you specify to which of the two DLLs it will be bound using the *Debug* attribute. This is specified in the opening declaration statement in the `.aspx`, `.asax` or `.asmx` file. If the statement specifies `"Debug=true"`, the Web Page or Web Service will be bound to the full development version. If it specifies `"Debug=false"`, the Web Page or Web Service will be bound to the run-time version.

If you omit the `Debug=` attribute in your Web page, the value will be determined from the various .NET `config` files on your computer.

## Forcing a suspension

If an APL error occurs in an APL .NET object, a suspension will occur and the Session will be available for debugging. But what if you want to force this to happen so that you can Trace your code and see what is happening?

If your APL class is built directly from a workspace, you can force a suspension by setting stops in your code before using *Export* to build the DLL. If your class is a Web Page or Web Service where the code is contained in a workspace using the *workspace behind* technique (See Chapter 8), you can set stops in this workspace before you `)SAVE` it.

If your APL class is defined entirely in a Web Page, Web Service, or an APLScript file, the only way to set a break point is to insert a line that sets a stop explicitly using `⎕STOP`. It is essential that this line appears after the definition of the function in the script. For example, to set a stop in the `Intro\intro1.aspx` example discussed in Chapter 8, the script section could be as follows:
```xml
<script language="dyalog" runat="server">
 
∇Rotate args
:Access Public
:Signature Reverse Object,EventArgs
 
(⊃args).Text←⌽Pressme.Text
∇
 
3 ⎕STOP 'Rotate'
 
</script>
```

As an alternative, you can always insert a deliberate error into your code!

Finally, you can usually force a suspension by generating a Weak Interrupt. This is done from the pop-up menu on the APL icon in the System Tray that is associated with the full development version of the Dyalog DLL. Note that selecting Weak Interrupt from this menu will not have an immediate effect, but it sets a flag that will cause Dyalog APL to suspend when it next executes a line of APL code. You will need to activate your object in some way, for example, by calling a method, for this to occur. Note that this technique may not work if the Dyalog DLL is busy because a thread switch automatically resets the Weak Interrupt flag. In these circumstances, try again.

The run-time version of the Dyalog DLL does not display an icon in the System Tray.

## Using the Session, Editor and Tracer

When an DYALOG.NET object suspends execution, all other active APL .NET objects bound to the full development version of the Dyalog DLL that are currently being executed by the same client application will also suspend. Furthermore, all the classes currently being hosted by the Dyalog DLL are visible to the APL developer whether active (an instance is currently being executed) or not. Note that if a client application, such as ASP.NET, is also hosting APL .NET objects bound to the *runtime* version of the Dyalog DLL, these objects will be hosted in a separate workspace attached to the run-time version of the Dyalog DLL and will not be visible to the developer.

Debugging a running DYALOG.NET object is substantially the same process as debugging a stand-alone multi-threaded APL application. However, there are some important things to remember.

Firstly, the namespace structure above your APL class should be treated as being inviolate. There is nothing to prevent you from deleting namespaces, renaming namespaces, or creating new ones in the workspace. However, you do so at your peril!

Similarly, you should not alter, delete or rename any functions that have been automatically generated on your behalf by the APLScript compiler. These functions are also inviolate.

If execution in the Dyalog DLL is suspended, you may not execute `)CLEAR` or `)RESET`.  You may execute `)OFF` or `⎕OFF`, but if you do so, the client application will terminate. If you attempt to close the APL Session window, you will be warned that this will terminate the client application and you may cancel the operation or continue (and exit).

If you fix a problem in a suspended function and then press *Resume* or *Continue* (Tracer) or execute a branch, and the execution of the currently invoked method succeeds, you will be left with an empty state indicator (assuming that no other threads are actively involved). The Dyalog DLL is at this stage idle, waiting for the next client request and the state indicator will be empty.

If, at this point, you close the APL Session window, a dialog box will give you the option of terminating the (client) application, or simply hiding the APL Session Window. If you execute `)OFF` or `⎕OFF` the client application will terminate.

Note that in the discussion above, a reference to terminating the client application means that APL executes `Application.Exit()`. This may cause the application to terminate cleanly (as with ASP.NET) or it may cause it to crash.
