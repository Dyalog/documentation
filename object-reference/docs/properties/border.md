# <span>Border</span> <span>Property</span>

[**Applies To**](../propertyapplies/border.md)

**Description**

This property specifies whether or not an object is displayed with a border around it. It is a single number with the value 0 (no border)1 (Border), or 2. The value 2 applies only to a [Form](../objects/form.md) and is used in combination with `('EdgeStyle' 'Dialog')` to obtain standard dialog box appearance

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), the value of the Border property is only relevant if [Sizeable](sizeable.md), [Moveable](moveable.md), [SysMenu](sysmenu.md), [MaxButton](maxbutton.md) and [MinButton](minbutton.md) are **all** 0.

## Note

The value of the Border property may only be assigned by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and may **not** be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws).
