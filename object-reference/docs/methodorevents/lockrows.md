# <span>LockRows</span> <span>Method 226</span>

**Description**

This method is used to lock one or more Rows of a [Grid](../objects/grid.md).
However, LockRows is not supported in combination with hierarchical row titles
as specified by the [RowTitleDepth](../properties/rowtitledepth.md) property.

The argument to LockRows is a 1 or 2-element vector as follows.

|-----|---------|--------------------------------|
|`[1]`|Row(s)   |integer scalar, vector or matrix|
|`[2]`|Lock flag|0 or 1                          |

*Row(s)* may be a scalar or a vector specifying the row or rows to be
locked or unlocked. Alternatively, it may be a matrix whose first row specifies
the data rows to be locked and whose second row specifies *where* in the
Grid they are to be locked.

If the *Lock flag* is 1, the corresponding rows are locked. This is the
default and may be omitted. If the *Lock flag* is 0, the corresponding rows
are unlocked.

<h2 class="example">Examples</h2>
```apl
      F.G.LockRows 3         ⍝Lock 3rd row
      F.G.LockRows 3 0       ⍝Unlock 3rd row
      F.G.LockRows (4 5)     ⍝Lock 4th and 5th rows
      F.G.LockRows (2 1⍴8 4) ⍝Lock row 8 at 4
      F.G.LockRows 3         ⍝Lock 3rd row
      F.G.LockRows 3 0       ⍝Unlock 3rd row
      F.G.LockRows (4 5)     ⍝Lock 4th and 5th rows
      F.G.LockRows (2 1⍴8 4) ⍝Lock row 8 at 4
```

The result is an integer matrix containing the indices of all locked rows and
the positions at which they are currently locked.

The expression:
```apl
      F.G.LockRows ⊂⍬
```

may therefore be used to obtain the indices of the locked rows, and
```apl
      F.G.LockRows(F.G.LockRows ⊂⍬) 0
```

unlocks all currently locked rows.

Locks are additive. If row 4 is locked, locking row 5 results in both rows 4
and 5 being locked.

A locked row remains fixed in position and does not scroll vertically. The
user may enter and edit cells in a locked row in the normal way, but the
behaviour of the various cell movement keys (Tab, up and down cursor, and so
forth) differs when a locked row is encountered. As a general rule, if a
keystroke attempts to move the cursor into a locked row from an adjacent row,
and the adjacent row has been scrolled, it is unscrolled and the cursor remains
in the (new) row adjacent to the fixed row. If not, the cursor moves into the
locked row.

When you lock a row, the position you specify for it to be locked at is a
position *in the data* and not the physical position of the column as
displayed in the Grid. The physical column in the Grid depends upon the value of
the Index property at the time it was locked.

If `R` is the value specified for where a
given row is to be locked, the value of the physical row `P` at which it will be displayed in the Grid named `GRID` is given by the expression:
```apl
P←R-(⊃GRID ⎕WG 'Index')-⎕IO
```

Furthermore, the position of a locked row given by the result of the LockRows
method changes (with the Index property) as the Grid is scrolled.

**Application**

Objects: [Grid](../objects/grid.md)
