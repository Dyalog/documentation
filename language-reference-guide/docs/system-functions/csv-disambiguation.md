---
search:
  exclude: true
---

# <span>Comma Separated Values</span> `⎕CSV`

## Monadic `⎕CSV` means

[Import CSV](csv-monadic.md)
```apl
      ⎕CSV ('1,2,3' '4,5,6') '' 2
1 2 3
4 5 6
```

## Dyadic `⎕CSV` means

[Export CSV](csv-dyadic.md)
```apl
      (2 3⍴⍳6) ⎕CSV ''
1,2,3
4,5,6
```
