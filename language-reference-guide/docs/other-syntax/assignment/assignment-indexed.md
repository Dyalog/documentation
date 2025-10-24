<!-- Hidden search keywords -->
<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment (Indexed)</span> <span class="command">{R}←X[I]←Y</span></h1>

Indexed Assignment is the Assignment function modified by the Indexing function.  The phrase `[I]←` is treated as the function for descriptive purposes.

`Y` may be any array.  `X` may be the *name* of any array or a selection from a named array `(EXP X)[I]←Y`, see [Assignment (Selective)](assignment-selective.md).  `I` must be a valid index specification.  The shape of `Y` must conform with the shape (implied) of the indexed structure defined by `I`.  If `Y` is a scalar or a 1-element vector it will be extended to conform.  A side effect of Indexed Assignment is to change the value of the indexed elements of `X`.

`R` is the value of `Y`.  If the result is not explicitly assigned or used it is suppressed.

`⎕IO` is an implicit argument of Indexed Assignment.

Three forms of indexing are permitted.

## Simple Indexed Assignment

For vector `X`, `I` is a simple integer array whose items are from the set `⍳⍴R`.  Elements of `X` identified by index positions `I` are replaced by corresponding elements of `Y`.

<h2 class="example">Examples</h2>
```apl
      +A←⍳5
1 2 3 4 5
 
      A[2 3]←10 ⋄ A
1 10 10 4 5
 
```

The last-most element of `Y` is assigned when an index is repeated in `I`:
```apl
      A[2 2]←100 101 ⋄ A
1 101 10 4 5
```

For matrix `X`, `I` is composed of two simple integer arrays separated by the semicolon character (`;`).  The arrays select indices from the rows and columns of `X` respectively.

<h2 class="example">Examples</h2>
```apl
      +B←2 3⍴'REDSUN'
RED
SUN
 
      B[2;2]←'O' ⋄ B
RED
SON
```

For higher-rank array `X`, `I` is a series of simple integer arrays with adjacent arrays separated by a single semicolon character (`;`).  Each array selects indices from an axis of `X` taken in row-major order.

<h2 class="example">Examples</h2>
```apl
      C
11 12 13
14 15 16
 
21 22 23
24 25 26
 
      C[1;1;3]←103 ⋄ C
11 12 103
14 15  16
 
21 22  23
24 25  26
```

An indexing array may be ELIDED.  That is, if an indexing array is omitted from the `K`th axis, the indexing vector `⍳(⍴X)[K]` is implied:
```apl
      C[;1;2 3]←2 2⍴112 113 122 123 ⋄ C
11 112 113
14  15  16
 
21 122 123
24  25  26
 
      C[;;]←0 ⋄ C
0 0 0
0 0 0
 
0 0 0
0 0 0
```

## Choose Indexed Assignment

The index specification `I` is a non-simple integer array. Each item identifies a single element of `X` by a set of indices with one element per axis of `X` in row-major order.

<h2 class="example">Examples</h2>
```apl
      C
11 12 13 14
21 22 23 24
 
      C[⊂1 1]←101 ⋄ C
101 12 13 14
 21 22 23 24
 
      C[(1 2) (2 3)]←102 203 ⋄ C
101 102  13 14
 21  22 203 24
 
      C[2 2⍴(1 3)(2 4)(2 1)(1 4)]←2 2⍴103 204 201 104 ⋄ C
101 102 103 104
201  22 203 204
```

A scalar may be indexed by the enclosed empty vector:
```apl
      S
10
      S[⊂⍳0]←⊂'VECTOR' ⋄ S
 VECTOR 
      S[⊂⍳0]←5 ⋄ S
5
```

Choose Indexed Assignment may be used very effectively in conjunction with Index Generator (`⍳`) and Structural functions in order to assign into an array:
```apl
      C
11 12 13 14
21 22 23 24
 
      ⍳⍴C
1 1  1 2  1 3  1 4
2 1  2 2  2 3  2 4
 
      C[1 1⍉⍳⍴C]←1 2 ⋄ C
 1 12 13 14
21  2 23 24
 
      C[2 ¯1↑⍳⍴C]←99 ⋄ C
 1 12 13 99
21  2 23 99
```

## Reach Indexed Assignment

The index specification `I` is a non-simple integer array, each of whose items reach down to a nested element of `X`.  The items of an item of `I` are simple vectors (or scalars) forming sets of indices that index arrays at successive levels of `X` starting at the top-most level.  A set of indices has one element per axis at the respective level of nesting of `X` in row-major order.

<h2 class="example">Examples</h2>
```apl
      D←(2 3⍴⍳6)(2 2⍴'SMITH' 'JONES' 'SAM' 'BILL')
 
      D
 1 2 3   SMITH  JONES
 4 5 6   SAM    BILL
 
      ≡J←⊂2 (1 2)
¯3
 
      D[J]←⊂'WILLIAMS' ⋄ D
 1 2 3   SMITH  WILLIAMS
 4 5 6   SAM    BILL
 
      D[(1 (1 1))(2 (2 2) 1)]←10 'W' ⋄ D
 10 2 3   SMITH  WILLIAMS
  4 5 6   SAM    WILL
 
      E
 GREEN  YELLOW  RED
 
      E[⊂2 1]←'M' ⋄ E
 GREEN  MELLOW  RED
```

The context of indexing is important.  In the last example, the indexing method is determined to be Reach rather than Choose since `E` is a vector, not a matrix as would be required for Choose.  Observe that:
```apl
      ⊂2 1 ←→ ⊂(⊂2),(⊂1)
```

Note that for any array `A`, `A[⊂⍬]` represents a scalar quantity, which is the whole of `A`, so:
```apl
      A←5⍴0
      A
0 0 0 0 0
      A[⊂⍬]←1
      A
1
```

## Combined Indexed and Selective Assignment

Instead of `X` being a name, it may be a selection from a named array, and the statement is of the form `(EXP X)[I]←Y`.
```apl
      MAT←4 3⍴'Hello' 'World'
      (2↑¨MAT)[1 2;]←'#'
      MAT
 ##llo  ##rld  ##llo 
 ##rld  ##llo  ##rld 
 Hello  World  Hello 
 World  Hello  World
```
```apl
      MAT←4 3⍴'Hello' 'World'
      ⎕ML←1 ⍝ ∊ is Enlist
     (∊MAT)[2×⍳⌊0.5×⍴∊MAT]←'#'
      MAT
 H#l#o  #o#l#  H#l#o 
 #o#l#  H#l#o  #o#l# 
 H#l#o  #o#l#  H#l#o 
 #o#l#  H#l#o  #o#l# 
```
