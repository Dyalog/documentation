<div style="display: none;">
  ←
</div>

<h1 class="heading"><span class="name">Indexing</span> <span class="command">R←X[Y]</span></h1>

`X` may be  any array. `Y` must be a valid index specification. `R` is an array composed of elements indexed from `X` and the shape of `R` is determined by the index specification.

This form of Indexing, using brackets, does not follow the normal syntax of a dyadic function. For an alternative method of indexing, see [Index](../primitive-functions/index-function/index.md).

`⎕IO` is an implicit argument of Indexing.

Three forms of indexing are permitted. The form used is determined by context.

## Simple Indexing

For vector `X`, `Y` is a simple integer array composed of items from the set `⍳⍴X`.


`R` consists of elements selected according to index positions in `Y`. `R` has the same shape as `Y`.

<h2 class="example">Examples</h2>
```apl
      A←10 20 30 40 50
 
      A[2 3⍴1 1 1 2 2 2]
10 10 10
20 20 20
 
      A[3]
30
 
      'ONE' 'TWO' 'THREE'[2]
 TWO
```


For matrix `X`, `Y` is composed of two simple integer arrays separated by the semicolon character (`;`). The arrays select indices from the rows and columns of `X` respectively.

<h2 class="example">Examples</h2>
```apl
      +M←2 4⍴10×⍳8
10 20 30 40
50 60 70 80
 
      M[2;3]
70
```


For higher-rank array `X`, `Y` is composed of a simple integer array for each axis of `X` with adjacent arrays separated by a single semicolon character (`;`). The arrays select indices from the respective axes of `X`, taken in row-major order.

<h2 class="example">Examples</h2>
```apl
      ⊢A←2 3 4⍴10×⍳24
 10  20  30  40
 50  60  70  80
 90 100 110 120
 
130 140 150 160
170 180 190 200
210 220 230 240
 
      A[1;1;1]
10
 
      A[2;3 2;4 1]
240 210
200 170
```


If an indexing array is omitted for the `K`th axis, the index vector `⍳(⍴X)[K]` is assumed for that axis.

<h2 class="example">Examples</h2>
```apl
      A[;2;]
 50  60  70  80
170 180 190 200
 
      M
10 20 30 40
50 60 70 80
 
      M[;]
10 20 30 40
50 60 70 80
 
      M[1;]
10 20 30 40
 
      M[;1]
10 50
```

## Choose Indexing


The index specification `Y` is a non-simple array. Each item identifies a single element of `X` by a set of indices with one element per axis of `X` in row-major order.

<h2 class="example">Examples</h2>
```apl
      M
10 20 30 40
50 60 70 80
 
      M[⊂1 2]
20
 
      M[2 2⍴⊂2 4]
80 80
80 80
 
      M[(2 1)(1 2)]
50 20
```


A scalar may be indexed by the enclosed empty vector:
```apl
      S←'Z'
      S[3⍴⊂⍳0]
ZZZ
```


Simple and Choose indexing are indistinguishable for vector `X`:
```apl
      V←10 20 30 40
 
      V[⊂2]
20
      ⊂2
2
      V[2]
20
```

## Reach Indexing

The index specification `Y` is a non-simple integer array, each of whose items reach down to a nested element of `X`. The items of an item of `Y` are simple vectors (or scalars) forming sets of indices that index arrays at successive levels of `X` starting at the top-most level. A set of indices has one element per axis at the respective level of nesting of `X` in row-major order.

<h2 class="example">Examples</h2>
```apl
      G←('ABC' 1)('DEF' 2)('GHI' 3)('JKL' 4)
      G←2 3⍴G,('MNO' 5)('PQR' 6)
      G
  ABC  1   DEF  2   GHI  3
  JKL  4   MNO  5   PQR  6
 
      G[((1 2)1)((2 3)2)]
 DEF  6
 
      G[2 2⍴⊂(2 2)2]
5 5
5 5
      G[⊂⊂1 1]
  ABC  1
 
      G[⊂1 1]
  ABC  1
 
      V←,G
 
      V[⊂⊂1]
  ABC  1
 
      V[⊂1]
  ABC  1
 
      V[1]
  ABC  1
```

## Indexing  Classes

If `Y` is a ref to an instance of a Class with a Default property, indexing is applied to the Default property. Similarly, indexing applied to a .NET collection returns the appropriate item(s) of the collection.

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
      c[2;3;]
UVWX
```
