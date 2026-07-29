# Writing Classes based on OLEClient

You may define APL Classes (See Language Reference) based upon the OLEClient object. For example:
```apl
:Class Excel: 'OLEClient'
    ∇ ctor wkbk
      :Access Public
      :Implements Constructor :Base ,⊂('ClassName' 'Excel.Application')
      Workbooks.Open ⊂wkbk
    ∇
:EndClass ⍝ Excel
```
```apl
      XL←⎕NEW Excel 'f:\help11.0\days.xls'
      XL.Workbooks[1].Sheets[1].UsedRange.Value2
   From      To    Days  Hours 
  38790   38791       0   3.25 
  38792   38792  [Null]   2.25 
  38793   38793  [Null]   2.5  
  38799   38799  [Null]   5    
  38800   38800  [Null]   3    
 [Null]  [Null]  [Null]  16
```
