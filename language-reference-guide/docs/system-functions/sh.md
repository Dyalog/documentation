---
search:
  exclude: true
---





<h1 class="heading"><span class="name">Unix Shell</span> <span class="command">⎕SH</span></h1>


## Monadic `⎕SH` means


[Execute Unix Command](execute-unix-command.md)
```apl
       ⎕SH'ls'
FILES WS temp
```

## Dyadic `⎕SH` means


[Start Unix Auxiliary Processor](start-unix-auxiliary-processor.md)
```apl
      )CLEAR
clear ws
      'xutils' ⎕SH 'xutils'
      )FNS
avx     box     dbr     getenv  hex     ltom    ltov    mtol    ss      vtol

```
