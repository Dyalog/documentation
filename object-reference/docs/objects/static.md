# <span>Static</span> <span>Object</span>

[Parents](../parentlists/static.md), [Children](../childlists/static.md), [Properties](../proplists/static.md), [Methods](../methodlists/static.md), [Events](../eventlists/static.md)

**Purpose:** This object is primarily used to display graphics in a sub-window.

**Description**

The overall appearance of an empty Static object is controlled by the value of its [Style](../properties/style.md) property which may be one of the following character vectors:

|----------------------------|------------------------|
|`'BlackFrame'`              |`'BlackBox'`            |
|`'GreyFrame' or 'GrayFrame'`|`'GreyBox' or 'GrayBox'`|
|`'WhiteFrame'`              |`'WhiteBox'`            |

Note that the colours implied by the [Style](../properties/style.md) are not "hard-coded" but are actually defined by the current Windows colour scheme as follows:

|---------|------------------------|
|Black    |Window Border Colour    |
|Grey/Gray|Desktop Colour          |
|White    |Window Background Colour|

If the background colour of the [Form](form.md) is also set to the Window Background Colour, it follows that the [Style](../properties/style.md)s `'WhiteFrame'` and `'WhiteBox'` make the Static itself invisible (against the background), although the **contents** of the Static will show. This makes the Static appear like an invisible clipping window.
