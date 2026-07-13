# <span>DockMove</span> <span>Event 481</span>

**Applies To:** [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**

If enabled, this event is reported by a host object when a dockable object (the client) is dragged over it. The event will only be reported if the name of the client object is included in the list of objects that the host object will accept, which is defined by its DockChildren property.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows :

|-----|-----------------|-----------------------|
|`[1]`|Object           |ref or character vector|
|`[2]`|Event            |`'DockMove'` or 481    |
|`[3]`|Client Object    |ref or character vector|
|`[4]`|Edge             |character vector       |
|`[5]`|y-position       |number                 |
|`[6]`|x-position       |number                 |
|`[7]`|Outline rectangle|(see below)            |

The 4<sup>th</sup> element of the event message Edge is a character vector that indicates along which edge of the host object the client object will be docked if the mouse button is released. It is either  `'Top'`, `'Bottom'`, `'Left'`, `'Right'` or `'None'`. The latter indicates that the object will not be docked. An object will dock only if the mouse pointer is inside, and sufficiently near to an edge of, the host.

The 5<sup>th</sup> and 6<sup>th</sup> elements of the event message report the position of the mouse pointer in the host object.

The 7<sup>th</sup> element of the event message is a 4-element nested vector containing the y-position, x-position, height and width of a rectangle. If Edge is `'None'`, this is the bounding rectangle of the client object. Otherwise, the rectangle describes a docking zone in the host that the client object will occupy when the mouse button is released.

If a callback function returns 0, the system displays the bounding rectangle and not a docking zone, and the docking operation is inhibited. You could use this mechanism to prohibit docking along one or more edges, whilst allowing it along others.

A callback function may modify the event message to cause a different sized docking zone to be displayed, or to force docking along a particular edge.

The DockMove event is generated repeatedly as the docking object is dragged.
