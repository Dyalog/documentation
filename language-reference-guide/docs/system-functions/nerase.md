---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NERASE NERASE
</div>







# <span>Native File Erase</span> `{R}←X ⎕NERASE Y`{{key}}



This function erases (deletes) a tied native file.  `Y` is a negative integer tie number associated with a tied native file.  `X` is a simple character vector or scalar containing the name of the same file and must be **identical** to the name used when it was opened by `⎕NCREATE` or `⎕NTIE`.


The shy result of `⎕NERASE` is the tie number that the erased file had.

<h2 class="example">Example</h2>
```apl
      file ⎕NERASE file ⎕NTIE 0
```




