# The Default Property

A single Numbered Property may be identified as the *Default* Property for the Class. If a Class has a Default Property, indexing with the `⌷` primitive function and `[...]` indexing may be applied to the Property directly via a reference to the Class or Instance.

The Numbered Property example of the [ComponentFile Class](component-file-class-example.md){: .noprint } can be extended by adding the control word `Default` to the `:Property` statement for the `Component` Property.

Indexing may now be applied directly to the Instance `F1`. In essence, `F1[n]` is simply shorthand for `F1.Component[n]` and `n⌷F1` is shorthand for `n⌷F1.Component`
```apl
    :Property Numbered Default Component
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
 
      F1←⎕NEW ComponentFile 'test1'
      F1.Append¨(⍳5)×⊂⍳4
1 2 3 4 5
      F1.Count
5
 
      F1[4]
 4 8 12 16
      (⊂4 3)⌷F1
 4 8 12 16  3 6 9 12 
      ((⊂4 3)⌷F1)←'Hello' 'World'
      F1[3]
 World
```

Note however that this feature applies only to indexing.
```apl
      4⊃F1
DOMAIN ERROR
      4⊃F1
     ^
```
