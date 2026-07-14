# <span>FormatString</span> <span>Property</span>

**Applies To:** [ButtonEdit](../objects/buttonedit.md), [Edit](../objects/edit.md), [Grid](../objects/grid.md), [Label](../objects/label.md), [Spinner](../objects/spinner.md)

**Description**

The FormatString property specifies one or more `⎕FMT` format specifications to be used to format data in an Grid or single-line Edit. When applied to a Grid, it is either a simple character vector that specifies the format specification for the entire Grid, or a vector of character vectors. If it is a vector, its elements are mapped to individual cells via the CellTypes property. When applied to an Edit object, FormatString must be a simple character vector.

APL derives the text to be displayed in a cell by calling `⎕FMT` with a left argument of the corresponding element of FormatString and a right argument of the cell value. If the format specification is invalid, the text displayed is blank.

When a formatted Edit object receives the focus, it redisplays the contents in its raw (unformatted) form. When the Edit loses the focus, its contents are reformatted. When the user moves to a formatted Grid cell, the text remains formatted until the user presses a non-movement key or enters *in-cell* mode. The data is then redisplayed in its raw form for editing. Data in the cell is reformatted when the user moves away.

In a Grid, formatted data may be aligned vertically using the [AlignChar](alignchar.md) property as illustrated in the following example.
```apl
      'F'⎕WC'Form'
      'F.G'⎕WC'Grid'(¯50+?10 10⍴100)(0 0)(100 100)
      'F.G'⎕WS'FormatString' 'M<(>N<)>F12.3'
      'F.G'⎕WS'AlignChar' '.'
```

![](../img/gridfmt.gif)
