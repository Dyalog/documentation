# <span>DockStart</span> <span>Event 480</span>

**Applies To:** [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**

If enabled, this event is reported by a dockable object (one whose [Dockable](../properties/dockable.md) property is set to 1) when the user starts to drag it using the mouse.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'DockStart'` or 480   |

A callback function may prevent the docking operation from starting by returning 0.

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).
