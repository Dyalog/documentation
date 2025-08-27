<h1 class="heading"><span class="name">Key Features</span></h1>

## Upgrading from Version 17.1 to Version 19.0

Please note that if you are upgrading from Version 17.1 to Version 19.0, you should read the [Release Notes for Version 18.0](https://help.dyalog.com/19.0/index.htm#RelNotes18.0/Key%20Features.htm) and the [Release Notes for Version 18.2](https://help.dyalog.com/19.0/index.htm#RelNotes18.2/Key%20Features.htm) in conjunction with this document.

## Linux Restriction

There is a new restriction in Version 19.0 for Linux which will also apply in forthcoming new versions.

Under macOS and Linux, if the configuration parameter **ENABLE_CEF** is 1, Auxiliary Processors cannot be used (they hang on error). The default value is 1 unless you are not running under a desktop (for example, you are running Dyalog in a PuTTY session when the default is 0).

## Dyalog APL on macOS

- Dyalog APL Version 19.0 is available as both a native Intel-based macOS version and a native ARM-based macOS version. Version 19.0 is expected to be the last version to be compiled for Intel-based Macs.

## New Language Features

- Currently, multi-threaded applications rely on hand-picked token types and require coordination between developers in the choice of these tokens. There is a new system function designed to remove the need for hard-coded token numbers. See [Allocate Token Range](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/talloc.htm#AllocateTokens).

## Improved Language Features

- A variant option `CharSet` is provided to restrict the result of `⎕JSON` export to ASCII characters. Non-ASCII characters are converted to encoded strings. 
- The memory manager has been extended to give the programmer finer control over `WS FULL` errors. See [Memory Manager Statistics](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Memory%20Manager%20Statistics.htm#MemoryManagerStatistics).
- `⎕NCOPY` and `⎕NMOVE` now provide an option for an APL callback function to be invoked during execution. This allows the programmer to monitor and/or report progress and/or abort when processing a lot of data. See [Extension to Native File Functions](extension-to-native-file-functions.md).
- The Recurse variant option for `⎕NINFO` has been extended to allow a limit to the level of sub-directories that are searched.  See [Native File Information](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/ninfo.htm#File_Info).
- `⎕NINFO` has been extended to provide file times as UTC Dyalog Date Numbers. See [Native File Information](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/ninfo.htm#File_Info).
- The list of standard characters for the `S` qualifier of `⎕FMT` has been extended to include the high minus symbol (`¯`). See [Format (Dyadic)](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/Format%20Dyadic.htm#Format(Dyadic)).
- An option is provided to control the implementation of lexical scope in Namespace and Class scripts. This extension applies only to `⎕FIX`; scripts fixed using the editor are unaffected by this change. See [Lexical Scope in Scripts](lexical-scope-in-scripts.md) and [Fix Script](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/fix.htm#FixScript).
- An option is provided to control whether or not source code is retained in the workspace exactly as it was typed. This is now the default. See [Source as Typed](./source-as-typed.md), [Discard Source Information](../language-reference-changes/discard-source-code.md) and [Discard Source Information](../language-reference-changes/discard-source-information.md).
- Support is added for LZ4 *frames* which allows the LZ4 compression library to handle data > 2GB in size. Previously, extremely large file components could not be compressed because the LZ4 library could not process them and they were written uncompressed. Now, these large components will (in the absence of any other reason) be compressed as well. However, such components will be unreadable by previous Versions. `3012⌶` allows the user to specify that LZ4 frames should not be used for component compression, for when interoperability is required. See [Enable Compression of Large Components](../language-reference-changes/enable-compression-of-large-components.md). `219⌶` has been extended to allow arrays >2GB to be compressed.
- There is a new I-beam function to set the parameters for generating aplcore files dynamically. See [Set aplcore Parameters](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Set%20aplcore%20Parameters.htm#set_aplcore_parameters).
- `⎕FHOLD` now accepts an optional left argument to specify a time-out. See [File Hold](../language-reference-changes/fhold.md).
- The right argument to `⎕SIGNAL` may include 1006 (`TIMEOUT` error).

## GUI Improvements

- The HTMLRenderer provides a number of new Properties and Methods. See [AllowContextMenu](../object-reference-changes/allowcontextmenu.md), [ExecuteJavaScript](../object-reference-changes/executejavascript.md), [GetZoomLevel](../object-reference-changes/getzoomlevel.md), [IsLoading](../object-reference-changes/isloading.md), [LoadEnd](../object-reference-changes/loadend.md), and [SetZoomLevel](../object-reference-changes/setzoomlevel.md).

## Session Initialisation Improvements

- There is a new Boolean configuration parameter that determines whether or not the Session is initialised on start-up. See [DYALOG_INITSESSION](../configuration-parameters/dyalog-initsession.md). By default this is 1 for the development version and 0 for the run-time. This must be 1 to use Link.
- Nested directory structures are now supported.
- Every top-level directory that is loaded as a namespace in `⎕SE` can have a `Run` function which will be called after everything has been loaded. See [DyalogStartup_X](../configuration-parameters/dyalogstartup-x.md) for how to disable this.
- Note that Link is now required for Session initialisation. See [DyalogLink](../configuration-parameters/dyaloglink.md) for how to use a non-default Link.
- The list of directories from which `⎕SE` is populated can now be extended rather than just replaced. See [DyalogStartupSE](../configuration-parameters/dyalogstartupse.md).

## Session Improvements

- Multi-line input, which was introduced in 18.0, is now enabled by default. On Windows this can be changed by selecting/unselecting the "Enable Multiline Input" Checkbox on the Session tab of the Configure dialog, or on all platforms by setting the configuration parameter DYALOG_LINEEDITOR_MODE to 0 (disabled) or 1 (enabled).
- The log file used by the Session is now unique to the instance of Dyalog that is running and is reported by a new LogFile property of `⎕SE`. Previously, multiple instances of the Dyalog program shared the same session log. See [Log_File](../configuration-parameters/log-file.md). 
- Session log files are now saved in JSON format.
- The Session window (optionally) reserves the first column for information. See [DYALOG_GUTTER_ENABLE](../configuration-parameters/dyalog-gutter-enable.md). On TTY-versions it is hidden by default.
- Lines output to the Session which are associated with errors are now syntax coloured using the *error* colour for the selected Session colour scheme.
- The Caption property of the Session, which was previously read-only, can now be set. See below.
- When you edit an object by double-clicking the mouse or pressing the `<ED>` key, or executing `)ED`, and the name of the object is followed by `[n]`, the Editor will position the cursor on line number `n`. Note that there must not be a space between the last character of the name and the "`[`".

## Session Caption

The Caption property of the Session may be set dynamically to a character vector comprising free text and field names. Field names must be enclosed in braces and are replaced in-situ by corresponding values.

|Field Name|Description                          |
|----------|-------------------------------------|
|{TITLE}   |the window specific text             |
|{WSID}    |`⎕WSID`                              |
|{NSID}    |current namespace                    |
|{SNSID}   |short version of namespace (no `#` .)|
|{PRODUCT} |for example, Dyalog APL/W            |
|{VER_A}   |for example, 19                      |
|{VER_B}   |for example, 0                       |
|{VER_C}   |for example, 47586 (SVN revision)    |
|{PID}     |process ID (decimal)                 |
|{CHARS}   |"Classic" or "Unicode"               |
|{BITS}    |"32" or "64"                         |

Table: Session Caption Fields

<h3 class="example">Example</h3>
```apl
     ⎕SE.Caption←'Pete: {WSID} {Product} {VER_A}.{VER_B}'
```

The Session caption in a `CLEAR WS` will change to:
```apl
     Pete: CLEAR WS Dyalog APL/W-64 19.0
```

Note that Caption returns the codified string used to set it.
```apl
     ⎕SE.Caption
Pete: {WSID} {Product} {VER_A}.{VER_B}
```
