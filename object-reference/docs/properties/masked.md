# <span>Masked</span> <span>Property</span>

**Applies To:** [ImageList](../objects/imagelist.md)

**Description**

The Masked property specifies whether or not the [ImageList](../objects/imagelist.md) will contain opaque or transparent images. It may be 0, 1(the default), 2, or 3.

Masked must be established when the [ImageList](../objects/imagelist.md) is created by `⎕WC` and may not subsequently be altered. An inappropriate value of Masked will cause the images to be drawn incorrectly.

If Masked is 0, the [ImageList](../objects/imagelist.md) expects opaque [Bitmap](../objects/bitmap.md) objects.

If Masked is 1, the [ImageList](../objects/imagelist.md) expects low-colour (4-bit or 8-bit) [Icon](../objects/icon.md) objects whose transparency is defined by their [Mask](mask.md) property.

If Masked is 2,  the [ImageList](../objects/imagelist.md) expects [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) objects whose alpha channel (the degree of transparency of each pixel) is encoded in its source file along with the colours.

If Masked is 3 and [Native Look and Feel ](../miscellaneous/windows-xp-look-and-feel.md)

 is enabled, the behaviour is the same as if Masked were 2. If Native Look and Feel is not enabled, it behaves as if Masked were 1. This setting provides the greatest degree of portability for applications whose users may or may not have Native Look and Feel enabled. This value is used for the ImageLists on the Dyalog Session CoolBars.
