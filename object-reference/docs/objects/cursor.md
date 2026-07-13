# <span>Cursor</span> <span>Object</span>

[Parents](../parentlists/cursor.md), [Children](../childlists/cursor.md), [Properties](../proplists/cursor.md), [Methods](../methodlists/cursor.md), [Events](../eventlists/cursor.md)


**Purpose:** This object defines a cursor.

**Description**

The [File](../properties/file.md) property defines the name of a cursor file associated with the Cursor object, or it specifies the name of a DLL and the resource number or name of the cursor therein. If you omit the file extension, the system assumes .CUR. To use an animated cursor you must therefore specify the .AMI extension explicitly.

If the value of the [File](../properties/file.md) property is set by [`⎕WS`](../../../language-reference-guide/system-functions/ws), no immediate action is taken, but the corresponding file may subsequently be read or written using the [FileRead](../methodorevents/fileread.md) or [FileWrite](../methodorevents/filewrite.md) methods.

The [Bits](../properties/bits.md) and [Mask](../properties/mask.md) properties define the appearance of the cursor. Both are Boolean matrices with a shape of 32  32. The colour of each pixel in the cursor is defined by the following table. Note that a 0 in [Bits](../properties/bits.md) combined with a 1 in [Mask](../properties/mask.md) causes the corresponding pixel to be the colour of the background. This is used to give the cursor a non-rectangular shape.

|-----|-----|-----|----------|-------|
|Bits |0    |1    |0         |1      |
|Mask |0    |0    |1         |1      |
|Pixel|Black|White|Background|Inverse|

The [HotSpot](../properties/hotspot.md) property determines the point within the cursor that registers its position over another object.

A Cursor is **used** by setting the [CursorObj](../properties/cursorobj.md) property of another object to its name or ref.


