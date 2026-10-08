---
search:
  boost: 2
---

# <span>Account Information</span> `R←⎕AI`{{key}}

This is a simple integer vector, whose four elements are:

|--------|-------------------------------------------------|
|`⎕AI[1]`|user identification.                             |
|`⎕AI[2]`|compute time for the APL session in milliseconds.|
|`⎕AI[3]`|connect time for the APL session in milliseconds.|
|`⎕AI[4]`|keying time for the APL session in milliseconds. |

Elements beyond 4 are not defined but reserved.

<h2 class="example">Example</h2>

```apl
     ⎕AI
52 7396 2924216 2814831
```

!!! unix "Dyalog on Unix"
    Under Unix, `⎕AI[1]` is the real user ID, as reported by `id -ru`. [`⎕AN`](an.md) is the name of this user, except on Linux, where it is the login name whenever the process has one. The effective user ID is reported by [`⎕SYSTEM`](system.md#hosteffectiveuserid).

!!! windows "Dyalog on Microsoft Windows"
    Under Microsoft Windows, `⎕AI[1]` is the aplnid (network ID from configuration dialog box).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AI AI
</div>
