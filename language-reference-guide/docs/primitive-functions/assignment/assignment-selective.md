<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment (Selective)</span> <span class="command">(EXP X)←Y</span></h1>

`X` is the *name* of a variable in the workspace, possibly modified by the indexing function `(EXP X[I])←Y`, see [Assignment (Indexed)](assignment-indexed.md).  `EXP` is an expression that **selects** elements of `X`.  `Y` is an array expression. The result of the expression `Y` is allocated to the elements of `X` selected by `EXP`. Note that `X` may refer to a single name only.

The following functions may appear in the selection expression. Where appropriate these functions may be used with axis `[]` and with the Each operator `¨`.

Table: Functions for Selective Assignment {: #Selective_Assignment_Functions }

|----|------------------------------|
|`↑` |Take                          |
|`↓` |Drop                          |
|`,` |Ravel                         |
|`⍪` |Table                         |
|`⌽⊖`|Reverse, Rotate               |
|`⍴` |Reshape                       |
|`⊃` |Disclose, Pick                |
|`⍉` |Transpose (Monadic and Dyadic)|
|`/⌿`|Replicate                     |
|`\⍀`|Expand                        |
|`⌷` |Index                         |
|`∊` |Enlist ( `⎕ML≥1` )            |

Note: Mix and Split (monadic `↑` and `↓`), Type (monadic `∊` when `⎕ML<1`) and Membership (dyadic `∊`) may not be used in the selection expression.

<h2 class="example">Examples</h2>
```apl
      A←'HELLO'
      ((A∊'AEIOU')/A)←'*'
 
      A
H*LL*
 
      Z←3 4⍴⍳12
      (5↑,Z)←0
 
      Z
0  0  0  0
0  6  7  8
9 10 11 12

```
```apl
      MAT←3 3⍴⍳9
      (1 1⍉MAT)←0
 
      MAT
0 2 3
4 0 6
7 8 0
       
      ⎕ML←1⍝ so ∊ is Enlist
      names←'Andy' 'Karen' 'Liam'
      (('a'=∊names)/∊names)←'*'
      names
 Andy  K*ren  Li*m
```

## Each Operator

The functions listed in the table above may also be used with the Each Operator `¨`.

<h2 class="example">Examples</h2>
```apl
      A←'HELLO' 'WORLD'
      (2↑¨A)←'*'
      A
 **LLO  **RLD
 
      A←'HELLO' 'WORLD'
      ((A='O')/¨A)←'*'
      A
 HELL*  W*RLD

      A←'HELLO' 'WORLD'
      ((A∊¨⊂'LO')/¨A)←'*'
      A
 HE***  W*R*D
```

## Bracket Indexing

Bracket indexing may also be applied to the expression on the left of the assignment arrow.

<h2 class="example">Examples</h2>
```apl
      MAT←4 3⍴'Hello' 'World'
      (¯2↑¨MAT[;1 3])←'$'
      MAT
 Hel$$  World  Hel$$ 
 Wor$$  Hello  Wor$$ 
 Hel$$  World  Hel$$ 
 Wor$$  Hello  Wor$$ 

```
