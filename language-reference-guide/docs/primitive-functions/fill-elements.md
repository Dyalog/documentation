---
search:
  exclude: true
---

<h1 class="heading"><span class="name">Fill Elements</span></h1>

Some primitive functions may include fill elements in their result.  The fill element for an array is the enclosed type of the disclose of the array (`⊂∊⊃Y` for array `Y` with `⎕ML←0`).  The Type function (`∊` with `⎕ML←0`) replaces a numeric value with zero and a character value with `' '`.

The Disclose function (`⊃`) returns the first item of an array.  If the array is empty, `⊃Y` is the PROTOTYPE of `Y`.  The prototype is the type of the first element of the original array.

Primitive functions which may return an array including fill elements are Expand (`\` or `⍀`), Replicate (`/` or `⌿`), Reshape (`⍴`) and Take (`↑`).

<h2 class="example">Examples</h2>
```apl

      ML←0
      ∊⍳5
0 0 0 0 0
 
      ∊⊃(⍳3)('ABC')
0 0 0
 
      ⊂∊⊃(⍳3)('ABC')
 0 0 0
 
      ⊂∊⊃⊂(⍳3)('ABC')
  0 0 0
 
      A←'ABC' (1 2 3)
      A←0⍴A
      ⊂∊⊃A
 
      ' '=⊂∊⊃A
 1 1 1
```
