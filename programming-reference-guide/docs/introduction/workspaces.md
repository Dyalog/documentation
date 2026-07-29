# Workspaces

APL expressions are evaluated within a workspace. The workspace may contain objects, namely classes, namespaces, operators, functions and variables defined by the user. APL expressions may include references to primitive operators, functions and variables provided by APL. These objects do not reside in the workspace, but space is required for the actual process of evaluation to accommodate temporary data. During execution, APL records the state of execution through the STATE INDICATOR which is dynamically maintained until the process is complete. Space is also required to identify objects in the workspace in the SYMBOL TABLE. Maintenance of the symbol table is entirely dynamic. It grows and contracts according to the current workspace contents.

Workspaces may be explicitly saved with an identifying name. The workspace may subsequently be loaded, or objects may be selectively copied from a saved workspace into the current workspace.

Workspaces are stored in files whose names must conform to operating system conventions. When a workspace name is specified without a file suffix, these are added or implied. For further information, see [WSEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/wsext).

If the name of the file in which the workspace is saved contains spaces, the ws argument for the system functions `)SAVE`, `)COPY`, `)PCOPY`, `)LOAD`, `)XLOAD` and `)DROP` should be surrounded by two double-quote (") characters. To include a " character in the file name, you must specify two adjoining double-quotes (that is, """"). Note however that Windows does not allow double-quotes in file names, so this effectively applies only to non-Windows systems.

<h2 class="example">Examples</h2>
```apl
      )SAVE Pete's work
unacceptable char
```

The above statement fails because the presence of the space in the file name requires that it be surrounded by "s.
```apl
      )SAVE "Pete's work"
Pete's work.dws saved Sun Jan 17 16:23:17 2016

      )COPY "Pete's work" A B C
.\Pete's work.dws saved Sun Jan 17 16:23:17 2016

      )DROP "Pete's work"
Sun Jan 17 16:24:16 2016

```
