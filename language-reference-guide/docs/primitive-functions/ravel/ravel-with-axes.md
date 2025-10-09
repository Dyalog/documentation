<div style="display: none;">
  ,
</div>






<h1 class="heading"><span class="name">Ravel with Axes</span> <span class="command">R←,[K]Y</span></h1>



`Y` may be any array.


`K` is either:

- A simple fractional scalar adjacent to an axis of `Y`, or
- A simple integer scalar or vector of axes of `Y`, or
- An empty vector


Ravel with axis can be used with selective specification.


`R` depends on the case of `K` above.


If `K` is a fraction, the result `R` is an array of the same shape as `Y`, but with a new axis of length 1 inserted at the `K`th position.

```apl
      ⍴⍴R ←→ 1+⍴⍴Y
      ⍴R  ←→ (1,⍴Y)[⍋K,⍳⍴⍴Y]
```

<h2 class="example">Examples</h2>

```apl
      ,[0.5]'ABC'
ABC
      ⍴,[0.5]'ABC'
1 3
      ,[1.5]'ABC'
A
B
C
      ⍴,[1.5]'ABC'
3 1
 
      MAT←3 4⍴⍳12
      ⍴,[0.5]MAT
1 3 4
      ⍴,[1.5]MAT
3 1 4
      ⍴,[2.5]MAT
3 4 1
```


If `K` is an integer scalar or vector of axes of `Y`, then:

- `K` must contain contiguous axes of `Y` in ascending order
- `R` contains the elements of `Y` ravelled along the indicated axes


Note that if `K` is a scalar or single element vector, `R ←→ Y`.

```apl
      ⍴⍴R ←→ 1+(⍴⍴Y)-⍴,K
```

<h2 class="example">Examples</h2>

```apl
      M
 1  2  3  4
 5  6  7  8
 9 10 11 12
 
13 14 15 16
17 18 19 20
21 22 23 24
      ⍴M
2 3 4

```

```apl
      ,[1 2]M
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
17 18 19 20
21 22 23 24
      ⍴,[1 2]M
6 4
 
      ,[2 3]M
 1  2  3  4  5  6  7  8  9 10 11 12
13 14 15 16 17 18 19 20 21 22 23 24
 
      ⍴,[2 3]M
2 12
```


If `K` is an empty vector a new last axis of length 1 is created.

```apl
      ⍴R ←→ (⍴Y),1
```

<h2 class="example">Examples</h2>

```apl
      Q1←'January' 'February' 'March'
      ]display Q1
┌→─────────────────────────────┐
│ ┌→──────┐ ┌→───────┐ ┌→────┐ │
│ │January│ │February│ │March│ │
│ └───────┘ └────────┘ └─────┘ │
└∊─────────────────────────────┘
      ]display ,[⍳0]Q1
┌→───────────┐
↓ ┌→──────┐  │
│ │January│  │
│ └───────┘  │
│ ┌→───────┐ │
│ │February│ │
│ └────────┘ │
│ ┌→────┐    │
│ │March│    │
│ └─────┘    │
└∊───────────┘
```


See also: [Ravel](index.md).


