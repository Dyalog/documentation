




<h1 class="heading"><span class="name">Load Workspace</span> <span class="command">)LOAD {ws}</span></h1>



This command causes the named stored workspace to be loaded.  The current active workspace is lost.


`ws` specifies a file name. If no file extension is given, it is implied. See [WSEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/wsext).


If `ws` is a full or relative pathname, only the specified directory is examined.  If not, the APL workspace path (`WSPATH`) is traversed in search of the named workspace.  A stored workspace is one which has previously been saved with the system command `)SAVE` or the system function `⎕SAVE`.  Under Windows, if `ws` is omitted, the File Open dialog box is displayed.



If the workspace name is not valid or does not exist or if access to the workspace is not authorised, the system reports `ws not found`.  If the workspace name identifies a file or directory that is not a workspace, the system reports  `wsname is not a ws`.  If successfully loaded, the system reports workspace name `saved`, followed by the date and time when the workspace was last saved.  If the workspace is too large to be loaded into the APL session, the system reports `ws too large`.  After loading the workspace, the current namespace is set to `#` and the latent expression (`⎕LX`) is executed unless APL was invoked with the **-x** option. If the workspace was saved with a suspension, typing the expression `→1+⎕LC` will resume execution and switch back into the namespace associated with the suspended function.


If the workspace contains any GUI objects whose `Visible` property is 1, these objects will be displayed.  If the workspace contains a non-empty `⎕SM` but does not contain an SM GUI object, the form defined by `⎕SM` will be displayed in a window on the screen.


Holding the Ctrl key down while entering a `)LOAD` command or selecting a workspace from the session file menu causes the incoming latent expression to be *traced.*


Holding the Shift key down while selecting a workspace from the session file menu will *prevent* execution of the latent expression.

<h2 class="example">Example</h2>
```apl

      )LOAD dfns
C:\Program Files\Dyalog\Dyalog APL-64 ...

An assortment of D Functions and Operators.

      tree #                ⍝ Workspace map.
      ↑¯10↑↓attrib ⎕NL 3 4  ⍝ What's new?
      notes find 'Word'     ⍝ Apropos "Word".
```


