# Idiom Recognition

*Idioms* are commonly used expressions that are recognised and evaluated internally, providing a significant performance improvement.

For example, the idiom `BV/⍳⍴A` (where `BV` is a Boolean vector and `A` is an array) would (in earlier Versions of Dyalog APL) have been evaluated in 3 steps as follows:

1. Evaluate `⍴A` and store result in temporary variable `temp1` (`temp1` is just an arbitrary name for the purposes of this explanation)
2. Evaluate `⍳temp1` and store result in temporary variable `temp2`.
3. Evaluate `BV/temp2` 
4. Discard temporary variables

In the current Version of Dyalog APL, the expression is recognised in its entirety and processed in a single step as if it were a single primitive function. In this case, the resultant improvement in performance is between 2 and 4.5.

Idiom recognition is precise; an expression that is almost identical but not exactly identical to an expression given in the [Idiom List](idiom-list.md) table will not be recognised.

For example, `⎕AV⍳` will be recognised as an idiom, but `(⎕AV)⍳` will not. Similarly, `(,)/` would not be recognized as the Join idiom.
