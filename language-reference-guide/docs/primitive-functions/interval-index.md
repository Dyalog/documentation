---
search:
  boost: 2
---

# <span>Interval Index</span> `R←X⍸Y`{{key}}

!!! note "Classic Edition"
    The symbol `⍸` (Iota Underbar) is not available in Classic Edition, and Interval Index is instead represented by `⎕U2378`.

`X` is an ordered non-scalar array that represents a set of intervals or ranges.

Note that the `i`<sup>th</sup> interval starts at  `X[i]`, then includes all subsequent values up to but not including `X[i+1]`.

For example, if `X` is  `(1 3 5)` it defines 4 intervals numbered 0 to 3 as follows.

|---|--------------------------|-----------|
|0  |less than 1               |`<1`       |
|1  |between 1 and 3           |`(≥1)∧(<3)`|
|2  |between 3 and 5           |`(≥3)∧(<5)`|
|3  |greater than or equal to 5|`≥5`       |

If `X` is `'AEIOU'` it defines 6 intervals numbered 0 to 5 as follows:

|---|---------------|------------|
|0  |before A       |`⎕UCS 0,⍳64`|
|1  |between A and E|`ABCD`      |
|2  |between E and I|`EFGH`      |
|3  |between I and O|`IJKLMN`    |
|4  |between O and U|`OPQREST`   |
|5  |U and after    |`UVWXYZ...` |

`Y` is an array of the same type (numeric or character) as `X`.

The result `R` is an integer array that identifies into which interval  the corresponding value in `Y` falls.

Like dyadic `⍳` (see [Index Of](index-of.md)), Interval Index works with major cells. For a vector these are its elements; for a matrix its rows, and so forth.

`X` and `Y` are compared using  the same logic as monadic `⍋` (see [Grade Up](grade-up.md)) which is independent of `⎕CT` and `⎕DCT`.

`⎕IO` is an implicit argument of Interval Index. In all the following examples, `⎕IO` is 1.

<h2 class="example">Example</h2>
```apl

      10 20 30⍸11 1 31 21
1 0 3 2
```

In the above example:

- 11 is between `X[1]` and `X[2]` so the answer is 1.
- 1 is less than  `X[1]` so the answer is 0
- 31 is greater than `X[⍴X]` so the answer is 3
- 21 is between `X[2]` and `X[3]` so the answer is 2.
```apl
      'AEIOU' ⍸ 'DYALOG'
1 5 1 3 4 2
```

And in the alphabetic example above:

- "D" is between `X[1]` and `X[2]`, so the answer is 1
- "Y" is after `X[⍴X]` so the answer is 5
- "A" is between `X[1]` and `X[2]`, so the answer is 1
- as so on ...

<h2 class="example">Example (Classification)</h2>

Commercially, olive oil is graded as follows:

- if its acidity is less than 0.8%, as "Extra Virgin"
- if its acidity is less than 2%, as "Virgin"
- if its acidity is less than 3.3%, as "Ordinary"
- otherwise, as "Lampante"
```apl

     grades←'Extra Virgin' 'Virgin' 'Ordinary' 'Lampante'
     acidity←0.8 2 3.3

     samples←1.3 1.9 0.7 4 .6 3.2
     acidity⍸samples
1 1 0 3 0 2
     samples,⍪grades[1+acidity⍸samples]
┌───┬────────────┐
│1.3│Virgin      │
├───┼────────────┤
│1.9│Virgin      │
├───┼────────────┤
│0.7│Extra Virgin│
├───┼────────────┤
│4  │Lampante    │
├───┼────────────┤
│0.6│Extra Virgin│
├───┼────────────┤
│3.2│Ordinary    │
└───┴────────────┘

```

<h2 class="example">Example (Data Consolidation by Interval)</h2>

`x` represents some data sampled in chronological order at timestamps `t`.
```apl

      ⍴x
200000
      x
3984300 2020650 819000 1677100 3959200 2177250 3431800 ...
```
```apl

      ⍴t
200000 3
```
```apl
      (10↑t) (¯10↑t)
┌─────┬────────┐
│0 0 0│23 59 54│
│0 0 0│23 59 55│
│0 0 0│23 59 56│
│0 0 0│23 59 56│
│0 0 0│23 59 58│
│0 0 2│23 59 58│
│0 0 3│23 59 59│
│0 0 3│23 59 59│
│0 0 4│23 59 59│
│0 0 5│23 59 59│
└─────┴────────┘
```

