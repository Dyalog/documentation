# <span>CMap</span> <span>Property</span>

**Description**

This property defines the table of colours (the colour map) used by a [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) object or by a bitmap stored in the Windows clipboard. Its value is a 3-column integer matrix of numbers in the range 0-255. Each row represents a separate colour which is indexed (0-origin) by values in the [Bits](bits.md) property. The 3 columns refer to the intensities of the red, green and blue components of colour respectively.

Please note that [Bits](bits.md) and CMap may **only** be used to represent an image with a colour palette of **256 colours or less**. If the colour palette is larger, the values of [Bits](bits.md) and CMap reported by `⎕WG` will be (0 0). For a high-colour image, use [CBits](cbits.md) instead.

When you create a [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) by specifying [Bits](bits.md) and CMap, the actual colours you obtain are not necessarily those that you specified. This is partly due to hardware restrictions and partly due to the way in which Windows manages colours. Firstly, your display adapter and driver limit the number of pure colours that can be displayed at any one time and therefore define a maximum size for the colour map. For example, on a **standard** VGA you are limited to 16 different pure colours (additional ones are provided by **dithering**).

Secondly, Windows reserves a certain number of colours in the colour map for its own use. When an application requests a new colour (that is, one that is not already installed in the colour map), MS-Windows either assigns it to a spare entry, or allocates the **closest match** if the colour map is full. The value of [Bits](bits.md) and CMap after [`⎕WC`](../../../language-reference-guide/system-functions/wc) reflect the actual colours allocated and may bear little resemblance to the values you assigned to these properties initially.

Note that if you are running 16 colours, MS-Windows reserves all 16 entries in the colour map for its own use. This means that on a 16-colour system, you **cannot** use any colours other than the default ones reserved by MS-Windows. In practice, the "standard" 16-colour CMap is shown in the following table.

Table: The default 16-colour CMap { #default-16-colour-cmap }

|Bits[]|CMap      |||Colour      |
|------|----|---|---|------------|
|1     |0   |0  |0  |Black       |
|2     |128 |0  |0  |Dark red    |
|3     |0   |128|0  |Dark Green  |
|4     |128 |128|0  |Olive Green |
|5     |0   |0  |128|Dark Blue   |
|6     |128 |0  |128|Dark Magenta|
|7     |0   |128|128|Dark Cyan   |
|8     |128 |128|128|Dark Grey   |
|9     |192 |192|192|Light Grey  |
|10    |255 |0  |0  |Red         |
|11    |0   |255|0  |Green       |
|12    |255 |255|0  |Yellow      |
|13    |0   |0  |255|Blue        |
|14    |255 |0  |255|Magenta     |
|15    |0   |255|255|Cyan        |
|16    |255 |255|255|White       |

If you are using a 256-colour set-up, the first 9 and the last 7 entries of the 256-colour CMap are the same as the first 9 and last 7 entries of the 16-colour CMap shown above. The intervening entries represent additional colours or are initially unused (0 0 0). New colours that you specify will be allocated to unused entries until the table is full.

**Application**

Objects: [Bitmap](../objects/bitmap.md), [Clipboard](../objects/clipboard.md), [Cursor](../objects/cursor.md), [Icon](../objects/icon.md)
