---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NXLATE NXLATE
</div>






<h1 class="heading"><span class="name">Native File Translate</span> <span class="command">{R}←{X}⎕NXLATE Y</span></h1>



This associates a character translation vector with a native file or, if `Y` is 0, with the use by `⎕DR`.


A translate vector is a 256-element vector of integers from 0-255. Each element maps the corresponding `⎕AV` position onto an ANSI character code.


For example, to map `⎕AV[17+⎕IO]` onto ANSI 'a' (code 97), element 17 of the translate vector is set to 97.


`⎕NXLATE` is a non-Unicode (Classic Edition) feature and is retained in the Unicode Edition only for compatibility.



`Y` is either a negative integer tie number associated with a tied native file or 0.  If `Y` is negative, monadic `⎕NXLATE` returns the current translation vector associated with the corresponding native file. If specified, the left argument `X` is a 256-element vector of integers that specifies a new translate vector.  In this case, the old translate vector is returned as a shy result.  If `Y` is 0, it refers to the translate vector used by `⎕DR` to convert to and from character data.


The system treats a translate vector with value `(⍳256)-⎕IO` as meaning *no translation* and thus provides raw input/output bypassing the whole translation process.


The default translation vector established at `⎕NTIE` or `⎕NCREATE` time  is derived from the mapping defined in the current output translation table (normally WIN.DOT) and maps alphabetic, numeric and most other characters in `⎕AV`  to their corresponding ANSI positions. However, some characters are not resolved  by this process and it is recommended that users define translate vectors to cover all cases.

## Unicode Edition


`⎕NXLATE` is relevant in the Unicode Edition only to process Native Files that contain characters expressed as indices into `⎕AV`, such as files written by the Classic Edition.


In the Unicode Edition, when reading data from a Native File using conversion code 82, incoming bytes are translated first to `⎕AV` indices using the translation table specified by `⎕NXLATE`, and then to type 80, 160 or 320 using `⎕AVU`. When writing data to a Native File using conversion code 82, characters are converted using these two translation tables in reverse.


