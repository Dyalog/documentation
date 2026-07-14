---
search:
  exclude: true
---

# <span>TabControl</span> <span>Example 6</span>

Note that the icons used in this example are provided in the `ws` sub-directory.
```apl
icodir←(2 ⎕NQ'.' 'GetEnvironment' 'Dyalog'),'\ws\'
```
```apl
'F'⎕WC'Form' 'TabControl: Align Right'('Size' 40 30)
'F.TC'⎕WC'TabControl'('Align' 'Right')

'F.TC.IL'⎕WC'ImageList'
'F.TC.IL.'⎕WC'Icon'(icodir,'aplicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'funicon.ico')
'F.TC.IL.'⎕WC'Icon'(icodir,'editicon.ico')

'F.TC'⎕WS'ImageListObj' 'F.TC.IL'

'F.TC.T1'⎕WC'TabButton' 'One'('ImageIndex' 1)
'F.TC.T2'⎕WC'TabButton' 'Two'('ImageIndex' 2)
'F.TC.T3'⎕WC'TabButton' 'Three'('ImageIndex' 3)

'F.TC.S1'⎕WC'SubForm'('TabObj' 'F.TC.T1')
'F.TC.S2'⎕WC'SubForm'('TabObj' 'F.TC.T2')
'F.TC.S3'⎕WC'SubForm'('TabObj' 'F.TC.T3')
```

![](../img/tab6.gif)
