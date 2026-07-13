# <span>FileRead</span> <span>Method 90</span>



**Applies To:** [Bitmap](../objects/bitmap.md), [Cursor](../objects/cursor.md), [Icon](../objects/icon.md), [Metafile](../objects/metafile.md), [RichEdit](../objects/richedit.md)

**Description**


This method causes the object to be recreated from the file named in its [File](../properties/file.md) property.


The FileRead method is niladic.


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'FileRead'` or 90     |


If you attach a callback function to this event and have it return a value of 0, the object will not be recreated from file.



