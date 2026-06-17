---
search:
  boost: 2
---
<div style="display: none;">
  /
  reduce
</div>

<h1 class="heading"><span class="name">Reduce</span> <span class="command">R←f/[K]Y</span></h1>

`f` must be a dyadic function.  `Y` may be any array whose items in the sub-arrays along the `K`<sup>th</sup> axis are appropriate to function `f`.

The axis specification is optional.  If present, `K` must identify an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←f⌿Y` implies the first axis of `Y`.

`R` is an array formed by applying function `f` between items of the vectors along the `K`<sup>th</sup> (or implied) axis of `Y`. For a typical vector `Y`, the result `R` is:
```apl
       R  ←→ ⊂(1⊃Y)f(2⊃Y)f......f(n⊃Y)
```

The shape `S` of `R` is the shape of `Y` excluding the `K`<sup>th</sup> axis, i.e.
```apl
       S  ←→  ⍴R  ←→  (K≠⍳⍴⍴Y)/⍴Y
```

If `Y` is a scalar then for any function `f`, `R` is `Y`.

If the length of the `K`<sup>th</sup> axis of `Y` is 1, or if the length of any other axis of `Y` is 0, then `f` is not applied and `R` is `S⍴Y`.

Otherwise, if the length of the `K`<sup>th</sup> axis is 0 then the result depends on `f` and on `⊃Y` (the prototypical item of `Y`) as follows:

If `f` is one of the functions listed in [](#IdentityElements) then `R` is `S⍴⊂I`, where `I` is formed from `⊃Y` by replacing each depth-zero item of `⊃Y` with the *identity element* from the table.

Otherwise, if `f` is Catenate, `R` is `S⍴⊂0/⊃Y`. If `f` is Catenate First, `R` is `S⍴⊂0⌿⊃Y`. If `f` is Catenate along the J<sup>th</sup> axis, `R` is `S⍴⊂0/[J]⊃Y`. See [Catenate/Laminate](../../primitive-functions/catenate-laminate.md).

Otherwise, `DOMAIN ERROR` is reported.

Table: Identity Elements {: #IdentityElements }

|Function|&nbsp;| Identity |
|---|---|----------|
|Add|`+`| `0`      |
|Subtract|`-`| `0`      |
|Multiply|`×`| `1`      |
|Divide|`÷`| `1`      |
|Residue|`| `        |`0`|
|Minimum|`⌊`| `M`    |
|Maximum|`⌈`| `-M`     |
|Power|`*`| `1`      |
|Binomial|`!`| `1`      |
|And|`∧`| `1`      |
|Or|`∨`| `0`      |
|Less|`<`| `0`      |
|Less or Equal|`≤`| `1`      |
|Equal|`=`| `1`      |
|Greater|`>`| `0`      |
|Greater or Equal|`≥`| `1`      |
|Not Equal|`≠`| `0`      |
|Encode|`⊤`| `0`      |
|Union|`∪`| `⍬`      |
|Replicate|`/⌿`| `1`      |
|Expand|`\⍀`| `1`      |
|Rotate|`⌽⊖`| `0`      |

In [](#IdentityElements), `M` represents the largest representable value. Typically this is 1.7E308, unless [`⎕FR`](../../system-functions/fr.md) is `1287`, in which case it becomes 1E6145

<h2 class="example">Examples</h2>
```apl
      ∨/0 0 1 0 0 1 0
1
      MAT
1 2 3
4 5 6
 
      +/MAT
6 15
 
```
```apl
      +⌿MAT
5 7 9
 
      +/[1]MAT
5 7 9
 
      +/(1 2 3)(4 5 6)(7 8 9)
 12 15 18
 
      ,/'ONE' 'NESS'
 ONENESS
 
      +/⍳0
0
```
```apl
      (⊂⍬)≡,/⍬ 
1
      (⊂'')≡,/0⍴'Hello' 'World' 
1
      (⊂0 3 4⍴0)≡⍪/0⍴⊂2 3 4⍴0
1
```

## Evaluation Order

In its initial implementation, Dyalog evaluated `+/` and `×/` in left-to-right (non-ISO standard) order because `+` and `×` are commutative and left-to-right evaluation was faster. 
 
The imprecise way in which large and non-integral values can be stored means that there are some cases in which evaluation order affects the result. For example:
```apl 
      +/ 1E100 ¯1E100 1
1
      +/ 1 1E100 ¯1E100
0
``` 
For backwards compatibility reasons, `+/` and `×/` of simple vectors are still evaluated in left-to-right order and that will not change. Any deviation from this, such as arguments that are not simple vectors (for example, higher-rank arrays or nested arguments) or additional qualifications of the derived function (for example, with bracket axes or application of the rank operator) can change the evaluation order. This means that some sums and products can give different results to those that might be expected. For example:
```apl 
      +/ 1E100 ¯1E100 1
1
      +/ [1E100 ¯1E100 1 ⋄ 1E100 ¯1E100 1]
0 0
      +/ (1E100 ¯1E100) (¯1E100 1E100) 1
0 0 
      +∘⊢/ 1E100 ¯1E100 1
0
```
This also applies to `+⌿` and `×⌿`.
