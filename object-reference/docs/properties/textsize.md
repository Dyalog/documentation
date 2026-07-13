# <span>TextSize</span> <span>Property</span>

[**Applies To**](../propertyapplies/textsize.md)

**Description**


This property has been replaced by the [GetTextSize](../methodorevents/gettextsize.md) method, which should be used instead. TextSize is retained only for compatibility with previous versions of Dyalog.


TextSize is a "read-only" property that reports the size of the bounding rectangle of a text item in a given font. The result is given in the co-ordinate system of the object in question. This property is useful for positioning [Text](../objects/text.md) objects.


When you query TextSize you give the text item in whose size you are interested and, optionally, the name of a [Font](../objects/font.md) object. The text item may be a simple scalar, a vector or a matrix. If the [Font](../objects/font.md) is omitted, the result is given using the current font for the object in question. When you query TextSize on its own, you must enclose the argument to [`⎕WG`](../../../language-reference-guide/system-functions/wg). This is because APL would otherwise not be able to distinguish between the text string and font name associated with `'TextSize'` and other properties with the same name as these items.

<h2 class="example">Examples</h2>
```apl
      '.' ⎕WG ⊂'TextSize' 'Hello World'
2.666666746 9.625

      'FNT1' ⎕WC 'FontObj' 'Arial' 72
      '.' ⎕WG ⊂'TextSize' 'Hello World' 'FNT1'
12 41.875

      '.' ⎕WS 'Coord' 'Pixel'
      '.' ⎕WG ('TextSize' (3 11⍴'Hello World')) 'Coord'
39 55  Pixel
```



