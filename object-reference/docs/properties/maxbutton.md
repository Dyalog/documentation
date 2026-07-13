# <span>MaxButton</span> <span>Property</span>

**Applies To:** [Form](../objects/form.md), [HTMLRenderer](../objects/htmlrenderer.md), [SubForm](../objects/subform.md)

**Description**

This property determines whether or not an object has a "maximise" button. Pressing this button will cause a [Form](../objects/form.md) or [HTMLRenderer](../objects/htmlrenderer.md) to be resized to occupy the entire screen, or a [SubForm](../objects/subform.md) to occupy the entire area of its parent. Pressing it again will restore the object to its original size. MaxButton is a single number with the value 0 (no maximise button) or 1 (maximise button is provided). The default is 1.

Note that MaxButton is independent of [Sizeable](sizeable.md), that is, you can define an object that can be maximised but not resized. If any of the properties MaxButton, [MinButton](minbutton.md), [SysMenu](sysmenu.md) and [Sizeable](sizeable.md) are set to 1, the object will have a title bar.
