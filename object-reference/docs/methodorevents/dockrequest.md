# <span>DockRequest</span> <span>Event 482</span>

**Applies To:** [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**

If enabled, this event is reported by a client object just before it is docked in a host object, when the user releases the mouse button.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows :

|-----|-----------------|-----------------------|
|`[1]`|Object           |ref or character vector|
|`[2]`|Event            |`'DockRequest'` or 482 |
|`[3]`|Host Object      |ref or character vector|
|`[4]`|Edge             |character vector       |
|`[5]`|y-position       |number                 |
|`[6]`|x-position       |number                 |
|`[7]`|Outline rectangle|4-element nested       |

Elements 4-7 of this event message are the same as those reported by [DockMove](./dockmove.md), and the effect of a callback function is identical. See [DockMove](./dockmove.md) for further information.
