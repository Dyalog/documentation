<h1 class="heading"><span class="name">Hash Table Size</span> <span class="command">{R}←8468⌶Y</span></h1>

Increases the amount of workspace allocated to internal hash tables. These tables are created when a set primitive is executed or by the Hash Array function (`1500⌶`).

## Note

**The purpose of this function is to allow the user to evaluate potential side-effects of the proposed increase in table size in the next major version of Dyalog.**

`Y` may be ⍬, or an integer 0, 1, 2, or 3.

If `Y` is 1, 2 or 3 the hash table size is increased by the factor `2*Y`. If `Y` is 0, the hash table size is reset to its default value. In these cases, the shy result `R` is the previous value of the scale factor.

If `Y` is ⍬ the size is unaffected and the (non-shy) result is the current value of the scale factor.

It is recommended that users test their code using the maximum value 3.

For more information, see [Search Functions and Hash Tables](https://help.dyalog.com/19.0/index.htm#Language/Defined%20Functions%20and%20Operators/Search%20Functions%20and%20Hash.htm#SearchFunctionsAndHashTables) and [Hash Array](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Hash%20Array.htm#Hash_Array).
