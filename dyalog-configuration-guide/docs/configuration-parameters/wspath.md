# WSPath

The workspace search path: a list of directories searched, in order, when you `)LOAD` or `)COPY` a workspace, or start an Auxiliary Processor, without giving an explicit path. To load workspaces from the current directory, include `.` in the list.

Valid values are a list of directory paths, separated by `;` (Windows) or `:` (UNIX and macOS).

For example, on Windows `WSPath=.;D:\MYWS` causes `)COPY`, `)LOAD`, and `)LIB` to look first in the current directory, then in `D:\MYWS`.

Related parameters: [WSEXT](wsext.md).

See also the [Workspace tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-workspace-tab) of the Windows Configuration Dialog.
