---
search:
  boost: 2
---


# <span>Native File Tie</span> `{R}←X ⎕NTIE Y`{{key}}

`⎕NTIE` opens a native file.

`X` is a simple character vector or scalar containing a valid pathname for an existing native file.

`Y` is a 1- or 2-element vector.

`Y[1]` is `0` or a negative integer that specifies an unused tie number by which the file can subsequently be referred to. If `Y[1]` is `0`, the system allocates the available tie number closest to zero.

`Y[2]` is optional and specifies the mode in which the file is to be opened.  This is an integer value calculated as the sum of 2 codes.  The first code refers to the type of access needed from users who have already tied the native file.  The second code refers to the type of access you wish to grant to users who subsequently try to open the file while you have it open.

If `Y[2]` is omitted, the system tries to open the file with the default value of 66 (read and write access for this process and for any subsequent processes that attempt to access the file). If this fails, the system attempts to open the file with the value 64 (read access for this process, read and write for subsequent processes).

|Needed from existing users                     ||Granted to subsequent users                     ||
|--------------------------|---------------------|---------------------------|---------------------|
|0                         |read access          |16                         |no access (exclusive)|
|1                         |write access         |32                         |read access          |
|2                         |read and write access|48                         |write access         |
|&nbsp;                    |&nbsp;               |64                         |read and write access|

If `Y[2]` includes no code for subsequent users, they are granted no access, as with `16`.

On Unix systems, the second column has no meaning and only the first code (`16|mode`) is passed to the `open(2)` call as the access parameter. See include file `fcntl.h` for details. See also [Native File Lock](nlock.md) which is not platform dependent.

`R` is the tie number by which the file may subsequently be referred. If `Y[1]` is a negative integer, then `R` is a [shy](../../programming-reference-guide/introduction/results.md#shy-results) result; if `Y[1]` is 0, `R` is an explicit result.

If the native file is already tied, executing `⎕NTIE` with the same or a different tie number re-ties it with that tie number, and a tie number of `0` re-ties it with the tie number it already has. This can be used to re-tie the file with a different mode.

<h2 class="example">Example</h2>

```apl
ntie←{                  ⍝ tie file and return tie no.
    ⍺←2+64              ⍝ default all access.
    ⍵ ⎕NTIE 0 ⍺         ⍝ return new tie no.
}
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NTIE NTIE
</div>
