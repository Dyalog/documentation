# <span>ToolboxBitmap</span> <span>Property</span>

**Applies To:** [ActiveXControl](../objects/activexcontrol.md), [OCXClass](../objects/ocxclass.md)

**Description**

For an [ActiveXControl](../objects/activexcontrol.md), the ToolboxBitmap property is a character vector or ref that specifies the name of, or ref to, a [Bitmap](../objects/bitmap.md) object that may be used by a host application to represent the [ActiveXControl](../objects/activexcontrol.md) when its complete visual appearance is not required. For example, if you add an ActiveX control to the Microsoft Visual Basic development environment, its bitmap is added to the toolbox. The Bitmap should therefore be of an appropriate size, usually 24 x 24 pixels.

For an [OCXClass](../objects/ocxclass.md), The ToolboxBitmap is a read-only property that reports a bitmap image associated with an OLE Control. This is intended for use by a GUI design tool. Its value is a 2-element vector. The first element is an integer matrix of pixel colours corresponding to the Bits property of a Bitmap object. The second element is a 3-column integer matrix specifying the colour map and corresponds to the CMap property of a Bitmap object.

Thus you can construct a Bitmap object directly from this property with an expression such as:
```apl
      'BM'⎕WC'Bitmap' '','GAUGE' ⎕WG'ToolboxBitmap'
```

where `GAUGE` is the name of an [OCXClass](../objects/ocxclass.md).
