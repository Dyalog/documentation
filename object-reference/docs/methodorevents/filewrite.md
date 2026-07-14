# <span>FileWrite</span> <span>Method 91</span>

**Applies To:** [Bitmap](../objects/bitmap.md), [Cursor](../objects/cursor.md), [Icon](../objects/icon.md), [Metafile](../objects/metafile.md), [RichEdit](../objects/richedit.md)

**Description**

This method causes the object to be written to the file named in its [File](../properties/file.md) property. For the Bitmap and Icon objects this method will write a file of type .BMP and .ICO to a file with the appropriate extension. If [File](../properties/file.md) specifies any other extension, the method will fail with a `DOMAIN ERROR`:
```apl
 DOMAIN ERROR: This object cannot be saved to this type of file.
```

The FileWrite method is niladic.

If you attach a callback function to this event and have it return a value of 0, the object will not be written to file. You could use this to avoid overwriting an existing file.
