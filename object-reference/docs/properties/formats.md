# <span>Formats</span> <span>Property</span>



**Applies To:** [Clipboard](../objects/clipboard.md)

**Description**


This is a "read-only" property that identifies the formats in which data is currently available in the clipboard. It is a vector of character vectors containing the names of the corresponding [Clipboard](../objects/clipboard.md) properties for which data may be obtained using [`⎕WG`](../../../language-reference-guide/system-functions/wg). In the following example data was copied to the Windows clipboard from Microsoft Excel. This product stores data in CF_Text and the older device-dependent CF_Bitmap formats. The latter excludes colour map information, so [CMap](cmap.md) is not available.
```apl
      'CL' ⎕WC 'Clipboard'
      'CL' ⎕WG 'Formats'
 Bits  CMap  Text
```



