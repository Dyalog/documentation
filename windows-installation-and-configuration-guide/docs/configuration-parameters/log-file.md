<h1 class="heading"><span class="name">Log_File</span></h1>

This parameter specifies the path (absolute or relative to the working directory) and name of the Session log file.

Session log files are not interchangeable between different versions/editions/widths of Dyalog. In addition, starting multiple instances of a Dyalog interpreter with the same log file name will only create a log file for the first instance started.

This is mitigated by including a __\*__ character in the default Session log’s filename, for example, __log.\*.dlfx__ or __log\*.dlfx__. In this situation, at start-up, Dyalog attempts to open, and then lock, a file in which the __\*__ is replaced with an increasing integer value starting from __000__, for example, __log\*.dlfx__ results in files called __log000.dlfx__, __log001.dlfx__, and so on. If a file cannot be opened and locked, the value is incremented. This means that starting multiple instances of the same interpreter simultaneously will create and open multiple log files with different values. If one or more instances are then closed, starting a new instance will re-open the closed log file for that interpreter that has the lowest value. The process fails, and no log will be created or used, if the value would exceed __999__.

NOTE: The LogFile property of `⎕SE` reports the name of the log file that is being used.

The default is __<DocumentsDirectory\>\Dyalog APL-<bits\> <DyalogMajor\><DyalogMinor\> <Unicode|Classic\> Files\default_\*.dlfx__, for example, __C:\Users\Bob\Documents\Dyalog APL-64 20.0 Unicode Files\default_\*.dlfx__

See also [Use log file](../configuring-the-ide/configuration-dialog/configuration-dialog-session-tab.md).
