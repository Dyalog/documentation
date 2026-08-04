---
search:
  exclude: true
---

# <span>File Name Parts</span> `⎕NPARTS`

## Monadic `⎕NPARTS` means

[File Name Parts](nparts-monadic.md)
```apl
      ⎕NPARTS '/usr/lib/file.txt'
 /usr/lib/  file  .txt 
```

## Dyadic `⎕NPARTS` means

[Normalised File Name Parts](nparts-dyadic.md)
```apl
      1 ⎕NPARTS'c:/tmp\foo.txt'
 c:/tmp/  foo  .txt 
```
