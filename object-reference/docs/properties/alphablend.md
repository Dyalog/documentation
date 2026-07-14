# <span>AlphaBlend</span> <span>Property</span>

**Applies To:** [Form](../objects/form.md)

**Description**

The AlphaBlend property specifies a level of translucency which allows the
area behind a Form to show through.

AlphaBlend is a scalar integer value in the range 0 to 255.

A value of 255 (the default) specifies no translucency, and the Form is
entirely opaque obliterating anything behind it.

A value of 0 specifies total translucency and the Form itself is not visible.
Furthermore, mouse events over the Form will not be reported by the Form itself
but will be passed to any other windows underneath the Form.

Values in between specify varying levels of translucency.
