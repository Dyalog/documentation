# WSPath

This parameter defines the workspace path. This is a list of directories that are searched in the order specified when you `)LOAD` or `)COPY` a workspace and when you start an Auxiliary Processor without explicitly specifying a path in the name. The directory paths are specified using Operating System specific conventions and separated by ";" (Windows) or ":" (UNIX).

Note that  to load workspaces from the current directory, "." must be included in the list defined by **WSPath**..

The following Windows example causes `)COPY` , `)LOAD` and `)LIB` to look first in the current directory, then in `D:\MYWS` .
```apl
WSPath=.;D:\MYWS
```

See also [Workspace search path](../configuring-the-ide/configuration-dialog/configuration-dialog-workspace-tab.md).
