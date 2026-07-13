---
search:
  exclude: true
---

# <span>CoolBar</span> <span>Example 2</span>


```apl
'F'⎕WC'Form' 'CoolBar Object with simple controls'('Size' 25 40)
'F'⎕WS'Coord' 'Pixel'

'F.CB'⎕WC'CoolBar'

:With 'F.CB.C1'⎕WC'CoolBand'
    'E1'⎕WC'Edit' 'Edit1'
:EndWith

:With 'F.CB.C2'⎕WC'CoolBand'
    'C1'⎕WC'Combo'('One' 'Two' 'Three')('SelItems' 0 1 0)
:EndWith

:With 'F.CB.C3'⎕WC'CoolBand'
    'E2'⎕WC'Edit'(3 5⍴'Edit2')('Style' 'Multi')
:EndWith
```


![](../img/cool2.gif)


