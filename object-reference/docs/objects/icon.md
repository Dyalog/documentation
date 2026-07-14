# <span>Icon</span> <span>Object</span>

[Parents](../parentlists/icon.md), [Children](../childlists/icon.md), [Properties](../proplists/icon.md), [Methods](../methodlists/icon.md), [Events](../eventlists/icon.md)

**Purpose:** This object defines an icon.

**Description**

The [File](../properties/file.md) property specifies the name of an icon  file (.ICO. .GIF or .PNG), or the name of a DLL or EXE file and the identity of the icon within it.

The Style property identifies the size of the icon and must be `'Large'` or `'Small'`. The former specifies a 32x32 icon and is the default; the latter specifies a 16x16 icon. The size of the icon is not embedded within the icon data, so it is **essential** to specify Style correctly. Note that a single file may contain both sizes of an icon. Style is only relevant when loading an Icon from file.

If the value of the [File](../properties/file.md) property is set by [`⎕WS`](../../../language-reference-guide/system-functions/ws), no immediate action is taken, but the corresponding file may subsequently be read or written using the [FileRead](../methodorevents/fileread.md) or [FileWrite](../methodorevents/filewrite.md) methods.

16-bit icons contain fewer than 256 colours and each pixel is either transparent or opaque. The images in such Icons are represented by the [Bits](../properties/bits.md), [Mask](../properties/mask.md) and [CMap](../properties/cmap.md) properties.

32-bit icons are 24-bit images with an 8-bit alpha channel which specifies the degree of transparency of each pixel. The pixels in these Icons are represented by the [CBits](../properties/cbits.md) property.

[CBits](../properties/cbits.md) is a rank-2 numeric array whose dimensions represent the rows and columns of pixels in the Icon. The values in [CBits](../properties/cbits.md) represent the colour and of each pixel and also its transparency.

[Bits](../properties/bits.md) is an integer matrix whose elements define the colours of each pixel in the icon in terms of their (0-origin) indices into [CMap](../properties/cmap.md). When the icon is displayed on the screen, the way in which these colours combine with those currently displayed on the screen (the background) is specified by [Mask](../properties/mask.md). This is a Boolean matrix of the same size as [Bits](../properties/bits.md). The following table shows how the colour of each resulting pixel is determined.

|-----|------|----------|----------|
|Bits |Colour|0         |Colour    |
|Mask |0     |1         |1         |
|Pixel|Colour|Background|New Colour|

If an element of [Mask](../properties/mask.md) is 0, the corresponding element of [Bits](../properties/bits.md) defines the colour of the resulting pixel that is displayed on the screen. If an element of [Mask](../properties/mask.md) is 1, the resulting pixel that is displayed on the screen is either the current background colour or is a new colour chosen by MS-Windows to be visible against the background. A non rectangular icon is obtained by setting those elements of [Bits](../properties/bits.md) and [Mask](../properties/mask.md) that you want to exclude from the shape to be 0 and 1 respectively.

The size of [Bits](../properties/bits.md) is restricted by the capabilities of the current display driver. [Mask](../properties/mask.md) must have the same shape as [Bits](../properties/bits.md).

An Icon is **used** by setting the [IconObj](../properties/iconobj.md) property or [Picture](../properties/picture.md) property of another object to its name or ref.
