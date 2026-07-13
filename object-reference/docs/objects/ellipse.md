# <span>Ellipse</span> <span>Object</span>

[Parents](../parentlists/ellipse.md), [Children](../childlists/ellipse.md), [Properties](../proplists/ellipse.md), [Methods](../methodlists/ellipse.md), [Events](../eventlists/ellipse.md)

**Purpose:** A Graphical object to draw ellipses, arcs, and pie-slices.

**Description**

This object duplicates much of the functionality of the [Circle](circle.md) object, but differs in two major respects. Firstly, ellipses, circles, and arcs
are specified in terms of their **bounding rectangles**, rather than in terms
of their centre(s) and radii. Secondly, the Ellipse object behaves like any
other (rectangular) object when it is resized by its parent. The [Circle](circle.md) object behaves differently in that when resized by its parent, it maintains a
constant ratio between its **physical** height and width.

The [Points](../properties/points.md) property specifies one or more
sets of co-ordinates which define the position(s) of one or more bounding
rectangles. The position is defined to be the position of the corner that is **nearest** to the origin of its parent. The default is therefore its top-left corner.

The [Size](../properties/size.md) property specifies the height and
width of each bounding rectangle, measuring away from the origin. To obtain a
perfect circle, you must take the **aspect ratio** of the device into
account. This is available from the [DevCaps](../properties/devcaps.md) property of the [Root](root.md) and [Printer](printer.md) objects. Alternatively you can use the [Circle](circle.md) object.

The [Start](../properties/start.md) and/or [End](../properties/end.md) properties are used to draw partial ellipses and circles. They specify start and
end angles respectively, measuring from the x-axis at the centre of the bounding
rectangle in a counter-clockwise direction and are expressed in radians. The
type of arc is controlled by [ArcMode](../properties/arcmode.md) as
follows:

|ArcMode|Effect|
|---|---|
|0|An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) .|
|1|An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) .       In addition, a single straight line is drawn from one end of the arc to       the other, resulting in a segment.|
|2|An arc is drawn from [Start](../properties/start.md) to [End](../properties/end.md) .       In addition, two lines are drawn from each end of the arc to the centre,       resulting in a pie-slice.|

[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) define the style and width of the lines used to draw the boundaries of the
ellipse(s), circle(s) or arc(s). [FCol](../properties/fcol.md) and [BCol](../properties/bcol.md) determine the colour of the lines.

[FStyle](../properties/fstyle.md) specifies whether or not the
ellipse(s), circle(s) or arc(s) are filled, and if so, how. For a solid fill ([FStyle](../properties/fstyle.md) 0), [FillCol](../properties/fillcol.md) defines the fill colour used.
For a pattern fill ([FStyle](../properties/fstyle.md) 1-6) [FillCol](../properties/fillcol.md) defines the colour of the hatch lines and [BCol](../properties/bcol.md) the colour of the spaces between them.

The value of [Dragable](../properties/dragable.md) determines
whether or not the object can be dragged. The value of [AutoConf](../properties/autoconf.md) determines whether or not the Ellipse object is resized when its parent is
resized.

The structure of the property values is best considered separately for single
and multiple ellipses, circles or arcs.

## Single Ellipse, Circle or Arc

For a single ellipse, circle or arc, [Points](../properties/points.md) is a 2-element vector which specifies the y-coordinate and x-coordinate of the
top-left corner of the bounding rectangle.

[Size](../properties/size.md) is also a simple 2-element vector
whose elements specify the height and width of the bounding rectangle.

[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) are both simple scalar numbers.

[FStyle](../properties/fstyle.md) is either a single number
specifying a standard fill pattern, or the name of a [Bitmap](bitmap.md) object which is to be used to fill the ellipse, circle or arc.

[FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) are each either single numbers
representing standard colours, or 3-element vectors which specify colours
explicitly in terms of their RGB values.

<h2 class="example">Examples</h2>

First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```

Draw a complete ellipse within the bounding rectangle located at (y=10, x=5)
with (height=30, width=50) :
```apl
      'F.E1' ⎕WC 'Ellipse' (10 5)(30 50)
```

Draw an elliptical arc within the same bounding rectangle as above, occupying
the upper right quadrant (0 to 90 degrees):
```apl
      'F.E1' ⎕WC 'Ellipse' (10 5)(30 50)('End'(○0.5))
