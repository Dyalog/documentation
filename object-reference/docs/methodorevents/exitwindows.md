# <span>ExitWindows</span> <span>Event 131</span>

**Applies To:** [Root](../objects/root.md)

**Description**

If enabled, this event is reported when the user attempts to terminate the Windows Operating System. When this is done, Windows gives all running applications the opportunity to prevent it. Typically, an application that has unsaved changes will display a dialog box warning the user of this situation and offering the opportunity to cancel the termination. The default action for this event is to allow Windows to close. You can prevent this by returning a zero from a callback function. You can also prevent the user from closing Windows down by disabling the event altogether. This is achieved by setting its action code to `¯`1. In most cases this is less preferable than the callback method as it does not allow you to inform the user as to why Windows won't terminate.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'ExitWindows'` or 131 |
|`[3]`|Flag  |0 or 1                 |

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).
