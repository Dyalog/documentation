# <span>Step</span> <span>Property</span>

[**Applies To**](../propertyapplies/step.md)

**Description**

This property determines the size of changes reported when the user clicks a scroll arrow (small change) or clicks on the body of the scrollbar (large change). The object's [Thumb](thumb.md) property increases or decreases by this amount.

For a [Scroll](../objects/scroll.md) object, Step is a 2-element numeric vector whose first element specifies the value of the "small change" and whose second element specifies the value of the "large change".

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), Step is a 4-element numeric vector. The first two elements refer to the [Form](../objects/form.md)'s vertical scrollbar and the second two elements refer to the [Form](../objects/form.md)'s horizontal scrollbar.

For the above objects, values of Step must be between 1 and the value of the [Range](range.md) property.

For a [Locator](../objects/locator.md) object, Step is a 2-element integer vector (default value 1 1) that specifies the increments (in pixels) by which the size or position of the [Locator](../objects/locator.md) changes in the Y and X directions respectively as the user moves the [Locator](../objects/locator.md).
