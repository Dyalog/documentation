---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕IO IO
</div>

# <span>Index Origin</span> `⎕IO`

`⎕IO` determines the index of the first element of a non-empty vector.

`⎕IO` may be assigned the value 0 or 1.  The value in a clear workspace is 1. `⎕IO` has Namespace scope.

`⎕IO` is an implicit argument of any function derived from the bracket axis (`[K]`), of the monadic functions Fix (`⎕FX`), Grade Down (`⍒`), Grade Up (`⍋`), Index Generator (`⍳`), Roll (`?`), and Where (`⍸`), and of the dyadic functions Deal (`?`), Grade Down (`⍒`), Grade Up (`⍋`), Index (`⌷`), Index Of (`⍳`), Indexed Assignment, Indexing, Pick (`⊃`), Transpose (`⍉`), Interval Index (`⍸`), and Dyadic Format (`⎕FMT`).

<h2 class="example">Examples</h2>
```apl
        ⎕IO←1
        ⍳5
1 2 3 4 5
 
        ⎕IO←0
        ⍳5
0 1 2 3 4
 
        +/[0]2 3⍴⍳6
3 5 7
 
        'ABC',[¯.5]'='
ABC
===
```
