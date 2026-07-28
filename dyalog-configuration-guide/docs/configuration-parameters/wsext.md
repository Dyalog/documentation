# WSEXT

This parameter specifies workspace filename extensions. It complements the **WSPATH** parameter in that together they determine the file search order to satisfy `)LOAD` or `)COPY`; it also specifies the filename extension to add on `)SAVE` or `)CONTINUE` if none is explicitly provided.

WSEXT is a string that specifies a colon-separated list of one or more extensions, including any period (".") which separates the extension from its basename.

If undefined, WSEXT defaults to `.dws:` on Windows and macOS, and `:.dws:.DWS` on all other platforms.

In the Windows case, this means that `)LOAD myws` will search first for a file named `myws.dws` , and then for a file named `myws` (with no extension). As file names are not case-sensitive under Windows, this will find `myws.DWS` or `MyWs.Dws` and so forth. If none are found with this extension, it will load `myws` , `MyWs` , `MYWS` etc.

In the second (non-Windows) case note that `)LOAD myws` will search first for a file named `myws` , then `myws.dws` , then `myws.DWS`.

When `)SAVE` and `⎕SAVE` is used without specifying a file extension, the first extension defined by WSEXT is applied to complete the file name. The default is therefore `.dws` in all cases.
