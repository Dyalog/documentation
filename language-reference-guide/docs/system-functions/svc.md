---
search:
  exclude: true
---

# <span>Shared Variable Access Control</span> `⎕SVC`

`⎕SVC` deals with the access control of shared variables, which controls the order in which partners can set and use their values.

## Query Shared Variable Access Control

[Monadic `⎕SVC`](svc-monadic.md) returns the effective access control vector of a shared variable:

```apl
      ⎕SVC 'X'
1 1 1 1
```

## Set Shared Variable Access Control

[Dyadic `⎕SVC`](svc-dyadic.md) sets your access control vector of a shared variable:

```apl
      1 ⎕SVC 'X EXTNAME'
1 1 1 1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVC SVC
</div>
