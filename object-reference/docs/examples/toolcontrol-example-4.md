---
search:
  exclude: true
---

# <span>ToolControl</span> <span>Example 4</span>


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


