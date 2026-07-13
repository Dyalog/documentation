# <span>Marker</span> <span>Object</span>

[Parents](../parentlists/marker.md), [Children](../childlists/marker.md), [Properties](../proplists/marker.md), [Methods](../methodlists/marker.md), [Events](../eventlists/marker.md)

**Purpose:** A graphical object used to draw polymarkers.

**Description**

The [Points](../properties/points.md) property specifies one or more sets of points at which one or more sets of polymarkers are to be drawn.

The [Style](../properties/style.md) property determines the symbol that is drawn at each of a set of points. Marker styles are specified either by numbers which represent the following symbol shapes.

|---|---|
|0  |. { .shaded }  |
|1  |`+`|
|2  |`*`|
|3  |`⎕`|
|4  |`×`|
|5  |`⋄`|
|6  |`∘`|

or by character vectors containing the names of [Bitmap](bitmap.md) or [Icon](icon.md) objects.

The height of each symbol is specified by the value of the [Size](../properties/size.md) property. However this applies only to [Style](../properties/style.md)s 1-6 and is ignored if [Style](../properties/style.md) is 0 or the name of a [Bitmap](bitmap.md). The colour of each symbol is specified by the [FCol](../properties/fcol.md) property. The default is black.

The value of [Dragable](../properties/dragable.md) determines whether or not the object can be dragged. The value of [AutoConf](../properties/autoconf.md) determines whether or not the Marker object is resized when its parent is resized.

The structure of the property values is best considered separately for single and multiple sets of polymarkers.

## Single Set of Polymarkers

For a single set of polymarkers, [Points](../properties/points.md) is either a 2-column matrix of (y,x) co-ordinates, or a 2-element vector of y and x co-ordinates respectively.

[Style](../properties/style.md) and [Size](../properties/size.md) are both simple scalar numbers.

[FCol](../properties/fcol.md) is either a single number representing a standard colour, or a 3-element vector which specifies the marker colour explicitly in terms of RGB values.

<h2 class="example">Examples</h2>

First make a [Form](form.md):
```apl
      'F' ⎕WC 'Form'
```

Draw a point at (y=20, x=10):
```apl
      'F.M1' ⎕WC 'Marker' (20 10)
```

Draw a row of points at (y=20, x=10, 20, ... 90) : (Note scalar extension of y-coordinate)
```apl
      'F.M1' ⎕WC 'Marker' (20(10×⍳9))
```

Draw "+" symbols at each corner of a box:
```apl
      Y ← 10 10 50 50
      X ← 10 50 50 10
      'F.M1' ⎕WC 'Marker' (Y X) 1
```

Ditto, but draw them 10% high:
```apl
      'F.M1' ⎕WC 'Marker' (Y X) 1 10
```

Ditto, but use "*" symbols in green:
```apl
      'F.M1' ⎕WC 'Marker' (Y X) 2 10 (0 255 0)
```

## Multiple Sets of Polymarkers

To draw multiple sets of polymarkers with a single name, [Points](../properties/points.md) is a nested vector whose items are themselves 2-column matrices or 2-element nested vectors.

[Style](../properties/style.md) and [Size](../properties/size.md) may be simple scalars specifying a single type and/or size of symbol to be used for all the sets of polymarkers, or vectors specifying different symbols and/or sizes for each set.

[FCol](../properties/fcol.md) may be a single number or a single (enclosed) 3-element vector applying to all the sets of polymarkers. Alternatively, [FCol](../properties/fcol.md) may be a vector whose elements refer to each of the sets of polymarkers in turn. If so, the elements may be single numbers or nested RGB triplets, or a combination of the two.

<h2 class="example">Examples</h2>

First make a [Form](form.md):
```apl
      'F' ⎕WC 'Form'
```

Draw a "`⎕`" at (10,20) and a "`⋄`" at (20,20):
```apl
      'F.M1' ⎕WC 'Marker'((1 2⍴10 20)(1 2⍴20 20)) (3 5)
```

Draw "+" symbols at each corner of one box and  "`○`" symbols at each corner of another:
```apl
      Y1 X1 ← (10 10 50 50) (10 50 50 10)
      Y2 X2 ← (20 20 40 40) (20 40 40 20)
      'F.M1' ⎕WC 'Marker' ((Y1 X1)(Y2 X2)) (1 6)
```

Ditto, but draw the "+" symbols with height 2% and the "`○`" symbols 5%:
```apl
      'F.M1' ⎕WC 'Marker' ((Y1 X1)(Y2 X2)) (1 6) (2 5)
```

Ditto, but draw the "+" symbols in red and the "`○`" symbols in blue:
```apl
      'F.M1' ⎕WC 'Marker' ((Y1 X1)(Y2 X2)) (1 6) (2 5)
                          ('FCol' (255 0 0)(0 0 255))
```
