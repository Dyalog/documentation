<div style="display: none;">
  ⍒
</div>

<h1 class="heading"><span class="name">Dyadic Grade Down</span> <span class="command">R←X⍒Y</span></h1>

`Y` must be a simple character array of rank greater than 0. `X` must be a simple character array of rank 1 or greater. `R` is a simple integer vector of shape `1↑⍴Y` containing the permutation of `⍳1↑⍴Y` that places the sub-arrays of `Y` along the first axis in descending order according to the collation sequence `X`. The indices of any set of identical sub-arrays in `Y` occur in `R` in ascending order.

If `X` is a vector, the following identity holds:
```apl
      X⍒Y ←→ ⍒X⍳Y
```

A left argument of rank greater than 1 allows successive resolution of duplicate orderings in the following way.

Starting with the last axis:

- The characters in the right argument are located along the current axis of the left argument.  The position of the first occurrence gives the ordering value of the character.
- If a character occurs more than once in the left argument its lowest position along the current axis is used.
- If a character of the right argument does not occur in the left argument, the ordering value is one more than the maximum index of the current axis - as with dyadic iota.

The process is repeated using each axis in turn, from the last to the first, resolving duplicates until either no duplicates result or all axes have been exhausted.

For example, if index origin is 1:

|Left argument:       |Right argument:       |
|---------------------|----------------------|
| `abc`               | `ab`                 |
| `ABA`               | `ac`                 |
| &nbsp;              | `Aa`                 |
| &nbsp;              | `Ac`                 |

Along last axis:

|Character:            |Value:                    |Ordering:       |
|----------------------|--------------------------|----------------|
| `ab`                 | `1 2`                    | `3`            |
| `ac`                 | `1 3`                    | =1   <-duplicate ordering with |
| `Aa`                 | `1 1`                    | `4`            |
| `Ac`                 | `1 3`                    | =1   <-respect to last axis.   |

Duplicates exist, so resolve these with respect to the first axis:

|Character:       |Value:             |Ordering:     |
|-----------------|-------------------|--------------|
| `ac`            | `1 1`             | `2`          |
| `Ac`            | `2 1`             | `1`          |

So the final row ordering is:
```
        ab              3
        ac              2
        Aa              4
        Ac              1
```

That is, the order of rows is 4 2 1 3 which corresponds to a descending row sort of:
```
        Ac              1
        ac              2
        ab              3
        Aa              4
```

<h2 class="example">Examples</h2>
```apl
      ⍴S1
2 27
      S1
 ABCDEFGHIJKLMNOPQRSTUVWXYZ
 abcdefghijklmnopqrstuvwxyz
      S2
 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
      S3
 AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
      S4
 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```


The following results are tabulated for comparison:
```
X       X[S1⍒X;]    X[S2⍒X;]    X[S3⍒X;]    X[S4⍒X;]
FIRsT     TAPE        rAT         TAPE        TAPE
TAP       TAP         fIRST       TAP         TAP
RATE      RATE        TAPE        rAT         RATE
FiRST     rAT         TAP         RATE        rAT
FIRST     RAT         RATE        RAT         RAT
rAT       MAT         RAT         MAT         MAT
fIRST     fIRST       MAT         fIRST       FIRsT
TAPE      FiRST       FiRST       FiRST       FiRST
MAT       FIRsT       FIRsT       FIRsT       FIRST
RAT       FIRST       FIRST       FIRST       fIRST
```

`⎕IO` is an implicit argument of Grade Down.


