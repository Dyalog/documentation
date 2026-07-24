# <span>Help</span> <span>Event 400</span>

**Description**

If enabled, this event is reported when the user clicks on an object which has a callback defined for this event, the user having previously clicked on the Question (?) button in the title bar of the parent Form.  The presence of the Question (?) button is determined by the value of the [HelpButton](../properties/helpbutton.md) property.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :

|-----|------------|-----------------------|
|`[1]`|Object      |ref or character vector|
|`[2]`|Event       |`'Help` or 400         |
|`[3]`|Y-coordinate|Number                 |
|`[4]`|X-coordinate|Number                 |

The y and x-coordinates refer to the position of the mouse pointer in the object which was clicked on, and are reported in the coordinate system of that object.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Image](../objects/image.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Poly](../objects/poly.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [Text](../objects/text.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
