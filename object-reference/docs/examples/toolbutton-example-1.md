---
search:
  exclude: true
---

# <span>ToolButton</span> <span>Example 1</span>


```apl
'F'⎕WC'Form' 'ToolControl: Dropdown Buttons'('Size' 20 40)
'F.TB'⎕WC'ToolControl'('ShowDropDown' 1)

:With 'F.FMENU'⎕WC'Menu' ⍝ Popup File menu
    'NEW'⎕WC'MenuItem' '&New'
    'OPEN'⎕WC'MenuItem' '&Open'
    'CLOSE'⎕WC'MenuItem' '&Close'
:EndWith

:With 'F.EMENU'⎕WC'Menu' ⍝ Popup File menu
    'CUT'⎕WC'MenuItem' 'Cu&t'
    'COPY'⎕WC'MenuItem' '&Copy'
    'PASTE'⎕WC'MenuItem' '&Paste'
:EndWith

'F.TB.B1'⎕WC'ToolButton' 'File'('Style' 'DropDown')('Popup' 'F.FMENU')
'F.TB.B2'⎕WC'ToolButton' 'Edit'('Style' 'DropDown')('Popup' 'F.EMENU')
```


![](../img/tool9.gif)


