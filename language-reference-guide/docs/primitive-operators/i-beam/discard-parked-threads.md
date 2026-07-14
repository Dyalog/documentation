---
search:
  boost: 2
---

<!-- Hidden search keywords -->
<div style="display: none;">
  2502⌶
</div>

# <span>Discard Parked Threads</span> `R←2502⌶Y`{{key}}

APL threads that Dyalog creates to serve incoming .NET requests are not terminated when their work is done. They persist so that if another call comes in on the same .NET thread the same APL thread can handle it. In effect the thread is *parked* until it is needed again. If the thread is not required, there is a small performance cost in maintaining it in this state.

`(2502⌶0)`
 removes all parked threads from the workspace.
