# <span>AnimOpen</span> <span>Method 290</span>

**Description**

The AnimOpen method opens an AVI file in an Animation object.

The argument to AnimOpen is a 1 or 2-element array as follows:

|-----|-----------|----------------|
|`[1]`|File       |character vector|
|`[2]`|Resource id|integer         |

If a single element is specified, it represents the name of a .AVI file.

If 2 elements are specified, the first element specifies the name of a DLL or EXE and the second element identifies the particular AVI resource stored in that file. The identifier may be its name (a character string) or its resource id (a non-zero positive integer).

If the [AutoPlay](../properties/autoplay.md) property is set to 1, the animation will play immediately. Otherwise, only the first frame will be displayed.

Note that the Animation object can only play AVI files or resources that have no sound and can only display uncompressed AVI files or .AVI files that have been compressed using Run-Length Encoding (RLE). If you attempt to open an inappropriate AVI file, the operation will fail with a DOMAIN ERROR and the following message will be displayed in the Status Window:

*AVI file includes sound data or is in a format not supported by the Animation object*

**Application**

Objects: [Animation](../objects/animation.md)
