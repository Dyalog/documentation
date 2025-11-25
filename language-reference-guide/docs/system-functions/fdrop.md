---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FDROP FDROP
</div>






<h1 class="heading"><span class="name">File Drop Component</span> <span class="command">{R}←⎕FDROP Y</span></h1>


## Access code 32


`Y` must be a simple integer vector of length 2 or 3 whose elements are:


|---|---|
|`[1]`|a file tie number|
|`[2]`|a number specifying the position and number of components to be dropped.  A positive value indicates that components are to be removed from the beginning of the file; a negative value indicates that components are to be removed from the end of the file|
|`[3]`|an optional passnumber which if omitted is assumed to be zero|



The shy result of a `⎕FDROP` is a vector of the numbers of the dropped components. This is analogous to `⎕FAPPEND` in that the result is potentially useful for updating some sort of dictionary:
```apl
      cnos,←vec ⎕FAPPEND¨tie ⍝ Append index to dictionary
      
      cnos~←⎕FDROP tie,-⍴vec ⍝ Remove index from dict.
```


Note that the result vector, though potentially large, is generated only on request.

<h1 class="example">Examples</h1>
```apl
      ⎕FSIZE 1
1 21 5436 4294967295
 
      ⎕FDROP 1 3 ⋄ ⎕FSIZE 1
4 21 5436 4294967295
 
      ⎕FDROP 1 ¯2 ⋄ ⎕FSIZE 1
4 19 5436 4294967295
 
```


