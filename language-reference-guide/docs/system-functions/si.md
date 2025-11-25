---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SI SI
</div>






<h1 class="heading"><span class="name">State Indicator</span> <span class="command">R←⎕SI</span></h1>



`R` is a nested vector of vectors giving the names of the functions or operators in the execution stack.

<h2 class="example">Example</h2>
```apl

      )SI
#.PLUS[2]*
.
#.MATDIV[4]
#.FOO[1]*
⍎

      ⎕SI
 PLUS  MATDIV  FOO

      (⍴⎕LC)=⍴⎕SI
1
```



If execution stops in a callback function, `⎕DQ` will appear on the stack, and may occur more than once
```apl
      )SI
#.ERRFN[7]*
⎕DQ
#.CALC
⎕DQ
#.MAIN
```


To edit the function on the top of the stack:
```apl
      ⎕ED ⊃⎕SI
```


The name of the function which called this one:
```apl
      ⊃1↓⎕SI
```


To check if the function `∆N` is pendent:
```apl
     ((⊂∆N)∊1↓⎕SI)/'Warning : ',∆N,' is pendent'
```


See also [Extended State Indicator](xsi.md).