`u` represents timestamps for 5-minute intervals:
```apl

      ⍴u
288 3
      (10↑u) (¯10↑u)
┌──────┬───────┐
│0  0 0│23 10 0│
│0  5 0│23 15 0│
│0 10 0│23 20 0│
│0 15 0│23 25 0│
│0 20 0│23 30 0│
│0 25 0│23 35 0│
│0 30 0│23 40 0│
│0 35 0│23 45 0│
│0 40 0│23 50 0│
│0 45 0│23 55 0│
└──────┴───────┘
```

Therefore, the expression `(u⍸t){+/⍵}⌸x` summarises `x` in 5-minute intervals.
```apl

      u ⍸ t
1 1 1 1 1 1 1 1 1 1 ... 288 288 288 288 288 288

      (u⍸t) {+/⍵}⌸ x
1339083050 1365108650 1541944750 1393476000 1454347100 ...

      (u⍸t) {(⍺⌷u),+/⍵}⌸ x
 0  0 0 1339083050
 0  5 0 1365108650
 0 10 0 1541944750
 0 15 0 1393476000
   ...
23 45 0 1388823150
23 50 0 1453472350
23 55 0 1492078850

```

### Higher-Rank Left Argument

If `X` is a higher rank array, the function compares sub-arrays in `Y`  with the major cells of  `X`, where a major cell is  a sub-array on the leading dimension of `X` with shape `1↓⍴X`. In this case, the shape of the result `R` is `(1-⍴⍴X)↓⍴Y`.

<h2 class="example">Example</h2>
```apl
      x ← ↑ 'Fi' 'Jay' 'John' 'Morten' 'Roger'
      x
Fi
Jay   
John  
Morten
Roger 
      ⍴x
5 6

```
```apl
      y ← x ⍪ ↑ 'JD' 'Jd' 'Geoff' 'Alpha' 'Omega' 'Zeus  '
      y
Fi
Jay   
John  
Morten
Roger 
JD    
Jd    
Geoff 
Alpha 
Omega 
Zeus

```
```apl
      x ⍸ y
1 2 3 4 5 1 2 1 0 4 5
      y ,⍪ x⍸y
Fi     1
Jay    2
John   3
Morten 4
Roger  5
JD     1
Jd     2
Geoff  1
Alpha  0
Omega  4
Zeus   5
```

<h2 class="example">Further Example</h2>
```apl
      ⍴x
5 6
      ⍴y
3 3 6
      x
Fi    
Jay   
John  
Morten
Roger 
      y
Fi    
Jay   
John  
      
Morten
Roger 
JD    
      
Jd    
Geoff 
Alpha 
      x⍸y
1 2 3
4 5 1
2 1 0

```

<h2 class="example">Nested Array Example</h2>

A card-player likes to sort a hand into suits spades, hearts, diamond, clubs (fortunately alphabetic) and high-to-low within each suit.
```apl
      suits←'Clubs' 'Diamonds' 'Hearts' 'Spades'
      pack←,(⊂¨suits)∘.,1↓14 ⍝ 11=Jack ... 14=Ace
      hand←↑(,pack)[7?52]
      hand←hand[⍒hand;]
      hand
┌────────┬──┐
│Spades  │12│
├────────┼──┤
│Hearts  │12│
├────────┼──┤
│Hearts  │7 │
├────────┼──┤
│Hearts  │2 │
├────────┼──┤
│Diamonds│11│
├────────┼──┤
│Diamonds│9 │
├────────┼──┤
│Clubs   │8 │
└────────┴──┘
```

Another card, the 10 of diamonds is dealt. Where must it go in the hand ?
```apl
      (⊖hand)⍸'Diamonds' 10 ⍝ left arg must be sorted up
2
      (¯2↓hand)⍪'Diamonds' 10⍪¯2↑hand
┌────────┬──┐
│Spades  │12│
├────────┼──┤
│Hearts  │12│
├────────┼──┤
│Hearts  │7 │
├────────┼──┤
│Hearts  │2 │
├────────┼──┤
│Diamonds│11│
├────────┼──┤
│Diamonds│10│
├────────┼──┤
│Diamonds│9 │
├────────┼──┤
│Clubs   │8 │
└────────┴──┘
```

Note that if `(∧/Y∊X)` and `X` is sorted and `⎕CT=0` ,then `x⍸y` is the same as `x⍳y`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍸
</div>
