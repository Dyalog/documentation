
<!-- Hidden search keywords -->
<div style="display: none;">
  2041⌶
</div>






<h1 class="heading"><span class="name">Override COM Default Value</span> <span class="command">R←{X}(2041⌶)Y</span></h1>



!!! note
    **Windows only**


Certain COM objects, for example, VT_BLOBs, cannot be represented in APL or may be in error. By default Dyalog will generate a `DOMAIN ERROR` in these cases. For COM objects of type **VT_EMPTY** the interpreter by default returns `⎕NULL`.


`2041⌶` allows the APL programmer to specify what is returned by the interpreter in these cases.



`Y` may be `1` or `2`.


If `Y` is `1`, then `X` specifies the value that is returned instead of `⎕NULL` when the COM object is of type **VT_EMPTY**.


If `Y` is `2`, then `X` specifies the value that is returned when the COM object is in error, or is of a type that cannot be represented in APL.


In both cases, omitting `X` results in the default behaviour being restored.


`R` is the previous value specified; if there was no previous value then this function will perform its task but generate a `VALUE ERROR`.


