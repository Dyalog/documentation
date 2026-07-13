# <span>Poly</span> <span>Object</span>



[Parents](../parentlists/poly.md), [Children](../childlists/poly.md), [Properties](../proplists/poly.md), [Methods](../methodlists/poly.md), [Events](../eventlists/poly.md)



**Purpose:** A graphical object used to draw lines, polygons, and filled areas.

**Description**


The [Points](../properties/points.md) property specifies one or more sets of co-ordinates through which one or more lines are drawn. The resulting polygon(s) may also be filled.



[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) define the style and width of the lines. [FCol](../properties/fcol.md) and [BCol](../properties/bcol.md) determine the colour of the lines.


[FStyle](../properties/fstyle.md) specifies whether or not the polygon(s) are filled, and if so, how. For a solid fill ([FStyle](../properties/fstyle.md) 0), [FillCol](../properties/fillcol.md) defines the fill colour used. For a pattern fill ([FStyle](../properties/fstyle.md) 1-6) [FillCol](../properties/fillcol.md) defines the colour of the hatch lines and [BCol](../properties/bcol.md) the colour of the areas between them.


Note that if you specify filling, you do not have to define a **closed** polygon. The first and last points will automatically be joined for you if necessary.


The value of [Dragable](../properties/dragable.md) determines whether or not the object can be dragged. The value of [AutoConf](../properties/autoconf.md) determines whether or not the Poly object is resized when its parent is resized.


The structure of the property values is best considered separately for single and multiple polylines or polygons.


## Single Polyline or Polygon


For a single polyline or polygon, [Points](../properties/points.md) is either a 2-column matrix of (y,x) co-ordinates, or a 2-element vector of y and x co-ordinates respectively.


[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) are both simple scalar numbers.


[FStyle](../properties/fstyle.md) is either a single number specifying a standard fill pattern, or the name of a [Bitmap](bitmap.md) object which is to be used as a "brush" to fill the polygon.


[FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) are each either single numbers representing standard colours, or 3-element vectors which specify colours explicitly in terms of their RGB values.


<h2 class="example">Examples</h2>


First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```


Draw a single line from (y=20, x=10) to (y=30, x=50)
```apl
      'F.L1' ⎕WC 'Poly' ((20 30)(10 50))
```


or
```apl
      L ← 2 2⍴20 10 30 50
      'F.L1' ⎕WC 'Poly' L
```


Draw a horizontal line from (y=20, x=10) to (y=20, x=50). Note scalar extension of y-coordinate.
```apl
      'F.L1' ⎕WC 'Poly' (20(10 50))
```


Draw an empty box in green :
```apl
      Y ← 10 10 50 50 10
      X ← 10 50 50 10 10
      'F.L1' ⎕WC 'Poly' (Y X) (0 255 0)
```


Ditto, using a green/blue dashed line ([LStyle](../properties/lstyle.md) 1) :
```apl
      'F.L1' ⎕WC 'Poly' (Y X) (0 255 0)(0 0 255) 1
```


Draw a red filled rectangle with a black border 5 pixels wide :
```apl
      'F.L1' ⎕WC 'Poly' (Y X) (0 0 0) ('LWidth' 5)
                        ('FStyle' 0)('FillCol' 255 0 0)
```


## Multiple Polylines/Polygons


To draw a set of polylines or polygons with a single name, [Points](../properties/points.md) is a nested vector whose items are themselves 2-column matrices or 2-element nested vectors.


[LStyle](../properties/lstyle.md) and [LWidth](../properties/lwidth.md) may each be simple scalar values (applying to all the polylines) or simple vectors whose elements refer to each of the corresponding polylines in turn.


[FStyle](../properties/fstyle.md) may be a simple scalar numeric or a simple character vector ([Bitmap](bitmap.md) name) applying to all polylines, or a vector whose elements refer to each of the corresponding polylines in turn.


Similarly, [FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FillCol](../properties/fillcol.md) may each be single numbers or a single (enclosed) 3-element vector applying to all the polylines. Alternatively, these properties may contain vectors whose elements refer to each of the polylines in turn. If so, their elements may be single numbers or nested RGB triplets, or a combination of the two.


<h2 class="example">Examples</h2>


First make a [Form](form.md) :
```apl
      'F' ⎕WC 'Form'
```


Draw two concentric triangles :
```apl
      BY ← 10 10 50 10
      BX ← 15 65 40 15
      RY ← 15 15 40 15
      RX ← 25 55 40 25
      'F.L1' ⎕WC 'Poly' ((BY BX)(RY RX))
```


Or, using matrices :
```apl
      BT ← BY,[1.5]BX
      RT ← RY,[1.5]RX
      'F.L1' ⎕WC  P←'Poly' (BT RT)
```


Ditto, but draw the first blue, the second red :
```apl
      'F.L1' ⎕WC P,⊂((0 0 255)(255 0 0))
```


Ditto, but make the lines 3 pixels wide :
```apl
      'F.L1' ⎕WC P, ((0 0 255)(255 0 0))('LWidth' 3)
```


Ditto, but make the line widths 3 and 6 pixels respectively :
```apl
      'F.L1' ⎕WC P, ((0 0 255)(255 0 0))('LWidth' 3 6)
```


Draw the first hollow, but fill the second in green :
```apl
      'F.L1' ⎕WC P, ('FStyle' ¯1 0)('FillCol' (⊂0 255 0))
```


