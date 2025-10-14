---
search:
  exclude: true
---





<h1 class="heading"><span class="name">Windows Command</span> <span class="command">⎕CMD</span></h1>


## Monadic `⎕CMD` means


[Execute Windows Command](execute-windows-command.md)
```apl
      ⎕CMD'dir'
 Volume in drive C is OS
 Volume Serial Number is B438-9B76

 Directory of C:\Users\Pete\Documents\Dyalog APL-64 17.0 Unicode Files

23/06/2018  15:59    <DIR>          .
23/06/2018  15:59    <DIR>          ..
23/06/2018  14:53           181,488 default.dlf
13/06/2018  20:13         1,262,296 def_uk.dse
14/06/2018  14:36           108,976 UserCommand20.cache
               3 File(s)      1,552,760 bytes
               2 Dir(s)  101,371,097,088 bytes free

```

## Dyadic `⎕CMD` means


[Start Windows Auxiliary Processor](start-windows-auxiliary-processor.md)
```apl
      )CLEAR
clear ws
      'xutils' ⎕CMD ''
      )FNS
avx     box     dbr     getenv  hex     ltom    ltov    mtol    ss      vtol

```


[Language Elements](../symbols/language-elements.md)


