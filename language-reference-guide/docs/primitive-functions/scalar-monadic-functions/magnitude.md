




<h1 class="heading"><span class="name">Magnitude</span> <span class="command">R←|Y</span></h1>



`Y` may be any numeric array. `R` is numeric composed of the absolute (unsigned) values of `Y`.


Note that the magnitude of a complex number `(a+ib)` is defined to be `(a <sup>2</sup> +b <sup>2</sup> ) <sup>0.5</sup>`.

<h2 class="example">Examples</h2>
```apl
      |2 ¯3.4 0 ¯2.7
2 3.4 0 2.7
 
      |3j4
5
```


`⎕IO` is an implicit argument of magnitude.



