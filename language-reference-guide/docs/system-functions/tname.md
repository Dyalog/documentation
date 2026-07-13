---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TNAME TNAME
</div>






# <span>Current Thread Name</span> `⎕TNAME`



The system variable `⎕TNAME` reports and sets the name of the current APL thread. This name is used to identify the thread in the Tracer.


The default value of `⎕TNAME` is an empty character vector. `⎕TNAME` has workspace scope.


You may set `⎕TNAME` to any valid character vector, but it is recommended that control characters (such as `⎕AV[⎕IO]` ) be avoided.

<h2 class="example">Example</h2>
```apl
      ⎕TNAME←'Dylan'
      ⎕TNAME
Dylan
```



