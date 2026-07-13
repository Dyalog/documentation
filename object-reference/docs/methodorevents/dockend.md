# <span>DockEnd</span> <span>Event 484</span>

**Applies To:** [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**

If enabled, this event is reported by a client object after it has been successfully docked in a host object.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'DockEnd'` or 484     |

This event is reported for information only and cannot be cancelled or inhibited in any way.
