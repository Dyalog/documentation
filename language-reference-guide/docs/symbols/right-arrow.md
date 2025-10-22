---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Right Arrow</span> <span class="command">→</span></h1>

Monadic Right Arrow means
[Branch](../other-syntax/branch.md)
```apl
Syntax:  Branch (Clear suspension)

      → Label  ⍝ branch to Label:
      → ⎕LC    ⍝ resume suspended execution
      → 0      ⍝ exit current function and resume calling line
      →        ⍝ clear one stack suspension

Branching is superseded by the more modern
control structures such as :If ... :EndIf
```
[Language Elements](../glyphs.md)


