---
search:
  exclude: true
---

<h1 class="heading"><span class="name">Primitive Operators</span></h1>

|------------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------|
|[Each](each/each-with-monadic-operand.md)      |`f¨Y`                     |apply monadic `f` to elements of `Y`                                                                    |
|[Dyadic Each](each/each-with-dyadic-operand.md)|`Xf¨Y`                    |apply dyadic `f` to corresponding elements of `X` and `Y`                                               |
|[Rank](rank.md)                           |`f(⍤k)Y`                  |apply monadic `f` to k-cells of `Y`                                                                     |
|[Dyadic Rank](rank.md)                    |`Xf(⍤kx ky)Y`             |dyadic `f` placed between kx-cells of `X` and  ky-cells of `Y`                                          |
|[Power](power.md)                         |`X(f⍣g)Y`                 |apply monadic or dyadic `f` repeatedly to `Y`                                                           |
|[Reduce](reduce/index.md)                       |`f/Y`                     |dyadic `f` placed between each sub-array along (last) axis of `Y`                                       |
|[Reduce First](reduce-first.md)           |`f⌿Y`                     |dyadic `f` placed between each sub-array along (first) axis of `Y`                                      |
|[N-Wise Reduce](reduce/reduce-n-wise.md)         |`Xf/Y`                    |dyadic `f` placed between items of sub-vectors of length `X` of `Y`                                     |
|[Scan](scan.md)                           |`f\Y`                     |successive reductions along (last) axis of `Y`                                                          |
|[Scan First](scan-first.md)               |`f⍀Y`                     |successive reductions along (first) axis of `Y`                                                         |
|[Commute](commute.md)                     |`{X}f⍨Y`                  |commute arguments of dyadic `f`                                                                         |
|[Constant](constant.md)                   |`{X}A⍨Y`                  |gives result `A`                                                                                        |
|[Atop](atop.md)                           |`f⍤gY`                    |gives result `f g Y`                                                                                    |
|`Xf⍤gY`                                   |gives result `X (f g) Y`                                                                                                          ||
|[Over](over.md)                           |`f⍥gY`                    |gives result `f g Y`                                                                                    |
|`Xf⍥gY`                                   |gives result `(g X) f g Y`                                                                                                        ||
|[Beside](beside.md)                       |`f∘gY`                    |gives result `f g Y`                                                                                    |
|`Xf∘gY`                                   |gives result `X f g Y`                                                                                                            ||
|[Bind](bind.md)                           |`I∘gY`                    |gives result `I g Y`                                                                                    |
|`f∘kY`                                    |gives result `⍵ f Y`                                                                                                              ||
|[Inner Product](inner-product.md)         |`Xf.gY`                   |apply `f` and `g` like `+` and `×` in matrix multiplication                                             |
|[Outer Product](outer-product.md)         |`X∘.gY`                   |apply dyadic `g` to all combinations of elements from `X` and `Y`                                       |
|[Key](key.md)                             |`f⌸Y`                     |dyadic `f` placed between unique major-cells of `Y` and the collected corresponding major-cells of `⍳≢Y`|
|[Dyadic Key](key.md)                      |`Xf⌸Y`                    |dyadic `f` placed between unique major-cells of `X` and the collected corresponding major-cells of `Y`  |
|[Spawn](spawn.md)                         |`Xf&Y`                    |start a new thread with f applied to its argument(s)                                                    |
|[I-Beam](i-beam.md)                       |`{f}(X⌶)Y`                |provides a range of system-related services                                                             |