```

Ditto, but between 45 and 135 degrees :
```apl
      'F.E1' ⎕WC 'Ellipse' (10 5)(30 50)('Start'(○0.25))('End'(○0.75))
```

Ditto, but join the points of the arc to the centre of the ellipse, making a
"pie-slice":
```apl
      'F.E1' ⎕WC 'Ellipse' (10 5)(30 50)('Start'(○0.25))('End'(○0.75))('ArcMode' 2)
```

Ditto, but use a green line and solid red fill :
```apl
      'F.E1' ⎕WC 'Ellipse' (10 5)(30 50)('Start'(○0.25))('End'(○0.75))('ArcMode' 2)('FCol' 0 0 255)('FStyle' 0)('FillCol' 255 0 0)
```

## Multiple Ellipses, Circles or Arcs

To draw a set of ellipses, circles, or arcs with a single name, [Points](../properties/points.md) may be a simple 2-element vector (specifying the location of all the bounding
rectangles), **or** a 2-column matrix whose first column specifies their
y-coordinates and whose second column specifies their x-coordinates, **or** a
2-element nested vector whose first element specifies their y-coordinate(s) and
whose second element specifies their x-coordinate(s).

Likewise, [Size](../properties/size.md) may be a simple 2-element
vector (applying to all the bounding rectangles), **or** a 2-column matrix
whose first column specifies their heights and whose second column specifies
their widths, **or** a 2-element nested vector whose first element specifies
their height(s) and whose second element specifies their width(s).

If specified, [Start](../properties/start.md) and/or [End](../properties/end.md) define arcs in terms of the angles made by drawing a line from the centre of the
bounding box to the two ends of the arc. Both properties may be simple scalars,
or vectors containing one element per arc drawn.

If [Start](../properties/start.md) is specified, but not [End](../properties/end.md),
end angles default to `(¯1↓+\Start),○2`.
If [End](../properties/end.md) is specified, but not [Start](../properties/start.md),
start angles default to `0,¯1↓+\End`

This means that you can draw a pie-chart using either [Start](../properties/start.md) or [End](../properties/end.md) angles; you do not have to specify both.

[ArcMode](../properties/arcmode.md), [LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) may each be simple scalar values
(applying to all the ellipses, circles or arcs) or simple vectors whose elements
refer to each of the corresponding ellipses, circles or arcs in turn.

[FStyle](../properties/fstyle.md) may be a simple scalar numeric or
a simple character vector ([Bitmap](bitmap.md) name)
applying to all rectangles, or a vector whose elements refer to each of the
corresponding ellipses, circles or arcs in turn.

Similarly, [FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) may each be single numbers or a
single (enclosed) 3-element vector applying to all the rectangles.
Alternatively, these properties may contain vectors whose elements refer to each
of the rectangles in turn. If so, their elements may be single numbers or nested
RGB triplets, or a combination of the two.

The [Coord](../properties/coord.md), [Dragable](../properties/dragable.md) and [Data](../properties/data.md) properties are specified for the
object as a whole, and may not be allocated different values for each individual
ellipse, circle or arc that is drawn.

<h2 class="example">Examples</h2>

First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```

Draw two ellipses in bounding rectangles located at (y=5, x=10) and (y=5,
x=60), each of (height=40, width=10)
```apl
      'F.E1' ⎕WC 'Ellipse' ((5 5)(10 60)) (40 10)
```

Ditto, using scalar extension for (y=5) :
```apl
      'F.E1' ⎕WC 'Ellipse' (5(10 60)) (40 10)
```

Ditto, but draw the first with (height=40, width=30) and the second with
(height=20, width=10) :
```apl
      'F.E1' ⎕WC 'Ellipse' (5(10 60)) ((40 20)(30 10))
```

Draw an elliptical Pie-Chart in a bounding rectangle located at (y=5, x=10)
with a height and width equal to 40% of the height and width of the parent [Form](form.md).
Each of the 4 pie-slices is bounded by a black line :
```apl
      Data ←12 27 21 40
      ANGLES←0,¯1↓((○2)÷+/Data)×+\Data
      COLS←(255 0 0)(0 255 0)(255 255 0)(0 0 255)
      PATS←1 2 3 4

      'F.PIE' ⎕WC 'Ellipse'(5 10)(40 40)
                  ('Start' ANGLES)('ArcMode' 2)
                  ('FCol' (⊂0 0 0))('FStyle' PATS)
                  ('FillCol' COLS)
```
