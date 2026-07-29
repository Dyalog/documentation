---
search:
  boost: 2
---

# <span>File Read Access</span> `R←⎕FRDAC Y`{{key}}

## Access code 4096

`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber. If the passnumber is omitted it is assumed to be zero. The result is the access matrix for the designated file.

For details see [File Access Control](../../../programming-reference-guide/component-files/component-files/#file-access-control).

<h2 class="example">Examples</h2>
```apl
      ⎕FRDAC 1
28 2105 16385
 0 2073 16385
31   ¯1     0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRDAC FRDAC
</div>
