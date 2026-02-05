




<h1 class="heading"><span class="name">List Global Defined Functions</span> <span class="command">)FNS {nm}</span></h1>



This command displays the names of global defined functions in the active workspace or current namespace.  Names are displayed in [`⎕AV`](../system-functions/av.md) collation order.  If a name is included after the command, only those names starting at or after the given name in collation order are displayed.

<h2 class="example">Examples</h2>
```apl
      )FNS
ASK DISPLAY GET PUT ZILCH
      )FNS G
GET PUT ZILCH
```



