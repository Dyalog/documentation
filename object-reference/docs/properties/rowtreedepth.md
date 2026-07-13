# <span>RowTreeDepth</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


The RowTreeDepth property specifies the structure of the rows in a [Grid](../objects/grid.md) object. It is either a scalar 0 or an integer vector of the same length as the number of rows in the [Grid](../objects/grid.md). RowTreeDepth is similar to the [Depth](depth.md) property of the [TreeView](../objects/treeview.md) object.


A value of 0 indicates that the corresponding row is a top-level row. A value of 1 indicates that the corresponding row is a child of the most recent row whose RowTreeDepth is 0; a value of 2 indicates that the corresponding row is a child of the most recent row whose RowTreeDepth is 1, and so forth.


When you set RowTreeDepth, the [Grid](../objects/grid.md) is redrawn so that only rows with a RowTreeDepth of 0 are visible.


The [RowSetVisibleDepth](../methodorevents/rowsetvisibledepth.md) method can be used to make data visible to a specific depth.

<h2 class="example">Example</h2>
```apl
      'F'⎕WC'Form' 'Grid: TreeView Feature'
      'F.G'⎕WC'Grid'(30 2⍴2/⍳30)
      F.G.RowTreeDepth←30⍴0 1 2 2
```


![](../img/gridtree1.gif)


The user can interact with the tree images to expand and contract rows of the [Grid](../objects/grid.md).


![](../img/gridtree2.gif)



