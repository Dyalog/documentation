
<!-- Hidden search keywords -->
<div style="display: none;">
  2010⌶
</div>

<h1 class="heading"><span class="name">Update DataTable</span> <span class="command">R←{X}2010⌶Y</span></h1>

!!! note
    **.NET Framework only**

This function performs a *block update* of an instance of the ADO.NET object System.Data.DataTable. This object may only be updated using an explicit row-wise loop, which is slow at the APL level. `2010⌶` implements an *internal* row-wise loop which is much faster on large arrays. Furthermore, the function handles NULL values and the conversion of internal APL data to the appropriate .NET datatype in a more efficient manner than can be otherwise achieved. These 3 factors together mean that the function provides a significant improvement in performance compared to calling the row-wise programming interface directly at the APL level.

`Y` is a 2, 3 or 4-item array containing:

1. A reference to an instance of System.Data.DataTable.
2. A matrix with the same number of columns as the table specified by `Y[1]`.
3. An optional vector which specifies for each column in the DataTable the values in `Y[2]`which should be converted to a System.DBNull.
4. An optional vector which specifies the indices (in zero origin) of the rows of the DataTable which are to be updated. If omitted, the matrix specified by `Y[2]` will be *appended* to the DataTable.

The optional argument `X` is  Boolean vector, where a 1 indicates that the corresponding column of  `Y[2]` is a string from which the new values  should be converted according to that column's data type.

<h2 class="example">Example</h2>

Shown firstly for comparison is the type of code that is required to update a DataTable by looping:
```apl
      ⎕USING←'System' 'System.Data,system.data.dll'
      dt←⎕NEW DataTable
      ac←{dt.Columns.Add ⍺ ⍵}
      'S1' 'S2' 'I1' 'D1' ac¨String String Int32 DateTime
 S1  S2  I1  D1
 
      NextYear←DateTime.Now+{⎕NEW TimeSpan (4↑⍵)}¨⍳n←365
      data←(⍕¨⍳n),(n⍴'odd' 'even'),(10|⍳n),⍪NextYear
      ¯2 4↑data
 364  even  4  18-01-2011 14:03:29 
 365  odd   5  19-01-2011 14:03:29 
 
      ar←{(row←dt.NewRow).ItemArray←⍵ ⋄ dt.Rows.Add row}
      t←3⊃⎕AI ⋄ ar¨↓data ⋄ (3⊃⎕AI)-t
449
```

This result shows that this code can only insert roughly 800 rows per second (`3⊃⎕AI` returns elapsed time in milliseconds), because of the need to loop on each row and perform a noticeable amount of work each time around the loop.

`2010⌶` does all the looping in compiled code:
```apl
      dt.Rows.Clear ⍝ Delete the rows inserted above
      SetDT←2010⌶
      t←3⊃⎕AI ⋄ SetDT dt data ⋄ (3⊃⎕AI)-t
4
```

So in this case, using `2010⌶` achieves over 90,000 rows per second.

## DateTime columns

Creating large arrays of DateTime objects in the workspace takes additional resources, and unless the data is already stored that way, it is not necessary to convert it to .NET objects. Data in `⎕TS` format (7-element integer vector) or in a suitable character format may be used directly. The former is a specific Dyalog optimisation; the latter a feature of .NET Version 4.0. The following examples use numeric and character data for the dates:
```apl
   months←12⍴31 ⋄ months[2 4 6 9 11]←29 30 30 30 30
   n←⍴NextYear←7↑¨⊃,/(⍳12){(⊂2016,⍺),¨⍳⍵}¨months
   data←(⍕¨⍳n),(n⍴'odd' 'even'),(10|⍳n),⍪NextYear
   SetDT dt data

```
```apl
    
   n←⍴NextYear←⊃,/(⍳12){(⊂'2016/',(⍕⍺),'/'),∘⍕¨⍳⍵}¨months
   data←(⍕¨⍳n),(n⍴'odd' 'even'),(10|⍳n),⍪NextYear
   SetDT dt data

```

## Using Strings

In circumstances where .NET fails to accept character data automatically, it is possible to force conversion from character format to the corresponding .NET type.

If specified, the optional left argument `X` instructs the system to pass the corresponding columns of data to the Parse() method of the data type for those columns prior to performing the update.

In the following example, the left argument is not strictly necessary using .NET Version 4.0, but  forces parsing for the data in the 4th column:
```apl
   months←12⍴31 ⋄ months[2 4 6 9 11]←29 30 30 30 30
   n←⍴NextYear←⊃,/(⍳12){(⊂'2016/',(⍕⍺),'/'),∘⍕¨⍳⍵}¨months
   data←(⍕¨⍳n),(n⍴'odd' 'even'),(10|⍳n),⍪NextYear
   0 0 0 1 SetDT dt data

```

## Handling Nulls

If applicable, `Y[3]`  is a vector with as many elements as the DataTable has columns, indicating the value that should be converted to `System.DBNull` as data is written. For example, using the same DataTable as above:
```apl
      t
 <null>  odd    1  21-01-2010 14:50:19 
 two     even   2  22-01-2010 14:50:19 
 three   odd   99  23-01-2010 14:50:19
 
      dt.Rows.Clear ⍝ Clear the contents of dt
      SetDT dt t ('<null>' 'even' 99 '')
```

Above, we have declared that the string `'<null>'` should be considered to be a null value in the first column, `'even'` in the second column, and the integer `99` in the third.

## Updating Selected Rows

Sometimes, you may have read a very large number of rows from a DataTable, but only want to update a single row, or a very small number of rows. Row indices can be provided as the fourth element of the argument to `2010⌶`. If you are not using `Y[3]` explicitly, you can just use an empty vector as a placeholder. Continuing from the example above, we could replace the first row in our DataTable using:
```apl
      SetDT←2010⌶
      SetDT dt (1 4⍴'one' 'odd' 1 DateTime.Now) ⍬ 0
```

!!! note
    - `Y[2]` must be provided as a matrix, even if you only want to update a single row, 
    - `Y[4]` specifies row indices using zero origin (the first row has number 0).
    - `Y[2]` must be provided as a matrix, even if you only want to update a single row, 
    - `Y[4]` specifies row indices using zero origin (the first row has number 0).

!!! warning
    If you are experimenting with writing to a DataTable, note that you should call `dt.Rows.Clear` each time to clear the current contents of the table. Otherwise you will end up with a very large number of rows after a while.



