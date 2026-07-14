# <span>MenuItem</span> <span>Object</span>

[Parents](../parentlists/menuitem.md), [Children](../childlists/menuitem.md), [Properties](../proplists/menuitem.md), [Methods](../methodlists/menuitem.md), [Events](../eventlists/menuitem.md)

**Purpose:** This object allows the user to initiate an action or to select an option from a menu.

**Description**

The [Caption](../properties/caption.md) property determines the text string that is displayed in its parent as the menu option. The size of a MenuItem is determined by the size of its [Caption](../properties/caption.md), or by the size of the largest object ([Menu](menu.md), MenuItem or [Separator](separator.md)) with the same parent. The position of the MenuItem is normally determined by the order in which it is created in relation to other objects with the same parent. However, you can use the [Posn](../properties/posn.md) property to **insert** a new MenuItem into an existing structure. For example, having defined three MenuItem objects as children of a [Menu](menu.md), you can insert a fourth one between the first and the second by specifying its [Posn](../properties/posn.md) to be 2. Note that the value of [Posn](../properties/posn.md) for the MenuItems that were previously second and third will then be reset to 3 and 4 respectively.

The [Style](../properties/style.md) property may be `'Check'` (the default) or `'Radio'`. [Style](../properties/style.md) determines the type of graphic displayed alongside the Caption if the MenuItem is *checked*.

The [Checked](../properties/checked.md) property is a single number with the value 0 or 1. 0 means not checked (the default), 1 means checked and a tick mark or radio dot is placed alongside its [Caption](../properties/caption.md). This property is frequently used to indicate which of a choice of options is currently set.

If a MenuItem is a child of a [MenuBar](menubar.md) which is itself a child of a [Form](form.md) or [SubForm](subform.md), the Align property can be set to `'Right'`. This is used to position a single MenuItem (or [Menu](menu.md)) at the rightmost end of a [MenuBar](menubar.md). This does not apply if the [MenuBar](menubar.md) is owned by a [ToolControl](toolcontrol.md).

If you set the [EdgeStyle](../properties/edgestyle.md) property to `'Plinth'`, the MenuItem will take on an appearance that is similar to a pushbutton and be raised when not selected and recessed when selected. Note that to enable 3-dimensional appearance, you must set [EdgeStyle](../properties/edgestyle.md) to something other than `'None'` for all the objects above the MenuItem in the tree.

The [BtnPix](../properties/btnpix.md) property is used to display a picture in a MenuItem. [BtnPix](../properties/btnpix.md) specifies the names of, or refs to, three [Bitmap](bitmap.md) objects. The first [Bitmap](bitmap.md) is displayed when the MenuItem does not have the focus (normal), the second when it does have the focus (highlighted). The third [Bitmap](bitmap.md) is displayed when the MenuItem is made inactive ([Active](../properties/active.md) property is 0). If [Caption](../properties/caption.md) is also defined, it is displayed **on top of** the bitmaps.

Alternatively, you may display an image alongside the [Caption](../properties/caption.md) using the [ImageIndex](../properties/imageindex.md) property. This selects a picture from the [ImageList](imagelist.md) associated with the [ImageListObj](../properties/imagelistobj.md) property of the parent [Menu](menu.md).

[EdgeStyle](../properties/edgestyle.md), [BtnPix](../properties/btnpix.md), [FontObj](../properties/fontobj.md), [FCol](../properties/fcol.md) and [BCol](../properties/bcol.md) are not effective if the MenuItem is the direct child of a [MenuBar](menubar.md).

A MenuItem generates a [Select](../methodorevents/select.md) event (if enabled) when the user chooses it.
