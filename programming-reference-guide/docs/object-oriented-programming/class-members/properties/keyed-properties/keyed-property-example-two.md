# Example 2

A second example of a Keyed Property is provided by the `KeyedFile` Class which is based upon the [ComponentFile Class](../component-file-class-example.md){: .noprint } used previously.
```apl
:Class KeyedFile: ComponentFile
    :Field Public Keys
    ⎕ML←0
    
    ∇ Open filename
      :Implements Constructor :Base filename
      :Access Public Instance
      :If Count>0
          Keys←{⊃⍵⊃⎕BASE.Component}¨⍳Count
      :Else
          Keys←0⍴⊂''
      :EndIf
    ∇
    
    :Property Keyed Component
    :Access Public Instance
        ∇ r←get arg;keys;sink
          keys←⊃arg.Indexers
          ⎕SIGNAL(~^/keys∊Keys)/3
          r←{2⊃⍵⊃⎕BASE.Component}¨Keys⍳keys
        ∇
        ∇ set arg;new;keys;vals
          vals←arg.NewValue
          keys←⊃arg.Indexers
          ⎕SIGNAL((⍴,keys)≠⍴,vals)/5
          :If ∨/new←~keys∊Keys
              sink←Append¨↓⍉↑(⊂new)/¨keys vals
              Keys,←new/keys
              keys vals/⍨←⊂~new
          :EndIf
          :If 0<⍴,keys
              Replace¨↓⍉↑(Keys⍳keys)(↓⍉↑keys vals)
          :EndIf
        ∇
    :EndProperty
    
:EndClass ⍝ Class KeyedFile
```

```apl

 
      K1←⎕NEW KeyedFile 'ktest'
      K1.Count
0
      K1.Component[⊂'Pete']←42
      K1.Count
1
      K1.Component['John' 'Geoff']←(⍳10)(3 4⍴⍳12)
      K1.Count
```
```apl

3
      K1.Component['Geoff' 'Pete']
 1  2  3  4  42
 5  6  7  8    
 9 10 11 12    
      K1.Component['Pete' 'Morten']←(3 4⍴'∘')(⍳⍳3)
      K1.Count
4
      K1.Component['Morten' 'Pete' 'John']
  1 1 1  1 1 2  1 1 3   ∘∘∘∘  1 2 3 4 5 6 7 8 9 10 
  1 2 1  1 2 2  1 2 3   ∘∘∘∘                       
                        ∘∘∘∘                       
```
