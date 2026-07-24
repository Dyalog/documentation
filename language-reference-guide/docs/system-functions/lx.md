---
search:
  boost: 2
---

# <span>Latent Expression</span> `⎕LX`

This may be a character vector or scalar representing an APL expression.  The expression is executed automatically when the workspace is loaded.  If APL is invoked using the  `-x`  flag, this execution is suppressed.

The value of `⎕LX` in a clear workspace is `''`. `⎕LX` has workspace scope.

<h2 class="example">Example</h2>
```apl
      ⎕LX←'''GOOD MORNING PETE'''
 
      )SAVE GREETING
GREETING saved Tue Sep 8 10:49:29 1998
 
      )LOAD GREETING
./GREETING saved Tue Sep 8 10:49:29 1998
GOOD MORNING PETE
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕LX LX
</div>
