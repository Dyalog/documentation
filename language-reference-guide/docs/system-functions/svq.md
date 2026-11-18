---
search:
  boost: 2
---

# <span>Query Shared Variable</span> `R←⎕SVQ Y`{{key}}

In other implementations of APL, this function returns the shared variable offers that partners have made to you, and that you have not yet responded to. DDE does not make this possible. Therefore, `⎕SVQ` is implemented only for compatibility, and signals `NONCE ERROR`.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVQ` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVQ SVQ
</div>
