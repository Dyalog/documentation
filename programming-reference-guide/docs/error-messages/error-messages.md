# Introduction

The error messages reported by APL are described in this section.  Standard APL messages that provide information or report error conditions are summarised in ["APL Error Messages"](apl-errors.md) and described later in alphabetical order.

APL also reports messages originating from the Operating System (WINDOWS or UNIX) which are summarised in ["Typical Operating System Error Messages"](os-errors.md) and ["Windows Operating System Messages"](windows-errors.md).  Only those Operating System error messages that might occur through normal usage of APL operations are described here.  Other messages could occur as a direct or indirect consequence of using the Operating System interface functions `⎕CMD` and `⎕SH` or system commands `)CMD` and `)SH`, or when a non-standard device is specified for the system functions `⎕ARBIN` or `⎕ARBOUT`.  Refer to the WINDOWS or UNIX reference manual for further information about these messages.

Most errors may be trapped using the system variable `⎕TRAP`, thereby retaining control and inhibiting the standard system action and error report.  The table, [Trappable Event Codes](../../../language-reference-guide/system-functions/trap) identifies the error code for trappable errors.  The error code is also identified in the heading block for each error message when applicable.

See *Dyalog Programming Reference Guide* for a full description of the Error Handling facilities in Dyalog APL.
