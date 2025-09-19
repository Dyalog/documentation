<div style="display: none;">
  ⍋
</div>






<h1 class="heading"><span class="name">Dyadic Grade Up</span> <span class="command">R←X⍋Y</span></h1>



`Y` must be a simple character array of rank greater than 0. `X` must be a simple character array of rank 1 or greater. `R` is a simple integer vector being the permutation of `⍳1↑⍴Y` that places the sub-arrays of `Y` along the first axis in ascending order according to the collation sequence `X`.


If `X` is a vector, the following identity holds:
```apl
      X⍋Y ←→ ⍋X⍳Y
```


If `X` is a higher-rank array, each axis of `X` represents a grading attribute in increasing order of importance (the first axis is the least significant and the last axis is the most significant).  If a character is repeated in `X`, it is treated as though it were located at the position in the array determined by the lowest index in each axis for all occurrences of the character.  The character has the same weighting as the character located at the derived position in `X`.


<h2 class="example">Examples</h2>
```apl
      (2 2⍴'ABBA') ⍋ 'AB'[?5 2⍴2] ⍝ A and B are equivalent
1 2 3 4 5
 
        ]display A←2 14⍴' abcdegiklmnrt ABCDEGIKLMNRT'
┌→─────────────┐
↓ abcdegiklmnrt│
│ ABCDEGIKLMNRT│
└──────────────┘
 
      V←'Ab' 'AB' 'aba' 'ABA' 'abaca' 'abecedarian'
      V,←'Abelian' 'black' 'blackball' 'black belt'
      V,←'blacking' 'Black Mass'
 
      ]display M←↑V
┌→──────────┐
↓Ab         │
│AB         │
│aba        │
│ABA        │
│abaca      │
│abecedarian│
│Abelian    │
│black      │
│blackball  │
│black belt │
│blacking   │
│Black Mass │
└───────────┘
```
```apl

 
      ]display M (M[(,A)⍋M;]) (M[(,⍉A)⍋M;]) (M[A⍋M;])
┌→────────────────────────────────────────────────────────┐
│ ┌→──────────┐ ┌→──────────┐ ┌→──────────┐ ┌→──────────┐ │
│ ↓Ab         │ ↓aba        │ ↓aba        │ ↓Ab         │ │
│ │AB         │ │abaca      │ │abaca      │ │AB         │ │
│ │aba        │ │abecedarian│ │abecedarian│ │aba        │ │
│ │ABA        │ │black      │ │Ab         │ │ABA        │ │
│ │abaca      │ │black belt │ │Abelian    │ │abaca      │ │
│ │abecedarian│ │blackball  │ │AB         │ │abecedarian│ │
│ │Abelian    │ │blacking   │ │ABA        │ │Abelian    │ │
│ │black      │ │Ab         │ │black      │ │black      │ │
│ │blackball  │ │Abelian    │ │black belt │ │black belt │ │
│ │black belt │ │AB         │ │blackball  │ │Black Mass │ │
│ │blacking   │ │ABA        │ │blacking   │ │blackball  │ │
│ │Black Mass │ │Black Mass │ │Black Mass │ │blacking   │ │
│ └───────────┘ └───────────┘ └───────────┘ └───────────┘ │
└∊────────────────────────────────────────────────────────┘'
```


