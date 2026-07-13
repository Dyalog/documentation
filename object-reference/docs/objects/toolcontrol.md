# <span>ToolControl</span> <span>Object</span>



[Parents](../parentlists/toolcontrol.md), [Children](../childlists/toolcontrol.md), [Properties](../proplists/toolcontrol.md), [Methods](../methodlists/toolcontrol.md), [Events](../eventlists/toolcontrol.md)



**Purpose:** The ToolControl object provides a standard Windows ToolBar.

**Description**


The ToolControl object provides an interface to the native Windows ToolBar control and supersedes the Dyalog APL [ToolBar](toolbar.md) object.



The tools on a ToolControl are normally represented by [ToolButton](toolbutton.md) objects, but the ToolControl may also act as a parent for other objects, including a [MenuBar](menubar.md) (see below).


Unlike the [ToolBar](toolbar.md), the ToolControl fully determines the positioning of its children automatically and this is governed by their order of creation. The Posn property of any child of a ToolControl is therefore read-only. Furthermore, the height of objects in a ToolControl may be no greater than that of a [ToolButton](toolbutton.md) in the same ToolControl. This in turn is governed by the sizes of the [FontObj](../properties/fontobj.md) and [ImageList](imagelist.md) in use in that ToolControl. ToolControl objects should be used in preference to [ToolBar](toolbar.md) objects.


If a ToolControl is the child of a [Form](form.md), its position and orientation is defined by its [Align](../properties/align.md) property. This property is ignored if the ToolControl is the child of a [CoolBand](coolband.md).


The overall appearance of the [ToolButton](toolbutton.md) objects displayed by the ToolControl is defined by the [Style](../properties/style.md) property of the ToolControl itself, rather than by individual [ToolButtons](toolbutton.md). This may be `'Buttons'`, `'FlatButtons'`, `'List'` or `'FlatList'`.
```apl
'F'⎕WC'Form' 'ToolControl: FlatButtons Style (default)'('Size' 10 40)
'F.TB'⎕WC'ToolControl'

'F.TB.IL'⎕WC'ImageList'('Masked' 0)
'F.TB.IL.'⎕WC'Bitmap'('Comctl32' 120)
'F.TB'⎕WS'ImageListObj' 'F.TB.IL'

'F.TB.B1'⎕WC'ToolButton' 'New'('ImageIndex' 7)
'F.TB.B2'⎕WC'ToolButton' 'Open'('ImageIndex' 8)
'F.TB.B3'⎕WC'ToolButton' 'Save'('ImageIndex' 9)
```


![](../img/tool1.gif)


![](../img/tool2.gif)
```apl
'F.TB'⎕WC'ToolControl'('Style' 'Buttons')
```


![](../img/tool3.gif)
```apl
'F.TB'⎕WC'ToolControl'('Style' 'FlatList')
```


![](../img/tool4.gif)
```apl
'F.TB'⎕WC'ToolControl'('Style' 'List')
```


The presence or absence of a recessed line drawn above, below, to the left of, or to the right of the ToolControl is controlled by the [Divider](../properties/divider.md) property whose default is 1 (show divider).


The [MultiLine](../properties/multiline.md) property specifies whether or not [ToolButtons](toolbutton.md) (and other controls) are arranged in several rows (or columns) when there are more than will otherwise fit. If [MultiLine](../properties/multiline.md) is 0 (the default), the ToolControl object clips its children and the user must resize it to bring more objects into view.
```apl
'F'⎕WC'Form' 'ToolControl: MultiLine 0'('Size' 20 36)
'F.TB'⎕WC'ToolControl'('Style' 'List')

'F.TB.IL'⎕WC'ImageList'('Masked' 0)('Size' 24 24)
'F.TB.IL.'⎕WC'Bitmap'('ComCtl32' 121)⍝ STD_LARGE
'F.TB'⎕WS'ImageListObj' 'F.TB.IL'

'F.TB.B1'⎕WC'ToolButton' 'Cut'('ImageIndex' 1)
'F.TB.B2'⎕WC'ToolButton' 'Copy'('ImageIndex' 2)
'F.TB.B3'⎕WC'ToolButton' 'Paste'('ImageIndex' 3)
'F.TB.B4'⎕WC'ToolButton' 'Undo'('ImageIndex' 4)
'F.TB.B5'⎕WC'ToolButton' 'Redo'('ImageIndex' 5)
'F.TB.B6'⎕WC'ToolButton' 'Delete'('ImageIndex' 6)
```


