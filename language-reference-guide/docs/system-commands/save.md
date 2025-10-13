




<h1 class="heading"><span class="name">Save Workspace</span> <span class="command">)SAVE {-force} {ws}</span></h1>



This command compacts (see [Workspace Available](../system-functions/wa.md) for details) and saves the active workspace.


If specified, `ws` is a full or relative path name to the file in which the workspace will be written. If `ws` is omitted, it defaults to `⎕WSID`. Unless the path specified by `ws` or `⎕WSID` is a full pathname, it is taken to be relative to the current working directory which may be obtained by the expression: `⊃1 ⎕NPARTS ''`.


If  `ws` specifies a file name other than that implied by  `⎕WSID`, the specified file must not already exist unless the **force** parameter is specified.. If `ws` is omitted or resolves to the same file as  `⎕WSID`, an existing stored workspace with the same name will be replaced.


See [Programmer's Guide: "Workspaces"](../../../programming-reference-guide/introduction/workspaces) for the rules for specifying a workspace name.


If an extension is not specified, an extension is added according to the [**WSEXT** parameter](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters)..


A workspace may not be saved if any threads (other than the root thread 0) are running or if there are any Edit or Trace windows open. Otherwise, the workspace is saved with its state of execution intact, however certain operations may be performed before it is saved. For further information, see [Set Workspace Save Options](../primitive-operators/i-beam/set-workspace-save-options.md).




`)SAVE` may fail with one of the following error messages:


|---|---|
|`unacceptable char`|The given workspace name was ill-formed|
|`not saved this ws is WSID`|An attempt was made to change the name of the workspace for the save, and the renamed workspace already existed. This error can be overridden by specifying the `-force` argument.|
|`not saved this ws is CLEAR WS`|The active workspace was `CLEAR WS` and no attempt was made to change the name.|
|`Can't save - file could not be created.`|The workspace name supplied did not represent a valid file name for the current Operating System.|
|`cannot create`|The user does not have access to create the file OR the workspace name conflicts with an existing non-workspace file.|
|`cannot save with windows open`|A workspace may not be saved if trace or edit windows are open.|
|`Cannot overwrite old workspace`|An attempt was made to save the workspace with a newer version of the interpreter than that with which it was originally saved. This error can be avoided by specifying the `-force` argument.|


After a successful save, the system reports the workspace name, followed by the word  "`saved`" and the current time and date; and if `ws` specified a new name, `⎕WSID` is assigned that name.


<h2 class="example">Example</h2>
```apl
      )SAVE MYWORK
./MYWORK saved Thu Sep 17 10:32:20 1998
```


Note that any time prior to executing `)SAVE`, the active workspace may be renamed by the system command `)WSID` or by assigning a name to the system variable `⎕WSID`.


A stored workspace may subsequently be loaded with the system command `)LOAD` or the system function `⎕LOAD`, and objects may be copied from a stored workspace with the system commands `)COPY` or `)PCOPY` or the system function `⎕CY`.



