---
search:
  boost: 2
---
<div style="display: none;">
  \
  scan
</div>

# <span>Scan</span> `R←f\[K]Y`{{key}}

`f` may be any dyadic function that returns a result.  `Y` may be any array whose items in the sub-arrays along the `K`th axis are appropriate to the function `f`.

The axis specification is optional.  If present, `K` must identify an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←f⍀Y` implies the first axis of `Y`.

`R` is an array formed by successive reductions along the `K`th axis of `Y`.  If `V` is a typical vector taken from the `K`th axis of `Y`, then the `I`<sup>th</sup> element of the result is determined as `f/I↑V`.

The shape of `R` is the same as the shape of `Y`.  If `Y` is an empty array, then `R` is the same empty array.

<h2 class="example">Examples</h2>
```apl
      ∨\0 0 1 0 0 1 0
0 0 1 1 1 1 1
 
      ^\1 1 1 0 1 1 1
1 1 1 0 0 0 0
 
      +\1 2 3 4 5
1 3 6 10 15
 
      +\(1 2 3)(4 5 6)(7 8 9)
 1 2 3  5 7 9  12 15 18
```
```apl

      M
1 2 3
4 5 6
 
      +\M
1 3  6
4 9 15
 
      +⍀M
1 2 3
5 7 9
 
      +\[1]M
1 2 3
5 7 9
 
      ,\'ABC'
A AB  ABC
 
      T←'ONE(TWO) BOOK(S)'
 
      ≠\T∊'()'
0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0
 
      ((T∊'()')⍱≠\T∊'()')/T
ONE BOOK
 
```

## Evaluation Order

In its initial implementation, Dyalog evaluated `+\` and `×\` as a single left-to-right pass (non-ISO standard) because `+` and `×` are commutative and left-to-right evaluation was faster. 
 
The imprecise way in which large and non-integral values can be stored means that there are some cases in which evaluation order affects the result. For example (note the rightmost element of the result):
```apl 
      +\ 1E100 ¯1E100 1
1E100 0 1
      +\ 1 1E100 ¯1E100
1 1E100 0
``` 
For backwards compatibility reasons, `+\` and `×\` of simple vectors are still evaluated in left-to-right order and that will not change. Any deviation from this, such as arguments that are not simple vectors (for example, higher-rank arrays or nested arguments) or additional qualifications of the derived function (for example, with bracket axes or application of the rank operator) can change the evaluation order. This means that some running sums and products can give different results to those that might be expected. For example:
```apl 
      +\ 1E100 ¯1E100 1
1E100 0 1
      {⍺+⍵}\1E100 ¯1E100 1
1E100 0 0
      +∘⊢\ 1E100 ¯1E100 1
1E100 0 0
```
This also applies to `+⍀` and `×⍀`.
