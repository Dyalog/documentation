# <span>ColorButton</span> <span>Object</span>

[Parents](../parentlists/colorbutton.md), [Properties](../proplists/colorbutton.md), [Methods](../methodlists/colorbutton.md), [Events](../eventlists/colorbutton.md)

**Purpose:** The ColorButton object allows the user to select a colour.

**Description**

The ColorButton object displays a coloured box, with an optional drop down button. When the user clicks the ColorButton with the left mouse button, a colour selection drop-down appears below it, allowing the user to select a new colour.

The [CurrentColor](../properties/currentcolor.md) property (default 0 0 0) is a 3-element integer vector that specifies and reports the RGB value of the currently selected colour.

The [DefaultColors](../properties/defaultcolors.md) property is a nested matrix which specifies the RGB values of the colours shown in the colour selection box. The shape of [DefaultColors](../properties/defaultcolors.md) determines the number of rows and columns in the colour selection drop-down. Each element of [DefaultColors](../properties/defaultcolors.md) is a 3-element integer vector specifying an RGB colour value.

The [OtherButton](../properties/otherbutton.md) property is Boolean and specifies whether or not the user can select a colour using the Windows colour selection dialog box.

If [OtherButton](../properties/otherbutton.md) is 1 (the default), the final row of the colour selection drop-down contains a button labelled "Other…". If the user clicks this button, the standard Windows colour selection dialog box is displayed, allowing the user to select any colour that the computer can render.

If [OtherButton](../properties/otherbutton.md) is 0, the button labelled "Other…" is not present and the user is restricted to the choice of colours provided by the [DefaultColors](../properties/defaultcolors.md) property.

The [CustomColors](../properties/customcolors.md) property is a 1-row, 16-column nested matrix which specifies the RGB values of the Colours displayed in the *Custom colors* section of the Windows colour selection dialog box. Each element of [CustomColors](../properties/customcolors.md) is a 3-element integer vector specifying an RGB colour value.

The [ShowDropDown](../properties/showdropdown.md) property is Boolean (default 1) and specifies whether or not a drop-down button is displayed in the ColorButton object.

When the user clicks a ColorButton with the left mouse button, the object generates a [DropDown](../methodorevents/dropdown.md) event just before it displays the colour selection drop-down. This event may be used to set the [DefaultColors](../properties/defaultcolors.md) and/or [CustomColors](../properties/customcolors.md) properties dynamically.

When the user selects a new colour, the ColorButton generates a [ColorChange](../methodorevents/colorchange.md) event.
