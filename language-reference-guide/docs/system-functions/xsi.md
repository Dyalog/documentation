<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XSI XSI
</div>






<h1 class="heading"><span class="name">Extended State Indicator</span> <span class="command">R←⎕XSI</span></h1>



`R` is a nested vector of character vectors giving the full path names of the functions or operators in the execution stack. Note that if a function has changed space, its original (home) space is reported, rather than its current one.


<h2 class="example">Example</h2>


In the following, function `foo` in namespace `x` has called `goo` in namespace `y`.  Function `goo` has then changed space (`⎕CS`) to namespace `z` where it has been suspended:
```apl
 
      )SI
[z] y.goo[2]*
x.foo[1]
 
```



`⎕XSI` reports the full path name of each function:
```apl
       ⎕XSI
 #.y.goo  #.x.foo
```


This can be used for example, to edit all functions in the stack, irrespective of the current namespace by typing:    `⎕ED ⎕XSI`


See also [State Indicator](si.md).



