<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FR FR
</div>






<h1 class="heading"><span class="name">Floating-Point Representation</span> <span class="command">⎕FR</span></h1>



The value of `⎕FR` determines the way that floating-point operations are performed.


If `⎕FR` is 645, all floating-point calculations are performed using IEEE 754 64-bit floating-point operations and the results of these operations are represented internally using *binary64*[^1] floating-point format.


If `⎕FR` is 1287, all floating-point calculations are performed using IEEE 754-2008 128-bit decimal floating-point operations and the results of these operations are represented internally using *decimal128*[^2] format.



Note that when you change `⎕FR`, its new value only affects subsequent floating-point operations and results. Existing floating-point values stored in the workspace remain unchanged.


The default value of `⎕FR` (its value in a `clear ws`) is configurable.


`⎕FR`  has namespace scope but may be localised. If so, like most other system variables, it inherits its initial value from the global environment.


**However:** Although `⎕FR` *can* vary, the system is *not designed* to allow "seamless" modification during the running of an application and the dynamic alteration of is not recommended.  Strange effects may occur. For example, the type of a constant contained in a line of code (in a function or class), will depend on the value of `⎕FR` *when the function is fixed*.



Also note:
```apl
      ⎕FR←1287
      x←1÷3
      
      ⎕FR←645
      x=1÷3
1
```




The decimal number has 17 more 3's. Using the tolerance which applies to binary floats (type 645), the numbers are equal. However, the "reverse" experiment yields 0, as tolerance is much narrower in the decimal universe:
```apl
      ⎕FR←645
      x←1÷3
      ⎕FR←1287
      x=1÷3
0
```



Since `⎕FR` can vary, it will be possible for a single workspace to contain floating-point values of both types (existing variables are not converted when `⎕FR` is changed). For example, an array that has just been brought into the workspace from external storage may have a different type from `⎕FR` in the current namespace. Conversion (if necessary) will only take place when a *new* floating-point array is generated as the result of "a calculation". The result of a computation returning a floating-point result will *not* depend on the type of the arrays involved in the expression: `⎕FR` at the time when a computation is performed decides the result type, alone.



Structural functions generally do NOT change the type, for example:
```apl
      ⎕FR←1287
      x←1.1 2.2 3.3
      
      ⎕FR←645
      ⎕DR x
1287
      ⎕DR 2↑x
1287
```




128-bit decimal numbers not only have greater precision (roughly 34 decimal digits); they also have significantly larger range – from `¯1E6145` to `1E6145`. Loss of precision is accepted on conversion from 645 to 1287, but the magnitude of a number may make the conversion impossible, in which case a `DOMAIN ERROR` is issued:
```apl
      ⎕FR←1287
      x←1E1000
      ⎕FR←645 ⋄ x+0
DOMAIN ERROR
```




When experimenting with `⎕FR` it is important to note that numeric constants entered into the Session are evaluated (and assigned a data type) before the line is actually executed. This means that constants are evaluated according to the value of `⎕FR` that pertained before the line was entered. For example:
```apl
      ⎕FR←645
      ⎕FR
645
 
      ⎕FR←1287 ⋄ ⎕DR 0.1
645
      ⎕DR 0.1
1287
```




WARNING: The use of COMPLEX numbers when `⎕FR` is 1287 is not recommended, because:

- any 128-bit decimal array into which a complex number is inserted or appended will be forced in its entirety into complex representation, potentially losing precision.
- All comparisons are done using `⎕DCT` when `⎕FR` is 1287, and the default value of `1E¯28` is equivalent to 0 for complex numbers.





[^1]: https://en.wikipedia.org/wiki/Double_precision_floating-point_format
[^2]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
