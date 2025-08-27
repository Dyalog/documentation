<h1 class="heading"><span class="name">Log_File</span></h1>

This parameter specifies the pathname to the Session log file; it can be absolute or relative to the working directory.

The Session log file is not interchangeable between different versions/editions/widths of Dyalog – this means that opening a new instance of Dyalog will overwrite any contents of the Session log file populated by an already‑running instance. However, if the LOG_FILE parameter contains a '`*`' (for example,  `JD.*.dlf` ) then at start-up Dyalog will attempt to open, and then **lock**, a file where the '`*`' has been replaced with an increasing integer value (starting with 000, so `JD.000.dlf`, `JD.001.dlf` etc). If said file cannot be opened and locked, the value will be incremented. The process will fail, and no log will be used if the extension number would exceed 999.

The default is `Users\<username>\Documents\Dyalog APL-<bits> <DyalogMajor>.<DyalogMinor> <Unicode|Classic> Files\default_*.dlf`, for example, `Users\Bob\Documents\Dyalog APL-64 19.0 Unicode Files\default_*.dlf`

Note that the LogFile property of `⎕SE` reports the name of the log file that is being used.

See also [Use log file](https://help.dyalog.com/19.0/index.htm#UserGuide/The%20APL%20Environment/Configuration%20Dialog%20Session%20Tab.htm).
