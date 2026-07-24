---
search:
  boost: 2
---

# <span>Materialise</span> `R←⌷Y`{{key}}

If `Y` is a ref to an instance of a Dyalog Class with a Default  property:

- If the Default property is Simple, `⌷` returns its value. 
- If the Default property is Numbered, `⌷` returns an array whose shape is determined by the PropertyShape function and whose items are constructed by calling the ProperyGet function repeatedly with the corresponding set of indices. However, see **Performance Considerations**.
- If the Default property is Keyed,  `NONCE ERROR` is reported, because in this case APL has no way to determine the list of all the elements.

If  `Y` is a ref to an instance of a COM or .NET Collection object, `⌷` returns a vector containing all its items.

Otherwise, if `Y` is an array, `Y` is returned.

<h2 class="example">Example</h2>

The following example uses the sample [ComponentFile Class](../../../programming-reference-guide/object-oriented-programming/class-members/properties/component-file-class-example).
```apl
     )LOAD ComponentFile
...\Samples\OO4APL\ComponentFile.dws saved ...
      F1←⎕NEW ComponentFile 'test1'

      F1
#.[ComponentFile]

      F1.Append¨(⍳5)×⊂⍳4
1 2 3 4 5
      ⌷F1
┌───────┬───────┬────────┬─────────┬──────────┐
│1 2 3 4│2 4 6 8│3 6 9 12│4 8 12 16│5 10 15 20│
└───────┴───────┴────────┴─────────┴──────────┘

```

The following example shows how `⌷`obtains the items in an Excel Sheets collection .
```apl
      wb←ex.Workbooks.Open⊂'budget.xls'
      wb.Sheets
#.[OLEClient].[Workbooks].[_Workbook].[Sheets]
      ⌷wb.Sheets
 #.[_Worksheet]  #.[_Worksheet]  #.[_Worksheet]
      (⌷wb.Sheets).Name
┌────┬────┬────┐
│2012│2011│2010│
└────┴────┴────┘

```

## Performance Considerations

Note that the *values* of the index set are obtained or assigned by calls to the corresponding PropertyGet and PropertySet functions. Furthermore, if there is a sequence of primitive functions to the left of the Index function, that operate on the index set itself (functions such as dyadic `⍴,↑,↓,⊃`) as opposed to functions that operate on the *values* of the index set (functions such as `+,⌈,⌊,⍴¨`), calls to the PropertyGet and PropertySet functions are deferred until the required index set has been completely determined. The full set of functions that cause deferral of calls to the PropertyGet and PropertySet functions is the same as the set of functions that applies to selective specification.

If for example, `CompFile` is an Instance of the [ComponentFile Class](../../../programming-reference-guide/object-oriented-programming/class-members/properties/component-file-class-example):
```apl
       1↑⌽⌷CompFile
```

would only call the PropertyGet function (for `CompFile`) once, to get the value of the last element.

Note that similarly, the expression
```apl
      10000⍴⌷CompFile
```

would call the PropertyGet function 10000 times, on repeated indices if `CompFile` has less than 10000 elements. The deferral of access function calls is intended to be an optimisation, but can have the opposite effect. You can avoid unnecessary repetitive calls by assigning the result of `⌷` to a temporary variable.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⌷ materialise materialize
</div>
