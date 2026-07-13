---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ARBIN ARBIN
</div>






# <span>Arbitrary Input</span> `R←X ⎕ARBIN Y`{{key}}



This transmits a stream of 8-bit codes in `Y` to an output device specified by `X` prior to reading from an input device specified by `X`.



`Y` may be a scalar or a simple vector of integer numbers in the range 0-255.


`X` may take several forms:


|--------------------------|--------|-------|
|`terminate (input output)`|`⎕ARBIN`|`codes`|
|`terminate input`         |`⎕ARBIN`|`codes`|


## terminate


This is a numeric scalar or vector that specifies how the read operation should be terminated.

- If it is a numeric scalar, it defines the number of bytes to be read.
- If it is a numeric vector, it defines a set of terminating bytes.
- If it is the null vector, the read terminates on Newline (10).



## input


This is a simple numeric scalar that specifies the input device.

- If it is positive or zero, it represents a file descriptor that must have been associated by the command that started Dyalog APL.
- If it is negative, it represents the tie number of a file opened by `⎕NTIE` or `⎕NCREATE`.



## output


If specified, this is a simple numeric integer that identifies the output device.

- If it is positive or zero, it represents a file descriptor that must have been associated by the command that started Dyalog APL.
- If it is negative, it represents the tie number of a file opened by `⎕NTIE` or `⎕NCREATE`.



The result `R` is a simple numeric vector.  Each item of `R` is the numeric representation of an 8-bit code in the range 0 to 255 received from the input device.  The meaning of the code is dependent on the characteristics of the input device.  If a set of delimiters was defined by `terminate`, the last code returned will belong to that set.


`⎕RTL` (Response Time Limit) is an implicit argument of `⎕ARBIN`.  This allows a time limit to be imposed on input.  If the time limit is reached, `⎕ARBIN` returns with the codes read up to that point. This does not apply under Windows.


The operation will fail with a `DOMAIN ERROR` if  `Y` contains anything other than numbers in the range 0-255, or  if the current process does not have permission to read from or write to the specified device(s).


## Examples (UNIX)
```apl
      )SH mkfifo ./fifo

```
```apl

      in←'./fifo'⎕NTIE 0
      out←'./fifo'⎕NTIE 0

```
```apl

      (10 (in out))⎕ARBIN ⎕UCS ⎕D
48 49 50 51 52 53 54 55 56 57

```
```apl

      (⍬ (in out))⎕ARBIN 10
10

```
```apl
⍝ cope with parity on line ending 10
      ((10+0 128) (in out))⎕ARBIN 10
10

```



