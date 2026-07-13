# Adding a Centigrade Label & Edit Field

Now we need to add a corresponding Centigrade label and edit field. We'll call these objects `LC` and `C` respectively, and place them 40% down the Form.
```apl
'TEMP.LC' ⎕WC'Label' 'Centigrade' (40 10) 
'TEMP.C' ⎕WC 'Edit' '' (40 40)(⍬ 20)('FieldType' 'Numeric')
```

![](../img/temperature-converter-4.png)
