# <span>PName</span> <span>Property</span>

**Description**

This property is a character vector that specifies the face name for a [Font](../objects/font.md) object, or the printing device associated with a [Printer](../objects/printer.md). It is case-independent.

For a [Printer](../objects/printer.md), PName contains the description of the printer followed by a comma (,) and then the device to which it is attached.

<h2 class="example">Example</h2>
```apl
      'PR1' ⎕WC 'Printer'
      'PR1' ⎕WG 'PName'
HP Universal Printing PS,hp4200
```

**Application**

Objects: [Font](../objects/font.md), [Printer](../objects/printer.md)
