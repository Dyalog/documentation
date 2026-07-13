# <span>RowTitleDepth</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


RolTitleDepth specifies the structure of a set of hierarchical row titles.



It
is an integer vector with the same length as the RowTitles property. A value of
0 indicates that the corresponding element of RowTitles is a top-level title. A
value of 1 indicates that the corresponding title is a sub-title of the most
recent title whose RowTitleDepth is 0; a value of 2 indicates that the
corresponding title is a sub-title of the most recent title whose RowTitleDepth
is 1, and so forth. For example:
```apl
      'F'⎕WC'Form'('Coord' 'Pixel')('Size' 318 310)
      'F'⎕WS'Caption' 'Hierarchical Column Titles' 
      'F.G'⎕WC'Grid'(?12 4⍴100)(0 0)(318 310)      
      'F.G'⎕WS('TitleWidth' 150)('TitleHeight' 0)  
      'F.G'⎕WS'CellWidths' 40                      

      Q1←'Q1' 'Jan' 'Feb' 'Mar'                    
      Q2←'Q2' 'Apr' 'May' 'Jun'                    
      Q3←'Q3' 'Jul' 'Aug' 'Sep'                    
      Q4←'Q4' 'Oct' 'Nov' 'Dec'                    
      RT←(⊂'1995'),Q1,Q2,Q3,Q4                     
      RD←0,16⍴1 2 2 2                              

      'F.G'⎕WS('RowTitles'RT)('RowTitleDepth'RD)

      'F.G'⎕WS'RowTitleAlign' 'Centre'
```


![](../img/gridrt.gif)


Note that the [LockRows](../methodorevents/lockrows.md) method is not
supported in combination with hierarchical row titles.


