# <span>Clipboard</span> <span>Object</span>



[Parents](../parentlists/clipboard.md), [Children](../childlists/clipboard.md), [Properties](../proplists/clipboard.md), [Methods](../methodlists/clipboard.md), [Events](../eventlists/clipboard.md)



**Purpose:** This object provides access to the Windows clipboard.

**Description**


When an application places data in the Windows clipboard, it may store it in one or more formats. An application wishing to retrieve data from the clipboard can then choose which format to read it in. Dyalog APL supports standard clipboard formats, including CF_TEXT, CF_BITMAP and CF_METAFILE. If there is any data in the clipboard, the [Formats](../properties/formats.md) property lists the formats in which it may be retrieved.



In addition, the [Array](../properties/array.md) property may be used to set or retrieve clipboard contents in Dyalog APL array format.


Data is read from the clipboard using [`⎕WG`](../../../language-reference-guide/system-functions/wg), specifying the name of the appropriate property for the data that you want.


If the data has been stored in CF_Text format, the value of [Formats](../properties/formats.md) will include `'Text'` and you may retrieve the data by querying the value of the [Text](../properties/text.md) property with [`⎕WG`](../../../language-reference-guide/system-functions/wg).


If the data has been stored in **device-independent** bitmap format, the value of [Formats](../properties/formats.md) will include `'CBits'`, `'Bits'` and `'CMap'`. To retrieve the bitmap pattern and colour map, you may query the values of the [CBits](../properties/cbits.md), or [Bits](../properties/bits.md) and [CMap](../properties/cmap.md) properties using [`⎕WG`](../../../language-reference-guide/system-functions/wg).


If the data has been stored in **device-dependent** bitmap format, only the bitmap pattern is available and [Formats](../properties/formats.md) will contain `'Bits'` but not `'CMap'`. In this case you can query the [Bits](../properties/bits.md) property but not [CMap](../properties/cmap.md) without which you cannot realise the bitmap. However, if data was posted in this format, it is highly probable that the current Windows colour map applies to it. For a standard 16-colour device this is given under the description of the [CMap](../properties/cmap.md) property.



The following example retrieves text from the clipboard :
```apl
      'CL' ⎕WC 'Clipboard'
      Data ← 'CL' ⎕WG 'Text'
```




The next example retrieves a bitmap from the clipboard and defines it as a [Bitmap](bitmap.md) object named `'BM'` ready for use :
```apl
      'BM' ⎕WC 'Bitmap' '', 'CL' ⎕WG 'Bits' 'CMap'
```




Data may be placed in the clipboard using [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws). To store text, you simply set the [Text](../properties/text.md) property. You may use a simple character vector or matrix, or a vector of character vectors. For example :
```apl
      'CL' ⎕WS 'Text' 'Hello World'
```




To store a bitmap you can set either the [Picture](../properties/picture.md) property to the **name** of a [Bitmap](bitmap.md) object, or you can set the [Bits](../properties/bits.md) and [CMap](../properties/cmap.md) properties explicitly. The former is more efficient, especially for large bitmaps, for example :
```apl
      'CL' ⎕WS 'Bitmap' 'BM'
```


or
```apl
      Bits CMap ← 'BM' ⎕WG 'Bits' 'CMap'
      'CL' ⎕WS ('Bits' Bits)('CMap' CMap)
```



Note that if you use the latter method, you must set **both** properties in one [`⎕WS`](../../../language-reference-guide/system-functions/ws) statement. This is also true if you wish to store data in both Text and Bitmap formats together.


The [Metafile](../properties/metafileobj.md) property allows graphical information to be restored in and retrieved from the clipboard in Windows Metafile format. See the description of the [Metafile](../properties/metafileobj.md) property for details.


A [ClipChange](../methodorevents/clipchange.md) (120) event is generated when another application places data in the clipboard.


