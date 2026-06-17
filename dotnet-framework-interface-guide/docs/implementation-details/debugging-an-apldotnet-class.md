<h1 class="heading"><span class="name">Debugging an APL .NET Class</span></h1>

All APL .NET objects are executed by the Dyalog DLL. The full development version of the Dyalog DLL contains all of the development and debug facilities of the APL Session, including the **Editor** windows and **Trace** window. The run-time version contains no debugging facilities. The choice of which version of the Dyalog DLL is used is made when the assembly is exported from APL using the **File|Export** menu or compiled using **dyalogc.exe**:

- If an APL .NET object that is bound to the full development version generates an untrapped APL error (such as a `VALUE ERROR`) and the client application is configured so that it is allowed to interact with the desktop, then the APL code will suspend and the APL Session window will be displayed. Otherwise, an exception is generated.

- If an APL .NET object that is bound to the run-time version of the Dyalog DLL generates an untrapped APL error, an exception will be generated.

## Specifying the DLL

There are several ways to specify which of the two versions of the Dyalog DLL (full development or run-time) your APL .NET class will be bound:

!!! Info "Information"
    The appropriate DLL must be available when the class is subsequently invoked – if the DLL to which the APL .NET class is bound is not present, then an exception will be generated.
	
- If you build a .NET class from a workspace using the **File**/**Export** menu item, the value in the **Runtime application** checkbox specifices the Dyalog DLL version; if **Runtime application** is not checked then the .NET class will be bound to the full development version, and if **Runtime application** is checked then the .NET class will be bound to the run-time version.

- If you build a .NET class using the Dyalog .NET Compiler, it will be bound to the full development version by default. This can be changed to the run-time version by specifying the `/runtime` flag.

- If your APL .NET class is a web page or a web service, the <code class="language-nonAPL">Debug</code> attribute determines the Dyalog DLL version. This is specified in the opening declaration statement in the **.aspx**, **.asax** or **.asmx** file. If the statement specifies <code class="language-nonAPL">"Debug=true"</code>, then the web page or web service will be bound to the full development version. If the statement specifies <code class="language-nonAPL">"Debug=false"</code>, then the web page or web service will be bound to the run-time version. If you omit the <code class="language-nonAPL">Debug=</code> attribute in your web page, then the value will be determined from the various .NET <code class="language-nonAPL">config</code> files on your computer.

## Forcing a Suspension

If an APL error occurs in an APL .NET object, a suspension will occur and the Session will be available for debugging. It is possible to force this to happen so that you can trace your code.

If your APL class is built directly from a workspace, you can force a suspension by setting stops in your code before using Export to build the DLL. If your class is a web page or web service where the code is contained in a workspace using the _workspace behind_ technique (see [Workspace Behind](../writing-aspnet-webpages/workspace-behind.md)), you can set stops in this workspace before you `)SAVE` it.

If your APL class is defined entirely in a web page, web service, or APL Source file, the only way to set a break point is to insert a line that sets a stop explicitly using `⎕STOP`. It is essential that this line appears after the definition of the function in the script. For example, to set a stop in the web page example from [Your First APL Web Page](../writing-aspnet-webpages/your-first-apl-web-page.md) (code is **[DYALOG]\Samples\asp.net\tutorial\intro1.aspx**), the script section would be amended as follows:
```apl
<script language="dyalog" runat="server">

∇Rotate args
:Access Public
:Signature Reverse Object,EventArgs
(⊃args).Text←⌽Pressme.Text
∇

3 ⎕STOP 'Rotate'

</script>
```

Alternatively, you can introduce a deliberate error into your code!

Finally, you can usually force a suspension by generating a weak interrupt. This is done from the pop-up menu on the APL icon in the System Tray that is associated with the full development version of the Dyalog DLL (the run-time version of the Dyalog DLL does not display an icon in the System Tray). Selecting **Weak Interrupt** from this menu will not have an immediate effect, but it sets a flag that will cause Dyalog to suspend when it next executes a line of APL code. You will need to activate your object in some way, for example, by calling a method, for this to occur. This technique might not work if the Dyalog DLL is busy as a thread switch could automatically reset the Weak Interrupt flag; in this situation, retry.

## Using the Session, Edit, and Trace Windows

!!! Info "Information"
    In this section, a reference to terminating the client application means that APL executes <code class="language-nonAPL">Application.Exit()</code>. This might cause the application to terminate cleanly (as with ASP.NET) or it could cause it to crash.

When an APL .NET object suspends execution, all other active APL .NET objects bound to the full development version of the Dyalog DLL that are currently being executed by the same client application will also suspend. In addition, all the classes currently being hosted by the Dyalog DLL are visible to the APL developer whether active (an instance is currently being executed) or not.

!!! Info "Information"
    If a client application, such as ASP.NET, is also hosting APL .NET objects bound to the  run-time version of the Dyalog DLL, these objects will be hosted in a separate workspace attached to the run-time version of the Dyalog DLL and will not be visible to the developer.

Debugging a running APL .NET object is mostly the same process as debugging a stand-alone multi-threaded APL application. However, there are some important things to remember:

- The namespace structure above your APL class should be treated as being inviolate. There is nothing to prevent you from deleting namespaces, renaming namespaces, or creating new ones in the workspace, but this should not be done.
- You should not alter, delete or rename any functions that have been automatically generated on your behalf by the Dyalog .NET Compiler; these functions should also be treated as being inviolate.
- If execution in the Dyalog DLL is suspended, you cannot execute `)CLEAR` or `)RESET`. You can execute `)OFF` or `⎕OFF`, but doing so will cause the client application to terminate. If you attempt to close the APL Session window, you will be warned that this will terminate the client application.
- If you fix a problem in a suspended function and then press **Resume** or **Continue** (in the **Trace** window) or execute a branch, and the execution of the currently-invoked method succeeds, the state indicator will be emptied (assuming that no other threads are actively involved). The Dyalog DLL is idle at this stage, waiting for the next client request.
- If, at this point, you close the **Session** window, a dialog box will give you the option of terminating the (client) application, or hiding the **Session** window. If you execute `)OFF` or `⎕OFF`, the client application will terminate.
