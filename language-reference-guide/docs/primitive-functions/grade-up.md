---
search:
  boost: 2
---

# <span>Grade Up</span> `R←⍋Y`{{key}}

`Y` may be any array of rank greater than 0 but may not contain namespaces. `R` is an integer vector being the permutation of `⍳1↑⍴Y` that places the sub-arrays along the first axis in ascending order. The rules for comparing items of `Y` with one another are as follows:

## Rules for comparing simple scalars

- Numeric comparisons are  exact, as if `⎕CT←⎕DCT←0` and `⎕FR←1287`
- Two real numbers are compared numerically, thus 1.2 precedes 3.
- In the  Unicode Edition two characters are compared numerically according to their position in the Unicode table. Thus `'a'` (`⎕UCS 97`) precedes`'b'` (`⎕UCS 98`). In the Classic Edition characters are compared according to their index in `⎕AV`.
- Complex numbers are ordered by first comparing their real parts. If these are equal, the order is determined by comparing their imaginary parts.Thus `1J¯2` precedes `1` which precedes `1J2`.
- `⎕NULL` (which represents a null item obtained from an external source) precedes all numbers, and all numbers precede all characters.Thus `⎕NULL` precedes 100, and 100 precedes `'A'`. 

## Rules for comparing non-scalar arrays

- Arrays are compared item by item in ravel order.
- For arrays of equal  shape, the order is determined by the first pair of items which differ, thus `(1949 4 29)` precedes `(1949 4 30)`. Similarly `('April' 29)` precedes `('April' 30)`.
- Arrays with the same rank but different shape are ordered as if the shorter array were padded with items that precede all other types of item (negative infinity) including `⎕NULL`. Thus `'car'` precedes `'carpet'`and `(1949 4)` precedes `(1949 4 30)`. An alternative model is to say that shorter arrays precede longer ones that begin the same way. For character vectors this is described as Lexicographical ordering, which is the order that words appear in a dictionary.
- Arrays with differing rank are ordered by first extending the shape of the lower-ranked array with 1s at the beginning, and then comparing the resultant equal-rank arrays as described above. So, to compare a vector (rank 1) with a matrix (rank 2), the vector is reshaped into a 1-row matrix.
- Empty arrays are compared first by type alone, so an empty numeric array precedes an empty character array, regardless of rank or shape.Thus `((0 3 2)⍴0)` precedes `''`. If the empty arrays are of the same type, they are sorted in order of their shape vector, working right to left.So `((0 5 2)⍴99)` precedes `((0 3 4)⍴0)`  and`((0 3 4)⍴'')` precedes `((1 0 5 4)⍴'')`.

`⎕IO` is an implicit argument of Grade Up.

<h2 class="example">Examples</h2>
```apl
      ⍋22.5 1 15 3 ¯4
5 2 4 3 1

```
```apl
      M
2 3 5
1 4 7
     
2 3 4
5 2 4
     
2 3 5
1 2 6
      ⍋M
2 3 1

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
4 1 3 2</code></pre></td>
 <td><pre><code>      ⍋M
2 4 1 3</code></pre></td>
</tr>
<tr>
 <td><pre><code>      M[⍋M;]
3 bears
Goldilocks
Porridge
porridge</code></pre></td>
 <td><pre><code>      M[⍋M;]
porridge
3 bears
Goldilocks
Porridge</code></pre></td>
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
      ⍋pb
2 4 3 1 6 5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍋ grade
</div>
