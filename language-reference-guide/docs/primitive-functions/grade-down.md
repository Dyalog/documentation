---
search:
  boost: 2
---

# <span>Grade Down</span> `R←⍒Y`{{key}}

`Y` may be any array of rank greater than 0 but may not contain namespaces. `R` is an integer vector being the permutation of `⍳1↑⍴Y` that places the sub-arrays along the first axis in descending order. For the rules for comparing items of `Y` with one another, see [Grade Up](grade-up.md).

`⎕IO` is an implicit argument of Grade Down.

<h2 class="example">Examples</h2>
```apl
      ⍒22.5 1 15 3 ¯4
1 3 4 2 5

```
```apl
      M
2 3 5
1 4 7
     
2 3 4
5 2 4
     
2 3 5
1 2 6
      ⍒M
1 3 2

```

!!! note
    Character arrays sort differently in the Unicode and Classic Editions.

```apl
      M
Goldilocks
porridge   
Porridge   
3 bears 
```

<table>
<tr>
 <th>Unicode Edition</th>
 <th>Classic Edition</th>
</tr>
<tr>
 <td><pre><code>      ⍋M
2 3 1 4</code></pre></td>
 <td><pre><code>      ⍋M
3 1 4 2</code></pre></td>
</tr>
<tr>
 <td><pre><code>      M[⍋M;]
porridge
Porridge
Goldilocks
3 bears
</code></pre></td>
 <td><pre><code>      M[⍋M;]
Porridge
Goldilocks
3 bears
porridge
</code></pre></td>
</tr>
</table>

```apl
      ⍴pb
6 3
      pb
┌────────┬─────┬───┐
│Rivers  │Jason│554│
├────────┼─────┼───┤
│Daintree│John │532│
├────────┼─────┼───┤
│Rivers  │Jason│543│
├────────┼─────┼───┤
│Foad    │Jay  │558│
├────────┼─────┼───┤
│Scholes │John │547│
├────────┼─────┼───┤
│Scholes │John │535│
└────────┴─────┴───┘
      ⍒pb
5 6 1 3 4 2

```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍒ grade
</div>
