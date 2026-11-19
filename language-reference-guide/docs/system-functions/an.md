---
search:
  boost: 2
---

# <span>Account Name</span> `R←⎕AN`{{key}}

This is a system constant: a simple character vector that is the name of the user that the interpreter runs as. [`⎕SYSTEM`](system.md) gives more information of this kind, such as the user's identifier and the name of the computer.

<h2 class="example">Example</h2>

```apl
      ⎕AN
pete
      ⍴⎕AN
4
```

## Result

Under Microsoft Windows, `R` is the name of the user account that the interpreter runs under.

Under Unix, `R` is the name that the user database, usually **/etc/passwd**, gives for the real user identifier (UID) of the interpreter's process, which is also its [user number](ai.md#user-number). Environment variables such as `USER` do not affect it. If the user database has no entry for the UID, `R` is empty.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AN AN
</div>
