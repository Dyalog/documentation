<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NAPPEND NAPPEND
</div>






<h1 class="heading"><span class="name">Native File Append</span> <span class="command">{R}←X ⎕NAPPEND Y</span></h1>



This function appends the ravel of its left argument `X` to the end of the designated native file.  `X` must be a simple homogeneous APL array.  `Y` is a 1- or 2-element integer vector.  `Y[1]` is a negative integer that specifies the tie number of a native file.  The optional second element `Y[2]` specifies the data type to which the array `X` is to be converted before it is written to the file.


The shy result is the location of the internal file pointer which will be pointing to the end of the newly written data.


Note that `8 ⎕NINFO ⊃Y` can be used to report the current position of the file pointer.


## Unicode Edition


Unless you specify the data type in `Y[2`], a character array will by default be written using type 80.


If the data will not fit into the specified character width (bytes) `⎕NAPPEND` will fail with a `DOMAIN ERROR`.


As a consequence of these two rules, you must specify the data type (either 160 or 320) in order to write Unicode characters whose code-point are in the range 256-65535 and >65535 respectively.

<h2 class="example">Example</h2>
```apl

			
      n←'test'⎕NCREATE 0
      'abc' ⎕NAPPEND n

      'ταβέρνα'⎕NAPPEND n
DOMAIN ERROR
      'ταβέρνα'⎕NAPPEND n
     ∧

      'ταβέρνα'⎕NAPPEND n 160

      ⎕NREAD n 80 3 0
abc
      ⎕NREAD n 160 7
ταβέρνα
```


To write 2 or more lines, you must insert appropriate end-of-line codes.
```apl
      ('hello',(⎕UCS 13 10),'world')⎕NAPPEND ¯1 ⍝ Windows
      ('hello',(⎕UCS 10),'world')⎕NAPPEND ¯1    ⍝ Other
```


