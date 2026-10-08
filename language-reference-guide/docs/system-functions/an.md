---
search:
  boost: 2
---

# <span>Account Name</span> `R←⎕AN`{{key}}

This is a simple character vector containing the user's login name.

Under Unix, this is the name that the `logname` command reports: the user who logged in, even after `su` or `sudo` has changed the user ID. If the process has no login name, `⎕AN` is the name of the real user. By contrast, [`⊃⎕AI`](ai.md) is always the real user ID, so the two can identify different users. The effective user is reported by [`⎕SYSTEM`](system.md#hosteffectiveusername).

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
