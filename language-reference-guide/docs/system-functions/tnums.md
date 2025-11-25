---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TNUMS TNUMS
</div>






<h1 class="heading"><span class="name">Thread Numbers</span> <span class="command">R←⎕TNUMS</span></h1>



`⎕TNUMS` reports the numbers of all current threads.


`R` is a simple integer vector of the base thread and all its living descendants.

<h2 class="example">Example</h2>
```apl
      ⎕TNUMS
0 2 4 5 6 3 7 8 9
```



