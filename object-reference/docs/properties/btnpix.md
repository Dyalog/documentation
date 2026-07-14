# <span>BtnPix</span> <span>Property</span>

**Applies To:** [Button](../objects/button.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md)

**Description**

This property is used to customise the appearance of a [Button](../objects/button.md), [Menu](../objects/menu.md) or [MenuItem](../objects/menuitem.md). It specifies the names of or refs to up to 3 [Bitmap](../objects/bitmap.md) objects to be used to display the object under different circumstances. In general, BtnPix is a 3-element vector of character vectors or refs. However, if it defines a single [Bitmap](../objects/bitmap.md), it may be a single ref, a simple character scalar or vector, or an enclosed character vector.

The first [Bitmap](../objects/bitmap.md) is displayed when the object is shown in its normal state. For a [Button](../objects/button.md), this is when its [State](state.md) is 0. The second [Bitmap](../objects/bitmap.md) is used for a [Menu](../objects/menu.md) or [MenuItem](../objects/menuitem.md), when the object is selected (highlighted), or for a [Button](../objects/button.md) when its [State](state.md) is 1. The third [Bitmap](../objects/bitmap.md) is used when the object is disabled by having its [Active](active.md) property set to 0.

For a [Button](../objects/button.md) with [Style ](style.md)`'Push'`, this means that when the user clicks the [Button](../objects/button.md), its appearance switches from the first to the second [Bitmap](../objects/bitmap.md), and then back again. To maintain the standard 3-D appearance, the [Bitmap](../objects/bitmap.md)s should contain the correct shadow lines around their edges. For [Button](../objects/button.md)s with [Style ](style.md)`'Radio'` or `'Check'`, the [Button](../objects/button.md) will display one or other of the two [Bitmap](../objects/bitmap.md)s according to its current [State](state.md).

For example, to have a [Button](../objects/button.md) that displays a "Tick" or a "Cross" according to its [State](state.md):
```apl
      'YES' ⎕WC 'Bitmap' 'C:\WDYALOG\YES.BMP'
      'NO'  ⎕WC 'Bitmap' 'C:\WDYALOG\NO.BMP'
      'f1.r1' ⎕WC 'Button'('Style' 'Check')
                          ('BtnPix' 'YES' 'NO')
```
