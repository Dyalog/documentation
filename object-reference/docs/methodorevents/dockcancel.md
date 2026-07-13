# <span>DockCancel</span> <span>Event 485</span>



**Applies To:** [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**


If enabled, this event is reported by a client object when the user aborts a docking operation by pressing Escape.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'DockCancel'` or 485  |


This event is reported for information only and cannot be cancelled or inhibited in any way.


The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).



