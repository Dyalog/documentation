---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NRENAME NRENAME
</div>






<h1 class="heading"><span class="name">Native File Rename</span> <span class="command">{R}←X ⎕NRENAME Y</span></h1>



`⎕NRENAME` is used to rename a native file.


`Y` is a negative integer tie number associated with a tied native file.  `X` is a simple character vector or scalar containing a valid (and unused) file name.


The shy result of `⎕NRENAME` is the tie number of the renamed file.



