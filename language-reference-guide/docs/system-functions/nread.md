---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NREAD NREAD
</div>






<h1 class="heading"><span class="name">Native File Read</span> <span class="command">R←⎕NREAD Y</span></h1>



This monadic function reads data from a native file. `Y` is a 3- or 4-element integer vector whose elements are as follows:


|---|---|
|`[1]`|negative tie number,|
|`[2]`|conversion code (see below),|
|`[3]`|count. If this value is `¯1` , all of the elements defined by `Y[2]` are read from the position specified by `Y[4]` to the end of the file. This may result in the last few bytes in the file being ignored if they do not form a complete element.|
|`[4]`|start byte, counting from 0. If this value omitted or is `¯1` , data is read starting from the current position in the file (initially `0` ).|


## Notes


`8 ⎕NINFO ⊃Y` can be used to report the current position of the file pointer.


`Y[2]` specifies conversion to an APL internal form as follows. Note that the internal formats for character arrays differ between the Unicode and Classic Editions.


If both `Y[3]` and `Y[4]` have the value `¯1`, then `⎕NREAD` reads data from the current position in the file to the end of the file.


`⎕NREAD` can be used with any file. However, calling `⎕NREAD` with at least one of `Y[3 4]` set to `¯1` is intended for regular files only; using on pipes, FIFOs or other special types of file is not recommended.



Table: Unicode Edition: Conversion Codes


|Value  |Number of bytes read|Result Type      |Result shape|
|-------|--------------------|-----------------|------------|
|11     |count               |1 bit Boolean    |8 `×` count |
|80     |count               |8 bits character |count       |
|82 [^1]|count               |8 bits character |count       |
|83     |count               |8 bits integer   |count       |
|160    |2 `×` count         |16-bits character|count       |
|163    |2 `×` count         |16 bits integer  |count       |
|320    |4 `×` count         |32-bits character|count       |
|323    |4 `×` count         |32 bits integer  |count       |
|645    |8 `×` count         |64 bits floating |count       |
|1287   |16 `×` count        |128 bits decimal |count       |
|1289   |16 `×` count        |128 bits complex |count       |




Table: Classic Edition: Conversion Codes


|Value|Number of bytes read|Result Type     |Result shape|
|-----|--------------------|----------------|------------|
|11   |count               |1 bit Boolean   |8 `×` count |
|82   |count               |8 bits character|count       |
|83   |count               |8 bits integer  |count       |
|163  |2 `×` count         |16 bits integer |count       |
|323  |4 `×` count         |32 bits integer |count       |
|645  |8 `×` count         |64 bits floating|count       |
|1287 |16 `×` count        |128 bits decimal|count       |
|1289 |16 `×` count        |128 bits complex|count       |


<h2 class="example">Example</h2>
```apl

      DATA←⎕NREAD ¯1 160 (0.5×⎕NSIZE ¯1) 0 ⍝ Unicode
      DATA←⎕NREAD ¯1 82 (⎕NSIZE ¯1) 0      ⍝ Classic
      DATA←⎕NREAD ¯1 82 ¯1 0       ⍝ Shorter version

```




[^1]: Conversion code 82 is permitted in the Unicode Edition for compatibility and causes 1-byte data on file to be translated (according to ⎕NXLATE ) from ⎕AV indices into normal (Unicode) characters of type 80, 160 or 320.