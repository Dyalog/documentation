---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLEAR CLEAR
</div>






<h1 class="heading"><span class="name">Clear Workspace</span> <span class="command">⎕CLEAR</span></h1>



A clear workspace is activated, having the name `CLEAR WS`.  The active workspace is lost.  All system variables assume their default values.  The maximum size of workspace is available.


Apart from .NET objects, the contents of the session namespace `⎕SE` are not affected. .NET objects in `⎕SE` are disconnected from .NET because `⎕CLEAR` closes the current .NET AppDomain.

<h2 class="example">Example</h2>
```apl

      ⎕CLEAR
      ⎕WSID
CLEAR WS
```



