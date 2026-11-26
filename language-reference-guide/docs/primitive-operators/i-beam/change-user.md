---
search:
  boost: 2
---


# <span>Change User</span> `R←4001⌶Y`{{key}}

`Y` is a character vector that specifies a valid Unix user name. The function changes the *userid (uid)* and *groupid (gid)* of the process to values that correspond to the specified user name.

It is only possible to change the user name if the *effective uid* is 0 (that is, the process has root privileges).

If the operation is successful, `R` is the user name specified in `Y`, and the [user number](../../system-functions/ai.md) in `⊃⎕AI` becomes that user's identifier (UID).

Under macOS, [`⎕AN`](../../system-functions/an.md) also becomes the user name specified in `Y`. Under AIX and Linux, `⎕AN` is the name that the user logged in with, and does not change. [`⎕SYSTEM.Host.UserId`](../../system-functions/system.md#hostuserid) and `⎕SYSTEM.Host.UserName` do not change on any of the three. Under Linux, in a session with no login name, `⎕AN` and `⎕SYSTEM.Host` change too, because they follow the real UID there.

If the operation fails, the function generates a `FILE ERROR 1 Not Owner` error.

If the argument to `4001⌶` is other than a non-empty simple character vector, the function generates a `DOMAIN ERROR`.

If the argument is not the name of a valid user the function generates a `FILE ERROR 3 No such process`.

If the argument is the same name as the current effective user, then the function returns that name, but has no effect.

If the argument is a valid name other than the name of the effective user id of the current process, and that effective user id is not root the function generates a `FILE ERROR 1 Not owner`.

<!-- Hidden search keywords -->
<div style="display: none;">
  4001⌶
</div>
