---
search:
  boost: 2
---

# <span>Account Name</span> `R←⎕AN`{{key}}

This is a system constant: a simple character vector that is the name of the user. [`⎕SYSTEM`](system.md) provides additional information, for example, the user's identifier and the name of the computer.

<h2 class="example">Example</h2>

```apl
      ⎕AN
pete
      ⍴⎕AN
4
```

## Result

Under Microsoft Windows, `R` is the name of the user account that the interpreter runs under.

Under Linux, `R` is the name that the user logged in with. Starting the interpreter with `sudo` or `su`, or changing the user with [Change User](../primitive-operators/i-beam/change-user.md), does not change it. If there is no login name (for example, in a container), `R` is the name that the user database, usually **/etc/passwd**, gives for the real user identifier (UID) of the interpreter's process, or empty if the user database has no entry for that UID.

Under macOS, `R` is the name that the user database gives for the real UID of the interpreter's process, which is also its [user number](ai.md#user-number). Starting the interpreter with `sudo`, or changing the user with Change User, changes it.

Environment variables, such as `USERNAME` under Microsoft Windows and `USER` under Unix, do not affect `R`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AN AN
</div>
