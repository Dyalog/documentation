<div style="display: none;">
  ⌸
</div>

<h1 class="heading"><span class="name">Key</span> <span class="command">R←{X}f⌸Y</span></h1>

!!! note "Classic Edition"
    The symbol `⌸` is not available in Classic Edition, and the Key operator is instead represented by `⎕U2338`.

`f` may be any dyadic function that returns a result.

If `X` is specified, it is an array whose major cells specify keys for corresponding major cells of `Y`.  The Key operator `⌸` applies the function `f` to each unique key in `X` and the major cells of `Y` having that key.

If `X` is omitted, `Y` is an array whose major cells represent keys. In this case, the Key operator applies the function `f` to each unique key in  `Y` and the  elements of `⍳≢Y` having that key.  `f⌸Y` is the same as `Y f⌸⍳≢Y`.

The elements of `R` appear in the order in which they first appear in `Y`.

Key is similar to the GROUP BY clause in SQL.

`⎕CT` and `⎕DCT` are  implicit arguments of the Key operator.

<h2 class="example">Example</h2>

In this example, both arrays are vectors so their major cells are their elements. The function `{⍺':'⍵}` is applied between the unique elements in `suits` (`'Spades' 'Hearts' 'Clubs'`) and the elements in `cards` grouped according to their corresponding elements in `suits`, that is, (`'2' 'Ace'`), (`'Queen' 'Jack'`) and (`,'4'`).
```apl
      cards←'2' 'Queen' 'Ace' '4' 'Jack'
      suits←'Spades' 'Hearts' 'Spades' 'Clubs' 'Hearts'

      suits,[1.5]cards
 Spades  2     
 Hearts  Queen 
 Spades  Ace   
 Clubs   4     
 Hearts  Jack
  
       suits {⍺':'⍵}⌸ cards
  Spades  : 2 Ace         
  Hearts  :  Queen  Jack  
  Clubs   : 4
```

## Monadic Examples
```apl

      {⍺ ⍵} ⌸ suits ⍝ indices of unique major cells
  Spades   1 3 
  Hearts   2 5 
  Clubs    4
  
      {⍺,≢⍵} ⌸ suits ⍝ count of unique major cells
 Spades  2
 Hearts  2
 Clubs   1

```
```apl
       letters←'zabayza'
       {⍺(≢⍵)}⌸letters
z 2
a 3
b 1
y 1
```

## Further Examples

`x` is a vector of stock codes, `y` is a corresponding matrix of values.
```apl
      ⍴x
10
      ⍴y
10 2
     x,y
 IBM   13 75
 AAPL  45 53
 GOOG  21  4
 GOOG  67 67
 AAPL  93 38
 MSFT  51 83
 IBM    3  5
 AAPL  52 67
 AAPL   0 38
 IBM    6 41
```

If we apply the function `{⍺ ⍵}` to `x` and `y` using the `⌸` operator, we can see how the rows (its major cells) of `y` are grouped according to the corresponding elements (its major cells) of `x`.
```apl
      x{⍺ ⍵}⌸y
 IBM   13 75 
        3  5 
        6 41 
 AAPL  45 53 
       93 38 
       52 67 
        0 38 
 GOOG  21  4 
       67 67 
 MSFT  51 83       
```

More usefully, we can apply the function `{⍺(+⌿⍵)}`, which delivers the stock codes and the corresponding totals in `y`:
```apl
      x{⍺(+⌿⍵)}⌸y
  IBM    22 121  
  AAPL   190 196 
  GOOG   88 71   
  MSFT   51 83   
```

There is no need for the function to use its left argument. So to obtain just the totals in `y` grouped by the stock codes in `x`:
```apl
       x{+⌿⍵}⌸y
 22 121
190 196
 88  71
 51  83
```

## Defined Function Example

This example appends the data for a stock into a component file named by the symbol.
```apl
     ∇ r←stock foo data;fid;file
[1]    file←⊃stock
[2]    :Trap 0
[3]        fid←file ⎕FTIE 0
[4]        file ⎕FERASE fid
[5]    :EndTrap
[6]    fid←file ⎕FCREATE 0
[7]    r←data ⎕FAPPEND fid
[8]    ⎕FUNTIE fid
     ∇
```
```apl
     x foo⌸y
1 1 1 1
```

<h2 class="example">Example</h2>
```apl

      {⍺ ⍵} ⌸ suits ⍝ indices of unique major cells
  Spades   1 3 
  Hearts   2 5 
  Clubs    4
  
      {⍺,≢⍵} ⌸ suits ⍝ count of unique major cells
 Spades  2
 Hearts  2
 Clubs   1

```

## Another Example

Given a list of names and scores., the problem is to sum the scores for each unique name. A solution is presented first without using the Key operator, and then with the Key operator.
```apl
      names ⍝ 12, some repeat
 Pete  Jay  Bob  Pete  Pete  Jay  Jim  Pete  Pete  Jim
 Pete  Pete 

      (∪names)∘.≡names
1 0 0 1 1 0 0 1 1 0 1 1
0 1 0 0 0 1 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1 0 0

      scores
66 75 71 100 22 10 67 77 55 42 1 78

      b←↓(∪names)∘.≡names
      ]disp b/¨⊂⍳12
┌→──────────────┬───┬─┬────┐
│1 4 5 8 9 11 12│2 6│3│7 10│
└~─────────────→┴~─→┴→┴~──→┘

      +/¨b/¨⊂scores
399 85 71 109

      ]disp {⊂⍵}⌸ names
┌→──────────────┬───┬─┬────┐
│1 4 5 8 9 11 12│2 6│3│7 10│
└~─────────────→┴~─→┴→┴~──→┘

      names {+/⍵}⌸ scores
399 85 71 109
```
