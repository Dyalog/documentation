# DYALOG_EVENTLOGNAME

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system.

The name of the Windows Event Log to which an event message is written (or the source of the event message, depending on the Registry entries defined) when Dyalog would otherwise pop up a message box because of an unexpected termination.

Valid values are an event log name or event source name.

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

Related parameters: [DYALOG_EVENTLOGGINGLEVEL](dyalog-eventlogginglevel.md).

For more information, see [Handling Unexpected Application Errors in Windows](../../../programming-reference-guide/error-trapping/handling-unexpected-errors).
