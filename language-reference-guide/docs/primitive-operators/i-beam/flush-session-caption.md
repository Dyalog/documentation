---
search:
  boost: 2
---

<!-- Hidden search keywords -->
<div style="display: none;">
  2022⌶
</div>

# <span>Flush Session Caption</span> `R←2022⌶Y`{{key}}

!!! note
    **Windows only**

Under Windows, the Session Caption displays information such as the name of the current workspace. The contents of the Caption can be modified: see *Window Captions* in the *Installation and Configuration Guide* for more details.

However, the Caption is updated only at the six-space prompt; calling `⎕LOAD` for example from within a function will not result in the Caption being updated at the end of the `⎕LOAD`.

This I-Beam causes the Session Caption to be updated (flushed) when called. Note that this I-Beam does not alter the contents of the Caption.

<h2 class="example">Example</h2>
```apl

      2022⌶0    
```
