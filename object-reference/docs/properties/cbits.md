# <span>CBits</span> <span>Property</span>



**Applies To:** [Bitmap](../objects/bitmap.md), [Clipboard](../objects/clipboard.md), [Icon](../objects/icon.md)

**Description**


The CBits property represents the pixels that make up a picture..


CBits provides an alternative representation to that provided by the [Bits](bits.md) and [CMap](cmap.md) properties which apply only to images with 256 colours or under. CBits may be used to represent both low-colour and high-colour images.


CBits is a rank-2 numeric array whose dimensions represent the rows and columns of pixels in the image. The values in CBits represent the colour of each pixel and (for an [Icon](../objects/icon.md)) its transparency.


For a [Bitmap](../objects/bitmap.md), the colour value of each pixel is obtained by encoding the red, green and blue components, that is:
```apl
      PIXEL←256⊥RED GREEN BLUE
```


where `RED`, `GREEN` and `BLUE` are numbers in the range 0-255.


