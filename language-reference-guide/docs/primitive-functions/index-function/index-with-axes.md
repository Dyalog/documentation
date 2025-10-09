<div style="display: none;">
  ⌷
</div>






<h1 class="heading"><span class="name">Index with Axes</span> <span class="command">R←{X}⌷[K]Y</span></h1>



`X` must be a scalar or vector of depth `≤2`, of integers each `≥⎕IO`. `Y` may be any array. `K` is a simple scalar or vector specifying axes of `Y`. The length of `K` must be the same as the length of `X`:
```apl
      (⍴,X) ≡ ⍴,K
```


In general, the result `R` is similar to that obtained by square-bracket indexing with elided subscripts. Items of `K` distribute items of `X` along the axes of `Y`. For example:
```apl
      I J ⌷[1 3] Y  ←→  Y[I;;J] 
```


Note that index with axis may be used with selective specification. `⎕IO` is an implicit argument of index with axis.


<h2 class="example">Examples</h2>
```apl
     ⎕IO←1
 
     ⎕←CUBE←10⊥¨⍳2 3 4
111 112 113 114
121 122 123 124
131 132 133 134
               
211 212 213 214
221 222 223 224
231 232 233 234
 
      2⌷[1]CUBE
211 212 213 214
221 222 223 224
231 232 233 234
 
      2⌷[3]CUBE
112 122 132
212 222 232
 
      CUBE[;;2] ≡ 2⌷[3]CUBE
1
      (1 3)4⌷[2 3]CUBE
114 134
214 234
 
      CUBE[;1 3;4] ≡ (1 3)4⌷[2 3]CUBE
1
      
```
```apl
      (2(1 3)⌷[1 3]CUBE)←0 ⋄ CUBE ⍝ Selective assignment.
111 112 113 114
121 122 123 124
131 132 133 134
               
  0 212   0 214
  0 222   0 224
  0 232   0 234
```


