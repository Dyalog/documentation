
<!-- Hidden search keywords -->
<div style="display: none;">
  8415⌶
</div>

<h1 class="heading"><span class="name">Singular Value Decomposition</span> <span class="command">R←(8415⌶)Y</span></h1>

`Y` is a simple numeric matrix. `⎕FR` must be 645.

The result `R` is a 4 element vector whose elements are as follows.

|-----|---|-----------------------------------------------------------------------|
|`[1]`|`U`|a unitary matrix                                                       |
|`[2]`|`S`|a diagonal matrix                                                      |
|`[3]`|`V`|a unitary matrix                                                       |
|`[4]`|`f`|a Boolean flag indicating whether the algorithm converged (1)or not (0)|

This function computes a factorisation of the matrix `Y` such that:
```apl
      Y ≡ U +.× S +.× ⍉+V
```

This can be useful for analysing matrices for which `⌹` cannot compute an inverse, because they are singular or nearly singular.

For further information, see Wikipedia's article on [Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition).

!!! note
    This function signals `DOMAIN ERROR` if `⎕FR` is 1287. See [Floating-Point Representation ](../../system-functions/fr.md).



