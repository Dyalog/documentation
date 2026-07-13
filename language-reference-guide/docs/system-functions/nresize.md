---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NRESIZE NRESIZE
</div>






# <span>Native File Resize</span> `{R}←X ⎕NRESIZE Y`{{key}}



This function changes the size of a native file.


`Y` is a negative integer tie number associated with a tied native file.


`X` is a single integer value that specifies the new size of the file in bytes.  If `X` is smaller than the current file size, the file is truncated.  If `X` is larger than the current file size, the file is extended and the value of additional bytes is undefined.


The shy result of `⎕NRESIZE` is the tie number of the resized file.



