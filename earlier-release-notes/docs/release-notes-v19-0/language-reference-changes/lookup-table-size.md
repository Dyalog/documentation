<h1 class="heading"><span class="name">Lookup Table Size</span> <span class="command">R←8469⌶Y</span></h1>

Increases the maximum amount of workspace allocated to internal lookup tables. These tables are created when a set primitive is executed. Lookup tables are faster than hash tables, and are used when hashing is not required.

## Note

**The purpose of this function is to allow the user to evaluate potential side-effects of the proposed increase in table size in the next major version of Dyalog.**

`Y` may be `⍬`, or an integer from 0 to 16777216.

If `Y` is between 1 and 16777216 the function sets the lookup table size in bytes to that value. If `Y` is 0, the lookup table size is reset to its default value. In both cases, the shy result `R` is the previous value of the table size.

If `Y` is `⍬` the size is unaffected and the (non-shy) result is the current value of the scale factor.

It is recommended that users test their code using the maximum value.

For more information, see [Search Functions and Hash Tables](https://help.dyalog.com/19.0/index.htm#Language/Defined%20Functions%20and%20Operators/Search%20Functions%20and%20Hash.htm#SearchFunctionsAndHashTables) and [Hash Array](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Hash%20Array.htm#Hash_Array).
