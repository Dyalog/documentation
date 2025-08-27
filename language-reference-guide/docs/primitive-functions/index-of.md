<div style="display: none;">
  ⍳
</div>






<h1 class="heading"><span class="name">Index Of</span> <span class="command">R←X⍳Y</span></h1>



`Y` may be any array. `X` may be any array of rank 1 or more.


In general, the function locates the first occurrence of sub-arrays in `Y` which match major cells of  `X`, where a major cell is  a sub-array on the leading dimension of `X` with shape `1↓⍴X`. The shape of the result `R` is `(1-⍴⍴X)↓⍴Y`.


If a sub-array of `Y` cannot be found in `X`, then the corresponding element of `R` will be `⎕IO+⊃⍴X`.


In particular, if `X` is a vector, the result `R` is a simple integer array with the same shape as `Y` identifying where elements of `Y` are first found in `X`. If an element of `Y` cannot be found in `X`, then the corresponding element of `R` will be `⎕IO+⊃⍴X`.


Elements of `X` and `Y` are considered the same if `X≡Y` returns 1 for those elements.


`⎕IO`,  `⎕CT` and `⎕DCT` are implicit arguments of Index Of.


<h2 class="example">Examples</h2>
```apl
      ⎕IO←1
 
      2 4 3 1 4⍳1 2 3 4 5
4 1 3 2 6
 
      'CAT' 'DOG' 'MOUSE'⍳'DOG' 'BIRD'
2 4
```
```apl
      X←3 4⍴⍳12
```
```apl

      X
1  2  3  4
5  6  7  8
9 10 11 12
```
```apl

      X⍳1 2 3 4
1

```
```apl

      Y←2 4⍴1 2 3 4 9 10 11 12
      Y
1  2  3  4
9 10 11 12

      X⍳Y
1 3
      X⍳2 3 4 1
4

```
```apl
      X1←10 100 1000∘.+X
      X1
  11   12   13   14
  15   16   17   18
  19   20   21   22
                   
 101  102  103  104
 105  106  107  108
 109  110  111  112
                   
1001 1002 1003 1004
1005 1006 1007 1008
1009 1010 1011 1012

```
```apl
      X1⍳100 1000∘.+X
2 3
```
```apl
      x
United Kingdom
Germany       
France        
Italy         
United States 
Canada        
Japan         
Canada        
France        
      y
United Kingdom
Germany       
France        
Italy         
USA           
              
Canada        
Japan         
China         
India         
Deutschland   

```
```apl
      ⍴x
9 14
      ⍴y
2 5 14
      x⍳y
1 2  3  4 10
6 7 10 10 10

      x⍳x
1 2 3 4 5 6 7 6 3

```



Note that the expression `y⍳x` signals a `LENGTH ERROR` because it looks for major cells in the left argument, whose shape is `5 14` (that is `1↓⍴y`), which is not the same as the trailing shape of `x`.
```apl

      y⍳x
LENGTH ERROR
      y⍳x
     ∧
```


For performance information, see [Programmer's Guide: "Search Functions and Hash Tables"](../../../programming-reference-guide/introduction/search-functions-and-hash).



