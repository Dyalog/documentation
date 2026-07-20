---
search:
  boost: 2
---

# <span>File Size</span> `R←⎕FSIZE Y`{{key}}

`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The result is a 4 element numeric vector containing the following:

|Element|Description                                                                        |
|-------|-----------------------------------------------------------------------------------|
|1      |the number of first component                                                      |
|2      |1 + the number of the last component, (that is, the result of the next `⎕FAPPEND` )|
|3      |the current size of the file in bytes                                              |
|4      |the file size limit in bytes                                                       |

<h2 class="example">Example</h2>
```apl
      ⎕FSIZE 1
1 21 65271 4294967295
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FSIZE FSIZE
</div>
