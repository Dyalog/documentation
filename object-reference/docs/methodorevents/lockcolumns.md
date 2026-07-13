# <span>LockColumns</span> <span>Method 227</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This method is used to lock one or more columns of a [Grid](../objects/grid.md) object. However, LockColumns is not supported in combination with hierarchical
column titles as specified by the [ColTitleDepth](../properties/coltitledepth.md) property.




The argument to LockColumns is a 1 or 2-element vector as follows.


|-----|---------|--------------------------------|
|`[1]`|Column(s)|integer scalar, vector or matrix|
|`[2]`|Lock flag|0 or 1                          |



*Column(s)* may be a scalar or a vector specifying the column or columns
to be locked or unlocked. Alternatively, it may be a matrix whose first row
specifies the columns to be locked and whose second row specifies *where* they are to be locked.


If the *Lock flag* is 1, the corresponding columns are locked. This is
the default and may be omitted. If the *Lock flag* is 0, the corresponding
columns are unlocked

<h2 class="example">Examples</h2>
```apl
      F.G.LockColumns 3         ⍝Lock 3rd column
      F.G.LockColumns 3 0       ⍝Unlock 3rd column
      F.G.LockColumns (4 5)     ⍝Lock 4th & 5th cols
      F.G.LockColumns (2 1⍴8 4) ⍝Lock 8 at 4
      F.G.LockColumns 3         ⍝Lock 3rd column
      F.G.LockColumns 3 0       ⍝Unlock 3rd column
      F.G.LockColumns (4 5)     ⍝Lock 4th & 5th cols
      F.G.LockColumns (2 1⍴8 4) ⍝Lock 8 at 4
```


The result is an integer matrix containing the indices of all locked columns
and the positions at which they are currently locked.



The expression:
```apl
      F.G.LockColumns ⊂⍬
```


may therefore be used to obtain the indices of the locked columns, and:
```apl
      F.G.LockColumns(F.G.LockColumns ⊂⍬) 0
```


unlocks all currently locked columns.



Locks are additive. If column 4 is locked, locking column 5 results in both
columns 4 and 5 being locked.


A locked column remains fixed in position and does not scroll sideways. The
user may enter and edit cells in a locked column in the normal way, but the
behaviour of the various cell movement keys (Tab, left and right cursor, and so
forth) differs when a locked column is encountered. As a general rule, if a
keystroke attempts to move the cursor into a locked column from an adjacent
column, and the adjacent column has been scrolled, it is unscrolled and the
cursor remains in the (new) column adjacent to the fixed column. If not, the
cursor moves into the locked column.


When you lock a column, the position you specify for it to be locked at is a
position *in the data* and not the physical position of the column as
displayed in the [Grid](../objects/grid.md)*.* The physical
column in the [Grid](../objects/grid.md) depends upon the value of the
[Index](../properties/index-property.md) property at the time it was locked.



If `C` is the value specified for where a
given column is to be locked, the value of the physical column `P` at which it will be displayed in the Grid named `GRID` is:
```apl
      P←C-(2⊃GRID ⎕WG 'Index')-⎕IO
```



Furthermore, the position of a locked column given by the result of the
LockColumns method changes (with the [Index](../properties/index-property.md) property) as the [Grid](../objects/grid.md) is scrolled.


