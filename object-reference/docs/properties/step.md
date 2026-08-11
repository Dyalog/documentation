# <span>Step</span> <span>Property</span>

**Description**

This property determines the size of changes reported when the user clicks a scroll arrow (small change) or clicks on the body of the scrollbar (large change). The object's [Thumb](thumb.md) property increases or decreases by this amount.

For a [Scroll](../objects/scroll.md) object, Step is a 2-element numeric vector whose first element specifies the value of the "small change" and whose second element specifies the value of the "large change".

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), Step is a 4-element numeric vector. The first two elements refer to the [Form](../objects/form.md)'s vertical scrollbar and the second two elements refer to the [Form](../objects/form.md)'s horizontal scrollbar.

For the above objects, values of Step must be between 1 and the value of the [Range](range.md) property.

For a [Locator](../objects/locator.md) object, Step is a 2-element integer vector (default value 1 1) that specifies the increments (in pixels) by which the size or position of the [Locator](../objects/locator.md) changes in the Y and X directions respectively as the user moves the [Locator](../objects/locator.md).

For an [UpDown](../objects/updown.md) or [Spinner](../objects/spinner.md) object, Step specifies the amount by which the value changes each time the user clicks one of the arrows.

For a [TrackBar](../objects/trackbar.md) object, Step is a 2-element integer vector defining the small and large increments by which the [Thumb](thumb.md) moves. A small step is obtained by pressing a cursor movement key; a large step is obtained by clicking either side of the thumb or by pressing Page Up or Page Down.

For a [ProgressBar](../objects/progressbar.md) object, Step specifies the amount by which the [Thumb](thumb.md) is advanced each time the [ProgressStep](../methodorevents/progressstep.md) method is called.

**Application**

Objects: [Form](../objects/form.md), [Locator](../objects/locator.md), [ProgressBar](../objects/progressbar.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [SubForm](../objects/subform.md), [TrackBar](../objects/trackbar.md), [UpDown](../objects/updown.md)
