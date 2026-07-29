# <span>CursorObj</span> <span>Property</span>

**Description**

This property is used to associate a particular cursor with an object.

Its
value is either a simple scalar number which specifies a standard Windows
cursor, or the name of, or ref to, a [Cursor](../objects/cursor.md) object. The standard Windows cursors are :

|---|-------------------------------------------------|
|0  |arrow (Windows default)                          |
|1  |hourglass                                        |
|2  |crosshair                                        |
|3  |I-Beam                                           |
|4  |crossing vertical/horizontal double-headed arrows|
|5  |diagonal double-headed arrows (left-to-right)    |
|6  |vertical double-headed arrows                    |
|7  |diagonal double-headed arrows (right-to-left)    |
|8  |horizontal double-headed arrows                  |
|9  |upward pointing arrow                            |
|10 |box                                              |
|11 |crossing vertical/horizontal double-headed arrows|
|12 |no-entry sign                                    |
|13 |arrow with hourglass                             |
|14 |pointing hand                                    |

If CursorObj is set to anything other than an empty vector (which is the
default) it defines the appearance of the cursor when the mouse pointer is moved
into the object. If CursorObj is an empty vector, the shape of the cursor
remains unchanged when the mouse pointer enters the object. In effect, the
cursor is "inherited" from its parent. Exceptions to this rule are
certain objects which have special cursors by default.

If the value of CursorObj for the [Root](../objects/root.md) object
is set to anything other than an empty vector, it applies to **all**[ Form](../objects/form.md)s
and their children, irrespective of their own CursorObj values. Therefore, if
you want to indicate that your application is "working" and is not
responsive to input, you can simply do:
```apl
      '.' ⎕WS 'CursorObj' 1 ⍝ Hourglass cursor
```

Then to reset the application you do:
```apl
      '.' ⎕WS 'CursorObj' ''
```

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [MDIClient](../objects/mdiclient.md), [Poly](../objects/poly.md), [ProgressBar](../objects/progressbar.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [Text](../objects/text.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
