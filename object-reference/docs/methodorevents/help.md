# <span>Help</span> <span>Event 400</span>

[**Applies To**](../methodoreventapplies/help.md)

**Description**


If enabled, this event is reported when the user clicks on an object which has a callback defined for this event, the user having previously clicked on the Question (?) button in the title bar of the parent Form.  The presence of the Question (?) button is determined by the value of the [HelpButton](../properties/helpbutton.md) property.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------------|-----------------------|
|`[1]`|Object      |ref or character vector|
|`[2]`|Event       |`'Help` or 400         |
|`[3]`|Y-coordinate|Number                 |
|`[4]`|X-coordinate|Number                 |


The y and x-coordinates refer to the position of the mouse pointer in the object which was clicked on, and are reported in the coordinate system of that object.



