# <span>SelText</span> <span>Property</span>



**Applies To:** [ButtonEdit](../objects/buttonedit.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [Edit](../objects/edit.md), [RichEdit](../objects/richedit.md)

**Description**


This property determines or identifies the portion of text in an object that is currently selected and highlighted. It can be used to pre-select all or part of the text to be replaced or deleted when the user starts typing. It can also be used to query the area of text that the user has highlighted. This can be useful if you want to implement your own cut/paste/replace features.


SelText is always a 2-element integer vector. If the field contents (defined by the [Text](text.md) property) is a vector, SelText is simple. Its first element is the index of the first selected character and its second element is 1 + the index of the last selected character. The length of the selected string is therefore obtained by subtracting the first element from the second.


If there are no characters selected, the two elements are equal and specify the current position of the input cursor.


If the contents is a vector of vectors or a matrix, each element of SelText is a 2-element vector. The first item in each of the elements indexes the vector (in a vector of vectors) or row (in a matrix). The second item in each element indexes the position of the character in the vector or along the row. Again, the value reported for the last character in the selected string is 1 + its index.



