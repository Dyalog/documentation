---
search:
  boost: 2
---

# <span>Account Name</span> `R←⎕AN`{{key}}

This is a simple character vector containing the name of the user.

Under Unix, this is the name of the real user, the user that [`⊃⎕AI`](ai.md) identifies by number. The exception is Linux, where `⎕AN` is the login name whenever the process has one, as the `logname` command reports, so it names the user who logged in even after `su` or `sudo` has changed the user ID. Neither is necessarily the effective user, which [`⎕SYSTEM`](system.md#hosteffectiveusername) reports.

<h2 class="example">Example</h2>

```apl
      ⎕AN
Pete
 
      ⍴⎕AN
4
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AN AN
</div>
