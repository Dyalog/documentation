---
search:
  exclude: true
---

# <span>External Variable</span> `⎕XT`

`⎕XT` deals with external variables, whose values are stored in files instead of in the workspace.

## Query External Variable

[Monadic `⎕XT`](xt-monadic.md) returns the file that is associated with an external variable:

```apl
      'array' ⎕XT 'V'
      ⎕XT 'V'
array
```

## Associate External Variable

[Dyadic `⎕XT`](xt-dyadic.md) associates a variable with a file, which keeps the value when the variable is expunged:

```apl
      V←⍳5
      ⎕EX 'V'
      'array' ⎕XT 'F'
      F
1 2 3 4 5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XT XT
</div>
