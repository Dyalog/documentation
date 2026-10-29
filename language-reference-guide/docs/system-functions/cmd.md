---
search:
  exclude: true
---

# <span>Windows Processor</span> `⎕CMD`

`⎕CMD` runs a command through the Windows Command Processor, or starts a program, when called monadically, and starts an auxiliary processor when called dyadically. It is a synonym of [`⎕SH`](sh.md); either name can be used on any platform, with the same effect. The `⎕CMD` pages describe the behaviour under Microsoft Windows, and the `⎕SH` pages the behaviour under Unix.

## Call Windows Command Processor

[Monadic `⎕CMD`](cmd-monadic.md) runs a command and returns its output:

```apl
      ⎕CMD'echo Hello'
 Hello
```

## Start Windows Auxiliary Processor

[Dyadic `⎕CMD`](cmd-dyadic.md) starts an auxiliary processor, which defines external functions in the workspace:

```apl
      )CLEAR
clear ws
      'xutils' ⎕CMD ''
      )FNS
avx     box     dbr     getenv  hex     ltom    ltov    mtol    ss      vtol
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CMD CMD
</div>
