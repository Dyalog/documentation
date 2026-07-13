# Cells and Sub-arrays

Certain functions and operators operate on particular cells or sub-arrays of an array, which are identified and described as follows.

## K-Cells

A *rank-k* cell or *k-cell* of an array are terms used to describe a sub-array on the last `k` axes of the array. Negative `k` is interpreted as `r+k` where `r` is the rank of the array, and is used to describe a sub-array on the leading `|k` axes of an array.

If `X` is a 3-dimensional array of shape 2 3 4, the 1-cells are its 6 rows each of 4 elements; and its 2-cells are its 2  matrices each of shape 3 4. Its 3-cells is the array in its entirety. Its 0-cells are its individual elements.

## Major Cells

The *major cells* of an array `X` is a term used to describe the sub-arrays on the leading dimension of the array `X` with shape `1↓⍴X`. Using the k-cell terminology, the major cells are its `¯1`-cells.

The major cells of a vector are its elements (0-cells). The major cells of a matrix are its rows (1-cells), and the major cells of a 3-dimensional array are its matrices along the first dimension (2-cells).

<h3 class="example">Examples</h3>

In the following, the major cells of `A`  are 1979, 1990, 1997, 2007, and 2010; those of `B` are `'Thatcher'`, `'Major'`, `'Blair'`, `'Brown'`, and `'Cameron'`; and those of `C` are the four 2-by-3 matrices.
```apl
      A
1979 1990 1997 2007 2010      

      B
Thatcher
Major   
Blair   
Brown   
Cameron

   ⍴B
5 8

    ⎕←C←4 2 3⍴⍳24
 0  1  2
 3  4  5
        
 6  7  8
 9 10 11
        
12 13 14
15 16 17
        
18 19 20
21 22 23

```

Using the k-cell terminology, if `r` is the rank of the array, its major cells are its `r-1`-cells.

Note that if the right operand `k` of the Rank Operator `⍤` is negative, it is interpreted as `0⌈r+k`. Therefore the value `¯1` selects the major cells of the array.
