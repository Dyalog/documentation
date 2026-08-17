---
search:
  exclude: true
---

# <span>Export Object</span> `⎕EXPORT`

## Monadic `⎕EXPORT` means

[Query Export Type](export-monadic.md)
```apl
      ⎕FX 'MyFn' 'r←42'
      ⎕EXPORT 'MyFn'
1
      0 ⎕EXPORT 'MyFn'
      ⎕EXPORT 'MyFn'
0
```

## Dyadic `⎕EXPORT` means

[Set Export Type](export-dyadic.md)
```apl
      'utils' ⎕NS ⍬
      utils.⎕FX 'r←MyUtil y' 'r←Sub y'
      utils.⎕FX 'r←Sub y' 'r←y y'
      0 utils.⎕EXPORT 'Sub'
      ⎕PATH←'utils'
      MyUtil 10
10 10
      Sub 10
VALUE ERROR: Undefined name: Sub
      Sub 10
      ∧
```

!!! Legacy "Legacy"
    `⎕EXPORT` does not support derived functions and will not be extended to support them; nor will it be extended to support other types of functions that might be developed in the future. `⎕EXPORT` can therefore be considered an archaic feature.
