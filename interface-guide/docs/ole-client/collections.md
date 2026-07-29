# Collections

A collection is a special type of object that represents a set of other objects. Collections are typically implemented as properties. For example, the Excel Sheet object has a property named Sheets whose value is a collection object that represents a set of worksheets. Collections typically have a property called Count, which tells you how many objects there are, and a Default Property named Item that provides access to each member of the set. Item typically accepts a number or a name as an index and returns a reference to an object.

For example, if a workbook contains two worksheets named "P&L" and "2002 Sales" respectively, they might be accessed as follows:
```apl
      S1←Sheets.Item[1]
      S1.Name
P&L
      S2←Sheets.Item ['2002 Sales']
      S2.Index
2
```

Note that in old versions of Dyalog APL (pre-Version 11.0) the Item property was exposed as a method. This old behaviour may be select by setting `⎕WX` to 0 or 1 when you create the object. In which case:
```apl
      S1←Sheets.Item 1
      S1.Name
P&L
      S2←Sheets.Item '2002 Sales'
      S2.Index
2
```

Note that some collections work in origin 0 and some in origin 1; there is no way to tell which applies except from the documentation. Furthermore, collections are used for all sorts of purposes, and may not necessarily permit the instantiation of more than one member of the set at the same time. Collections are *not* the same as arrays.

As mentioned above, the Item property is typically the Default Property (see Language reference) of a Collection, so indexing may be applied directly to the Collection object.
```apl
      Sheets[1 2].Name
 P&L  2002 Sales
```

The `:For - :EndFor` control structure provides a convenient way to enumerate through the members of a collection without using the Item property. For example, the following code snippet accumulates the values in an Excel worksheet collection.
```apl
      DATA←0⍴⊂0 0⍴0
      :For S :In Sheets  ⍝ Enumerate SHEETS collection
          DATA,←⊂S.UsedRange.Value2
      :EndFor
```
