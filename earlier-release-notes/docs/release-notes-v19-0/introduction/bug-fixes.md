<h1 class="heading"><span class="name">Bug Fixes</span></h1>

A number of bug fixes implemented in Version {{ version_majmin }} may change the way that existing code operates and are therefore documented in this section.

- When **APL_COMPLEX_AS_V12** is set, the circular functions `(X○Y)` with `(|X)>7`, generate `DOMAIN ERROR` if the result would be complex.
- Previously, if GetTextSize was given an invalid font name it would use the default for the window that the method was invoked in. Now, invalid font names correctly generate `DOMAIN ERROR`.
- `⎕FMT` using the `E` qualifier now behaves as intended.
```apl
       'E13.6' ⎕FMT ¯4.56789E¯12 ¯4.56789E¯123 ⍝ previous
 ¯4.56789E¯12
 ¯4.5678E¯123

       'E13.6' ⎕FMT ¯4.56789E¯12 ¯4.56789E¯123 ⍝ new
¯4.56789E¯12
¯4.56789E¯123  ⍝ NEW - note alignment of the 'E's!

⍝ Old behaviour - note ¯1.234 printed as ¯1.23
⍝ despite 4 digits requested

```
```apl
        '|',('E12.4' ⎕FMT ¯1.234E¯123),'|'
|  ¯1.23E¯123|

⍝ NEW behaviour - honour request for 4 digits
        '|',('E12.4' ⎕FMT ¯1.234E¯123),'|'
| ¯1.234E¯123|

⍝ Honouring request can now prevent fitting!

        '|',('E10.4' ⎕FMT ¯1.234E¯123),'|'  ⍝ Old
|¯1.23E¯123|

        '|',('E10.4' ⎕FMT ¯1.234E¯123),'|'  ⍝ NEW
|**********|
```
