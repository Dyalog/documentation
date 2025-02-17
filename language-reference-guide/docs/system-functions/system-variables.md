<h1 class="heading"><span class="name">System Variables</span></h1>

System variables retain information used by the system in some way. Many system variables affect the behaviour of primitive functions and operators to which they act as *implicit arguments*.

System variables may be localised by inclusion in the header line of a defined function or in the argument list of the system function `⎕SHADOW`. When a system variable is localised, it retains its previous value until it is assigned a new one. This feature is known as "pass-through localisation". The exception to this rule is `⎕TRAP`.

A system variable can never be undefined. Default values are assigned to all system variables in a clear workspace.


|Name           |Description                               |Scope      |
|---------------|-----------------------------------------|-----------|
|[`⎕AVU`](avu.md)  |Atomic Vector – Unicode              |Namespace  |
|[`⎕CT`](ct.md)    |Comparison Tolerance                |Namespace  |
|[`⎕DCT`](dct.md)  |Decimal Comp Tolerance              |Namespace  |
|[`⎕DIV`](div.md)  |Division Method                     |Namespace  |
|[`⎕FR`](fr.md)    |Floating-Point Representation       |Namespace  |
|[`⎕IO`](io.md)    |Index Origin                        |Namespace  |
|[`⎕LX`](lx.md)    |Latent Expression                   |Workspace  |
|[`⎕ML`](ml.md)    |Migration Level                     |Namespace  |
|[`⎕PATH`](path.md)|Search Path                         |Session    |
|[`⎕PP`](pp.md)    |Print Precision                     |Namespace  |
|[`⎕PW`](pw.md)    |Print Width                         |Session    |
|[`⎕RL`](rl.md)    |Random Link                         |Namespace  |
|[`⎕RTL`](rtl.md)  |Response Time Limit                 |Namespace  |
|[`⎕SM`](sm.md)    |Screen Map                          |Workspace  |
|[`⎕TNAME`](tname.md)|Thread Name                      |Workspace  |
|[`⎕TRAP`](trap.md)|Event Trap                          |Workspace  |
|[`⎕USING`](using.md)|Microsoft .NET Search Path       |Namespace  |
|[`⎕WSID`](wsid.md)|Workspace ID                        |Workspace  |
|[`⎕WX`](wx.md)    |Window Expose                       |Namespace  |

In other words, [`⎕PATH`](path.md) and [`⎕PW`](pw.md) relate to the session. [`⎕LX`](lx.md), [`⎕SM`](sm.md), [`⎕TRAP`](trap.md), and [`⎕WSID`](wsid.md) relate to the active workspace. All the other system variables relate to the current namespace.

|Session   |Workspace     |Namespace        |
|----------|--------------|-----------------|
|[`⎕PATH`](path.md) |[`⎕LX`](lx.md)    |[`⎕AVU`](avu.md)   |
|[`⎕PW`](pw.md)     |[`⎕SM`](sm.md)    |[`⎕CT`](ct.md)     |
|&nbsp;                 |[`⎕TRAP`](trap.md) |[`⎕DCT`](dct.md)   |
|&nbsp;                 |[`⎕WSID`](wsid.md) |[`⎕DIV`](div.md)   |
|&nbsp;                 |&nbsp;               |[`⎕FR`](fr.md)     |
|&nbsp;                 |&nbsp;               |[`⎕IO`](io.md)     |
|&nbsp;                 |&nbsp;               |[`⎕ML`](ml.md)     |
|&nbsp;                 |&nbsp;               |[`⎕PP`](pp.md)     |
|&nbsp;                 |&nbsp;               |[`⎕RL`](rl.md)     |
|&nbsp;                 |&nbsp;               |[`⎕RTL`](rtl.md)   |
|&nbsp;                 |&nbsp;               |[`⎕USING`](using.md)|
|&nbsp;                 |&nbsp;               |[`⎕WX`](wx.md)     |

Note that the value assigned to a system variable must be appropriate; otherwise an error will be reported immediately.

<h2 class="example">Example</h2>
```apl
      ⎕IO←3
DOMAIN ERROR
      ⎕IO←3
      ^
```
