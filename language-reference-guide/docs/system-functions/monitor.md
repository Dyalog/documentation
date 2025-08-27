---
search:
  exclude: true
---





<h1 class="heading"><span class="name">Monitor Controls</span> <span class="command">⎕MONITOR</span></h1>


## Dyadic `⎕MONITOR` means


[Set Monitor Controls](set-monitor.md)
```apl
      +(0,⍳10) ⎕MONITOR 'FOO'
0 1 2 3 4 5
```

## Monadic `⎕MONITOR` means


[Query Monitor Controls](query-monitor.md)
```apl

      ⎕MONITOR 'FOO'
0 1 1418 1000 0
1 1   83    0 0
2 1  400    0 0
3 1  397    0 0
4 1  467 1000 0
5 1  100    0 0
```


[Language Elements](../symbols/language-elements.md)


