# <span>Thumb</span> <span>Property</span>

**Description**

This property determines and reports the position of the *thumb* in an object.

For a [Scroll](../objects/scroll.md) object, the value of Thumb is a single integer whose minimum value is 1 and whose maximum value is defined by the [Range](range.md) property.

For [ProgressBar](../objects/progressbar.md), [Spinner](../objects/spinner.md), [UpDown](../objects/updown.md) and [TrackBar](../objects/trackbar.md) objects, Thumb is a single numeric value in the range specified by the [Limits](limits.md) property.

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md) object, Thumb is a 2-element vector whose elements refer to the position of the thumb in the object's own built-in vertical and horizontal scrollbars respectively.

For other objects, Thumb is a single numeric value in the range defined by the Limits property.

**Application**

Objects: [Form](../objects/form.md), [ProgressBar](../objects/progressbar.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [SubForm](../objects/subform.md), [TrackBar](../objects/trackbar.md), [UpDown](../objects/updown.md)
