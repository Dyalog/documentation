# <span>Text</span> <span>Property</span>

[**Applies To**](../propertyapplies/text.md)

**Description**

This property is associated with the text contents of an object and is a character array.

In a [ButtonEdit](../objects/buttonedit.md), [Combo](../objects/combo.md), [StatusField](../objects/statusfield.md), [Spinner](../objects/spinner.md), or a single-line [Edit](../objects/edit.md) object, Text may be a simple scalar or a simple vector.

In a [RichEdit](../objects/richedit.md), a multi-line [Edit](../objects/edit.md) field or in a [MsgBox](../objects/msgbox.md), the value of Text may also be a simple matrix, or a vector of vectors. If so, "new-line" characters are appended to each row of the matrix, or to each vector in a vector of vectors, before being displayed. The user may insert or add a "new-line" character in a multi-line [Edit](../objects/edit.md) by pressing Ctrl-Enter (Enter itself is used to press [Button](../objects/button.md)s).

Note that if word-wrapping is in effect in a multi-line [Edit](../objects/edit.md) object, the structure of Text does not correspond to the lines displayed.

In a [Text](../objects/text.md) object, the value of the Text property may be a simple scalar, an enclosed vector or matrix, a simple vector, a simple matrix, or a vector of enclosed vectors or matrices.

In general, the value of Text returned by [`⎕WG`](../../../language-reference-guide/system-functions/wg) has the same structure that was assigned to it by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or by the most recent call to [`⎕WS`](../../../language-reference-guide/system-functions/ws). New-Line characters entered by the users are removed.

You can copy text into the Windows [Clipboard](../objects/clipboard.md) by using [`⎕WS`](../../../language-reference-guide/system-functions/ws) to set Text for a [Clipboard](../objects/clipboard.md) object. In this case you may specify a simple character scalar, vector or matrix, or a vector of character vectors. If you are retrieving data from the clipboard that has been stored by another application, Text will be either a character vector or a vector of character vectors.

The Text property of a [StatusField](../objects/statusfield.md) is updated automatically if its [Style](style.md) property is set to monitor the status of a key.
