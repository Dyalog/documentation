---
search:
  exclude: true
---

# <span>ToolControl</span> <span>Example 3</span>

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
