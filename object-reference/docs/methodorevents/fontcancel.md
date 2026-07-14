# <span>FontCancel</span> <span>Event 242</span>

[**Applies To**](../methodoreventapplies/fontcancel.md)

**Description**

If enabled, this event is reported when the user has pressed the *Cancel* button or closed the font selection dialog box that is displayed by the ChooseFont method.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'FontCancel'` or 242  |
