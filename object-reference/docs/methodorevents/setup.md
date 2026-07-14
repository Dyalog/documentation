# <span>Setup</span> <span>Method 101</span>

**Applies To:** [Printer](../objects/printer.md)

**Description**

This method causes the system to display a standard [Printer](../objects/printer.md) Setup dialog box and thereby allows the user to alter the printer settings. This is a "modal" dialog box that must be closed before the APL application can continue.

The Setup method is niladic.

If you attach a callback function to this event and have it return a value of 0, the dialog box will not appear.
