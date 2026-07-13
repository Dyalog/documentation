# <span>RowTreeImages</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


The RowTreeImages property is a simple character vector or ref, or a vector of character vectors or refs, that specifies the names(s) of, or ref(s) to, Bitmap objects that are used to display the tree nodes for a [Grid](../objects/grid.md) object.



Note that images in tree nodes are only displayed if [RowTreeStyle](rowtreestyle.md) is set to `'ImagesOnly'`, `'ImagesAndLines'`, or `'AllImagesAndLines'`.


If RowTreeImages is not specified default images are used.


The Bitmap specified by the 1<sup>st</sup> element of RowTreeImages is used to display *unopened* nodes.


The Bitmap specified by the 2<sup>nd</sup> element of RowTreeImages is used to display *opened* nodes.


The Bitmap specified by the 3<sup>rd</sup> element of RowTreeImages is used to display nodes *without children*.

<h2 class="example">Example</h2>
```apl
      'Closed'⎕WC'Bitmap' 'Folder.bmp'
      'Open'⎕WC'Bitmap' 'FolderOpen.bmp'
      'Item'⎕WC'Bitmap' 'Ideas'
      F.G.RowTreeStyle←'AllImagesAndLines'
      F.G.RowTreeImages←'Closed' 'Open' 'Item'
```


![](../img/gridtree11.gif)


