<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AT AT
</div>

<h1 class="heading"><span class="name">Attributes</span> <span class="command">R←{X} ⎕AT Y</span></h1>

`Y` can be a simple character scalar, vector or matrix, or a vector of character vectors representing the names of 0 or more defined functions or operators. Used dyadically, this function closely emulates the APL2 implementation. Used monadically, it returns information that is more appropriate for Dyalog APL.

`Y` specifies one or more names. If `Y` specifies a single name as a character scalar, a character vector, or as a scalar enclosed character vector, the result `R` is a vector. If `Y` specifies one or more names as a character matrix or as a vector of character vectors `R` is a matrix with one row per name in `Y`.

## Monadic Use

If `X` is omitted, `R` is a 4-element vector or a 4 column matrix with the same number of rows as names in `Y` containing the following attribute information:

`R[1]` or `R[;1]`: Each item is a 3-element integer vector representing the function header syntax:

|---|---|---|
|1|Function result|0 if the function has no result 1 if the function has an explicit result `¯1` if the function has a shy result|
|2|Function valence|0 if the object is a niladic function or not a function 1 if the object is a monadic function 2 if the object is a dyadic function `¯2` if the object is an ambivalent 				function|
|3|Operator valence|0 if the object is not an operator 1 if the object is a monadic operator 2 if the object is a dyadic operator|

The following values correspond to the syntax shown alongside:
```apl

        0  0  0     ∇ FOO
        1  0  0     ∇ Z←FOO
       ¯1  0  0     ∇ {Z}←FOO
        0 ¯2  0     ∇ {A} FOO B
       ¯1  1  2     ∇ {Z}←(F OP G)B
```

`R[2]` or `R[;2]`: Each item is the (`⎕TS` form) timestamp of the time the function was last fixed.

`R[3]` or `R[;3]`: Each item is an integer reporting the current `⎕LOCK` state of the function:

|---|-------------------------|
|`0`|Not locked               |
|`1`|Cannot display function  |
|`2`|Cannot suspend function  |
|`3`|Cannot display or suspend|

`R[4]` or `R[;4]`: Each item is a character vector - the network ID of the user who last fixed (edited) the function.

<h2 class="example">Example</h2>
```apl

    ∇ {z}←{l}(fn myop)r
[1]   ...

    ∇ z←foo
[1]   ...

    ∇ z←{larg}util rarg
[1]   ...

      ⎕LOCK'foo'

      util2←util
```
```apl


      ]display ⎕AT 'myop' 'foo' 'util' 'util2'
.→--------------------------------------------.
↓ .→------. .→-----------------.     .→---.   |
| |¯1 ¯2 1| |1996 8 2 2 13 56 0|   0 |john|   |
| '~------' '~-----------------'     '----'   |
| .→----.   .→------------.          .⊖.      |
| |1 0 0|   |0 0 0 0 0 0 0|        3 | |      |
| '~----'   '~------------'          '-'      |
| .→-----.  .→------------------.    .→---.   |
| |1 ¯2 0|  |1996 3 1 14 12 10 0|  0 |pete|   |
| '~-----'  '~------------------'    '----'   |
| .→-----.  .→-------------------.   .→-----. |
| |1 ¯2 0|  |1998 8 26 16 16 42 0| 0 |graeme| |
| '~-----'  '~-------------------'   '------' |
'∊--------------------------------------------'
```
## Dyadic Use


The dyadic form of `⎕AT` emulates APL2. It returns the same rank and shape result containing information that matches the APL2 implementation as closely as possible.

The number of elements or columns in `R` and their meaning depends upon the value of `X` which may be 1, 2, 3 or 4.

If `X` is 1, `R` specifies *valences* and contains 3 elements (or columns) whose meaning is as follows:

|---|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
|1  |Explicit result |1 if the object has an explicit result or is a variable 0 otherwise                                                                    |
|2  |Function valence|0 if the object is a niladic function or not a function 1 if the object is a monadic function 2 if the object is an ambivalent function|
|3  |Operator valence|0 if the object is not an operator 1 if the object is a monadic operator 2 if the object is a dyadic operator                          |

If `X` is 2, `R` specifies *fix times* (the time the object was last updated) for functions and operators named in `Y`. The time is reported as 7 integer elements (or columns) whose meaning is as follows. The fix time reported for names in `Y` which are not defined functions or operators is 0.

|---|-------------------------------------------|
|1  |Year                                       |
|2  |Month                                      |
|3  |Day                                        |
|4  |Hour                                       |
|5  |Minute                                     |
|6  |Second                                     |
|7  |Milliseconds (this is always reported as 0)|

If `X` is 3, `R` specifies *execution properties* and contains 4 elements (or columns) whose meaning is as follows:

|---|------------------------|---------------------------------------------------------------------------------------|
|1  |Displayable             |0 if the object is displayable 1 if the object is not displayable                      |
|2  |Suspendable             |0 if execution will suspend in the object 1 if execution will not suspend in the object|
|3  |Weak Interrupt behaviour|0 if the object responds to interrupt 1 if the object ignores interrupt                |
|4  |&nbsp;                  |(always 0)                                                                             |

If `X` is 4, `R` specifies *object size* and contains 2 elements (or columns) that both report the `⎕SIZE` of the object.
