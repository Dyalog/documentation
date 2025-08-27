<div style="display: none;">
  ÷
</div>






<h1 class="heading"><span class="name">Divide</span> <span class="command">R←X÷Y</span></h1>



`Y` must be a numeric array.  `X` must be a numeric array.  `R` is the numeric array resulting from `X` divided by `Y`.  System variable `⎕DIV` is an implicit argument of Divide.


If `⎕DIV=0` and `Y=0` then if `X=0`, the result of `X÷Y` is 1; if `X≠0` then `X÷Y` is a `DOMAIN ERROR.`


If `⎕DIV=1` and `Y=0`, the result of `X÷Y` is `0` for all values of `X`.

<h2 class="example">Examples</h2>
```apl
      2 0 5÷4 0 2
0.5 1 2.5
 
      3j1 2.5 4j5÷2 1j1 .2
1.5J0.5 1.25J¯1.25 20J25
 
      ⎕DIV←1
      2 0 5÷4 0 0
0.5 0 0
```



