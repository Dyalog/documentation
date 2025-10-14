
<!-- Hidden search keywords -->
<div style="display: none;">
  2035⌶
</div>






<h1 class="heading"><span class="name">Set Dyalog Pixel Type</span> <span class="command">R←2035⌶Y</span></h1>



!!! note
    **Windows only**


Determines how Coord `'Pixel'` is interpreted. This is determined initially by the value of the DYALOG_PIXEL_TYPE parameter and, when altered by this function,  applies to all subsequent GUI operations.


`Y` is a character vector that is either `'ScaledPixel'` or `'RealPixel'`. Any other value will cause a `DOMAIN ERROR`.


The result `R` is the previous value.


<h2 class="example">Example</h2>
```apl
      2035⌶'ScaledPixel'
RealPixel
      2035⌶'RealPixel'
ScaledPixel

      2035⌶'realpixel'
DOMAIN ERROR
      2035⌶'realpixel'
     ∧

```


