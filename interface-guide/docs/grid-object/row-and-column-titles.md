# Row and Column Titles

Row and column titles are defined by the RowTitles and ColTitles properties, each of which is a vector of character arrays. An element of RowTitles and ColTitles may be a character vector specifying a 1-row title, or a matrix or vector of vectors which specify multi-row titles.

The height of the area used to display column titles is specified by the TitleHeight property. The width of the area used to display row titles is defined by the TitleWidth property. The alignment of text within the title cells is defined by RowTitleAlign and ColTitleAlign and the colour of the text is specified by RowTitleFCol and ColTitleFCol.

Multi-level titles are also possible and are defined by the RowTitleDepth and ColTitleDepth properties. An example of what can be achieved is shown below.
```apl
     ∇ HierarchicalTitles;Q1;Q2;Q3;Q4;TITLES;CDEPTH
[1]    'F'⎕WC'Form' ''('Size' 313 362)('Coord' 'Pixel')
[2]    F.Caption←'Hierarchical Titles'
[3]    'F.G'⎕WC'Grid'(?12 6⍴100)(0 0)F.Size
[4]    F.G.(TitleWidth TitleHeight CellWidths)←120 60 40
[5]    Q1←'Q1' 'Jan' 'Feb' 'Mar'
[6]    Q2←'Q2' 'Apr' 'May' 'Jun'
[7]    Q3←'Q3' 'Jul' 'Aug' 'Sep'
[8]    Q4←'Q4' 'Oct' 'Nov' 'Dec'
[9]    TITLES←(⊂'2013'),Q1,Q2,Q3,Q4
[10]   CDEPTH←0,16⍴1 2 2 2
[11]   F.G.(RowTitles RowTitleDepth)←TITLES CDEPTH
[12]   F.G.RowTitleAlign←'Centre'
[13]   TITLES←'Wine' 'Red' 'White'
[14]   TITLES,←'Champagne' 'Red' 'White' 'Rose'
[15]   TITLES,←⊂↑'Beer' ' and' 'Cider'
[16]   CDEPTH←0 1 1 0 1 1 1 0
[17]   F.G.(ColTitles ColTitleDepth)←TITLES CDEPTH
     ∇
```

![](../img/grid-hierarchical-titles.png)
