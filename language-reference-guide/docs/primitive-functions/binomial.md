<div style="display: none;">
  !
</div>






<h1 class="heading"><span class="name">Binomial</span> <span class="command">R←X!Y</span></h1>



`X` and `Y` may be any numbers except that if `Y` is a negative integer then `X` must be an integer. `R` is numeric. An element of `R` is integer if corresponding elements of `X` and `Y` are integers.


Binomial is defined in terms of the function Factorial:
```apl
      X!Y ←→ (!Y)÷(!X)×!Y-X
```


Results are derived smoothly from the Beta function:
```apl
      Beta(X,Y) ←→ ÷Y×(X-1)!X+Y-1
```


For positive integer arguments, `R` is the number of selections of `X` things from `Y` things.

<h2 class="example">Example</h2>
```apl
      1 1.2 1.4 1.6 1.8 2!5
5 6.105689248 7.219424686 8.281104786 9.227916704 10
 
      2!3j2
1J5
```



