
<!-- Hidden search keywords -->
<div style="display: none;">
  5172⌶
</div>






<h1 class="heading"><span class="name">Discard Source Code</span> <span class="command">R←5172⌶Y</span></h1>



This specifies whether source code is discarded for functions and operators when they are created by the editor or by `⎕FIX`. See also [Discard Source Information](discard-source-information.md).


`Y` is 0 or 1.


If `Y` is 0 (the default), source code is retained in the workspace when an object is fixed.


If `Y` is 1, source code is not retained in the workspace when an object is fixed (source code already retained in the workspace is not discarded).


In all case the result `R` is the previous setting (0 or 1).



For further information, see [Source as Typed](../../../../earlier-release-notes/release-notes-v19-0/introduction/source-as-typed).


