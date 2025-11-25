---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FERASE FERASE
</div>






<h1 class="heading"><span class="name">File Erase</span> <span class="command">{R}←X ⎕FERASE Y</span></h1>


## Access code 4


`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  `X` must be a character scalar or vector containing the name of the file associated with the tie number `Y`.  This name must be identical with the name used to tie the file (except that the directory delimiters `/` and `\` are treated as being the same) and the file must be exclusively tied.  The file named in `X` is erased and untied.


The shy result of `⎕FERASE` is the tie number of the erased file.


<h1 class="example">Examples</h1>
```apl

      'SALES'⎕FERASE 'SALES' ⎕FTIE 0

      './temp' ⎕FCREATE 1
      'temp' ⎕FERASE 1
FILE NAME ERROR
      'temp'⎕FERASE 1
      
      ⎕←'.\temp'⎕FERASE 1 ⍝ Works with / or \
1
```


