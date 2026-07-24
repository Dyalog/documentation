---
search:
  boost: 2
---

# <span>Native File Untie</span> `{R}←⎕NUNTIE Y`{{key}}

This closes one or more native files.  `Y` is a scalar or vector of negative integer tie numbers.  The files associated with elements of `Y` are closed.  Native file untie with a zero length argument (`⎕NUNTIE ⍬`) flushes all file buffers to disk - see [File Untie](funtie.md) for more explanation.

The shy result of `⎕NUNTIE` is a vector of tie numbers of the files **actually untied**.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NUNTIE NUNTIE
</div>
