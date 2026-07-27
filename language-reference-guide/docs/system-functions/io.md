---
search:
  boost: 2
---

# <span>Index Origin</span> `⎕IO`

`⎕IO` determines the index of the first element of a non-empty vector.

`⎕IO` may be assigned the value 0 or 1.  The value in a clear workspace is 1. `⎕IO` has Namespace scope.

`⎕IO` is an implicit argument of any function derived from the bracket axis (`[K]`), of the monadic functions _fix_ (`⎕FX`), _grade down_ (`⍒`), _grade up_ (`⍋`), _index generator_ (`⍳`), _roll_ (`?`), and _where_ (`⍸`), of the dyadic functions _deal_ (`?`), _dyadic grade down_ (`⍒`), _dyadic grade up_ (`⍋`), _index_ (`⌷`), _index of_ (`⍳`), indexed assignment, indexing, _pick_ (`⊃`), _dyadic transpose_ (`⍉`), _interval index_ (`⍸`), and of the system function _extended diagnostic message_ (`⎕DMX`).

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

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕IO IO
</div>
