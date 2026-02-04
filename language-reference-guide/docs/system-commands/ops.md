




<h1 class="heading"><span class="name">List Global Defined Operators</span> <span class="command">)OPS {nm}</span></h1>



This command displays the names of global defined operators in the active workspace or current namespace.  Names are displayed in [`⎕AV`](../system-functions/av.md) collation order.  If a name is included after the command, only those names starting at or after the given name in collation order are displayed.

<h2 class="example">Examples</h2>
```apl
      )OPS
AND DOIF DUAL ELSE POWER
 
      )OPS E
ELSE POWER
```



