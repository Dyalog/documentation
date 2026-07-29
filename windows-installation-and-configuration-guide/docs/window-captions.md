# Window Captions

The captions of the various windows that comprise the Dyalog Integrated Development Environment (IDE) are user-configurable and defined by entries in the Windows registry in the *Captions* subkey of the main Dyalog key.

Note that this only applies when the windows are floating (un-docked). When a window is docked Dyalog displays a fixed non-configurable caption.

Note also that the *Captions* subkey is not created by the interpreter; the user must create the subkey and the values.

Each entry is a string value whose name identifies the window as follows:

|Window Name   |Description                                                                                                                       |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|
|Session       |The main Dyalog APL session window                                                                                                |
|Editor        |The Editor window                                                                                                                 |
|SysTray       |The hint on Dyalog icons in the System Tray                                                                                       |
|MessageBox    |The notification Message Box that is displayed in various circumstances; for example, when an object cannot be fixed by the Editor|
|Explorer      |The Workspace Explorer tool                                                                                                       |
|Rebuild Errors|The dialog box that is displayed if one or more objects cannot be re-instantiated when a workspace is loaded                      |
|Status        |The Status window                                                                                                                 |
|Event Viewer  |The Event Viewer                                                                                                                  |
|FindReplace   |The Find/Replace dialog box                                                                                                       |
|ExitDialog    |The Exit dialog box that is displayed when the user closes the Session window                                                     |
|WSSearch      |The Find Objects tool                                                                                                             |
|Syserror      |The Syserror Message Box                                                                                                          |

Each string value should contain a mixture of your own text and keywords which are enclosed in braces, for example, {TITLE}. Keywords act like variables and are replaced at display time by corresponding values as described in the table below.

|Keyword    |Value                                                                |
|-----------|---------------------------------------------------------------------|
|`{TITLE}`  |The window name shown in the first column of the previous table      |
|`{WSID}`   |Workspace ID ( `⎕WSID` )                                             |
|`{NSID}`   |Current Namespace                                                    |
|`{SNSID}`  |Current Namespace (short version)                                    |
|`{PRODUCT}`|The name of the Dyalog product, for example, "Dyalog APL/W - 64"     |
|`{VER_A}`  |The main version number, for example, "14"                           |
|`{VER_B}`  |The secondary version number, for example, "0"                       |
|`{VER_C}`  |The tertiary  version number (currently the internal revision number)|
|`{PID}`    |The process ID                                                       |
|`{CHARS}`  |"Classic" or "Unicode"                                               |
|`{BITS}`   |"32" or "64"                                                         |
|`{XLOC}`   |The namespace currently being explored (Explorer only)               |

For example, if the Registry contains *.\Captions\Session* whose value is:
```apl
    My APL ({WSID}) Version {VER_A}.{VER_B}[{VER_C}]  - {PID}
```

then the caption displayed in a new Dyalog APL Session window might be:
```apl
    My APL (CLEAR WS) Version 14.0[20105] - 4616
```
