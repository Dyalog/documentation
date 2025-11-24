---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NEXISTS NEXISTS
</div>






<h1 class="heading"><span class="name">Native File Exists</span> <span class="command">R←⎕NEXISTS Y</span></h1>



This function reports whether or not files and directories exist.


`Y` is a character vector or scalar containing a single file/directory name, or a vector of character vectors containing zero or more file/directory names.


If `Y` specifies a single name, the result `R` is a scalar 1 if a file or directory exists or 0 if not. If `Y` is a vector of character vectors, `R` is a vector of 1s and 0s with the same length as `Y`.



## Variant Options


`⎕NEXISTS` may be applied using the  Variant operator with the Wildcard option.

## Wildcard Option (Boolean)


|---|---|
|0|The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|


If the Wildcard option is 1, `R` indicates whether or not one or more matches to the corresponding pattern in `Y` exist.


<h2 class="example">Example</h2>
```apl

      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
1
      ⎕NEXISTS'/Users/Pete/Documents/temp/t1/t2'
1
      ⎕NEXISTS'/Users/Pete/Documents/temp/t1/t2/pd'
0

      ⊢⎕MKDIR'temp1' 'temp2'
1 1
      ⎕NEXISTS 'temp1' 'temp2' 'temp3'
1 1 0
      (⎕NEXISTS⍠1) 't*'
1

```

!!! note
    If `Y` is a symbolic link, `⎕NEXISTS` will return 1 whether or not the target of the symbolic link exists.


