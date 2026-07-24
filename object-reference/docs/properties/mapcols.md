# <span>MapCols</span> <span>Property</span>

**Description**

The MapCols property specifies whether or not the button colours in bitmaps and icons in an [ImageList](../objects/imagelist.md) are re-mapped to reflect the users colour preferences. If your bitmaps and icons represent buttons using the standard windows button colours, this property causes those colours to be changed to suit the user's own colour scheme.

MapCols is a single number with the value 0 (no colour mapping) or 1 (colours are automatically re-mapped. The default is 0.

If MapCols is 1, the following colour mappings are performed:

|Colour       |Description|Mapped to       |
|-------------|-----------|----------------|
|`0   0   0`  |Black      |Button Text     |
|`128 128 128`|Dark grey  |Button Shadow   |
|`191 191 191`|Light grey |Button Face     |
|`192 192 192`|Light grey |Button Face     |
|`255 255 255`|White      |Button Highlight|

**Application**

Objects: [ImageList](../objects/imagelist.md)
