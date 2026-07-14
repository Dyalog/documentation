# <span>Note</span> <span>Property</span>

**Applies To:** [Button](../objects/button.md)

**Description**

The Note property applies only to a [Button](../objects/button.md) whose Style is `'CommandLink'`.

It is a character vector (by default empty) that specifies text to be displayed below the [Caption](caption.md).

<h2 class="example">Example</h2>
```apl
'F'⎕WC'Form' 'CommandLink Button'
'F.clb'⎕WC'Button' 'Visit Us'('Style' 'CommandLink')  
F.clb.Size←80 200
F.clb.Note←'www.dyalog.com'
 
```

![](../img/commandlink-button2.png)
