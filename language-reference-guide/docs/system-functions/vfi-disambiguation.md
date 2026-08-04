---
search:
  exclude: true
---

# <span>Verify & Fix Input</span> `⎕VFI`

## Monadic `⎕VFI` means

[Parse Numbers](vfi-monadic.md)
```apl
      ⎕VFI '1 2 3'
 1 1 1  1 2 3 
```

## Dyadic `⎕VFI` means

[Parse Numbers with Separators](vfi-dyadic.md)
```apl
      ',' ⎕VFI '1,2,3'
 1 1 1  1 2 3 
```
