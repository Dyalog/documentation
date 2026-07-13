# <span>MouseWheel</span> <span>Event 8</span>

[**Applies To**](../methodoreventapplies/mousewheel.md)

**Description**

If enabled, this event is reported when the user rotates the mouse wheel.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 9-element vector as follows :

|-----|-----------|--------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                   |
|`[2]`|Event      |`'MouseWheel'` or 8                                                       |
|`[3]`|Y          |y-position of mouse (number)                                              |
|`[4]`|X          |x-position of mouse (number)                                              |
|`[5]`|Button     |button pressed<br/>1 = left button<br/>2 = right button<br/>4 = middle button         |
|`[6]`|Shift State|sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down|
|`[7]`|Delta      |integer                                                                   |
|`[8]`|Lines      |integer                                                                   |
|`[9]`|Wheel Delta|integer                                                                   |

The value of *Delta* indicates the distance that the wheel is rotated,§ expressed in multiples or divisions of *Wheel Delta*. A positive value indicates that the wheel was rotated forward, away from the user; a negative value indicates that the wheel was rotated backward, toward the user.

*Lines* specifies the number of lines to scroll when the wheel is rotated by I *Mouse Delta* unit. A value of `¯1` indicates that a whole screen is to be scrolled. These values are defined by the user's preferences (*Control Panel/Mouse*).
