# <span>MinButton</span> <span>Property</span>

This property determines whether or not an object has a "minimise" button. Pressing this button will cause the object to be iconified. Pressing it again will restore the object to its original size. MinButton is a single number with the value 0 (no minimise button) or 1 (minimise button is provided). The default is 1.

MinButton is independent of [Sizeable](sizeable.md), that is, you can define an object that can be minimised but not resized.

If any of the properties MinButton, [MaxButton](maxbutton.md), [SysMenu](sysmenu.md), and [Moveable](moveable.md) are set to 1, the object will have a title bar.

If either MinButton or [MaxButton](maxbutton.md) is `1`, then [HelpButton](helpbutton.md) is always hidden, irrespective of its value. This is a Microsoft Windows limitation.

## Application

Objects: [Form](../objects/form.md), [HTMLRenderer](../objects/htmlrenderer.md), [SubForm](../objects/subform.md)
