# <span>Rect</span> <span>Object</span>

[Parents](../parentlists/rect.md), [Children](../childlists/rect.md), [Properties](../proplists/rect.md), [Methods](../methodlists/rect.md), [Events](../eventlists/rect.md)

**Purpose:** A graphical object used to draw boxes.

**Description**

The [Points](../properties/points.md) property specifies one or more sets of co-ordinates which define the position(s) of one or more rectangles. The position of a rectangle is defined to be the position of the corner that is **nearest** to the origin of its parent. The default is therefore its top-left corner. The [Size](../properties/size.md) property specifies the height and width of each rectangle, measuring away from the origin.

The [Radius](../properties/radius.md) property specifies the curvature of the corners of the rectangle.

[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) define the style and width of the lines used to draw the boundaries of the rectangle(s). [FCol](../properties/fcol.md) and [BCol](../properties/bcol.md) determine the colour of the lines.

[FStyle](../properties/fstyle.md) specifies whether or not the rectangle(s) are filled, and if so, how. For a solid fill ([FStyle](../properties/fstyle.md) 0), [FillCol](../properties/fillcol.md) defines the fill colour used. For a pattern fill ([FStyle](../properties/fstyle.md) 1-6) [FillCol](../properties/fillcol.md) defines the colour of the hatch lines and [BCol](../properties/bcol.md) the colour of the spaces between them.

The [EdgeStyle](../properties/edgestyle.md) property may specify a 3-dimensional effect. If so, the boundary line around the rectangle is replaced by a border designed to achieve the desired effect.

The value of [Dragable](../properties/dragable.md) determines whether or not the object can be dragged. The value of [AutoConf](../properties/autoconf.md) determines whether or not the Rect object is resized when its parent is resized.

The structure of the property values is best considered separately for single and multiple rectangles :

## Single Rectangle

For a single rectangle, [Points](../properties/points.md) is either a 2-column matrix of (y,x) co-ordinates, or a 2-element vector of y and x co-ordinates respectively.

[Size](../properties/size.md) is a simple 2-element vector whose elements specify the height and width of the rectangle respectively.

[Radius](../properties/radius.md) is a 2-element vector which specifies the major (y-axis) and minor (x-axis) radii of an ellipse used to draw the corners of the rectangle. Its default value is (0 0) which yields right-angled corners.

[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) are both simple scalar numbers.

[FStyle](../properties/fstyle.md) is either a single number specifying a standard fill pattern, or the name of a [Bitmap](bitmap.md) object which is to be used as a "brush" to fill the rectangle.

[FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) are each either single numbers representing standard colours, or 3-element vectors which specify colours explicitly in terms of their RGB values.

<h2 class="example">Examples</h2>

First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```

Draw a single rectangle at (y=10, x=5) with height=30, width=50 :
```apl
      'F.R1' ⎕WC 'Rect' (10 5)(30 50)
```

Ditto with rounded corners (radii 10) :
```apl
      'F.R1' ⎕WC RC←'Rect' (10 5)(30 50)(10 10)
```

Ditto, but use a red line :
```apl
      'F.R1' ⎕WC RC,⊂(255 0 0)
```

Ditto, but fill in green
```apl
      'F.R1' ⎕WC RC(255 0 0) ('FStyle' 0)(0 255 0)
```

## Multiple Rectangles

To draw a set of rectangles with a single name, [Points](../properties/points.md) may be a simple 2-element vector (specifying the location of all the rectangles), **or** a 2-column matrix whose first column specifies their y-coordinates and whose second column specifies their x-coordinates, **or** a 2-element nested vector whose first element specifies their y-coordinate(s) and whose second element specifies their x-coordinate(s).

Likewise, [Size](../properties/size.md) may be a simple 2-element vector (applying to all the rectangles), **or** a 2-column matrix whose first column specifies their heights and whose second column specifies their widths, **or** a 2-element nested vector whose first element specifies their height(s) and whose second element specifies their width(s).

[Radius](../properties/radius.md) may be a simple 2-element vector (applying to all the rectangles), **or** a 2-column matrix whose first column specifies major radii and whose second column specifies minor radii, **or** a 2-element nested vector whose first element specifies major radii and whose second element specifies minor radii.

[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) may each be simple scalar values (applying to all the rectangles) or simple vectors whose elements refer to each of the corresponding rectangles in turn.

[FStyle](../properties/fstyle.md) may be a simple scalar numeric or a simple character vector ([Bitmap](bitmap.md) name) applying to all rectangles, or a vector whose elements refer to each of the corresponding rectangles in turn.

Similarly, [FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) may each be single numbers or a single (enclosed) 3-element vector applying to all the rectangles. Alternatively, these properties may contain vectors whose elements refer to each of the rectangles in turn. If so, their elements may be single numbers or nested RGB triplets, or a combination of the two.

<h2 class="example">Examples</h2>

First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```

Draw two rectangles at (y=5, x=10) and (y=5, x=60) each of (height=40, width=10)
```apl
      'F.R1' ⎕WC 'Rect' ((5 5)(10 60)) (40 10)
```

Ditto, using scalar extension for (y=5) :
```apl
      'F.R1' ⎕WC 'Rect' (5(10 60)) (40 10)
```

Ditto, but draw the first with (height=40, width=30) and the second with (height=20, width=10) :
```apl
      'F.R1' ⎕WC 'Rect' (5(10 60)) ((40 20)(30 10))
```

Draw two rectangles at (y=5, x=10) and (y=5, x=60) each of (height=40, width=10) and with rounded corners of radii (10,10) :
```apl
      'F.R1' ⎕WC RC←'Rect' (5(10 60)) (40 10) (10 10)
```

Ditto, using a green line for both :
```apl
      'F.R1' ⎕WC RC,⊂⊂0 255 0
```

Ditto, but using red and blue lines respectively :
```apl
      'F.R1'⎕WC RC,⊂(255 0 0)(0 0 255)
```
