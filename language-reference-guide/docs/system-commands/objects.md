




<h1 class="heading"><span class="name">List Global Namespaces</span> <span class="command">)OBJECTS {nm}</span></h1>



This command displays the names of global **namespaces** in the active workspace.  Names are displayed in the [`AV`](../system-functions/av.md) collating order.  If a name is included after the command, only those names starting at or after the given name in collating order are displayed.  Namespaces are objects created using [`⎕NS`](../system-functions/ns.md), [`)NS`](ns.md) or [`⎕WC`](../system-functions/wc.md) and have name class 9.


Note:  [`)OBS`](obs.md) can be used as an **alternative** to `)OBJECTS`

<h2 class="example">Examples</h2>
```apl
      )OBJECTS
FORM1   UTIL    WSDOC   XREF

      )OBS W
WSDOC   XREF

```



