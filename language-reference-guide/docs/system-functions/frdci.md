---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRDCI FRDCI
</div>






<h1 class="heading"><span class="name">File Read Component Information</span> <span class="command">R←⎕FRDCI Y</span></h1>


## Access code 512


`Y` must be a simple integer vector of length 2 or 3 containing the file tie number, component number and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.


The result is a 3 element numeric vector containing the following information:

1. the size of the component in bytes (that is, how much disk space it occupies).
2. the user number of the user who last updated the component.
3. the time of the last update in 60ths of a second since 1st January 1970 (UTC).

<h2 class="example">Example</h2>
```apl
      ⎕FRDCI 1 13
2200 207 3.702094494E10
```



