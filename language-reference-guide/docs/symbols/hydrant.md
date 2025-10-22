---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Hydrant</span> <span class="command">⍎</span></h1>

Monadic Hydrant means
[Execute expression](../primitive-functions/execute.md)
```apl
      ⍎ '1+1'
2
      V ← 1 2 3
      ⍎ 'V'
1 2 3 

```

Dyadic Hydrant means
[Execute expression in given namespace](../primitive-functions/execute.md)
```apl
      '#' ⍎ '⎕PP ⎕CT ⎕RL'
┌──┬─────┬────┐
│10│1E¯14│┌┬─┐│
│  │     │││1││
│  │     │└┴─┘│
└──┴─────┴────┘

```
[Language Elements](../glyphs.md)


