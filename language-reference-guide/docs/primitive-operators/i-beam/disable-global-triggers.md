
<!-- Hidden search keywords -->
<div style="display: none;">
  2007⌶
</div>






<h1 class="heading"><span class="name">Disable Global Triggers</span> <span class="command">R←2007⌶Y</span></h1>



This function is used to temporarily disable and re-enable [Global Triggers](../../../../programming-reference-guide/triggers/global-triggers).


`Y` is Boolean.


`R` is the previous value setting.


|`Y`|Effect                  |
|---|------------------------|
|`0`|Enable Global Triggers. |
|`1`|Disable Global Triggers.|


This function has effect only in the current thread and its effect is immediate. If there are pending triggers when triggers are disabled, those pending will be queued and fired when triggers are re-enabled.



