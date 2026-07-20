---
search:
  boost: 2
---


# <span>Hash Array</span> `R←{X}1500⌶Y`{{key}}

This function creates a hashed array, returns an unhashed copy of an array or reports the state of hashing of an array.

`Y` may be any array.

If `X` is omitted, the result `R` is a copy of `Y` that has been invisibly marked as hashed. `R` behaves the same as `Y` in all respects. The only difference is that dyadic `⍳` and related functions are expected to run faster when applied to a hashed array. The *hash* will be created the first time the array is used as an argument to `⍳` or other set functions. The *hashed* property is preserved across assignments and argument passing, but in general is not preserved by any primitive functions.

If `X` is 1, the result `R` returns an indication of whether `Y` has been marked for hashing or whether the hash has been created:

|`R`|State of `Y`                                                                 |
|---|-----------------------------------------------------------------------------|
|`0`|`Y` has not been marked for hashing                                          |
|`1`|`Y` has been marked for hashing, but the hash tables has not yet been created|
|`2`|`Y` has a hash table                                                         |

If `X` is 2, the result `R` is the unhashed form of `Y`.

<h2 class="example">Examples</h2>
```apl

      R←1500⌶1 2 3    ⍝ R is marked for hashing

      1 (1500⌶)R
1
      S←R             ⍝ S is marked for hashing
      {⍵⍳2 3 5}R      ⍝ R is now hashed
      1 (1500⌶)R
2
      U←(⍴R)⍴R        ⍝ U is not hashed
      U←⊃⊂R           ⍝   ditto
      1 (1500⌶)U
0
```

If `R` is a hashed array then certain forms of modified assignment will preserve and efficiently update the hash table:
```apl

      R,←Y    ⍝ only for scalar or vector R
      R⍪←Y
      R↓⍨←Y   ⍝ only for negative singleton Y
```

<h2 class="example">Examples</h2>
```apl
      R←1500⌶1 2 3 ⍝ R is hashed

      R,←5    ⍝ ,← preserves and updates
              ⍝ the hash table
      R
1 2 3 5
      R⍳2 4 6
2 5 5

      R↓⍨←¯2  ⍝ ↓⍨← preserves and updates
              ⍝ the hash table
      R
1 2
      R⍳2 4 6
2 3 3
```

The *hashed* property survives `)SAVE`/`)LOAD` and `)SAVE`/`)COPY`. It does not currently survive writing to a component file and reading back again.

<!-- Hidden search keywords -->
<div style="display: none;">
  1500⌶
</div>
