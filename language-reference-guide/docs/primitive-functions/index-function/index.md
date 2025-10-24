<div style="display: none;">
  ⌷
</div>

<h1 class="heading"><span class="name">Index</span> <span class="command">R←X⌷Y</span></h1>

`X` must be a scalar or vector of depth `≤2` of integers each `≥⎕IO`. `Y` may be any array. In general, the result `R` is similar to that obtained by square-bracket indexing in that:
```apl
      (I J ... ⌷ Y) ≡ Y[I;J;...]
```

The length of left argument `X` must be less than or equal to the rank of right argument `Y`. Any missing trailing items of `X` default to the index vector of the corresponding axis of `Y`.

Note that in common with square-bracket indexing, items of the left argument `X` may be of any rank and that the shape of the result is the concatenation of the shapes of the items of the left argument:
```apl
      (⍴X⌷Y) ≡ ↑,/⍴¨X
```

Index is sometimes referred to as *squad indexing*.

Note that index may be used with selective specification.

`⎕IO` is an implicit argument of index.

<h2 class="example">Examples</h2>
```apl
      ⎕IO←1
 
      VEC←111 222 333 444
      3⌷VEC
333
      (⊂4 3)⌷VEC
444 333
      (⊂2 3⍴3 1 4 1 2 3)⌷VEC
333 111 444
111 222 333
 
      ⎕←MAT←10⊥¨⍳3 4
11 12 13 14
21 22 23 24
31 32 33 34
 
      2 1⌷MAT
21
      2⌷MAT
21 22 23 24

```
```apl
 
      3(2 1)⌷MAT
32 31
      (2 3)1⌷MAT
21 31
      (2 3)(,1)⌷MAT
21
31
      ⍴(2 1⍴1)(3 4⍴2)⌷MAT
2 1 3 4
      ⍴⍬ ⍬⌷MAT
0 0
      (3(2 1)⌷MAT)←0 ⋄ MAT    ⍝ Selective assignment.
11 12 13 14
21 22 23 24
 0  0 33 34
```

## Indexing  Classes

If `Y` is a ref to an instance of a Class with a Default property, `⌷` is applied to the Default property. Similarly, `⌷` applied to a COM or .NET collection returns the appropriate item(s) of the collection.

<h2 class="example">Example</h2>
```apl
      ↑⎕SRC c
:Class c                 
    :Property Default p  
    :Access Public Shared
        ∇ r←get          
          r←2 3 4⍴⎕A     
        ∇                
    :EndProperty         
:EndClass                

      2⌷c
MNOP
QRST
UVWX
```
