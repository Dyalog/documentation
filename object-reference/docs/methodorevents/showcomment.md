# <span>ShowComment</span> <span>Event 223</span>

**Description**

If enabled, a [Grid](../objects/grid.md) will generate a ShowComment event when the user rests the mouse pointer over a commented cell. You may use this event to modify the appearance of the comment dynamically.

The event message reported as the result of `⎕DQ` or supplied as the right argument to your callback function is an 8-element vector containing the following:

|-----|------------------|-----------------------|
|`[1]`|Object            |ref or character vector|
|`[2]`|Event             |`'ShowComment'` or 223 |
|`[3]`|Cell row          |integer                |
|`[4]`|Cell column       |integer                |
|`[5]`|Comment text      |character vector       |
|`[6]`|Window height     |integer, pixels        |
|`[7]`|Window width      |integer, pixels        |
|`[8]`|Tip behaviour flag|(1 = yes; 0 = no)      |

A callback function may modify the standard behaviour. You may prevent the comment from being displayed by returning 0 as the result of the callback. Alternatively, you may modify the comment text, its window size, or its pop-up behaviour by changing the appropriate element(s) of the event message and returning the new event message as the result.

Note that if the comment window relates to a row or column *title*, the value reported in element [3] or [4] of the event message is `¯1`.

You may display the comment associated with a particular cell under program control by calling ShowComment as a method. In this case, only the *Cell row* and *Cell column* parameters need be specified. If however, you wish to override the comment text and/or its window size, you may do so (temporarily) by specifying the corresponding parameters. By default, a comment displayed under program control does not exhibit tip behaviour but remains visible until it is explicitly removed using the HideComment method.

Note that a comment will only be displayed if the specified cell is marked as a commented cell.

**Application**

Objects: [Grid](../objects/grid.md)
