# DYALOG_EVENTLOGGINGLEVEL

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system.

Whether a log entry is written to the Windows Event Log when Dyalog would otherwise pop up a message box because of an unexpected termination.

Valid values are:

- `0` : no entry is written to the Windows Event Log
- `1` : an entry is written to the Windows Event Log

<!-- REVIEW(values,default): confirm whether this is a Boolean or a multi-level setting, and its default; the source describes only whether an entry is written. -->

Related parameters: [DYALOG_EVENTLOGNAME](dyalog-eventlogname.md).

For more information, see [Handling Unexpected Application Errors in Windows](../../../programming-reference-guide/error-trapping/handling-unexpected-errors).
