---
search:
  exclude: true
---

# <span>Unix Processor</span> `⎕SH`

`⎕SH` runs a command through a Unix shell when called monadically, and starts an auxiliary processor when called dyadically. It is a synonym of [`⎕CMD`](cmd.md); either name can be used on any platform, with the same effect. The `⎕SH` pages describe the behaviour under Unix, and the `⎕CMD` pages the behaviour under Microsoft Windows.

## Call Unix Command Processor

[Monadic `⎕SH`](sh-monadic.md) runs a command and returns its output:

```apl
      ⎕SH'echo Hello'
Hello
```

## Start Unix Auxiliary Processor

[Dyadic `⎕SH`](sh-dyadic.md) starts an auxiliary processor, which defines external functions in the workspace:

```apl
      )CLEAR
clear ws
      'xutils' ⎕SH 'xutils'
      )FNS
avx     box     dbr     hex     ltom    ltov    mtol    ss      vtol
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SH SH
</div>
