# <span>RowSetVisibleDepth</span> <span>Method 173</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This method is used to set the maximum visible depth of data in rows of a [Grid](../objects/grid.md).


The argument to RowSetVisibleDepth is a numeric scalar as follows


|-----|-----|-------|
|`[1]`|Depth|integer|


All rows in the grid that have a value of [RowTreeDepth](../properties/rowtreedepth.md) less than or equal to *Depth* are expanded. Rows with a value of [RowTreeDepth](../properties/rowtreedepth.md) greater than *Depth* are collapsed.


Note:[ Expanding](./expanding.md) and [Retracting](./retracting.md) events are not generated when this method is called.




<h2 class="example">Examples</h2>
```apl
      'F'⎕WC'Form' 'Grid: TreeView Feature'
      'F.G'⎕WC'Grid'(30 2⍴2/⍳30)
      F.G.RowTreeDepth←30⍴0 1 2 2
```


![](../img/gridtree1.gif)
```apl
      F.G.RowSetVisibleDepth 1
```


![](../img/gridtree12.gif)

```apl
      F.G.RowSetVisibleDepth 99
```


![](../img/gridtree13.gif)


