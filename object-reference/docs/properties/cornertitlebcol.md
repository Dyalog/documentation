# <span>CornerTitleBCol</span> <span>Property</span>

**Description**

This property specifies the colour used to fill  the area in the left corner  a [Grid](../objects/grid.md) . This is the rectangle above the row titles and to the left of the column titles.

CornerTitleBCol may be a 3-element vector of integer values  in the range 0-255 which refer to the red, green and blue components of the colour respectively, or it may be a scalar that defines a standard Windows colour element (see [BCol](bcol.md) for details). Its default value is 0 which means that the colour derives from your current Windows colour scheme.

<h2 class="example">Example</h2>
```apl
      f.g.CornerTitleBCol←⊂255 0 0
```

![](../img/cornertitlebcol.png)

**Application**

Objects: [Grid](../objects/grid.md)
