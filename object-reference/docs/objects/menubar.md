# <span>MenuBar</span> <span>Object</span>

**Purpose:** Specifies a horizontal menu bar displayed at the top of a [Form](form.md) .

**Description**

Unless it is made invisible the MenuBar is always available to the user to initiate actions or to select options. A MenuBar has a fixed position and size.

It is possible to have more than one MenuBar associated with the same [Form](form.md) or [SubForm](subform.md), but only one of them should be [Visible](../properties/visible.md) at any one time.

The following example illustrates how a menu structure can be built up from a MenuBar. For clarity, the example is indented, and the definition of the [Event](../properties/event.md) property is omitted.
```apl
      'F'           ⎕WC 'Form' 'Menu Example'
      'F.M'         ⎕WC 'MenuBar'
      'F.M.FILE'    ⎕WC 'Menu' '&File'
      'F.M.MAT'     ⎕WC 'Menu' '&Materials'
      'F.M.MAT.B'   ⎕WC 'MenuItem' '&Brick'
      'F.M.MAT.C'   ⎕WC 'MenuItem' '&Concrete'
      'F.M.MAT.S'   ⎕WC 'MenuItem' '&Stone'
      'F.M.MAT.SEP' ⎕WC 'Separator'
      'F.M.MAT.W'   ⎕WC 'Menu'     '&Wood'
      'F.M.MAT.W.O' ⎕WC 'MenuItem' '&Oak'
      'F.M.MAT.W.T' ⎕WC 'MenuItem' '&Teak'
      'F.M.MAT.W.M' ⎕WC 'MenuItem' '&Mahogany'
```

Note that putting a [Separator](separator.md) (either [Style](../properties/style.md)) in a MenuBar has the effect of breaking the bar vertically, that is, the next [Menu](menu.md) or [MenuItem](menuitem.md) you add will appear on the left-hand side on the line below.

The [EdgeStyle](../properties/edgestyle.md) property has no effect on the appearance of a MenuBar or of a direct child of a MenuBar. However, if you want the sub-menus to have a 3-dimensional appearance, you **must** set the [EdgeStyle](../properties/edgestyle.md) property of the MenuBar to something other than `'None'`.

If the MenuBar is owned by a [Form](form.md) that is the parent of an [MDIClient](mdiclient.md), you can set the [MDIMenu](../properties/mdimenu.md) property to the name of the [Menu](menu.md) you wish to nominate as the *window*  menu. This menu will automatically be updated with the [Caption](../properties/caption.md)s of the child [SubForm](subform.md) and may be used to select the currently active one.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

Children: [Bitmap](../objects/bitmap.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [Separator](../objects/separator.md), [Timer](../objects/timer.md)

Properties: [ChildList](../properties/childlist.md), [Data](../properties/data.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [KeepOnClose](../properties/keeponclose.md), [MDIMenu](../properties/mdimenu.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md)
