# <span>Text</span> <span>Object</span>

[Parents](../parentlists/text.md), [Children](../childlists/text.md), [Properties](../proplists/text.md), [Methods](../methodlists/text.md), [Events](../eventlists/text.md)

**Purpose:** Writes text.

**Description**

The Text object is used to write arbitrary text. It can be used in a [Form](form.md), [SubForm](subform.md) or [Group](group.md) instead of a [Label](label.md). The main difference is that a [Label](label.md) is implemented as a true window object (thus consuming Windows resources). A Text object is not a window and consumes no MS-Windows resources. However, a [Label](label.md) supports [DragDrop](../methodorevents/dragdrop.md) events and has various
useful properties that are not shared by the Text object.

The contents of the Text object are defined by its [Text](../properties/text.md) property. This is a character array containing one of the following :

- a simple scalar
- an enclosed vector or matrix (also a scalar)
- a simple vector
- a simple matrix
- a vector of enclosed vectors or matrices

[Points](../properties/points.md) is either a simple 2-column matrix of (y,x) co-ordinates, or a 2-element vector of y-coordinates and x-coordinates
respectively.

There are two distinct cases:

1. [Points](../properties/points.md) specifies a single point. In
this case, Text may be a single scalar character, a simple vector, or a matrix
containing a block of text. The result is that the character, string, or matrix
is written at the specified point.
2. [Points](../properties/points.md) specifies more than one
    point. There are three possibilities:
      1. If Text is a scalar, its contents are written at each of the points in [Points](../properties/points.md). This means that by enclosing a vector or matrix, you can draw a string or block of text at several locations.
      2. If Text is a vector, each element of Text is written at the corresponding position in [Points](../properties/points.md).
      3. If Text is a matrix, each row of Text is written at the corresponding position in [Points](../properties/points.md).

[FontObj](../properties/fontobj.md) specifies a **single** font
to be used to write the Text. See a description of the [FontObj](../properties/fontobj.md) property for details.

[FCol](../properties/fcol.md) specifies the colour of the Text. For a single text item, FCol may be a single number which specifies one of the
standard MS-Windows colours, or a simple 3-element numeric vector of RGB colour intensities. If more than one text item is involved, [FCol](../properties/fcol.md) may be a vector which specifies the colour for each item separately. If so, its length must be the same as the number of points specified by [Points](../properties/points.md).

[BCol](../properties/bcol.md) specifies the background colour of the text, that is, the colour for the part of the character cell that is blank. It is
defined in the same way as [FCol](../properties/fcol.md).

[HAlign](../properties/halign.md) and [VAlign](../properties/valign.md) specify the horizontal and vertical alignment of the text respectively. They may each be numeric scalars or vectors with the same length as the number of points specified in [Points](../properties/points.md). See [HAlign](../properties/halign.md) and [VAlign](../properties/valign.md) for details.

When one or more of [FCol](../properties/fcol.md), [BCol](../properties/bcol.md), [HAlign](../properties/halign.md) and [VAlign](../properties/valign.md) are vectors, the different components of Text are drawn using the corresponding colours and alignments.

The value of the [Dragable](../properties/dragable.md) property specifies whether or not the Text object can be dragged by the user. The value
of the [AutoConf](../properties/autoconf.md) property determines whether or not the Text object is repositioned when its parent is resized.

<h2 class="example">Examples</h2>

Write `'A'` at (10,20)
```apl
      'g.t1' ⎕WC 'Text' 'A' (10 20)
```
Write `'h'` at (10,20) in red
```apl
      'g.t1' ⎕WC 'Text' 'h' (10 20) ('FCol' 255 0 0)
```
Write `'Hello'` at (10,20)
```apl
      'g.t1' ⎕WC 'Text' 'Hello' (10 20)
```
```apl
Write 'THIS IS A
       BLOCK OF
       TEXT     '   at (20,30)
```
```apl
      BLK←3 9⍴'THIS IS A BLOCK OF TEXT     '
      'g.t1' ⎕WC 'Text' BLK (10 20)
```
Write `'A'` at (10,20) and at (30,40)
```apl
      'g.t1' ⎕WC 'Text' 'A' ((10 30)(20 40))
```
Write a red `'+'` at (10,20) and a green `'+'` at (20 40)
```apl
      'g.t1' ⎕WC 'Text' '+' ((10 30)(20 40))('FCol' (255 0 0)(0 255 0))
```
Write `'Hello'` at (10,20) and at (30,40)
```apl
      'g.t1' ⎕WC 'Text' (⊂'Hello') ((10 30)(20 40))
```
Write `'A'` at (10,20) and `'B'` at (30,40)
```apl
      'g.t1' ⎕WC 'Text' 'AB' ((10 30)(20 40))
```
Write `'Hello'` at (10,20) and `'World'` at (30,40)
```apl
      'g.t1' ⎕WC 'Text' ('Hello' 'World')((10 30)(20 40))
```
