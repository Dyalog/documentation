<div style="display: none;">
  ≡
</div>

<h1 class="heading"><span class="name">Depth</span> <span class="command">(⎕ML) R←≡Y</span></h1>

`Y` may be any array. `R` is the maximum number of levels of nesting of `Y`. A simple scalar (rank-0 number, character or namespace-reference) has a depth of 0.

A higher rank array, all of whose items are simple scalars, is termed a *simple array* and has a depth of 1. An array whose items are not all simple scalars is *nested* and has a depth 1 greater than that of its most deeply nested item.

`Y` is of *uniform depth* if it is simple or if all of its items have the same uniform depth.

If `⎕ML<2` and `Y` is not of uniform depth then `R` is negated (therefore, when `⎕ML<2`, a negative value of `R` indicates non-uniform depth).

<h2 class="example">Examples</h2>
```apl
      ≡1
0
      ≡'A'
0
      ≡'ABC'
1
      ≡1 'A'
1 

```
```apl
      ⎕ML←0
 
      ≡A←(1 2)(3 (4 5)) ⍝ Non-uniform array
¯3
      ≡¨A          ⍝ A[1] is uniform, A[2] is non-uniform
1 ¯2
      ≡¨¨A
 0 0  0 1 

```
```apl
      ⎕ML←2
 
      ≡A
3
      ≡¨A
1 2
      ≡¨¨A
 0 0  0 1
```


