---
search:
  boost: 2
---

# <span>Partition</span> `R←X⊆[K]Y`{{key}}

!!! Info "Information"
    The symbol `⊆` (Left Shoe Underbar) is not available in Classic Edition, and _partition_ is instead represented by `⎕U2286`.

`Y` may be any non-scalar array.

`X` must be a simple scalar or vector of non-negative integers.

The axis specification is optional.  If present, it must be a simple integer scalar or one element array representing an axis of `Y`.  If absent, the last axis is implied.

`R` is an array of the elements of `Y` partitioned according to `X`.

A new partition is started in the result whenever the corresponding element in `X` is greater than the previous one. Items in `Y` corresponding to `0`s in `X` are not included in the result.

If `⎕ML≥3`, the symbol `⊂` means the same as `⊆`.

<h2 class="example">Examples</h2>
```apl
      ⎕ML←3
      ]Boxing ON
Was OFF
      1 1 1 2 2 3 3 3⊆'NOWISTHE'
┌───┬──┬───┐
│NOW│IS│THE│
└───┴──┴───┘
      1 1 1 0 0 3 3 3⊆'NOWISTHE'
┌───┬───┐
│NOW│THE│
└───┴───┘
      TEXT←'   NOW     IS      THE      TIME    '
      (' '≠TEXT)⊆TEXT
┌───┬──┬───┬────┐
│NOW│IS│THE│TIME│
└───┴──┴───┴────┘
```


```apl
      NMAT←[
      0  100 150
      0    0 350
      0 1000 500
      ]
      COLS←'Jan' 'Feb' 'Mar'
      ROWS←'Cakes' 'Biscuits' 'Buns'
      CMAT←⎕FMT(' ',ROWS),COLS⍪NMAT
      CMAT
           Jan   Feb  Mar 
 Cakes       0   100  150 
 Biscuits    0     0  350 
 Buns        0  1000  500 

      (∨⌿' '≠CMAT)⊆CMAT   ⍝ Split at blank cols.
┌────────┬───┬────┬───┐
│        │Jan│ Feb│Mar│
├────────┼───┼────┼───┤
│Cakes   │  0│ 100│150│
├────────┼───┼────┼───┤
│Biscuits│  0│   0│350│
├────────┼───┼────┼───┤
│Buns    │  0│1000│500│
└────────┴───┴────┴───┘

      N←4 4⍴⍳16
      N
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
      1 1 0 1⊆N
┌─────┬──┐
│1 2  │4 │
├─────┼──┤
│5 6  │8 │
├─────┼──┤
│9 10 │12│
├─────┼──┤
│13 14│16│
└─────┴──┘
      1 1 0 1⊆[1]N
┌───┬───┬───┬───┐
│1 5│2 6│3 7│4 8│
├───┼───┼───┼───┤
│13 │14 │15 │16 │
└───┴───┴───┴───┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
   ⊆ partition
</div>
