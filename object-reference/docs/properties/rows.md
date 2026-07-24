# <span>Rows</span> <span>Property</span>

**Description**

For [Combo](../objects/combo.md) objects with [Style](style.md)`'Drop'` or `'DropEdit'` this property determines the number of rows displayed in the drop-down listbox when it is displayed. Note that the height of the edit field of a [Combo](../objects/combo.md) of this type is dependent only upon the size of the font in use, and cannot otherwise be changed.

Rows is a "read-only" property for a [Combo](../objects/combo.md) with [Style ](style.md)`'Simple'` and an attempt to set it in a [Combo](../objects/combo.md) of this type with [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws) will generate a `NONCE ERROR`. Instead, the overall height of a Simple [Combo](../objects/combo.md) is determined by the first element of the [Size](size.md) property.

**Application**

Objects: [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md)
