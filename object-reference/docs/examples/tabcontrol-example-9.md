---
search:
  exclude: true
---

# <span>TabControl</span> <span>Example 9</span>

Note that the icons used in this example are provided in the `ws` sub-directory.
```apl
icodir←(2 ⎕NQ'.' 'GetEnvironment' 'Dyalog'),'\ws\'
```
```apl
'F'⎕WC'Form' 'TabControl: MultiLine Buttons'('Size' 25 40)
'F.TC'⎕WC'TabControl'('Style' 'Buttons')( 'MultiLine' 1))

'F.TC.IL'⎕WC'ImageList'
'F.TC.IL.'⎕WC'Icon'(icodir,'aplicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'funicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'editicon.ico')
'F.TC'⎕WS'ImageListObj' 'F.TC.IL'

'F.TC.T1'⎕WC'TabButton' 'First Tab'('ImageIndex' 1)
'F.TC.T2'⎕WC'TabButton' 'Second Tab'('ImageIndex' 2)
'F.TC.T3'⎕WC'TabButton' 'Third Tab'('ImageIndex' 3)
'F.TC.T4'⎕WC'TabButton' 'Fourth Tab'('ImageIndex' 1)
```

![](../img/tab9.gif)
