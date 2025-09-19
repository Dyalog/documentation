<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NTIE NTIE
</div>






<h1 class="heading"><span class="name">Native File Tie</span> <span class="command">{R}←X ⎕NTIE Y</span></h1>



`⎕NTIE` opens a native file.


`X` is a simple character vector or scalar containing a valid pathname for an existing native file.


`Y` is a 1- or 2-element vector.


`Y[1]` is a negative integer value that specifies an (unused) tie number by which the file may subsequently be referred.



`Y[2]` is optional and specifies the mode in which the file is to be opened.  This is an integer value calculated as the sum of 2 codes.  The first code refers to the type of access needed from users who have already tied the native file.  The second code refers to the type of access you wish to grant to users who subsequently try to open the file while you have it open.


If `Y[2]` is omitted, the system tries to open the file with the default value of 66 (read and write access for this process and for any subsequent processes that attempt to access the file). If this fails, the system attempts to open the file with the value 64 (read access for this process, read and write for subsequent processes).


|Needed from existing users                     ||Granted to subsequent users                     ||
|--------------------------|---------------------|---------------------------|---------------------|
|0                         |read access          |0                          |see note [^1]        |
|1                         |write access         |16                         |no access (exclusive)|
|2                         |read and write access|32                         |read access          |
|&nbsp;                    |&nbsp;               |48                         |write access         |
|&nbsp;                    |&nbsp;               |64                         |read and write access|


On UNIX systems, the second column has no meaning and only the first code (`16|mode`) is passed to the `open(2)` call as the access parameter. See include file `fcntl.h` for details. See also [Native File Lock](nlock.md) which is not platform dependent.


`R` is the tie number by which the file may subsequently be referred. If `Y[1]` is a negative integer, then `R` is a shy result; if `Y[1]` is 0, `R` is an explicit result.

## Automatic Tie Number Allocation


A tie number of 0 as argument to a create or tie operation, allocates, and returns as an explicit result, the first (closest to zero) available tie number. This allows you to simplify code. For example:


from:
```apl
      tie←¯1+⌊/0,⎕NNUMS    ⍝ With next available number,
      file ⎕NTIE tie       ⍝ ... tie file.
```


to:
```apl
      tie←file ⎕NTIE 0     ⍝ Tie with first available no.
```

<h2 class="example">Example</h2>
```apl
ntie←{                  ⍝ tie file and return tie no.
    ⍺←2+64              ⍝ default all access.
    ⍵ ⎕NTIE 0 ⍺         ⍝ return new tie no.
}
```

!!! note
    If the native file is already tied, executing `⎕NTIE` with the same or a different tie number simply re-ties it with the same or the new tie number. Re-tying a file with a tie number of 0, re-ties it with the same tie number. This feature can be used to re-tie the file using a different mode.




[^1]: The original meaning of this value is no longer relevant. 0 now means the same as 16 (no access).