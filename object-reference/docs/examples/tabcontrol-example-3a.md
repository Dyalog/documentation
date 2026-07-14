---
search:
  exclude: true
---

# <span>TabControl</span> <span>Example 3a</span>

Note that the icons used in this example are provided in the `ws` sub-directory.
```apl
icodir←(2 ⎕NQ'.' 'GetEnvironment' 'Dyalog'),'\ws\'
```
```apl
'F1'⎕WC'Form' 'TabControl: FlatButtons with FlatSeparators'('Size' 25 50)
'F1.TC'⎕WC'TabControl'('Style' 'FlatButtons')('FlatSeparators' 1)

'F1.TC.IL'⎕WC'ImageList'
'F.TC.IL.'⎕WC'Icon'(icodir,'aplicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'funicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'editicon.ico')
'F1.TC'⎕WS'ImageListObj' 'F1.TC.IL'

'F1.TC.T1'⎕WC'TabButton' 'One'('ImageIndex' 1)
'F1.TC.T2'⎕WC'TabButton' 'Two'('ImageIndex' 2)
'F1.TC.T3'⎕WC'TabButton' 'Three'('ImageIndex' 3)
```

![](../img/tab3a.gif)
