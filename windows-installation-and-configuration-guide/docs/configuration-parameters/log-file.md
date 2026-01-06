<h1 class="heading"><span class="name">Log_File</span></h1>

This parameter specifies the pathname to the Session log file; it can be absolute or relative to the working directory.

The Session log file is not interchangeable between different versions/editions/widths of Dyalog – this means that opening a new instance of Dyalog will overwrite any contents of the Session log file populated by an already-running instance. If you have more than one instance of Dyalog installed, then Dyalog Ltd strongly recommends using a different Session log file for each instance. This can be achieved by including a __\*__ character in the filename (for example, __log.\*.dlf__ or __log\*.dlf__). In this situation, at start-up, Dyalog attempts to open, and then locks, a file in which the __\*__ has been replaced with an increasing integer value starting with __000__, for example, __log\*.dlf__ results in files called __log000.dlf__, __log001.dlf__, and so on. If a file cannot be opened and locked, the value will be incremented. The process fails, and no log will be used, if the extension number would exceed __999__.

The default is __C:\Users\<username>\Documents\Dyalog APL-<bits> <DyalogMajor>.<DyalogMinor> <Unicode|Classic> Files\default_\*.dlf__, for example, __C:\Users\Bob\Documents\Dyalog APL-64 20.0 Unicode Files\default_\*.dlf__

Note that the LogFile property of `⎕SE` reports the name of the log file that is being used.

See also [Use log file](../configuring-the-ide/configuration-dialog/configuration-dialog-session-tab.md).
