---
search:
  exclude: true
---

# <span>Shared Variable Offer</span> `⎕SVO`

`⎕SVO` deals with offers to share variables with another APL workspace or another application.

## Query Shared Variable Degree of Coupling

[Monadic `⎕SVO`](svo-monadic.md) returns the degree of coupling of a shared variable:

```apl
      ⎕SVO 'DATA'
1
```

## Offer Shared Variable

[Dyadic `⎕SVO`](svo-dyadic.md) offers to share a variable:

```apl
      DATA←⍳9
      'DDE:' ⎕SVO 'DATA'
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVO SVO
</div>
