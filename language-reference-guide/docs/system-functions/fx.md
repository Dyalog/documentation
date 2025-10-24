<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FX FX
</div>





<h1 class="heading"><span class="name">Fix Definition</span> <span class="command">{R}←⎕FX Y</span></h1>



`Y` is the representation form of a function or operator which may be:

- its canonical representation form similar to that produced by `⎕CR` except that redundant blanks are permitted other than within names and constants, and the first and last rows may start with a del symbol (`∇`).
- its nested representation form similar to that produced by `⎕NR` except that redundant blanks are permitted other than within names and constants, and the first and last items may be del (`∇`) symbols.
- its object representation form produced by `⎕OR`.
- its vector representation form similar to that produced by `⎕VR` except that additional blanks are permitted other than within names and constants.


`⎕FX` attempts to create (fix) a function or operator in the workspace or current namespace from the definition given by `Y`.  `⎕IO` is an implicit argument of `⎕FX`. Note that `⎕FX` does not update the source of a scripted namespace, or of class or instance; the only two methods of updating the source of scripted objects is via the Editor, or by calling `⎕FIX`.


If the function or operator is successfully fixed, `R` is a simple character vector containing its name and the result is shy. Otherwise `R` is an integer scalar containing the (`⎕IO` dependent) index of the row of the canonical representation form in which the first error preventing its definition is detected. In this case the result `R` is **not shy**.

!!! Legacy "Legacy"
    Before Dyalog v20.0, it was possible to define dfns with unmatched parentheses and brackets. These are now rejected. TradFns will continue to fix as before, but subtle differences in how the code behaves might not be backwards-compatible and could have unexpected results.

Functions and operators which are pendent, that is, in the state indicator without a suspension mark (`*`), retain their original definition until they complete, or are cleared from the state indicator.  All other occurrences of the function or operator assume the new definition.  The function or operator will fail to fix if it has the same name as an existing variable, or a visible label.


