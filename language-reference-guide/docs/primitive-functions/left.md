<div style="display: none;">
  ⊣
</div>






<h1 class="heading"><span class="name">Left</span> <span class="command">R←X⊣Y</span></h1>



`X` and `Y` may be any arrays.


The result `R` is the left argument `X`.

<h2 class="example">Example</h2>
```apl
      42⊣'abc' 1 2 3
42
```


Note that when `⊣` is applied using reduction, the derived function selects the first sub-array of the array along the specified dimension. This is implemented as an idiom.


<h2 class="example">Examples</h2>
```apl
      ⊣/1 2 3
1
 
      mat←↑'scent' 'canoe' 'arson' 'rouse' 'fleet'
      ⊣⌿mat  ⍝ first row                          
scent
      ⊣/mat  ⍝ first column                       
scarf
```
```apl
      ⊣/[2]2 3 4⍴⍳24 ⍝ first row from each plane
 1  2  3  4
13 14 15 16
```


Similarly, with expansion:
```apl
      ⊣\mat
sssss
ccccc
aaaaa
rrrrr
fffff
      ⊣⍀mat
scent
scent
scent
scent
scent
```


