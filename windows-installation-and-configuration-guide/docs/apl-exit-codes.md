# APL Exit Codes

When APL or a bound **.exe** terminates, it returns an exit code to the calling environment. If APL is started from a desktop icon, the return code is ignored. However, if APL is started from a script (Unix) or a command processor, the exit code is available and can be used to determine whether to continue with other processing tasks. Additionally, APL applications can themselves return their own exit codes by calling [`⎕OFF`](../../language-reference-guide/system-functions/off) followed by an integer. The interpreter's own exit codes are:

|---|----------------------------------------------------------------------------------------------|
|0  |Successful `⎕OFF`, [`)OFF`](../../language-reference-guide/system-commands/off), [`)CONTINUE`](../../language-reference-guide/system-commands/continue), graphical exit from GUI.                           |
|1  |APL failed to start. This will occur if there was a failure to read a translate file, there is insufficient memory, or a critical parameter is incorrectly specified or missing.|
|2  |APL was terminated by SIGHUP or SIGTERM (Unix) or in response to a QUIT WINDOWS request. APL has done a clean exit. |
|3  |APL issued a syserror.                                                                        |
|4  |Runtime violation. This occurs if a runtime application attempts to read input from the Session. Only a development version has a Session. |
|5  |APL was unable to load the Conga libraries (Dyalog v14.1.25383 onwards – in Dyalog v16.0, the Ride libraries have been included in the Conga libraries. |
|6  |RIDE_INIT or one of its components was ill-defined, or APL was unable to use the port, and/or unable to resolve the hostname (14.1.25383 onwards)|
|7  |Reserved                                                                                       |
|8  |Microsoft Windows rejected APL's request to create a session window |
|9  |Dyalog has encountered a Microsoft Windows-related error when starting and is unable to continue (for example, it cannot register clipboard formats).|
|10 |CEF sub-process crash – something has gone unexpectedly wrong with either the HTMLRenderer or CEF sub-processes and cannot continue |
|11 |Cannot create c-stack (macOS only)                                                             |

Under Unix, exit codes greater than 127 indicates (127+signal number) of the untrapped signal which caused the process to terminate.

!!! Hint "Hints and Recommendations"
    APL applications can generate a custom return code by specifying an integer value to the right of `⎕OFF`. Dyalog recommends using values greater than 13 for this purpose.