![](../img/tool6.gif)


![](../img/tool7.gif)
```apl
'F.TB'⎕WC'ToolControl'('MultiLine' 1)('Style' 'List')
```


The [Transparent](../properties/transparent.md) property specifies whether or not the ToolControl is transparent. If so, the visual effect is as if the [ToolButtons](toolbutton.md) (and other controls) were drawn directly on the parent Form as illustrated below:
```apl
'F'⎕WC'Form' 'ToolControl: Transparent 1)'('Size' 10 40)
'F.BM'⎕WC'Bitmap' 'C:\WINDOWS\WINLOGO'
'F'⎕WS'Picture' 'F.BM' 1

'F.TB'⎕WC'ToolControl'('Transparent' 1)('Style' 'FlatList')
'F.TB.IL'⎕WC'ImageList'('Masked' 0)('Size' 24 24)
'F.TB.IL.'⎕WC'Bitmap'('ComCtl32' 121)⍝ STD_LARGE
'F.TB'⎕WS'ImageListObj' 'F.TB.IL'

'F.TB.B1'⎕WC'ToolButton' 'New'('ImageIndex' 7)
'F.TB.B2'⎕WC'ToolButton' 'Open'('ImageIndex' 8)
'F.TB.B3'⎕WC'ToolButton' 'Save'('ImageIndex' 9)
```


![](../img/tool8.gif)


The [ShowCaptions](../properties/showcaptions.md) property specifies whether or not the captions of [ToolButton](toolbutton.md) objects are drawn. Its default value is 1 (draw captions). [ToolButtons](toolbutton.md) drawn without captions occupy much less space and [ShowCaptions](../properties/showcaptions.md) provides a quick way to turn captions on/off for user customisation.


The [ShowDropDown](../properties/showdropdown.md) property specifies whether or not a drop-down menu symbol is drawn alongside [ToolButtons](toolbutton.md) which have [Style ](../properties/style.md)`'DropDown'`. [ShowDropDown](../properties/showdropdown.md) also affects the behaviour of such [ToolButton](toolbutton.md) objects when clicked.


The [ButtonsAcceptFocus](../properties/buttonsacceptfocus.md) property determines how the ToolControl responds to the Tab and cursor movement keys.


As a special case, the ToolControl may contain a [MenuBar](menubar.md) as its **only** child. In this case, Dyalog APL causes the menu items to be drawn as buttons as shown below.


Although nothing is done to prevent it, the use of other objects in a ToolControl containing a [MenuBar](menubar.md), is not supported.
```apl
'F'⎕WC'Form' 'ToolControl with MenuBar'('Size' 20 40)
'F.TB'⎕WC'ToolControl'

:With 'F.TB.MB'⎕WC'MenuBar'
    :With 'File'⎕WC'Menu' 'File'
        'New'⎕WC'MenuItem' 'New'
        'Open'⎕WC'MenuItem' 'Open'
        'Close'⎕WC'MenuItem' 'Close'
    :EndWith

    :With 'Edit'⎕WC'Menu' 'Edit'
        'Cut'⎕WC'MenuItem' 'Cut'
        'Copy'⎕WC'MenuItem' 'Copy'
        'Paste'⎕WC'MenuItem' 'Paste'
    :EndWith

:EndWith
```


![](../img/tool10.gif)


