---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WSID WSID
</div>






<h1 class="heading"><span class="name">Workspace Identification</span> <span class="command">⎕WSID</span></h1>



This is a simple character vector.  It contains the identification name of the active workspace.  If a new name is assigned, that name becomes the identification name of the active workspace, provided that it is a correctly formed name.


See [ Workspaces](../../../programming-reference-guide/introduction/workspaces) for workspace naming conventions.


It is useful, though not essential, to associate workspaces with a specific directory in order to distinguish workspaces from other files.


The value of `⎕WSID` in a clear workspace is `'CLEAR WS'`. `⎕WSID` has workspace scope.


<h2 class="example">Example</h2>
```apl

      ⎕WSID
CLEAR WS

      ⎕WSID←'ws/mywork       (UNIX)

      ⎕WSID←'B:\WS\MYWORK'   (Windows)

```


