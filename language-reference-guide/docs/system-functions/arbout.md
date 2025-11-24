---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ARBOUT ARBOUT
</div>






<h1 class="heading"><span class="name">Arbitrary Output</span> <span class="command">{R}←X ⎕ARBOUT Y</span></h1>



`Y` may be a scalar or a simple vector of integer numbers in the range 0-255.


`X` is a simple numeric integer that specifies the output device.

- (Non-Windows platforms only) If `X` is positive or zero, it represents a file descriptor that must have been associated by the command that started Dyalog APL.
- If `X` is negative, it represents the tie number of a file opened by `⎕NTIE` or `⎕NCREATE`.


If `Y` is an empty vector, no codes are sent to the output device.


The shy result `R` is `⍬`.


The operation will fail with a `DOMAIN ERROR` if  `Y` contains anything other than numbers in the range 0-255 or tie numbers associated with currently open native files, or  if the current process does not have permission to write to the specified device.



<h2 class="example">Examples</h2>


Write ASCII digits `'123'` to  stream 9:
```apl
      9 ⎕ARBOUT 49 50 51
```


Write ASCII characters `'ABC'` to `MYFILE`:
```apl
     'MYFILE' ⎕NCREATE ¯1
      ¯1 ⎕ARBOUT 65 66 67

```


Append the string `'Κάλο Πάσχα'` to the same file, and close it:
```apl
      ¯1 ⎕ARBOUT 'UTF-8' ⎕UCS'Κάλο Πάσχα' 
      ⎕NUNTIE ¯1
```



