# <span>OnTop</span> <span>Property</span>

[**Applies To**](../propertyapplies/ontop.md)

**Description**


This property may be used to cause a [Form](../objects/form.md) or [SubForm](../objects/subform.md) to be displayed on top of all other windows, even those owned by other applications.


Normally, [Form](../objects/form.md)s are brought to the front when they receive the input focus. [Form](../objects/form.md)s that do not have the input focus may be partially obscured by the one that does. If OnTop is set to 1, the [Form](../objects/form.md) or [SubForm](../objects/subform.md) remains at the front even if it doesn't have the input focus. Indeed, it may partially obscure the [Form](../objects/form.md) that does have the focus. The default value is 0 (normal).


More than one [Form](../objects/form.md) may have OnTop set to 1. If so, these [Form](../objects/form.md)s appear on top of all others, but may overlap one another. Other applications may also have windows with this property.


For a graphical object, the OnTop property controls how it is drawn in a [Grid](../objects/grid.md) relative to the grid lines and cell text. OnTop is applicable only if the graphic is the child of a [Grid](../objects/grid.md) and is otherwise ignored.


|---|-------------------------------------------------------------------|
|0  |Graphical object is drawn behind grid lines and cell text          |
|1  |Graphical object is drawn on top of grid lines but behind cell text|
|2  |Graphical object is drawn on top of grid lines and cell text       |



