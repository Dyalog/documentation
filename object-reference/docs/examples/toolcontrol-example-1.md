---
search:
  exclude: true
---

# <span>ToolControl</span> <span>Example 1</span>

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
