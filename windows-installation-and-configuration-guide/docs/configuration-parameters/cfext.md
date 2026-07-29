# CFEXT

This parameter specifies component file filename extensions.

CFEXT is a string that specifies a colon-separated list of one or more extensions, including any period (".") which separates the extension from its basename.

If undefined, CFEXT defaults to `.dcf:` on Windows and macOS, and `.dcf:.DCF:` on all other platforms.

In the Windows case, this means that `'myfile'⎕FTIE 0` will search first for a file named `myfile.dcf` , and then for a file named `myfile` (with no extension). As file names are not case-sensitive under Windows, this will find `myfile.DCF` or `MyFile.Dcf` and so forth. If none are found with this extension, it will load `myfile` , `MyFile` , `MYFILE` etc.

In the second (non-Windows) case note that `'myfile'⎕FTIE 0` will search first for a file named `myfile` , then `myfile.dcf` , then `myfile.DCF` .
