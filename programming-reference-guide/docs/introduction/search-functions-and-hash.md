# Search Functions and Hash Tables

Primitive dyadic *search* functions, such as `⍳` (index of) and `∊` (membership) have a *principal* argument in which items of the other *subject* argument are located.

In the case of `⍳`, the principal argument is the one on the left and in the case of `∊`, it is the one on the right. The following table shows the principal (P) and subject (s) arguments for each of the functions.

|---------------|-------------------|
|`P ⍳ s`        |Index of           |
|`s ∊ P`        |Membership         |
|`s ∩ P`        |Intersection       |
|`P ∪ s`        |Union              |
|`s ~ P`        |Without            |
|`P {(↓⍺)⍳↓⍵} s`|Matrix Iota (idiom)|
|`P∘⍋ and P∘⍒`  |Grade              |

The Dyalog APL implementation of these functions already uses a technique known as *hashing* to improve performance over a simple linear search. (Note that `⍷` (find) does not employ the same hashing technique, and is excluded from this discussion.)

Building a *hash table* for the principal argument takes a significant time but is rewarded by a considerably quicker search for each item in the subject. Unfortunately, the hash table is discarded each time the function completes and must be reconstructed for a subsequent call (even if its principal argument is identical to that in the previous one).

For optimal performance of *repeated* search operations, the hash table may be retained between calls, by binding the function with its principal argument using the primitive `∘` (compose) operator. The retained hash table is then used directly whenever this monadic derived function is applied to a subject argument.

Notice that retaining the hash table pays off only on a second or subsequent application of the derived function. This usually occurs in one of two ways: either the derived function is named for later (and repeated) use, as in the first example below or it is applied repeatedly as the operand of a primitive or defined operator, as in the second example.

## Example: naming a derived function.
```apl
      words←'red' 'ylo' 'grn' 'brn' 'blu' 'pnk' 'blk'
 
      find←words∘⍳                 ⍝ monadic find function
      find'blk' 'blu' 'grn' 'ylo'  ⍝ 
7 5 3 2
      find'grn' 'brn' 'ylo' 'red'  ⍝ fast find
3 4 2 1
```

## Example: repeated application by (`¨`) each operator.
```apl
      ∊∘⎕A¨'This' 'And' 'That'
 1 0 0 0  1 0 0  1 0 0 0
```
