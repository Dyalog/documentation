---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VFI VFI
</div>





<h1 class="heading"><span class="name">Verify & Fix Input</span> <span class="command">R←{X}⎕VFI Y</span></h1>




`Y` must be a simple character scalar or vector. `X` is optional.  If present, `X` must be a simple character scalar or vector.  `R` is a nested vector of length two whose first item is a simple logical vector and whose second item is a simple numeric vector of the same length as the first item of `R`.



`Y` is the character representation of a series of numeric constants.  If `X` is omitted, adjacent numeric strings are separated by one or more blanks.  Leading and trailing blanks and separating blanks in excess of one are redundant and ignored.  If `X` is present, `X` specifies one or more alternative separating characters.  Blanks in leading and trailing positions in `Y` and between numeric strings separated also by the character(s) in `X` are redundant and ignored.  Leading, trailing and adjacent occurrences of the character(s) in `X` are not redundant.  The character 0 is implied in `Y` before a leading character, after a trailing character, and between each adjacent pair of characters specified by `X`.


The length of the items of `R` is the same as the number of identifiable strings (or implied strings) in `Y` separated by blank or the value of `X`.  An element of the first item of `R` is 1 where the corresponding string in `Y` is a valid numeric representation, or 0 otherwise.  An element of the second item of `R` is the numeric value of the corresponding string in `Y` if it is a valid numeric representation, or 0 otherwise.

<h2 class="example">Examples</h2>
```apl

      ⎕VFI '2 -2 ¯2'
 1 0 1  2 0 ¯2
 
      ⎕VFI '12.1 1E1 1A1 ¯10'
 1 1 0 1  12.1 10 0 ¯10
 
      ⊃(//⎕VFI'12.1 1E1 1A1 ¯10')
12.1 10 ¯10
 
      ','⎕VFI'3.9,2.4,,76,'
 1 1 1 1 1  3.9 2.4 0 76 0
 
      '⋄'⎕VFI'1 ⋄ 2 3 ⋄ 4 '
 1 0 1  1 0 4
      (⍬ ⍬)≡⎕VFI''
1
```


