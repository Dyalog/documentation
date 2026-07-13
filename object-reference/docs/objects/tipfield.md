# <span>TipField</span> <span>Object</span>



[Parents](../parentlists/tipfield.md), [Children](../childlists/tipfield.md), [Properties](../proplists/tipfield.md), [Methods](../methodlists/tipfield.md), [Events](../eventlists/tipfield.md)



**Purpose:** To display pop-up help.

**Description**


The TipField is used to display pop-up help when the user moves the mouse pointer over an object.



Most of the GUI objects supported by Dyalog APL/W have a [Tip](../properties/tip.md) and a [TipObj](../properties/tipobj.md) property. [TipObj](../properties/tipobj.md) specifies the name of, or ref to, a TipField object, and [Tip](../properties/tip.md) specifies a "help" message. The TipField automatically pops-up to display the [Tip](../properties/tip.md) when the user moves the mouse pointer over the object. It disappears when the user moves the mouse pointer away.


The TipField is a simple box with a 1-pixel black border in which the text specified by [Tip](../properties/tip.md) is displayed. [FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FontObj](../properties/fontobj.md) can be used to customise the appearance of the text within the box. [FCol](../properties/fcol.md) specifies the colour of the text; [BCol](../properties/bcol.md) specifies the background colour with which the box is filled. The default is black on yellow.


If you wish to display [Tip](../properties/tip.md)s for particular objects in different fonts and colours, you must create a separate TipField for each combination of colour and font you need.


