# <span>CheckBoxes</span> <span>Property</span>

**Description**

The CheckBoxes property specifies whether or not check boxes are displayed
alongside items in a [ListView](../objects/listview.md) or [TreeView](../objects/treeview.md) object.

CheckBoxes is a single number with the value 0 (check boxes are not
displayed) or 1 (check boxes are displayed); the default is 0.

For a [TreeView](../objects/treeview.md), CheckBoxes will only be
honoured if the items have pictures associated with them (via the [ImageListObj](imagelistobj.md) and [ImageIndex](imageindex.md) properties).

For a [ListView](../objects/listview.md), CheckBoxes applies to all
settings of the [View](view.md) property.

The GetItemState method can be used to determine if a specific item in a [ListView](../objects/listview.md) or [TreeView](../objects/treeview.md) is checked. The result of the
method will have the 13<sup>th</sup> bit set if the item is checked.
```apl
      STATE←Form.ListView.GetItemState 11
      13⊃⌽(32⍴2)⊤STATE
1
```

The picture below illustrates the effect on the appearance of a [ListView](../objects/listview.md) object, of setting CheckBoxes to 1.

![](../img/lv-cb.gif)

**Application**

Objects: [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)
