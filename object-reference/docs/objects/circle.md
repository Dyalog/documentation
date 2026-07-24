# <span>Circle</span> <span>Object</span>

**Purpose:** A Graphical object to draw circles, arcs, and pie-slices.

**Description**

The [Points](../properties/points.md) property contains the co-ordinates of the centre of the circle. The size of the circle is determined by the [Radius](../properties/radius.md) property. This specifies the radius along the x-axis, the height is calculated so that the object is circular.

The [ RadiusMode](../properties/radiusmode.md) property determines whether or not the circle is adjusted by a pixel, if required in order to appear perfectly
round and perfectly centred. The default value is 0 (no adjustment is made).

The [Start](../properties/start.md) and/or [End](../properties/end.md) properties are used to draw partial circles. They specify start and end angles respectively, measuring from the x-axis in a counter-clockwise direction and are expressed in radians. The type of arc is controlled by [ArcMode](../properties/arcmode.md) as follows :

## ArcMode Effect

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0  |An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) .                                                                                                           |
|1  |An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) . In addition, a single straight line is drawn from one end of the arc to the other, resulting in a segment.|
|2  |An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) . In addition, two lines are drawn from each end of the arc to the centre, resulting in a pie-slice         |

.

[Points](../properties/points.md), [Radius](../properties/radius.md), [Start](../properties/start.md) and [End](../properties/end.md) can specify vectors so that several arcs, circles, pie slices, etc. can be drawn in one call (and with one name).

If [Start](../properties/start.md) is specified, but not [End](../properties/end.md), end angles default to `(¯1↓+\Start),○2`. If [End](../properties/end.md) is specified, but not [Start](../properties/start.md), start angles default to `0,¯1↓+\End`

This means that you can draw a pie-chart using either [Start](../properties/start.md) or [End](../properties/end.md) angles; you do not have to specify both.

<h2 class="example">Examples</h2>

A circle whose centre is (50,50) and radius 20
```apl
      'g.p1' ⎕WC 'Circle' (50 50) 20
```

An arc
```apl
      'g.arc' ⎕WC 'Circle' (50 50) 20 ('Start' (○0.75))('End' (○1.25))
```

Complete pie
```apl
      Data←12 27 21 40
      ANGLES←0,¯1↓((○2)÷+/Data)×+\Data
      COLS←(255 0 0)(0 255 0)(255 255 0)(0 0 255)
      PATS←1 2 3 4
      'g.pie' ⎕WC 'Circle' (50 50) 20 ('Start' ANGLES)
                  ('ArcMode' 2) ('FCol' (⊂0 0 0))
                  ('FStyle' PATS) ('FillCol' COLS)
```

Same pie as above, but 2nd slice is exploded by changing its centre and 4th slice is shrunk by reducing its radius :
```apl
      CY←50 52 50 50  ⍝ y-coord of centres
      R←20 20 20 17.5 ⍝ radii
      'g.pie' ⎕WC 'Circle' (50 CY) R ('Start' ANGLES)
                  ('ArcMode' 1) ('FCol' (⊂0 0 0))
                  ('FStyle' PATS) ('FillCol' COLS)
```

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [Metafile](../objects/metafile.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Children: [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [ArcMode](../properties/arcmode.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [DrawMode](../properties/drawmode.md), [End](../properties/end.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FillCol](../properties/fillcol.md), [FStyle](../properties/fstyle.md), [KeepOnClose](../properties/keeponclose.md), [LStyle](../properties/lstyle.md), [LWidth](../properties/lwidth.md), [MethodList](../properties/methodlist.md), [OnTop](../properties/ontop.md), [Points](../properties/points.md), [PropList](../properties/proplist.md), [Radius](../properties/radius.md), [RadiusMode](../properties/radiusmode.md), [Start](../properties/start.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [Help](../methodorevents/help.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [Select](../methodorevents/select.md)
