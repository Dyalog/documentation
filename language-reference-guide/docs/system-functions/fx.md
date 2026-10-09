---
search:
  boost: 2
---

# <span>Fix Definition</span> `{R}←⎕FX Y`{{key}}

`Y` is the representation form of a function or operator which may be:

- its canonical representation form similar to that produced by `⎕CR` except that redundant blanks are permitted other than within names and constants, and the first and last rows may start with a del symbol (`∇`).
- its nested representation form similar to that produced by `⎕NR` except that redundant blanks are permitted other than within names and constants, and the first and last items may be del (`∇`) symbols.
- its object representation form produced by `⎕OR`.
- its vector representation form similar to that produced by `⎕VR` except that additional blanks are permitted other than within names and constants.

`⎕FX` attempts to create (fix) a function or operator in the workspace or current namespace from the definition given by `Y`.  `⎕IO` is an implicit argument of `⎕FX`. `⎕FX` does not update the source of a scripted namespace, or of class or instance; the only two methods of updating the source of scripted objects is via the Editor, or by calling `⎕FIX`.

If the function or operator is successfully fixed, `R` is a simple character vector containing its name and the result is [shy](../../programming-reference-guide/introduction/results.md#shy-results). Otherwise `R` is an integer scalar containing the (`⎕IO` dependent) index of the row of the canonical representation form in which the first error preventing its definition is detected. In this case the result `R` is **not shy**.

A dfn or dop does not fix if any parenthesis or bracket in it is unmatched, because [array notation](../../programming-reference-guide/introduction/arrays/array-notation.md#defined-functions) lets a parenthesis or bracket span several lines.

`⎕FX` replaces an existing definition immediately: [`⎕CR`](cr.md) reports the new definition, and every subsequent call uses it, as does a suspended instance when execution resumes. An instance that is _pendent_, that is, in the state indicator without a suspension mark (`*`), continues to run the definition it started with until it completes or is cleared from the state indicator. The function or operator fails to fix if it has the same name as an existing variable or a visible label.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FX FX
</div>
