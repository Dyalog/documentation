# <span>RowHiddenDepth</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


The RowHiddenDepth property is read-only and identifies which rows of a Grid are currently hidden.



RowHiddenDepth is an integer vector with the same number of elements as there are rows in the Grid. The values in RowHiddenDepth indicate the current depth of the row in the visible hierarchy; that is, number of nodes that must be opened to display it. The value 0 means that the corresponding row is visible. The value 1 means that 1 node must be opened to display it; 2 means 2 nodes, and so forth.

<h2 class="example">Example</h2>
```apl
      'F'⎕WC'Form' 'Grid: RowHiddenDepth'     
       F.(Coord Size)←'Pixel'(163 306)         
       'F.G'⎕WC'Grid'(10 2⍴2/⍳10)('Size'F.Size)
       ⎕←F.G.RowTreeDepth←10⍴0 1 2 3
0 1 2 3 0 1 2 3 0 1           

```


![](../img/rowhiddendepth0.png)



With all nodes closed, RowHiddenDepth is the same as RowTreeDepth.
```apl
      F.G.RowHiddenDepth
0 1 2 3 0 1 2 3 0 1

```




The next picture shows the Grid after the user has opened nodes 5,6 and 9.


![](../img/rowhiddendepth1.png)
```apl
      F.G.RowHiddenDepth
0 1 2 3 0 0 0 1 0 0

```



