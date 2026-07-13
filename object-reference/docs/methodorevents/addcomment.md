# <span>AddComment</span> <span>Method 220</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This method is used to add a new comment to a [Grid](../objects/grid.md).




The argument to AddComment is a 3, 4 or 5 element array as follows:


|-----|----------------|---------------|
|`[1]`|Row             |integer        |
|`[2]`|Column          |integer        |
|`[3]`|Comment text    |character array|
|`[4]`|Height in pixels|integer        |
|`[5]`|Width in pixels |integer        |




For example, the following statement associates a comment with the cell at row 2, column 1; the text of the comment is "Hello", and the size of the comment window is 50 pixels (high) by 60 pixels (wide).
```apl
      F.G.AddComment 2 1 'Hello' 50 60
```



Note that if you specify a row number of `¯1`, the comment is added to the corresponding column *title*. Similarly, if you specify a column number of `¯1`, the comment is added to the corresponding row *title*.


The height and width of the comment window, specified by the last 2 elements of the argument are both optional. If the cell already has an associated comment, the new comment replaces it.



You can use a dfn to add several comments in one statement; for example:
```apl
      (1 2)(2 3){F.G.AddComment ⍺,⊂⍵}¨'Hello' 'Goodbye'
```



Note that just before the comment is displayed, the [Grid](../objects/grid.md) generates a [ShowComment](./showcomment.md) event which gives you the opportunity to (temporarily) change the text and/or window size of a comment dynamically.


The comment text specified by the 5th element of the argument to [`⎕NQ`](../../../language-reference-guide/system-functions/nq) must be a simple character scalar, vector, matrix or vector of vectors. Text specified by a simple character vector will be wrapped automatically if necessary. A matrix or vector of vectors may be used to explicitly specify multi-line text. If the array is a vector whose first element is an opening brace ({), the text is assumed to be in rich-text format (RTF) and is displayed accordingly. Note that there is no way for the user to scroll the text in the comment window and it is entirely your responsibility to ensure that the size of the window is appropriate for its contents.


