---
search:
  boost: 2
---

# <span>File Name Parts</span> `R←⎕NPARTS Y`{{key}}

Splits a file or directory name into its constituent parts.

To normalise the names before splitting them, use [dyadic `⎕NPARTS`](nparts-dyadic.md).

`Y` is a character vector or scalar containing a single name, or a vector of character vectors containing zero or more names. Names must conform to the file-naming rules of the host Operating System.

The file(s) need not exist; indeed this system function makes no attempt to identify or locate it/them.

If `Y` is a scalar or vector, the result `R` is a 3-element vector of character vectors as follows:

|-----|-----------|
|`[1]`|*path*     |
|`[2]`|*base name*|
|`[3]`|*extension*|

The *path* identifies the directory in which the file exists.

The *base name* is the name of the file stripped of its path and extension, if any.

The *extension* is the file extension including the leading ".".

If `Y` is a vector of character vectors, `R` is a vector of 3-element character vectors and is the same length as `Y`.

<h2 class="example">Examples</h2>

Note that `⊃1 ⎕NPARTS ''` returns the current working directory.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NPARTS NPARTS
</div>
