<div style="display: none;">
  ⊃
</div>






<h1 class="heading"><span class="name">Pick</span> <span class="command">R←X⊃Y</span></h1>



`Y` may be any array.


`X` is a scalar or vector of indices of `Y`.


`R` is an item selected from the structure of `Y` according to `X`.


Elements of `X` select from successively deeper levels in the structure of `Y`.  The items of `X` are simple integer scalars or vectors which identify a set of indices, one per axis at the particular level of nesting of `Y` in row-major order.  Simple scalar items in `Y` may be picked by empty vector items in `X` to any arbitrary depth.


`⎕IO` is an implicit argument of Pick.


<h2 class="example">Examples</h2>
```apl
      G←('ABC' 1)('DEF' 2)('GHI' 3)('JKL' 4)
 
      G←2 3⍴G,('MNO' 5)('PQR' 6)
 
      G
  ABC  1   DEF  2   GHI  3
  JKL  4   MNO  5   PQR  6

```
```apl
    ((⊂2 1),1)⊃G
JKL
 
      (⊂2 1)⊃G
 JKL  4

      ((2 1)1 2)⊃G
K
 
      (5⍴⊂⍳0)⊃10
10

```


