# <span>Align</span> <span>Property</span>

[**Applies To**](../propertyapplies/align.md)

**Description**


For an [Animation](../objects/animation.md), the Align property may be `'None'` or `'Centre'` (`'Center'`). If Align is `'None'`, the [Animation](../objects/animation.md) window is automatically resized to fit the AVI being played. If Align is `'Centre'`, the AVI is centred in the [Animation](../objects/animation.md) window. If the window is too small, the AVI is clipped.



For a [Button](../objects/button.md), [Menu](../objects/menu.md), or [MenuItem](../objects/menuitem.md) the Align property may be `'None'`, `'Left'` or `'Right'`. If the [Button](../objects/button.md) Style is `'Radio'` or `'Check'` this property specifies the position of the text relative to the button symbol. The default is `'Right'`. For a [Button](../objects/button.md) with Style `'Push'`, the value of Align is `'None'`.


For a [Button](../objects/button.md) with Style `'Radio'` or `'Check'` that is created as a child of a Grid the value of the Align property may also be `'Centre'` or `'Center'.` Either of these values causes the symbol part of the [Button](../objects/button.md) (the circle or checkbox) to be centred within the corresponding Grid cell(s).


For a [DateTimePicker](../objects/datetimepicker.md), the Align property specifies the horizontal alignment of the drop-down Calendar which may be `'Left'` (the default) or `'Right'`. This applies only if the Style of the DateTimePicker is `'Combo'`.


For a single-line [Edit](../objects/edit.md), Align specifies the vertical alignment of the text. It may be `'None'` (the default), `'Centre'` or `'Center'`.


For a [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), or [StatusField](../objects/statusfield.md), Align `'Right'` is used to position the object at the right end of its parent [MenuBar](../objects/menubar.md) or [StatusBar](../objects/statusbar.md). `'None'` is equivalent to `'Left'` which is the default.


For objects of type [CoolBar](../objects/coolbar.md), [Splitter](../objects/splitter.md), [Scroll](../objects/scroll.md), [StatusBar](../objects/statusbar.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md) and [ToolControl](../objects/toolcontrol.md), Align may be `'None'`, `'Top'`, `'Bottom'`, `'Left'` or `'Right'`. It specifies to which (if any) of the four sides of the parent the object is anchored and also the default position and size of the object. Specifying Align typically causes the [Attach](attach.md) property to be set to appropriate values as follows :


|----------|----------------------------------|
|`Align`   |`Attach`                          |
|`'Top'`   |`'Top' 'Left' 'Top' 'Right'`      |
|`'Bottom'`|`'Bottom' 'Left' 'Bottom' 'Right'`|
|`'Left'`  |`'Top' 'Left' 'Bottom' 'Left'`    |
|`'Right'` |`'Top' 'Right' 'Bottom' 'Right'`  |


These settings cause the object to remain at a fixed distance (in pixels) from the corresponding edge of the parent. Furthermore, the object will have a fixed height or width, but its length will stretch and shrink as the [Form](../objects/form.md) is resized.


Note that this does not apply to a [TabControl](../objects/tabcontrol.md) for which the default value of Attach is `'None'  'None'  'None'  'None'`, regardless of the value of Align.


The default value of Align is `'Right'` for a vertical [Scroll](../objects/scroll.md), `'Bottom'` for a horizontal [Scroll](../objects/scroll.md), and `'Top'` for a [CoolBar](../objects/coolbar.md), [TabBar](../objects/tabbar.md), [TabControl](../objects/tabcontrol.md), [ToolBar](../objects/toolbar.md) and [ToolControl](../objects/toolcontrol.md). Furthermore, unless [Posn](posn.md) and [Size](size.md) are specified explicitly, the object is placed along the corresponding edge of its parent.


For a [Scroll](../objects/scroll.md) object, Align also determines the direction of a [Scroll](../objects/scroll.md) object unless it is overridden by setting [HScroll](hscroll.md) or [VScroll](vscroll.md) directly. If neither [HScroll](hscroll.md) or VScroll is defined and Align is `'Top'` or `'Bottom'`, a horizontal scrollbar is provided. If neither [HScroll](hscroll.md) or [VScroll](vscroll.md) is defined and Align is `'None'`, `'Left'` or `'Right'`, a vertical scrollbar is provided.

!!! note
    The value of the Align property may **only** be assigned by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and may **not** be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws).


