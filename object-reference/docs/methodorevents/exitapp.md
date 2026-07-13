# <span>ExitApp</span> <span>Event 132</span>

**Applies To:** [Root](../objects/root.md)

**Description**

If enabled, this event is reported when the user attempts to terminate a Dyalog APL/W application from the Windows Task List.

The Windows Task list displays the names of all running applications. The name displayed for a Dyalog APL/W application is defined by the [Caption](../properties/caption.md) property of the system object `Root`. If you fail to define this property, there will be no entry for the application in the Task List.

If you wish to prevent the user from terminating your application from the Windows Task List, you may disable this event by setting its action code to `¯1`. However, if you do this, your user may be puzzled as to why the operation does not work as expected. An alternative is to attach a callback function to the event which displays a message box. Not only does this allow you to provide user feedback, but you can provide confirm/cancel options. If your callback function returns a zero, your application will not be terminated.

Note that this event only provides for termination via the Windows Task List. See also the [ExitWindows](./exitwindows.md) event.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'ExitApp'` or 132     |
