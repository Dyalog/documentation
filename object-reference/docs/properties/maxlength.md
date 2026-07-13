# <span>MaxLength</span> <span>Property</span>



**Applies To:** [ButtonEdit](../objects/buttonedit.md), [Edit](../objects/edit.md), [Spinner](../objects/spinner.md)

**Description**


This property specifies the maximum number of characters that the user may enter in a single-line [Edit](../objects/edit.md) object ( [Style](style.md) `'Single'`) or in the edit field associated with a [Spinner](../objects/spinner.md). It does not apply to a multi-line [Edit](../objects/edit.md) object ([Style ](style.md)`'Multi'`). MaxLength does not limit the length of the vector that you may assign to the [Text](text.md) property using [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws). However, if you overfill the field in this way, the user must delete excess characters before the object will accept further input.



