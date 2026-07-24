# <span>CustomColors</span> <span>Property</span>

**Description**

The CustomColors property is a 1-row, 16-column nested matrix which specifies the RGB values of the colours displayed in the *Custom colors* section of the Windows colour selection dialog box when displayed by a [ColorButton](../objects/colorbutton.md) object.

Each element of CustomColors is a 3-element integer vector specifying an RGB colour value.

By default, each element of CustomColors is (0 0 0). If the user selects a new custom colour from the Windows colour selection dialog box, its value will be reported by CustomColors. CustomColors must always have shape (1 16).

Note that CustomColors is maintained separately for each separate [ColorButton](../objects/colorbutton.md), and CustomColors defaults to `(1 16⍴⊂0 0 0)` for each new [ColorButton](../objects/colorbutton.md) that you create. If you want to maintain a global custom colour table for your application, you must do this yourself.

**Application**

Objects: [ColorButton](../objects/colorbutton.md)
