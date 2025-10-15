<div style="display: none;">
  ←
</div>






<h1 class="heading"><span class="name">Axis (with Dyadic Operand)</span> <span class="command">R←Xf[B]Y</span></h1>



`f` must be a dyadic primitive scalar function, or a dyadic primitive mixed function taken from [](#DyadicMixed) below. `B` must be a numeric scalar or vector. `X` and `Y` may be any arrays whose items are appropriate to function `f`. Axis does not follow the normal syntax of an operator.



Table: Primitive dyadic mixed functions with optional axis. {: #DyadicMixed }


|Function|Name|Range of B|
|---|---|---|
|`/ or ⌿`|Replicate|`B∊⍳⍴⍴Y`|
|`\ or ⍀`|Expand|`B∊⍳⍴⍴Y`|
|`⊂`|Partitioned Enclose|`B∊⍳⍴⍴Y`|
|`⌽ or ⊖`|Rotate|`B∊⍳⍴⍴Y`|
|`, or ⍪`|Catenate|`B∊⍳⍴⍴Y`|
|`, or ⍪`|Laminate|`(0≠1|B)^(B>⎕IO-1)^(B<⎕IO+(⍴⍴X)⌈⍴⍴Y)`|
|`↑`|Take|one or more axes of `Y`|
|`↓`|Drop|one or more axes of `Y`|
|`⌷`|Index|one or more axes of `Y`|


In most cases, `B` must be an integer value identifying the axis of `X` and `Y` along which function `f` is to be applied.


Exceptionally, `B` must be a fractional value for the Laminate function (`,`) whose upper and lower integer bounds identify a pair of axes or an extreme axis of `X` and `Y`. For Take (`↑`) and Drop (`↓`), `B` can be a **vector** of two or more axes.


`⎕IO` is an implicit argument of the derived function which determines the meaning of `B`.

<h2 class="example">Examples</h2>
```apl
      1 4 5 =[1] 3 2⍴⍳6
1 0
0 1
1 0
 
      2 ¯2 1/[2]2 3⍴'ABCDEF'
AA  C
DD  F
 
      'ABC',[1.1]'='
A=
B=
C=
 
      'ABC',[0.1]'='
ABC
===
 
      ⎕IO←O
 
      'ABC',[¯0.5]'='
ABC
===
```

## Axis with Scalar Dyadic Functions


The axis operator `[X]` can take a scalar dyadic function as operand. This has the effect of "stretching" a lower rank array to fit a higher rank one. The arguments must be conformable along the specified axis (or axes) with elements of the lower rank array being replicated along the other axes.


For example, if `H` is the higher rank array, `L` the lower rank one, `X` is an axis specification, and `f` a scalar dyadic function, then the expressions `Hf[X]L` and `Lf[X]H` are conformable if `(⍴L)←→(⍴H)[X]`. Each element of L is replicated along the remaining `(⍴H)~X` axes of `H`.


In the special case where both arguments have the same rank, the right one will play the role of the higher rank array. If `R` is the right argument, `L` the left argument, `X` is an axis specification and `f` a scalar dyadic function, then the expression `Lf[X]R` is conformable if `(⍴L)←→(⍴R)[X]`.

<h2 class="example">Examples</h2>
```apl
      mat
10 20 30
40 50 60
 
      mat+[1]1 2       ⍝ add along first axis
11 21 31
42 52 62
 
      mat+[2]1 2 3     ⍝ add along last axis
11 22 33
41 52 63
 
      cube
 100  200  300
 400  500  600
              
 700  800  900
1000 1100 1200
 
      cube+[1]1 2 
 101  201  301
 401  501  601
              
 702  802  902
1002 1102 1202
 
      cube+[3]1 2 3
 101  202  303
 401  502  603
              
 701  802  903
1001 1102 1203
 
      cube+[2 3]mat
 110  220  330
 440  550  660
              
 710  820  930
1040 1150 1260
 

```
```apl
      cube+[1 3]mat
 110  220  330
 410  520  630
              
 740  850  960
1040 1150 1260
```


