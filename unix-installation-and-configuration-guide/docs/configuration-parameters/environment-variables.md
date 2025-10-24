<h1 class="heading"><span class="name">Environment Variables</span></h1>

Environment variables are used to configure various aspects of Dyalog APL. The complete list appears in the *Dyalog for Microsoft Windows Installation and Configuration Guide: Configuration Parameters*; this section discusses those variables which are of particular importance to the Non-GUI versions of Dyalog APL, and lists those that have meaning to the UNIX versions. Additionally there some non-GUI-specific variables which are described below and some which either do not apply, or may not work as the user might at first expect.

Under UNIX, all environment variables should appear in UPPER CASE. For example, to set the default value of `⎕ML` to 3, then
```
$ export DEFAULT_ML=3
```

If a configuration parameter described in the *Dyalog for Microsoft Windows Installation and Configuration Guide* has a backslash "\" in its name (strictly speaking, appears in a subkey of the Dyalog key in the Windows Registry), this should be replaced with an underscore in the equivalent environment variable. This applies for example to SALT\CommandFolder.

Many of these environment variables are set in the mapl script; their values are either appropriate for the installation location of Dyalog APL, or are set to define reasonable default values.

The environment variables are broken down into several tables:

- [Table 1](#_table-1): The most commonly defined and used for non-GUI versions of Dyalog APL under UNIX. Most of these variables are essential for a usable APL session
- [Table 2](#_table-2): Variables used to control default values in the workspace
- [Table 3](#_table-3): Variables used to configure the Session
- [Table 4](#_table-4): Miscellaneous Variables used by non-GUI Dyalog APL
- [Table 5](#_table-5): Editor-related environment variables
- [Table 6](#_table-6): Tracer-related environment variables
- [Table 7](#_table-7): Ride-related environment variables
- [Table 8](#_table-8): SALT and User Command-related environment variables

Table: Commonly used Variables

|Variable|Notes|
|---|---|
|TERM<br/>APLK<br/>APLK0<br/>APLT<br/>APLTn|Define the input and output translate tables used by Dyalog APL. The values of APLK0 and APLTn override the values of APLK and APLT if set, and they in turn override the value of (Unicode) *default*, or (Classic) TERM if set.<p/><p/>APLK is for input translation, APLT for output translation.<p/><p/>These are used in conjunction with ..|
|`APLKEYS` `APLTTRANS`|Define the search path for the input and output translate tables respectively. If unset, the interpreter will default to `$DYALOG`; if `$DYALOG` too is not set, will default to `/usr/dyalog`.|
|`APLNID`|This variable is ignored by the UNIX versions of Dyalog APL: `⎕AI` and `⎕AN` pick up their values from the user's uid and `/etc/passwd`.|
|`APLSTATUSFD`|If set, this defines the stream number on which all messages for the Status Window appear. It is then possible to redirect this output when APL is started.<p/><p/>If unset, the output will appear in the same terminal window as the APL session, although it is not part of the session; such output can be removed by hitting SR (Screen Redraw - often defined to be Ctrl-L).|
|`DYALOG_NETCORE`|This parameter is a Boolean value with a default value of 1. If set to 0, it disables the .NET interface.|
|`DYALOG_SERIAL`|This parameter contains your Dyalog serial number. This must be set to the serial number issued to you. If not set, then the software is unregistered. For the full licence terms and conditions, see [https://www.dyalog.com/uploads/documents/Terms_and_Conditions.pdf](https://www.dyalog.com/uploads/documents/Terms_and_Conditions.pdf) .|
|`DYALOG_SERIALFILE`|This parameter specifies the full path to the text file containing your Dyalog serial number.|
|`ENABLE_CEF`|This parameter is a Boolean value with a default value of 1. If set to 0, it disables the [Chromium Embedded Framework (CEF)](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework) and at attempt to create an HTMLRenderer object (see [HTMLRenderer](../../../object-reference/objects/htmlrenderer)) will fail with an error message. See Note (below).|
|`ERRORONEXTERNALEXCEPTION`|By default, any error when calling `⎕NA` will result in APL terminating; if `ERRORONEXTERNALEXCEPTION` is set to 1, then APL will instead generate an event 91: `EXTERNAL DLL EXCEPTION` . Be aware however that the workspace may become corrupted. This is best used when developing `⎕NA` code rather than in production.|
|`LIBPATH`|A suitable entry for the Conga libraries needs to be added to the `LIBPATH` variable if Conga is to be used. For more information see the *Conga Guide*.|
|`MAXWS`|Defines the size of the workspace that will be presented to the user when Dyalog APL is started. A simple integer value will be treated as being in KB. K, M and G can be appended to the value to indicate KiB, MiB and GiB (binary) respectively. If unset, the default value is 256M.|
|`WSPATH`|Defines the search path for both workspaces and Auxiliary processors.<p/><p/>If unset, there is no default value. Workspaces and APs that are not on the `WSPATH` can be accessed using absolute or relative pathnames.|

## Note

Currently the value of the **Enable_CEF** parameter defined in the Windows Registry or in a
Configuration file is ignored. Only the value set in the command line or as an
environment variable is honoured. If not defined in this way, the default value
is used.

Under macOS and Linux, if the configuration parameter **ENABLE_CEF** is 1, Auxiliary Processors cannot be used (they hang on error). The default value is 1 unless you are not running under a desktop (for example, you are running Dyalog in a PuTTY session when the default is 0).

Table: Default workspace values

|Variable|Notes|
|---|---|
|`DEFAULT_DIV`|Default value for `⎕DIV` in a clear workspace.|
|`DEFAULT_IO`|Default value for `⎕IO` in a clear workspace.|
|`DEFAULT_ML`|Default value for `⎕ML` in a clear workspace.|
|`DEFAULT_PP`|Default value for `⎕PP` in a clear workspace.|
|`AUTO_PW` `DEFAULT_PW`|`⎕PW` is set by the interpreter when it starts, or when the session window is resized. Under UNIX if the terminal window is resized, the session will be resized when the interpreter next checks for input.|
|`DEFAULT_RTL`|Default value for `⎕RTL` in a clear workspace.|
|`DEFAULT_WX`|Default value for `⎕WX` in a clear workspace. Note that although the UNIX versions of Dyalog APL do not have GUI objects, `⎕SE` is present, and the value of `⎕WX` will affect the programmer's ability to run expressions such as `⎕SE.PropList`.|

For numeric values, the interpreter takes the value of the environment variable, and prepends a "0" to that string. It then parses the string, accepting characters until the first non-digit character is reached.

This string, now of digits only, is converted into an integer. If the resulting value is valid, then that is the value that will be used in the workspace. If the resulting value is invalid, then the default value will be used instead.

Table: Variables used to configure the Session

|Variable|Notes|
|---|---|
|`APLAN_FOR_OUTPUT`|Enable or disable use of [array notation](../../../programming-reference-guide/introduction/arrays/array-notation/) for session output|
|`DYALOGLINK`|Specifies the directory for Link|
|`DYALOGSTARTUPSE`|Specifies one or more *Session initialisation* directories that contain APL code to be installed in `⎕SE`|
|`DYALOGSTART_X`|Specifies whether the `Run` function is executed during Session startup|
|`DYALOG_GUTTER_ENABLE`|Enable or disable Session Gutter|
|`HISTORY_SIZE`|The size of the prior line buffer|
|`INPUT_SIZE`|The size of the buffer used to store lines marked for execution|
|`LOG_FILE` `LOG_FILE_INUSE` `LOG_SIZE`|These three variables determine the name of the session log file (default `~/.dyalog/session_log_<DyalogMajor><DyalogMinor><U|C><bits>_*.dlf`, for example, `~/.dyalog/session_log_190U64_*.dlf`), whether a log file is created or not, and the size of the log file in KB. Be aware: the session log file is not interchangeable between the different editions and widths of APL; in a mixed environment it is strongly recommended to use a different log file for each version.|
|`PFKEY_SIZE`|The size of the buffer used to hold `PFKEY` definitions: if this is too small, an attempt to add a new definition will result in a `LIMIT ERROR`.|
|`SESSION_FILE`|Defines the location of your session file; session file support was added in Dyalog 13.1. The default value is `$DYALOG/default.dse`|

To set values, use K to indicate KB. Note that the buffers will contain other information, so the buffer size will not be exact. Note also that multibyte Unicode characters will take up more space than single byte characters, and that 32 and 64 bit versions of Dyalog APL can require different amounts of space for holding the same information.

Example:
```
HISTORY_SIZE=4K my_apl_startup_script
```

Table: Miscellaneous Variables used by non-GUI Dyalog APL

|---|---|
|Variable|Notes|
|`APL_TEXTINAPLCORE`|If set with the value 1 the "Interesting Information" section is included in an aplcore file. Otherwise this section is omitted. By default the interpreter has this set to 0; it is the default APL script which sets it to 1.|
|`AUTOFORMAT` `TABSTOPS`|If `AUTOFORMAT` is 1, then control structures will be shown with indents, set at `TABSTOPS` spaces; the changes are reflected in the editor window when the `RD` (ReDraw) command key is hit.|
|`AUTOINDENT`|If `AUTOINDENT` is set to 1, then if a line is added it is indented the same as the previous line.|
|`AUTO_PW`|Introduced in 13.0. With `AUTO_PW=0` `⎕PW` remains fixed at the size of the terminal window when APL was started. When set to 1, or unset, `⎕PW` alters each time the terminal window is resized.|
|`DYALOG`|This variable is defined in the supplied `mapl` startup script, and is used to form the default values for `APLKEYS`, `APLTRANS`, `WSPATH` etc. If it is necessary to identify the location of the Dyalog executable, then a more reliable method is to determine the full path name from the appropriate file in the `/proc/<process_id_of_APL_session>/` subdirectory or from the output of `ps`.|
|`DYALOG_SHELL_SUBPROCESS`|On AIX, if `DYALOG_SHELL_SUBPROCESS` is `1` (the default on AIX), the interpreter starts a (small) child process that handles calls to `⎕SHELL`.|

These are the remaining variables listed in the *Dyalog for Microsoft Windows Installation and Configuration Guide* which are effective in the non-GUI UNIX versions of Dyalog APL

Table: Editor-related environment variables

|---|---|
|Variable|Notes|
|`APLAN_FOR_EDITOR`|Enable or disable use of [array notation](../../../programming-reference-guide/introduction/arrays/array-notation/) for editing arrays|
|`EDITOR_COLUMNS_*`|See [Configuring the Editor](../configuring-the-editor.md). Can be one of `EDITOR_COLUMNS_CHARACTER_ARRAY EDITOR_COLUMNS_CLASS EDITOR_COLUMNS_FUNCTION EDITOR_COLUMNS_NAMESPACE EDITOR_COLUMNS_NUMERIC_ARRAY`|
|`DYALOG_DISCARD_FN_SOURCE`|Specifies whether source code is retained in the workspace|

Table: Tracer-related environment variables

|--------------|--------------------------------------------------------------------------------------|
|Variable      |Notes                                                                                 |
|`TRACE_ON_ERROR`|With this is set to 1 (the default) the tracer is opened if an untrapped error occurs.|

Table: Ride-related environment variables

|---------|----------------------------------------------------------------------------|
|Variable |Notes                                                                       |
|`RIDE_INIT`|Enables and configures Ride; see the [Ride User Guide](https://dyalog.github.io/ride) for more information.|

Table: SALT and user commands related environment variables

|---|---|
|Variable|Notes|
|`SESSION_FILE`|Specifies the location of the file containing `⎕SE` . The default value is `$DYALOG/default.dse`|
|`UCMDCACHEFILE`|Specifies the location of the user command cache file. Defaults to `"UserCommand{UcmdMajor}{UcmdMinor}.{DyalogMajor}{DyalogMinor}{U|C}{bits}.cache"` , for example, `UserCommand25.182U64.cache` in the `dyalog` directory.|

Further information about SALT and user commands appear in the *User Commands User Guide* and the *SALT User Guide*.
