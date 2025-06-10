---
search:
  exclude: true
---

<h1 class="heading"><span class="name">TabControl</span> <span class="right">Example 1</span></h1>



Note that the icons used in this example are provided in the `ws` sub-directory.
```apl
icodir←(2 ⎕NQ'.' 'GetEnvironment' 'Dyalog'),'\ws\'
```
```apl
'F'⎕WC'Form' 'TabControl: Default'('Size' 25 50)
'F.TC'⎕WC'TabControl'

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


![](../img/tab1.gif)





