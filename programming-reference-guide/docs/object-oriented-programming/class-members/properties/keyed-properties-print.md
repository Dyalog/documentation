---
search:
  exclude: true
---

# Keyed Properties

A Keyed Property is similar to a Numbered Property except that it may **only** be accessed by indexing (so-called square-bracket indexing) and indices are not restricted to integers but may be arbitrary arrays.

To implement a Keyed Property, only a `get` and/or a `set` function are required. APL does not attempt to validate or resolve the specified indices in any way, so does not require the presence of a `shape` function for the Property.

However, APL **does** check that the rank and lengths of the indices correspond to the rank and lengths of the array to the right of the assignment (for an indexed assignment) and the array returned by the get function (for an indexed reference). If the rank or shape of these arrays fails to conform to the rank or shape of the indices, APL will issue a `RANK ERROR` or `LENGTH ERROR`.

Note too that indices **may be elided**. If `KProp` is a Keyed Property of Instance `I1`, the following expressions are all valid.
```apl
      I1.KProp
      I1.KProp[]←10
      I1.KProp[;]←10
      I1.KProp['One' 'Two';]←10
      I1.KProp[;'One' 'Two']←10
```

When APL calls a monadic `get` or a `set` function, it supplies an argument of type PropertyArguments,  which identifies which dimensions and indices were specified. See [PropertyArguments Class](../../../property-section/propertyarguments-class.md).

## Keyed Properties Example 1 {: .example }

The Sparse2 Class illustrates the implementation and use of a Keyed Property.

`Sparse2` represents a 2-dimensional sparse array each of whose dimensions are indexed by arbitrary character keys. The
sparse array is implemented as a Keyed Property named `Values`. The following expressions show how it might be used.

```apl
      SA1←⎕NEW Sparse2
      SA1.Values[⊂'Widgets';⊂'Jan']←100
      SA1.Values[⊂'Widgets';⊂'Jan']
100
      SA1.Values['Widgets' 'Grommets';'Jan' 'Mar' 'Oct']←10×2 3⍴⍳6
      SA1.Values['Widgets' 'Grommets';'Jan' 'Mar' 'Oct']
10 20 30
40 50 60
      SA1.Values[⊂'Widgets';'Jan' 'Oct']
10 30
      SA1.Values['Grommets' 'Widgets';⊂'Oct']
60
30
```

## Sparse2 Class Example {: .example }

```apl
:Class Sparse2  ⍝ 2D Sparse Array
    :Field Private keys
    :Field Private values
    ∇ make
      :Access Public
      :Implements Constructor
      keys←0⍴⊂'' ''
      values←⍬
    ∇
    :Property Keyed Values
    :Access Public Instance
        ∇ v←get arg;k
          k←arg.Indexers
          ⎕SIGNAL(2≠⍴k)/4
          k←fixkeys k
          v←(values,0)[keys⍳k]
        ∇
        ∇ set arg;new;k;v;n
          v←arg.NewValue
          k←arg.Indexers
          ⎕SIGNAL(2≠⍴k)/4
          k←fixkeys k
          v←(⍴k)(⍴⍣(⊃1=⍴,v))v
          ⎕SIGNAL((⍴k)≠⍴v)/5
          k v←,¨k v
          :If ∨/new←~k∊keys
              values,←new/v
              keys,←new/k
              k v/⍨←⊂~new
          :EndIf
          :If 0<⍴k
              values[keys⍳k]←v
          :EndIf
        ∇
    :EndProperty
    
    ∇ k←fixkeys k
      k←(2≠≡¨k){,(⊂⍣⍺)⍵}¨k
      k←⊃(∘.{⊃,/⊂¨⍺ ⍵})/k
    ∇
:EndClass ⍝ 2D Sparse Array
```

Internally, `Sparse2` maintains a list of keys and a list of values which are initialised to empty arrays by its
constructor.

When an indexed assignment is made, the `set` function receives a list of keys (indices) in `arg.Indexer` and values
in `arg.NewValue`. The function updates the values of existing keys, and adds new keys and their values to the internal
lists.

When an indexed reference is made, the `get` function receives a list of keys (indices) in `arg.Indexer`. The function
uses these keys to retrieve the corresponding values, inserting 0s for non-existent keys.

Note that in the expression:

```apl
 SA1.Values['Widgets' 'Grommets';'Jan' 'Mar' 'Oct']
```

the structure of `arg.Indexer` is:

```apl
.→-----------------------------------------------.
| .→---------------------. .→------------------. |
| | .→------. .→-------. | | .→--. .→--. .→--. | |
| | |Widgets| |Grommets| | | |Jan| |Mar| |Oct| | |
| | '-------' '--------' | | '---' '---' '---' | |
| '∊---------------------' '∊------------------' |
'∊-----------------------------------------------'
```

## Example {: .example }

A second example of a Keyed Property is provided by the `KeyedFile` Class which is based upon
the ComponentFile Class (see [Section](component-file-class-example.md)) used previously.

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
