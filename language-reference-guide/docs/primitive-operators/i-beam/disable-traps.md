
<!-- Hidden search keywords -->
<div style="display: none;">
  600⌶
</div>






<h1 class="heading"><span class="name">Disable Traps</span> <span class="command">R←600⌶Y</span></h1>



This function is used to temporarily disable the error trapping mechanism used by `:Trap` and `⎕TRAP`. This can be useful in debugging applications.


`Y` is an integer 0, 1 or 2 as shown in the following table.


`R` is the previous value (0, 1, or 2) of the trap state.


|`Y`|Effect                                                                                         |
|---|-----------------------------------------------------------------------------------------------|
|`0`|Enable all traps.                                                                              |
|`1`|Disable all traps.                                                                             |
|`2`|Disable traps in suspended functions from triggering when an error is generated in the Session.|


Note that the *Disable traps in session* option of the Session *Options* menu performs the same tasks as `(600⌶0)` and `(600⌶2)`.


For  error-guards in dfns `600⌶0` and `600⌶2` are equivalent; in neither case is an error generated in the session caught by an error guard in a suspended dfn.



