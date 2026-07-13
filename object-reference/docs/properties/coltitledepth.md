# <span>ColTitleDepth</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


ColTitleDepth specifies the structure of a set of hierarchical column titles.
It is an integer vector with the same length as the [ColTitles](coltitles.md) property. A value of 0 indicates that the corresponding element of [ColTitles](coltitles.md) is a top-level title. A value of 1 indicates that the corresponding title is a
sub-title of the most recent title whose ColTitleDepth is 0; a value of 2
indicates that the corresponding title is a sub-title of the most recent title
whose ColTitleDepth is 1, and so forth. For example:
```apl
      'F'⎕WC'Form'('Coord' 'Pixel')('Size' 200 498)
      'F'⎕WS'Caption' 'Hierarchical Column Titles' 
      'F.G'⎕WC'Grid'(?10 12⍴100)(0 0)(200 498)     
      'F.G'⎕WS('TitleWidth' 0)('TitleHeight' 60)   
      'F.G'⎕WS'CellWidths' 40                      

      Q1←'First Quarter' 'Jan' 'Feb' 'Mar'         
      Q2←'Second Quarter' 'Apr' 'May' 'Jun'        
      Q3←'Third Quarter' 'Jul' 'Aug' 'Sep'         
      Q4←'Fourth Quarter' 'Oct' 'Nov' 'Dec'        

      CT←(⊂'1995'),Q1,Q2,Q3,Q4                     
      CD←0,16⍴1 2 2 2                              

      'F.G'⎕WS('ColTitles'CT)('ColTitleDepth'CD)  
```


![](../img/gridct.gif)


Note that the [LockColumns](../methodorevents/lockcolumns.md) method is
not supported in combination with hierarchical column titles.



