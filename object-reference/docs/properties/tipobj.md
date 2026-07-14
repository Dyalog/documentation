# <span>TipObj</span> <span>Property</span>

[**Applies To**](../propertyapplies/tipobj.md)

**Description**

The TipObj property is a character vector or ref that specifies the name of, or ref to, a [TipField](../objects/tipfield.md) object in which the "help" message defined by the [Tip](tip.md) property is to be displayed. This message is displayed when the user positions the mouse pointer over the object.

Note that if TipObj is empty, its value is inherited from its parent. Thus setting TipObj on a [Form](../objects/form.md) defines the default [TipField](../objects/tipfield.md) (and thus the default appearance of all [Tip](tip.md)s) for all the controls in that [Form](../objects/form.md). Setting TipObj on [Root](../objects/root.md) defines the default [TipField](../objects/tipfield.md) for the entire application.
