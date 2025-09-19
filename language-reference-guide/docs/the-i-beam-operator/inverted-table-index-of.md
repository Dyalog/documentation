
<!-- Hidden search keywords -->
<div style="display: none;">
  8⌶
</div>






<h1 class="heading"><span class="name">Inverted Table Index-of</span> <span class="command">R←X(8⌶)Y</span></h1>



This function computes `X` index-of `Y` (viz. `X⍳Y`) where `X` and `Y` are compatible inverted tables. `R` is the indices of `Y` in `X`.


An inverted table is a (nested) vector all of whose items have the same number of major cells. That is, `1=⍴⍴⍵` and `(≢⊃⍵)=≢¨⍵`. An inverted table representation of relational data is more efficient in time and space than other representations.



The following is an example of an inverted table:
```apl
      X←(10 3⍴⎕A) (⍳10) 'metalepsis'
      X
┌───┬───────────────────┬──────────┐
│ABC│0 1 2 3 4 5 6 7 8 9│metalepsis│
│DEF│                   │          │
│GHI│                   │          │
│JKL│                   │          │
│MNO│                   │          │
│PQR│                   │          │
│STU│                   │          │
│VWX│                   │          │
│YZA│                   │          │
│BCD│                   │          │
└───┴───────────────────┴──────────┘
```


Using inverted tables, it is often necessary to perform a table look-up to find the "row" indices of one in another. Suppose there is a second table `Y`:
```apl

      Y←(⊂⊂3 1 4 1 5 9)⌷¨X
      Y
 GHI  3 1 4 1 5 9  tmamli 
 ABC                      
 JKL                      
 ABC                      
 MNO                      
 YZA  
```



To compute the indices of   `Y` in `X`  using dyadic `⍳`, it is necessary to first un-invert each of the tables in order to create nested matrices that `⍳` can handle.
```apl
      unvert ← {⍉↑⊂⍤¯1¨⍵}
      unvert X
┌───┬─┬─┐
│ABC│0│m│
├───┼─┼─┤
│DEF│1│e│
├───┼─┼─┤
│GHI│2│t│
├───┼─┼─┤
│JKL│3│a│
├───┼─┼─┤
│MNO│4│l│
├───┼─┼─┤
│PQR│5│e│
├───┼─┼─┤
│STU│6│p│
├───┼─┼─┤
│VWX│7│s│
├───┼─┼─┤
│YZA│8│i│
├───┼─┼─┤
│BCD│9│s│
└───┴─┴─┘

      (unvert X) ⍳ (unvert Y)
3 1 4 1 5 9
```




Each un-inverted table requires considerably more workspace than its inverted form, so if the inverted tables are large, this operation is potentially expensive in terms of both time and workspace.


`8⌶` is an optimised version of the above expression.
```apl
      X (8⌶) Y
3 1 4 1 5 9
```



