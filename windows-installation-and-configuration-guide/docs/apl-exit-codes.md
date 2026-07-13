# APL Exit Codes

When APL or a bound .EXE terminates, it returns an exit code to the calling environment. If APL is started from a desktop icon, the return code is ignored. However, if APL is started from a script (UNIX) or a command processor, the exit code is available and may be used to determine whether or not to continue with other processing tasks. The return codes are:

|---|----------------------------------------------------------------------------------------------|
|0  |Successful `⎕OFF` , `)OFF` , `)CONTINUE` , graphical exit from GUI                            |
|1  |APL failed to start. This will occur if there was a failure to read a translate file, there is insufficient memory, or a critical parameter is incorrectly specified or missing.|
|2  |APL was terminated by SIGHUP or SIGTERM (UNIX) or in response to a QUIT WINDOWS request. APL has done a clean exit. |
|3  |APL issued a syserror.                                                                        |
|4  |Runtime violation. This occurs if a runtime application attempts to read input from the Session. Only a development version has a Session. |
|5  |APL was unable to load the Conga libraries (14.1.25383 onwards). In 16.0 the Ride libraries have been included in the Conga libraries. |
|6  |RIDE_INIT or one of its components was ill-defined, or APL was unable to use the port, and/or unable to resolve the hostname (14.1.25383 onwards)|
|7  |Reserved                                                                                       |
|8  |Windows rejected APL's request to create a session window (in earlier versions this generated a syserror 126) |
|9  |Dyalog has encountered a Microsoft Windows-related error when starting and is unable to continue. For example it cannot register clipboard formats.|
|10 |CEF sub-process crash - something has gone unexpectedly wrong with either the HTMLRenderer or CEF sub-processes and cannot continue |
|11 |Cannot create c-stack (macOS only)                                                             |

## Notes

Under UNIX exit codes greater than 127 indicates (127+signal number) of the untrapped signal which caused the process to terminate.

APL applications can generate  a custom return code by specifying an integer value to the right of `⎕OFF`. Dyalog recommends using values greater than 12 for this purpose.
