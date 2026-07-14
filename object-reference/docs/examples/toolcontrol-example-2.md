---
search:
  exclude: true
---

# <span>ToolControl</span> <span>Example 2</span>

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
