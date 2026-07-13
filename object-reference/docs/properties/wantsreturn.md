# <span>WantsReturn</span> <span>Property</span>



**Applies To:** [Edit](../objects/edit.md), [RichEdit](../objects/richedit.md)

**Description**


This Boolean property specifies the behaviour of the Enter key for a multi-line [Edit](../objects/edit.md) (Style `'Multi'`) and a [RichEdit](../objects/richedit.md) object.


A value of 0 means that the Enter key is ignored by the [Edit](../objects/edit.md) or [RichEdit](../objects/richedit.md). Instead, the Enter key will (if appropriate) cause a Select event on a Button in the same Form. The user must press Ctrl+Enter to input a new line.


A value of 1 means that pressing the Enter key will introduce a new line into the object.


WantsReturn must be established when the object is created by `⎕WC` and may not subsequently be altered using `⎕WS`. Its default value is 0 in an Edit and 1 in a RichEdit.



