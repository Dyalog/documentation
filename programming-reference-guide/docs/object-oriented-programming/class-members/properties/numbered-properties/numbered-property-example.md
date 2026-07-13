# Example

The [ComponentFile Class](../component-file-class-example.md){: .noprint }  specifies a Numbered Property named `Component` which represents the contents of a specified component on the file.
```apl
    :Property Numbered Component
    :Access Public Instance
        ∇ r←shape
          r←¯1+2⊃⎕FSIZE tie
        ∇
        ∇ r←get arg
          r←⎕FREAD tie arg.Indexers
        ∇
        ∇ set arg
          arg.NewValue ⎕FREPLACE tie,arg.Indexers
        ∇
    :EndProperty
```

```apl

      F1←⎕NEW ComponentFile 'test1'
      
      F1.Append¨(⍳5)×⊂⍳4
1 2 3 4 5
      
      F1.Count
5
      
      F1.Component[4]
 4 8 12 16 
      
      4⊃F1.Component
4 8 12 16
      
      (⊂4 3)⌷F1.Component
 4 8 12 16  3 6 9 12 
```

Referencing a Numbered Property in its entirety causes APL to call the `get` function successively for every element.
```apl
      F1.Component
 1 2 3 4  2 4 6 8  3 6 9 12  4 8 12 16  5 10 15 20
      
      ((⊂4 3)⌷F1.Component)←'Hello' 'World'
      
      F1.Component[3]
 World
```

Attempting to access a Numbered Property with inappropriate indices generates an error:
```apl
      F1.Component[6]
INDEX ERROR
      F1.Component[6]
     ^
      F1.Component[1;2]
RANK ERROR
      F1.Component[1;2]
     ^
```
