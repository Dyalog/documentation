---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Ampersand</span> <span class="command">&</span></h1>

Ampersand is a monadic operator with an ambivalent operand

Operator Ampersand means
[Spawn](../primitive-operators/spawn.md)
```apl

      delay←{'Delayed: ',⎕DL ⍵}    ⍝ delay function

      delay 10    ⍝ delay for 10 seconds
Delayed:  10.2228

      ⎕←delay&10  ⍝ delay for 10 seconds in new thread 1
1

      2+3 4       ⍝ execute something in current thread
5 6
                  ⍝ thread 1 completes:
Delayed:  10.03183
```
[Language Elements](../glyphs.md)
